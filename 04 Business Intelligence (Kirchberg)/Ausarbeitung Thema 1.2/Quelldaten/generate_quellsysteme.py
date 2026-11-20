# -*- coding: utf-8 -*-
"""
Generator für die drei Quellsysteme des fiktiven Dart-Zubehör-Händlers
"DartPro Handel GmbH" (BI-Portfolio Thema 1.2, Kirchberg).

Erzeugt:
  Quelldaten/ERP_Export/*.csv        – ERP "NAVIRA ERP": Semikolon, cp1252, DD.MM.YYYY, Dezimalkomma, Preise netto
  Quelldaten/Shop_Export/*.csv       – Online-Shop "dartpro.shop": Komma, UTF-8, ISO-8601 (UTC), Dezimalpunkt, Preise brutto
  Quelldaten/CRM_Export.xlsx         – CRM "KontaktPilot": Excel-Export, Freitextfelder, US-Datumsformate
  Quelldaten/Hilfstabellen/*.csv     – Wechselkurse, PLZ→Bundesland
  Quelldaten/Problemverzeichnis.csv  – welches Integrationsproblem steckt wo (für die Ausarbeitung)

Alle Daten sind fiktiv. Jedes bewusst eingebaute Problem wird mit P-Nummer registriert
(siehe 02 Checkliste Integrationsprobleme.md).
"""
import csv, os, random, datetime as dt
from pathlib import Path
import openpyxl
from openpyxl.styles import Font

random.seed(1202)
OUT = Path(__file__).resolve().parent / "Quelldaten"
ERP, SHOP, HELP = OUT / "ERP_Export", OUT / "Shop_Export", OUT / "Hilfstabellen"
for d in (ERP, SHOP, HELP):
    d.mkdir(parents=True, exist_ok=True)

PROBLEME = []  # (P-Nr, System, Tabelle, Schlüssel, Beschreibung)
def P(nr, system, tabelle, key, text):
    PROBLEME.append((nr, system, tabelle, key, text))

D = lambda y, m, d: dt.date(y, m, d)
def de(d):  return d.strftime("%d.%m.%Y")
def dec(x, n=2): return f"{x:.{n}f}".replace(".", ",")
def iso(d, h=None):
    h = h if h is not None else random.randint(6, 22)
    return dt.datetime(d.year, d.month, d.day, h, random.randint(0, 59), random.randint(0, 59)).strftime("%Y-%m-%dT%H:%M:%SZ")

# ------------------------------------------------------------------ Stammdaten
VERKAEUFER = [  # VkNr, Name, Gebiet, Eintritt
    ("V01", "Müller, Thomas", "Süd", D(2015, 3, 1)),
    ("V02", "Keller, Sabine", "Nord", D(2018, 9, 1)),
    ("V03", "Yilmaz, Mehmet", "West", D(2020, 1, 15)),
    ("V04", "Hofer, Lea", "Ost", D(2023, 6, 1)),
    ("V99", "Online-Shop", "-", D(2019, 11, 1)),   # Pseudo-Verkäufer für importierte Shop-Aufträge
]
P("P23", "ERP", "ERP_Verkaeufer", "V99", "Pseudo-Verkäufer 'Online-Shop' – Kanal als Verkäufer modelliert (schematische Heterogenität)")

WARENGRUPPEN = [("10", "Steeldarts"), ("20", "Softdarts"), ("30", "Flights"), ("40", "Shafts"),
                ("50", "Dartboards"), ("60", "Zubehör"), ("70", "Bekleidung")]

# ArtNr sprechend: KAT-MAT-LFD-Vn  (Kategorie, Material, laufende Nr, Variante)
ARTIKEL = [  # ArtNr, Bezeichnung, WG, Gewicht_g, Preis_Netto, MwSt
    ("ST-TU-0001-V1", "Steeldart Tungsten 90% 22g",      "10", 22,   49.50, "1"),
    ("ST-TU-0001-V2", "Steeldart Tungsten 90% 24g",      "10", 24,   49.50, "1"),
    ("ST-TU-0002-V1", "Steeldart Tungsten 95% 23g Pro",  "10", 23,   79.00, "1"),
    ("ST-BR-0003-V1", "Steeldart Brass Einsteiger 21g",  "10", 21,   12.90, "1"),
    ("SD-TU-0004-V1", "Softdart Tungsten 80% 18g",       "20", 18,   34.90, "1"),
    ("SD-BR-0005-V1", "Softdart Brass 16g",              "20", 16,    9.90, "1"),
    ("SD-TU-0004-V2", "Softdart Tungsten 80% 20g",       "20", 20,   34.90, "1"),
    ("FL-NY-0010-V1", "Flights Standard 100 Mikron",     "30",  1,    1.50, "1"),
    ("FL-NY-0010-V2", "Flights Slim 100 Mikron",         "30",  1,    1.50, "1"),
    ("FL-NY-0011-V1", "Flights Standard 150 Mikron",     "30",  1,    2.20, "1"),
    ("SH-NY-0020-V1", "Shafts Nylon medium",             "40",  2,    1.90, "1"),
    ("SH-AL-0021-V1", "Shafts Aluminium medium",         "40",  3,    4.90, "1"),
    ("SH-CB-0022-V1", "Shafts Carbon short",             "40",  2,    7.90, "1"),
    ("BO-SI-0030-V1", "Dartboard Sisal Turnier",         "50", 4800, 59.00, "1"),
    ("BO-SI-0031-V1", "Dartboard Sisal Profi Blade",     "50", 5200, 89.00, "1"),
    ("BO-EL-0032-V1", "E-Dartboard Softtip Home",        "50", 3900, 129.00, "1"),
    ("ZU-ST-0040-V1", "Dartboard-Halterung Stahl",       "60", 650,   14.90, "1"),
    ("ZU-TX-0041-V1", "Dartmatte Teppich 3 m",           "60", 2100,  39.90, "1"),
    ("ZU-PL-0042-V1", "Dart-Case Kunststoff",            "60", 180,    8.90, "1"),
    ("ZU-PL-0043-V1", "Spitzen Softtip 100 Stück",       "60", 30,     3.90, "1"),
    ("ZU-ST-0044-V1", "Spitzen Steel Ersatz 10 Stück",   "60", 15,     4.50, "1"),
    ("BK-TX-0050-V1", "Dart-Shirt DartPro Gr. M",        "70", 220,   24.90, "1"),
    ("BK-TX-0050-V2", "Dart-Shirt DartPro Gr. L",        "70", 230,   24.90, "1"),
    ("ZU-PA-0045-V1", "Fachbuch 'Dart-Training'",        "60", 410,   19.50, "2"),  # MwSt 7 %
]
P("P12", "ERP", "ERP_Artikel", "alle", "Sprechender Schlüssel ArtNr = Kategorie-Material-LfdNr-Variante → zerlegen (Schematransformation)")
P("P14", "ERP", "ERP_Artikel", "ZU-PA-0045-V1", "MwSt-Code 2 (7 %) – Code nur über Mapping verständlich; Brutto/Netto-Umrechnung abhängig vom Code")

# Shop-Produkte: sku-Varianten, Englisch, Gewicht in kg, Preis brutto, Währung
SHOP_PRODUCTS = []
for art, bez, wg, g, net, mwst in ARTIKEL:
    if art == "BK-TX-0050-V2":
        continue  # existiert nur im ERP
    sku = art
    if art == "ST-TU-0001-V2": sku = "st-tu-0001-v2"            # Kleinschreibung
    if art == "FL-NY-0010-V2": sku = "FLNY0010V2"               # ohne Bindestriche
    if art == "ZU-PL-0042-V1": sku = "ZU-PL-0042-V1 "           # Leerzeichen am Ende
    satz = 1.19 if mwst == "1" else 1.07
    gross = round(net * satz, 2)
    cur = "EUR"
    name_en = {"ST": "Steel Dart", "SD": "Soft Dart", "FL": "Flights", "SH": "Shafts", "BO": "Dartboard", "ZU": "Accessory", "BK": "Apparel"}[art[:2]]
    cat = {"10": "Steel Darts", "20": "Soft Darts", "30": "Flights", "40": "Shafts", "50": "Boards", "60": "Accessories", "70": "Apparel"}[wg]
    SHOP_PRODUCTS.append([sku, f"{name_en} – {bez}", cat, f"{g/1000:.3f}", f"{gross:.2f}", cur, "true"])
SHOP_PRODUCTS.append(["BO-SI-0031-V1-CH", "Dartboard Sisal Profi Blade (CH)", "Boards", "5.200", "99.00", "CHF", "true"])
SHOP_PRODUCTS.append(["GC-0001", "Gift Card 25", "Gift Cards", "0.000", "25.00", "EUR", "true"])
P("P13", "Shop", "products", "st-tu-0001-v2 / FLNY0010V2 / 'ZU-PL-0042-V1 '", "Uneinheitliche Schreibweise des Schlüssels (Groß/Klein, fehlende Trennzeichen, Leerzeichen) → Standardisierung vor Join")
P("P15", "Shop", "products", "alle", "Gewicht in kg (ERP: g), Preis brutto (ERP: netto) → Maßeinheiten/Preisbasis vereinheitlichen")
P("P16", "Shop", "products", "BO-SI-0031-V1-CH", "Währung CHF → Umrechnung über Wechselkurstabelle")
P("P17", "Shop", "products", "GC-0001", "Produkt nur im Shop (Gutschein) – kein Pendant im ERP; BK-TX-0050-V2 nur im ERP (extensionale Überlappung)")
P("P18", "Shop", "products", "alle", "Warengruppe im ERP eigene Tabelle (Code), im Shop Textattribut 'category' (Attribut/Tabelle-Konflikt, Synonyme Zubehör/Accessories)")

# Kunden ---------------------------------------------------------------------
# Basis-Personen; daraus werden ERP-, Shop- und CRM-Sätze mit unterschiedlichen Darstellungen abgeleitet.
# Felder: key, anrede, vorname, nachname, titel, strasse, hausnr, plz, ort, land, geb, email, typ(P/V/H), in_erp, in_shop, in_crm, vk
PERS = [
    ("k01", "Herr", "Max",     "Mythenmetz",   "",        "Hauptstraße",     "12",  "88212", "Ravensburg",     "DE", D(1988,10,22), "max.mythenmetz@example.de",  "P", 1, 1, 1, "V01"),
    ("k02", "Frau", "Anna",    "Berg",         "Dr.",     "Seestraße",       "5",   "88045", "Friedrichshafen","DE", D(1979,3,14),  "anna.berg@example.de",       "P", 1, 1, 1, "V01"),
    ("k03", "Herr", "Tom",     "Berg",         "",        "Seestraße",       "5",   "88045", "Friedrichshafen","DE", D(1981,7,2),   "tom.berg@example.de",        "P", 0, 1, 1, "V01"),
    ("k04", "Firma","",        "DC Oberschwaben e.V.", "", "Vereinsweg",     "3",   "88250", "Weingarten",     "DE", None,          "vorstand@dc-oberschwaben.example", "V", 1, 0, 1, "V01"),
    ("k05", "Firma","",        "Sportshop Allgäu GmbH", "","Bahnhofstr.",    "44",  "87435", "Kempten",        "DE", None,          "einkauf@sportshop-allgaeu.example","H", 1, 0, 1, "V01"),
    ("k06", "Herr", "Jonas",   "Steiner",      "",        "Lindenallee",     "7a",  "01067", "Dresden",        "DE", D(1995,1,30),  "jonas.steiner@example.de",   "P", 1, 1, 1, "V04"),
    ("k07", "Frau", "Lena",    "Hoffmann",     "",        "Rosenweg",        "9",   "20095", "Hamburg",        "DE", D(1990,12,5),  "lena.hoffmann@example.de",   "P", 1, 1, 0, "V02"),
    ("k08", "Herr", "Peter",   "Groß",         "Dr. med.","Am Markt",        "1",   "50667", "Köln",           "DE", D(1965,5,19),  "peter.gross@example.de",     "P", 1, 1, 1, "V03"),
    ("k09", "Frau", "Sophie",  "Wagner",       "",        "Kirchgasse",      "15",  "6900",  "Bregenz",        "AT", D(1998,8,8),   "sophie.wagner@example.at",   "P", 1, 1, 1, "V01"),
    ("k10", "Herr", "Luca",    "Brunner",      "",        "Bahnhofstrasse",  "22",  "8400",  "Winterthur",     "CH", D(1992,2,29),  "luca.brunner@example.ch",    "P", 1, 1, 1, "V01"),
    ("k11", "Firma","",        "Dartclub Nordlicht", "",  "Deichstraße",     "18",  "28195", "Bremen",         "DE", None,          "info@dc-nordlicht.example",  "V", 1, 0, 1, "V02"),
    ("k12", "Herr", "Ali",     "Demir",        "",        "Industriestr.",   "3",   "40210", "Düsseldorf",     "DE", D(1985,11,11), "ali.demir@example.de",       "P", 1, 1, 1, "V03"),
    ("k13", "Frau", "Marie",   "Schulz",       "",        "Gartenstraße",    "30",  "04109", "Leipzig",        "DE", D(2001,4,1),   "marie.schulz@example.de",    "P", 1, 1, 1, "V04"),
    ("k14", "Herr", "Felix",   "Neumann",      "",        "Birkenweg",       "2",   "80331", "München",        "DE", D(1977,9,23),  "felix.neumann@example.de",   "P", 1, 0, 1, "V01"),
    ("k15", "Frau", "Hannah",  "Koch",         "",        "Mühlenstr.",      "11",  "88214", "Ravensburg",     "DE", D(1993,6,17),  "hannah.koch@example.de",     "P", 1, 1, 1, "V01"),
    ("k16", "Herr", "David",   "Richter",      "",        "Schlossallee",    "8",   "70173", "Stuttgart",      "DE", D(1983,1,9),   "david.richter@example.de",   "P", 1, 1, 0, "V01"),
    ("k17", "Firma","",        "Sportbedarf Nord GmbH", "","Hafenstraße",    "77",  "24103", "Kiel",           "DE", None,          "order@sportbedarf-nord.example","H",1, 0, 1, "V02"),
    ("k18", "Frau", "Julia",   "Fischer",      "",        "Waldweg",         "4",   "99084", "Erfurt",         "DE", D(1996,3,3),   "julia.fischer@example.de",   "P", 1, 1, 1, "V04"),
    ("k19", "Herr", "Niklas",  "Weber",        "",        "Ringstraße",      "60",  "60311", "Frankfurt",      "DE", D(1989,10,10), "niklas.weber@example.de",    "P", 1, 1, 1, "V03"),
    ("k20", "Frau", "Emma",    "Schäfer",      "",        "Poststraße",      "13",  "88400", "Biberach",       "DE", D(1970,12,24), "emma.schaefer@example.de",   "P", 1, 1, 1, "V01"),
    ("k21", "Herr", "Paul",    "Zimmermann",   "",        "Bergstr.",        "21",  "88131", "Lindau",         "DE", D(1999,7,7),   "paul.zimmermann@example.de", "P", 1, 1, 0, "V01"),
    ("k22", "Herr", "Erik",    "Lange",        "",        "Feldweg",         "6",   "19053", "Schwerin",       "DE", D(1975,2,2),   "erik.lange@example.de",      "P", 1, 0, 1, "V02"),
    ("k23", "Frau", "Clara",   "Krüger",       "",        "Sonnenstraße",    "19",  "90402", "Nürnberg",       "DE", D(1987,8,15),  "clara.krueger@example.de",   "P", 1, 1, 1, "V01"),
    ("k24", "Firma","",        "DC Oberschwaben e.V.", "", "Vereinsweg",     "3",   "88250", "Weingarten",     "DE", None,          "kasse@dc-oberschwaben.example", "V", 0, 1, 0, "V01"),  # Verein im Shop als Kunde
    ("k25", "Herr", "Ben",     "Hartmann",     "",        "Uferweg",         "2b",  "78462", "Konstanz",       "DE", D(1994,5,5),   "ben.hartmann@example.de",    "P", 1, 1, 1, "V01"),
    ("k26", "Frau", "Mia",     "Lorenz",       "",        "Amselweg",        "10",  "88069", "Tettnang",       "DE", D(2003,9,9),   "mia.lorenz@example.de",      "P", 0, 1, 1, "V01"),
    ("k27", "Herr", "Leon",    "Schmitt",      "",        "Kastanienallee",  "33",  "10435", "Berlin",         "DE", D(1991,11,30), "leon.schmitt@example.de",    "P", 1, 1, 0, "V04"),
    ("k28", "Frau", "Laura",   "Vogel",        "",        "Talstraße",       "27",  "72070", "Tübingen",       "DE", D(1986,6,6),   "laura.vogel@example.de",     "P", 1, 1, 1, "V01"),
    ("k29", "Herr", "Finn",    "Baumann",      "",        "Hügelweg",        "1",   "88212", "Ravensburg",     "DE", D(1997,1,1),   "finn.baumann@example.de",    "P", 0, 1, 1, "V01"),
    ("k30", "Frau", "Nina",    "Sauer",        "",        "Dorfstr.",        "5",   "17489", "Greifswald",     "DE", D(1982,4,18),  "nina.sauer@example.de",      "P", 1, 0, 1, "V02"),
    ("k31", "Herr", "Jan",     "Peters",       "",        "Nordring",        "40",  "26122", "Oldenburg",      "DE", D(1978,3,27),  "jan.peters@example.de",      "P", 1, 1, 0, "V02"),
    ("k32", "Frau", "Lisa",    "Meier",        "",        "Weinbergstraße",  "14",  "55116", "Mainz",          "DE", D(1990,10,2),  "lisa.meier@example.de",      "P", 0, 1, 1, "V03"),
    ("k33", "Herr", "Noah",    "Franke",       "",        "Schulstraße",     "8",   "88212", "Ravensburg",     "DE", D(2000,2,14),  "noah.franke@example.de",     "P", 0, 1, 0, "V01"),
    ("k34", "Frau", "Sara",    "Albrecht",     "",        "Lerchenweg",      "3",   "88250", "Weingarten",     "DE", D(1984,7,21),  "sara.albrecht@example.de",   "P", 0, 0, 1, "V01"),   # nur CRM (Lead)
    ("k35", "Herr", "Tim",     "Haas",         "",        "Eichenweg",       "17",  "89073", "Ulm",            "DE", D(1993,12,12), "tim.haas@example.de",        "P", 0, 0, 1, "V01"),   # nur CRM (Lead)
    ("k36", "Firma","",        "Gasthaus Zum Anker", "",  "Seeweg",          "1",   "88709", "Meersburg",      "DE", None,          "info@zum-anker.example",     "H", 1, 0, 1, "V01"),
]
PK = {p[0]: p for p in PERS}

# ---- ERP_Kunde (zwei Stände: 30.09.2026 und 31.10.2026) ------------------
erp_knr = {}
n = 1001
for p in PERS:
    if p[13]:
        erp_knr[p[0]] = n; n += 1
P("P01", "ERP/Shop", "ERP_Kunde / customers", "KdNr 1001… vs customer_id 1001…", "Numerische Schlüssel beider Systeme überlappen → Schlüsselkollision, künstlicher DWH-Schlüssel + Mapping-Tabelle nötig")

KDGRP = {"P": "01", "V": "02", "H": "03"}
def erp_kunde_rows(stand):
    rows = []
    for p in PERS:
        if not p[13]: continue
        k, anr, vn, nn, tit, strs, hnr, plz, ort, land, geb, mail, typ, *_ , vk = p
        knr = erp_knr[k]
        name1 = nn if typ != "P" else f"{tit + ' ' if tit else ''}{nn}, {vn}"   # Titel im Namensfeld
        name2 = "" if typ == "P" else {"k04": "Dartclub", "k05": "Inh. Franz Huber", "k11": "Dartclub", "k17": "Großhandel", "k36": "Inh. R. Schmid"}.get(k, "")
        strasse = f"{strs} {hnr}"
        gebdat = de(geb) if geb else "31.12.9999"
        tel = "000"
        if k == "k01": tel = "0751 1234567"
        if k == "k08": tel = "+49 221 998877"
        ges = "N"; angelegt = D(2021, 1, 10) + dt.timedelta(days=(knr - 1001) * 37)
        geaend = angelegt
        land_code = land
        if k == "k14": land_code = "D"            # uneinheitliche Länderkodierung
        if k == "k19": plz, ort = "60311", "Frankfurt a.M."
        if k == "k22": plz = "99999"              # Default-/Platzhalter-PLZ
        if k == "k23": ort = "Nuernberg"          # Umlaut-Schreibweise
        kdgrp = KDGRP[typ]
        if stand >= D(2026, 10, 15) and k == "k06":   # Umzug
            strasse, plz, ort = "Neue Gasse 2", "01099", "Dresden"; geaend = D(2026, 10, 15)
        if stand >= D(2026, 10, 20) and k == "k20":   # Namensänderung (Heirat)
            name1 = "Schäfer-Lutz, Emma"; geaend = D(2026, 10, 20)
        if stand >= D(2026, 10, 8) and k == "k14":    # Kundengruppe geändert Privat → Händler
            kdgrp = "03"; geaend = D(2026, 10, 8)
        if stand >= D(2026, 10, 25) and k == "k31":   # gesperrt
            ges = "J"; geaend = D(2026, 10, 25)
        if stand < D(2026, 10, 3) and k == "k36":     # Neukunde ab 03.10.
            continue
        if k == "k36": angelegt = geaend = D(2026, 10, 3)
        rows.append([knr, name1, name2, strasse, plz, ort, land_code, kdgrp, anr if typ == "P" else "Firma",
                     gebdat, tel, mail if k not in ("k21", "k30") else "", vk, ges, de(angelegt), de(geaend) + " 08:15:00"])
    return rows

ERP_HDR_K = ["KdNr", "Name1", "Name2", "Strasse", "PLZ", "Ort", "Land", "KdGruppe", "Anrede", "Geb_Dat", "Telefon", "EMail", "VkNr", "Gesperrt", "Angelegt_am", "Geaendert_am"]
P("P02", "ERP", "ERP_Kunde", "alle Privatkunden", "Name1 = 'Titel Nachname, Vorname' in einem Feld (Separierung/Elementizing nötig); bei Firmen/Vereinen = Firmenname (Homonym 'Name1')")
P("P03", "ERP", "ERP_Kunde", "Geb_Dat", "Null-Kodierung 31.12.9999 für unbekanntes Geburtsdatum (SAP-Stil)")
P("P04", "ERP", "ERP_Kunde", "Telefon", "Default-Wert '000' statt NULL")
P("P05", "ERP", "ERP_Kunde", f"{erp_knr['k14']} (k14)", "Land 'D' statt 'DE' – uneinheitliche Kodierung")
P("P06", "ERP", "ERP_Kunde", f"{erp_knr['k22']} (k22)", "PLZ 99999 = Platzhalter (unzulässiger Wert) → Plausibilitätsprüfung")
P("P07", "ERP", "ERP_Kunde", f"{erp_knr['k23']} (k23)", "Ort 'Nuernberg' vs. 'Nürnberg' (Zeichenketten vereinheitlichen)")
P("P08", "ERP", "ERP_Kunde", "Strasse", "Abkürzungen 'Str.' vs. 'Straße' vs. 'strasse' (Standardizing)")
P("P09", "ERP", "ERP_Kunde", "KdGruppe", "Kodierung 01/02/03 ohne Dokumentation; CRM: 'A-Kunde/B/C-Kunde' bzw. Typ; Shop: b2c/b2b → schwache Attributäquivalenz")
P("P10", "ERP", "ERP_Kunde", "Geaendert_am", "Zeitstempel ermöglicht Delta-Extraktion; zwei Exportstände (30.09./31.10.) → Historisierung Gültig-von/bis, Current Flag; Mehrfachänderungen zwischen Läufen gehen verloren")
P("P11", "ERP", "ERP_Kunde", f"{erp_knr['k06']} Umzug, {erp_knr['k20']} Heirat, {erp_knr['k14']} Gruppenwechsel, {erp_knr['k31']} gesperrt, {erp_knr['k36']} neu (nur im Stand 31.10.)", "Konkrete Änderungsfälle zwischen den Ständen für die Historisierung")
P("P19", "ERP", "ERP_Kunde", f"EMail {erp_knr['k21']}, {erp_knr['k30']}", "Fehlender Wert (leer) – Shop hat Pflichtfeld E-Mail (konfligierende NOT-NULL-Bedingung)")

# ---- ERP Aufträge ----------------------------------------------------------
STATUS_ERP = {"10": "offen", "20": "geliefert", "30": "fakturiert", "90": "storniert"}
ZAHLART = {"RE": "Rechnung", "VK": "Vorkasse", "LS": "Lastschrift", "PP": "PayPal (Shop)", "KK": "Kreditkarte (Shop)"}
erp_auftraege, erp_pos, erp_zahl, erp_lief = [], [], [], []
VERSAND = {"DHL": "DHL Paket", "DPD": "DPD", "ABH": "Abholung", "SPED": "Spedition"}
auf_nr = 50001
erp_kunden_liste = [p for p in PERS if p[13]]
art_by = {a[0]: a for a in ARTIKEL}

def add_erp_auftrag(k, datum, kanal, vk, status, zahlart, positionen, ext_ref="", rabatt_satz=None):
    global auf_nr
    knr = erp_knr[k]
    erp_auftraege.append([auf_nr, knr, vk, de(datum), status, zahlart, kanal, ext_ref, de(datum + dt.timedelta(days=2)) if status in ("20", "30") else ""])
    netto_sum = 0.0
    for i, (art, menge, preis, rabatt) in enumerate(positionen, 1):
        erp_pos.append([auf_nr, i, art, menge, dec(preis), dec(rabatt, 1)])
        if art in art_by:
            satz = 1.19 if art_by[art][5] == "1" else 1.07
            netto_sum += menge * preis * (1 - rabatt / 100) * satz
    if status in ("20", "30"):
        erp_zahl.append([f"Z{auf_nr}", auf_nr, de(datum + dt.timedelta(days=random.randint(3, 20))), dec(round(netto_sum, 2)), zahlart])
        # Lieferung(en): Teillieferung bei >2 Positionen mit 30 % Wahrscheinlichkeit
        versand = "ABH" if kanal == "MESSE" else random.choice(["DHL", "DHL", "DPD", "SPED"])
        if len(positionen) > 2 and random.random() < 0.3:
            erp_lief.append([f"L{auf_nr}-1", auf_nr, de(datum + dt.timedelta(days=2)), versand, "1", f"Pos 1-{len(positionen)-1}", "N"])
            erp_lief.append([f"L{auf_nr}-2", auf_nr, de(datum + dt.timedelta(days=9)), versand, "1", f"Pos {len(positionen)}", "N"])
        else:
            erp_lief.append([f"L{auf_nr}-1", auf_nr, de(datum + dt.timedelta(days=2)), versand, "1", "alle", "N"])
    elif status == "10":
        erp_lief.append([f"L{auf_nr}-1", auf_nr, "", random.choice(["DHL", "DPD"]), "0", "alle", "N"])
    auf_nr += 1
    return auf_nr - 1

ZEITRAUM = (D(2026, 6, 1), D(2026, 10, 31))
def rnd_date(a=ZEITRAUM[0], b=ZEITRAUM[1]):
    return a + dt.timedelta(days=random.randint(0, (b - a).days))

for _ in range(42):
    p = random.choice(erp_kunden_liste)
    if p[0] == "k36" and True:
        datum = rnd_date(D(2026, 10, 5))
    else:
        datum = rnd_date()
    npos = random.randint(1, 4)
    poss = []
    for _ in range(npos):
        a = random.choice(ARTIKEL)
        preis = a[4]
        if random.random() < 0.15: preis = round(a[4] * 0.9, 2)   # Sonderpreis ≠ Listenpreis
        rabatt = random.choice([0, 0, 0, 5, 10]) if p[12] == "P" else random.choice([10, 15, 20])
        poss.append((a[0], random.randint(1, 6 if p[12] == "P" else 30), preis, rabatt))
    status = random.choice(["30", "30", "30", "20", "10", "90"])
    add_erp_auftrag(p[0], datum, random.choice(["TEL", "MESSE", "AUSSEND"]), p[-1], status, random.choice(["RE", "VK", "LS"]), poss)
P("P20", "ERP", "ERP_Auftragspos", "EPreis_Netto ≠ ERP_Artikel.Preis_Netto", "Preis an der Entität (Artikel) UND an der Beziehung (Position) – allgemeinere Variante ins Zielschema (Skript-Beispiel 8.2.2.5)")
P("P21", "ERP", "ERP_Auftragspos", "Rabatt_Pct 0–100", "Rabatt in Prozent (0–100) vs. Shop discount_rate als Anteil (0–1) → Bereichseinschränkungs-Konflikt")
P("P22", "ERP", "ERP_Auftrag", "Status 10/20/30/90", "Homonym 'Status': ERP-Auftragsstatus (Codes) vs. Shop order status (Text) vs. CRM Kontaktstatus; Stornos (90) müssen gefiltert werden")
# Fehlerfälle
auf_fehler1 = add_erp_auftrag("k01", D(2026, 9, 12), "TEL", "V01", "30", "RE", [("ST-TU-0099-V1", 1, 59.00, 0), ("FL-NY-0010-V1", 5, 1.50, 0)])
P("P24", "ERP", "ERP_Auftragspos", f"{auf_fehler1}/1", "ArtNr ST-TU-0099-V1 existiert nicht in ERP_Artikel → referenzielle Integrität verletzt")
auf_fehler2 = add_erp_auftrag("k08", D(2026, 8, 3), "TEL", "V03", "30", "RE", [("BO-SI-0031-V1", 1, 89.00, 0), ("BO-SI-0031-V1", -1, 89.00, 0), ("BO-SI-0030-V1", 1, 59.00, 0)])
P("P25", "ERP", "ERP_Auftragspos", f"{auf_fehler2}/2", "Negative Menge -1 = Rücknahme/Korrekturposition (Null/negativ mit Semantik, unzulässig als Verkaufsmenge?) → Regel definieren")
erp_auftraege.append([auf_nr, 1099, "V01", "15.07.2026", "30", "RE", "TEL", "", "17.07.2026"]); erp_pos.append([auf_nr, 1, "SD-BR-0005-V1", 2, dec(9.90), dec(0, 1)]); auf_nr += 1
P("P26", "ERP", "ERP_Auftrag", f"{auf_nr-1}", "KdNr 1099 existiert nicht in ERP_Kunde (gelöschter Kunde) → referenzielle Integrität")

# ---- Shop ------------------------------------------------------------------
shop_cid = {}
n = 1001
shop_customers = []
COUNTRY_VARIANTS = {"DE": ["Germany", "Deutschland", "DE", "Germany"], "AT": ["Austria", "AT"], "CH": ["Switzerland", "Schweiz"]}
GENDER = {"Herr": "m", "Frau": "f", "Firma": ""}
for p in PERS:
    if not p[14]: continue
    k, anr, vn, nn, tit, strs, hnr, plz, ort, land, geb, mail, typ, *_ = p
    cid = n; n += 1; shop_cid[k] = cid
    first, last = (vn, nn) if typ == "P" else ("", nn)
    if k == "k02": first, last = "Anna", "Dr. Berg"          # Titel im Nachnamen
    if k == "k08": first, last = "Peter", "Gross"            # ß → ss
    if k == "k19": first, last = "Nik", "Weber"              # Rufname
    zip_ = plz
    if k in ("k06", "k13"): zip_ = plz.lstrip("0")           # führende Null verloren (01067 → 1067, 04109 → 4109)
    country = random.choice(COUNTRY_VARIANTS[land])
    gender = GENDER[anr] if random.random() < 0.85 else ""
    if k == "k12": gender = "d"
    if k == "k15": gender = "m"                               # Widerspruch zu ERP-Anrede 'Frau'
    bd = geb.strftime("%Y-%m-%d") if geb and random.random() < 0.7 else ""
    if k == "k10": bd = "1900-01-01"                          # Default-Datum
    if k == "k27": bd = "2031-11-30"                          # Zukunft (unzulässig)
    created = iso(rnd_date(D(2022, 1, 1), D(2026, 10, 20)))
    newsletter = random.choice(["true", "false"])
    erp_ref = ""
    if k in erp_knr and random.random() < 0.5:
        erp_ref = str(erp_knr[k])
        if k == "k09": erp_ref = f" {erp_knr[k]} "            # Leerzeichen
        if k == "k20": erp_ref = f"{erp_knr[k]:05d}"          # führende Null
    ctype = "b2b" if typ != "P" else "b2c"
    street = f"{strs} {hnr}"
    if k == "k01": street = "Hauptstr. 12"
    if k == "k15": street = "Muehlenstr. 11"
    shop_customers.append([cid, mail, first, last, gender, bd, street, zip_, ort if k != "k19" else "Frankfurt am Main", country, created, newsletter, ctype, erp_ref])
# Dublette: Anna Berg zweiter Account
shop_customers.append([n, "ann.berg@example.de", "Ann", "Berg", "f", "", "Seestr. 5", "88045", "Friedrichshafen", "Germany", iso(D(2026, 9, 2)), "false", "b2c", ""]); dup_anna = n; n += 1
P("P27", "Shop", "customers", f"{shop_cid['k02']} und {dup_anna}", "Dublette: dieselbe Person mit zwei Accounts (Anna/Ann Berg, gleiche Adresse) → Record Linkage über Name+PLZ")
P("P28", "Shop", "customers", f"{shop_cid['k06']}, {shop_cid['k13']}", "PLZ ohne führende Null (1067 statt 01067) – Datentypkonflikt Zahl vs. Text")
P("P29", "Shop", "customers", "country", "Land als 'Germany'/'Deutschland'/'DE' gemischt → Standardisierung auf ISO-Code")
P("P30", "Shop", "customers", "gender", "Geschlecht m/f/d/leer; ERP hat nur Anrede Herr/Frau/Firma; CRM 1/2 → Kodierungen vereinheitlichen; Widerspruch bei k15 (ERP 'Frau', Shop 'm')")
P("P31", "Shop", "customers", f"{shop_cid['k10']}, {shop_cid['k27']}", "birthdate 1900-01-01 (Default) und 2031-11-30 (Zukunft) → unzulässige Werte, Plausibilität")
P("P32", "Shop", "customers", f"{shop_cid['k09']}, {shop_cid['k20']}", "erp_customer_no mit Leerzeichen bzw. führender Null (5-stellig mit 0) → Trim/Typkonvertierung vor Mapping")
P("P33", "Shop", "customers", f"{shop_cid['k02']}, {shop_cid['k08']}", "Titel im Nachnamen ('Dr. Berg'), ß→ss ('Gross') → Matching erschwert")
P("P34", "Shop", "customers", "created_at", "ISO-8601 mit Uhrzeit in UTC vs. ERP DD.MM.YYYY lokal → Datumsformat + Zeitzone")
P("P35", "Shop", "customers", f"{shop_cid['k24']}", f"Verein 'DC Oberschwaben e.V.' im Shop als eigener Kunde (b2b) und im ERP als Kunde {erp_knr['k04']} – gleiche Organisation, unterschiedliche E-Mail → Objektidentifikation ohne Schlüssel")

shop_orders, shop_items = [], []
onr = 90001
ORDER_STATUS = ["paid", "shipped", "shipped", "shipped", "cancelled", "refunded", "pending"]
PAY = ["paypal", "creditcard", "invoice", "sofort"]
shop_cust_keys = [p[0] for p in PERS if p[14]]
shop_order_log = []  # (order_id, k, datum, status, items)
for _ in range(38):
    k = random.choice(shop_cust_keys)
    datum = rnd_date()
    status = random.choice(ORDER_STATUS)
    items = []
    for _ in range(random.randint(1, 3)):
        pr = random.choice(SHOP_PRODUCTS)
        price = float(pr[4])
        disc = random.choice([0, 0, 0, 0.1, 0.15])
        items.append((pr[0], random.randint(1, 5), price, disc, pr[5]))
    coupon = "DART10" if any(i[3] == 0.1 for i in items) else ""
    ship = 4.90 if sum(i[1] * i[2] for i in items) < 50 else 0.0
    total = round(sum(i[1] * i[2] * (1 - i[3]) for i in items) + ship, 2)
    shop_orders.append([onr, shop_cid[k], iso(datum), status, random.choice(PAY), coupon, f"{ship:.2f}", f"{total:.2f}", items[0][4]])
    for li, (sku, qty, price, disc, cur) in enumerate(items, 1):
        shop_items.append([onr, li, sku, qty, f"{price:.2f}", f"{disc:.2f}" if disc else ""])
    shop_order_log.append((onr, k, datum, status, items))
    onr += 1
# Fehlerfälle Shop
shop_orders.append([onr, 1099, iso(D(2026, 9, 18)), "shipped", "paypal", "", "0.00", "58.91", "EUR"]); shop_items.append([onr, 1, "ST-TU-0001-V1", 1, "58.91", ""]); onr += 1
P("P36", "Shop", "orders", f"{onr-1}", "customer_id 1099 existiert nicht in customers (Account gelöscht) → referenzielle Integrität")
shop_orders.append([onr, shop_cid["k13"], iso(D(2026, 10, 2)), "paid", "creditcard", "", "4.90", "4.90", "EUR"]); shop_items.append([onr, 1, "ZU-PL-0043-V1", 0, "4.64", ""]); onr += 1
P("P37", "Shop", "order_items", f"{onr-1}/1", "qty 0 (unzulässiger Wert) → filtern/protokollieren")
shop_orders.append([onr, dup_anna, iso(D(2026, 9, 3)), "shipped", "paypal", "", "0.00", "105.91", "EUR"]); shop_items.append([onr, 1, "BO-SI-0031-V1", 1, "105.91", ""]); onr += 1
P("P38", "Shop", "order_items", "discount_rate", "Rabatt als Anteil (0.10) und leer statt 0 → unterschiedliche Null-Kodierung und Wertebereich ggü. ERP Rabatt_Pct")
P("P39", "Shop", "orders", "alle", "Kein Attribut 'Kanal' und kein 'Verkäufer' – implizit immer Online (fehlendes, aber impliziertes Attribut)")
P("P40", "Shop", "orders", "payment_method", "Zahlungsart als Attribut am Auftrag; im ERP eigene Tabelle ERP_Zahlung (Attribut/Tabelle-Konflikt); Kodierung paypal/PP")

# Shop-Aufträge, die ins ERP importiert wurden (Überlappung der Fakten!)
import_count = 0
for (oid, k, datum, status, items) in shop_order_log:
    if status in ("paid", "shipped") and k in erp_knr and datum <= D(2026, 10, 28) and random.random() < 0.8:
        poss = []
        for sku, qty, price_gross, disc, cur in items:
            art = sku.strip().upper()
            if art == "FLNY0010V2": art = "FL-NY-0010-V2"
            if art.endswith("-CH"): art = art[:-3]
            if art not in art_by: continue
            satz = 1.19 if art_by[art][5] == "1" else 1.07
            fx = 0.95 if cur == "CHF" else 1.0
            poss.append((art, qty, round(price_gross * fx / satz, 2), round(disc * 100, 1)))
        if poss:
            add_erp_auftrag(k, datum + dt.timedelta(days=1), "SHOP", "V99", "30", random.choice(["PP", "KK"]), poss, ext_ref=f"WEB-{oid}")
            import_count += 1
P("P41", "ERP/Shop", "ERP_Auftrag.Ext_Referenz ↔ orders.order_id", f"{import_count} Aufträge", "Shop-Aufträge wurden ins ERP importiert (Kanal SHOP, Ext_Referenz 'WEB-<order_id>', Datum +1 Tag, Preise netto umgerechnet) → extensionale Überlappung der Fakten, Dubletten beim Umsatz vermeiden; nicht alle Shop-Aufträge sind im ERP (pending/cancelled, junge Aufträge)")

# ---- CRM -------------------------------------------------------------------
CRM_MA = [("TM", "Müller, Thomas", "Vertrieb Süd"), ("SK", "Keller, Sabine", "Vertrieb Nord"), ("MY", "Yilmaz, Mehmet", "Vertrieb West"),
          ("LH", "Hofer, Lea", "Vertrieb Ost"), ("NB", "Brandt, Nico", "Marketing")]
P("P42", "CRM", "Mitarbeiter", "alle", "Mitarbeiter als 'Nachname, Vorname' + Kürzel; ERP_Verkaeufer per VkNr → Zuordnung nur über Namen (kein gemeinsamer Schlüssel); 'Brandt, Nico' ohne ERP-Pendant; Schreibvariante 'T. Mueller' in Aktivitäten")
SEG = {"P": ["B", "C-Kunde", "B-Kunde", "C"], "V": ["A-Kunde", "A"], "H": ["A-Kunde", "A-Kunde", "B"]}
TYP = {"P": "Privat", "V": "Verein", "H": "Fachhandel"}
VK2MA = {"V01": "Müller, Thomas", "V02": "Keller, Sabine", "V03": "Yilmaz, Mehmet", "V04": "Hofer, Lea"}
crm_kontakte = []
crm_id = {}
n = 1
def mmdd(d): return d.strftime("%m/%d/%Y")
for p in PERS:
    if not p[15]: continue
    k, anr, vn, nn, tit, strs, hnr, plz, ort, land, geb, mail, typ, *_ , vk = p
    cid = f"CRM-{n:04d}"; n += 1; crm_id[k] = cid
    name = f"{tit + ' ' if tit else ''}{vn} {nn}".strip() if typ == "P" else nn
    adresse = f"{strs} {hnr}, {plz} {ort}" + ("" if land == "DE" else f", {land}")
    if k == "k06": adresse = "Lindenallee 7a, 01067 Dresden"     # alte Adresse (Umzug nicht im CRM → Aktualität/Widerspruch)
    if k == "k19": adresse = "Ringstraße 60, 60311 Frankfurt/Main"
    geschlecht = {"Herr": 1, "Frau": 2, "Firma": None}[anr]
    if k == "k01": geschlecht = 2                                 # Widerspruch zu Anrede 'Herr' (Tabelle 8.3 Mythenmetz!)
    gebt = ""
    if geb:
        r = random.random()
        gebt = mmdd(geb) if r < 0.55 else (geb.strftime("%d.%m.%y") if r < 0.8 else "")
    if k == "k09": gebt = "n/a"
    if k == "k12": gebt = "unbekannt"
    if k == "k01": gebt = "10/22/1988"
    segment = random.choice(SEG[typ]) if k not in ("k34", "k35") else "Lead"
    status = "Lead" if k in ("k34", "k35") else random.choice(["aktiv", "aktiv", "aktiv", "inaktiv"])
    quelle = random.choice(["Messe", "Web", "Empfehlung", "Kaltakquise", ""])
    profil = random.choice(["Steeldart", "Softdart", "E-Dart", "Steeldart", ""]) if typ == "P" else ""
    verein = ""
    if k in ("k01", "k15", "k29", "k33", "k34"): verein = "DC Oberschwaben e.V."
    if k in ("k07", "k22"): verein = "Dartclub Nordlicht"
    if k == "k25": verein = "DC Oberschwaben"                      # Schreibvariante
    liga = random.choice(["Bezirksliga", "Kreisliga", "Landesliga", ""]) if verein else ""
    nl = random.choice(["x", "", "Ja", "x"])
    betreuer = VK2MA.get(vk, "")
    if k in ("k34", "k35"): betreuer = "Brandt, Nico"
    erp_ref = str(erp_knr[k]) if k in erp_knr and random.random() < 0.7 else ""
    if k == "k12" and k in erp_knr: erp_ref = f"{erp_knr[k]:,}".replace(",", ".")   # '1.012' Tausenderpunkt
    shop_ref = str(shop_cid[k]) if k in shop_cid and random.random() < 0.5 else ""
    tel = random.choice(["0751 / 12 34 56", "+49 751 123456", "0751-123456", "999-999", ""])
    if k == "k08": tel = "0221 998877"
    lastc = rnd_date(D(2024, 1, 1), D(2026, 10, 28))
    if k in ("k30", "k22"): lastc = D(2024, 3, 11)                 # veraltet
    crm_kontakte.append([cid, name, TYP[typ], adresse, mail if k != "k01" else "Max.Mythenmetz@Example.de", tel, geschlecht, gebt, segment, status, quelle, profil, verein, liga, nl, betreuer, erp_ref, shop_ref, lastc])
# Dublette im CRM: Mythenmetz zweimal mit Tippfehler
crm_kontakte.append([f"CRM-{n:04d}", "Max Mythenmez", "Privat", "Hauptstr. 12, 88212 Ravensburg", "max.mythenmetz@example.de", "", 1, "22.10.88", "C-Kunde", "aktiv", "Messe", "Steeldart", "DC Oberschwaben e.V.", "Kreisliga", "", "Müller, Thomas", "", "", D(2026, 10, 12)])
dup_crm = f"CRM-{n:04d}"; n += 1
P("P43", "CRM", "Kontakte", f"{crm_id['k01']} / {dup_crm}", "Dublette mit Tippfehler ('Mythenmez'), unterschiedliche Groß-/Kleinschreibung der E-Mail; Geschlecht 2 vs. Anrede Herr im ERP (Widerspruch wie Tabelle 8.3)")
P("P44", "CRM", "Kontakte", "Name", "Vollständiger Name inkl. Titel in einem Feld ('Dr. Anna Berg') → Elementizing (Titel/Vorname/Nachname)")
P("P45", "CRM", "Kontakte", "Adresse", "Adresse als ein Freitextfeld 'Straße Nr, PLZ Ort[, Land]' → Separierung in Komponenten; Attribut/Tabelle-Konflikt zu ERP-Spalten")
P("P46", "CRM", "Kontakte", "Geburtstag", "Geburtsdatum als Text: MM/DD/YYYY, DD.MM.YY (zweistelliges Jahr → Jahrhundertregel), 'n/a', 'unbekannt', leer → Standardisierung + uneinheitliche Null-Kodierung")
P("P47", "CRM", "Kontakte", "Geschlecht", "Kodierung 1/2/leer (ERP: Anrede, Shop: m/f/d)")
P("P48", "CRM", "Kontakte", "Segment", "'A-Kunde'/'A'/'B'/'C-Kunde' gemischt (Schreibvarianten) und andere Dimension als ERP KdGruppe → schwache Attributäquivalenz, kleinster gemeinsamer Nenner")
P("P49", "CRM", "Kontakte", f"{crm_id['k06']}", "Alte Adresse (Umzug nur im ERP) → Aktualität/Widerspruch, Quellsystem priorisieren")
P("P50", "CRM", "Kontakte", f"{crm_id['k12']}", "ERP_KdNr als '1.012' mit Tausenderpunkt → Typkonvertierung")
P("P51", "CRM", "Kontakte", "Telefon", "Telefonnummern in vier Formaten + Default '999-999'")
P("P52", "CRM", "Kontakte", "Newsletter", "'x' / 'Ja' / leer vs. Shop true/false vs. ERP nicht vorhanden (fehlendes Attribut)")
P("P53", "CRM", "Kontakte", "Verein", f"'DC Oberschwaben e.V.' vs. 'DC Oberschwaben' (Schreibvariante); Verein ist zugleich ERP-Kunde {erp_knr['k04']} → Householding / Gruppenbildung")
P("P54", "CRM", "Kontakte", f"{crm_id['k30']}, {crm_id['k22']}", "Letzter Kontakt 2024 → Aktualitätsproblem (Status trotzdem 'aktiv')")
P("P55", "CRM", "Kontakte", f"{crm_id['k34']}, {crm_id['k35']}", "Leads nur im CRM (Einschluss/Teilmenge) – keine ERP-/Shop-Daten → Belegungsregel für fehlende Kennzahlen")
P("P56", "CRM", "Kontakte", "Status", "Homonym 'Status' (aktiv/inaktiv/Lead) ggü. Auftragsstatus")

crm_akt = []
an = 1
TYPEN = ["Call", "Mail", "Besuch", "Messe", "Telefonat", "E-Mail"]
MA_NAMES = [m[1] for m in CRM_MA]
for _ in range(70):
    kont = random.choice(crm_kontakte)
    datum = rnd_date(D(2025, 10, 1), D(2026, 10, 28))
    ma = random.choice(MA_NAMES)
    if random.random() < 0.08: ma = "T. Mueller"
    dauer = random.choice([5, 10, 15, 20, 30, 45, 60, -1])
    crm_akt.append([f"A{an:05d}", kont[0], datum, random.choice(TYPEN), ma, random.choice(["Interesse", "Angebot versendet", "kein Bedarf", "Rückruf vereinbart", "Bestellung", ""]), dauer]); an += 1
crm_akt.append([f"A{an:05d}", "CRM-0999", D(2026, 9, 9), "Call", "Keller, Sabine", "Interesse", 10]); an += 1
P("P57", "CRM", "Aktivitäten", f"A{an-1:05d}", "KontaktID CRM-0999 existiert nicht → referenzielle Integrität")
P("P58", "CRM", "Aktivitäten", "Dauer_min", "-1 als Null-Kodierung für unbekannte Dauer")
P("P59", "CRM", "Aktivitäten", "Typ", "Synonyme 'Call'/'Telefonat', 'Mail'/'E-Mail' → Kodierung vereinheitlichen")

crm_kamp = [("K01", "Messe Dart-Expo Stuttgart 2026", D(2026, 3, 14), D(2026, 3, 15), 8500), ("K02", "Newsletter Sommer-Sale", D(2026, 7, 1), D(2026, 7, 31), 1200), ("K03", "Vereinsaktion Herbst", D(2026, 10, 1), D(2026, 11, 30), 3000)]
crm_teiln = []
for kont in crm_kontakte:
    for kid, *_ in crm_kamp:
        if random.random() < 0.3:
            crm_teiln.append([kid, kont[0], random.choice(["eingeladen", "teilgenommen", "reagiert", "gekauft", ""])])

# ---- Hilfstabellen -----------------------------------------------------------
fx = [["Waehrung", "Kurs_EUR", "Gueltig_ab"], ["CHF", "0,95", "01.01.2026"], ["EUR", "1,00", "01.01.2026"]]
plz_bl = [["PLZ_Praefix", "Bundesland"], ["01", "Sachsen"], ["04", "Sachsen"], ["10", "Berlin"], ["17", "Mecklenburg-Vorpommern"], ["19", "Mecklenburg-Vorpommern"],
          ["20", "Hamburg"], ["24", "Schleswig-Holstein"], ["26", "Niedersachsen"], ["28", "Bremen"], ["40", "Nordrhein-Westfalen"], ["50", "Nordrhein-Westfalen"],
          ["55", "Rheinland-Pfalz"], ["60", "Hessen"], ["70", "Baden-Württemberg"], ["72", "Baden-Württemberg"], ["78", "Baden-Württemberg"], ["80", "Bayern"],
          ["87", "Bayern"], ["88", "Baden-Württemberg"], ["89", "Baden-Württemberg"], ["90", "Bayern"], ["99", "Thüringen"]]
P("P60", "Hilfstabellen", "PLZ_Bundesland / Wechselkurse", "-", "Anreicherung (Bundesland aus PLZ, EUR-Umrechnung) und Plausibilitätsprüfung PLZ↔Land (Verification)")

# ------------------------------------------------------------------ Schreiben
def write_csv(path, header, rows, sep, enc):
    with open(path, "w", newline="", encoding=enc) as f:
        w = csv.writer(f, delimiter=sep, quoting=csv.QUOTE_MINIMAL)
        w.writerow(header); w.writerows(rows)

write_csv(ERP / "ERP_Kunde_Stand_2026-09-30.csv", ERP_HDR_K, erp_kunde_rows(D(2026, 9, 30)), ";", "cp1252")
write_csv(ERP / "ERP_Kunde.csv", ERP_HDR_K, erp_kunde_rows(D(2026, 10, 31)), ";", "cp1252")
write_csv(ERP / "ERP_Verkaeufer.csv", ["VkNr", "Name", "Gebiet", "Eintritt"], [[v, nm, g, de(e)] for v, nm, g, e in VERKAEUFER], ";", "cp1252")
write_csv(ERP / "ERP_Warengruppe.csv", ["WG", "Bezeichnung"], WARENGRUPPEN, ";", "cp1252")
write_csv(ERP / "ERP_Artikel.csv", ["ArtNr", "Bezeichnung", "WG", "Gewicht_g", "Preis_Netto", "MwSt_Code"], [[a, b, w, g, dec(p), m] for a, b, w, g, p, m in ARTIKEL], ";", "cp1252")
write_csv(ERP / "ERP_Auftrag.csv", ["AufNr", "KdNr", "VkNr", "AufDatum", "Status", "Zahlart", "Kanal", "Ext_Referenz", "Lieferdatum"], erp_auftraege, ";", "cp1252")
write_csv(ERP / "ERP_Auftragspos.csv", ["AufNr", "Pos", "ArtNr", "Menge", "EPreis_Netto", "Rabatt_Pct"], erp_pos, ";", "cp1252")
write_csv(ERP / "ERP_Zahlung.csv", ["ZahlNr", "AufNr", "Zahldatum", "Betrag_Brutto", "Zahlart"], erp_zahl, ";", "cp1252")
erp_lief.append(["L50099-1", 50099, "12.08.2026", "DHL", "1", "alle", "J"])  # Retoure zu nicht exportiertem Auftrag
write_csv(ERP / "ERP_Lieferung.csv", ["LiefNr", "AufNr", "Lieferdatum", "Versandart", "Geliefert", "Umfang", "Retoure"], erp_lief, ";", "cp1252")
P("P64", "ERP", "ERP_Lieferung", "Teillieferungen L…-1/L…-2", "Lieferung als eigene Tabelle (1:n zum Auftrag, Teillieferungen); Shop kennt nur Status 'shipped' am Auftrag (Attribut/Tabelle-Konflikt); Lieferdatum zusätzlich redundant in ERP_Auftrag → Redundanz, führende Quelle festlegen")
P("P65", "ERP", "ERP_Lieferung", "L50099-1", "Retoure zu AufNr 50099, die im Export fehlt (Zeitraumfilter) → referenzielle Integrität; Versandart-Codes DHL/DPD/ABH/SPED undokumentiert; Lieferdatum leer bei offenen Lieferungen (Geliefert=0)")
P("P61", "ERP", "alle Exporte", "-", "Interoperabler Export: Semikolon-CSV, Zeichensatz Windows-1252 (Umlaute!), Dezimalkomma, Datum DD.MM.YYYY – Shop: Komma-CSV, UTF-8, Dezimalpunkt, ISO-Datum – CRM: Excel (syntaktische Heterogenität, Parser/Spaltentypen)")
P("P62", "ERP", "ERP_Kunde", "zwei Stände", "Extraktionsart: ERP Delta über Geaendert_am möglich; Shop/CRM nur Vollabzug (nicht unterstützende Quelle: Excel-Export) → Begründung der Extraktionsstrategie")

write_csv(SHOP / "customers.csv", ["customer_id", "email", "first_name", "last_name", "gender", "birthdate", "street", "zip", "city", "country", "created_at", "newsletter", "customer_type", "erp_customer_no"], shop_customers, ",", "utf-8")
write_csv(SHOP / "products.csv", ["sku", "name", "category", "weight_kg", "price_gross", "currency", "active"], SHOP_PRODUCTS, ",", "utf-8")
write_csv(SHOP / "orders.csv", ["order_id", "customer_id", "order_date", "status", "payment_method", "coupon", "shipping_cost", "total_gross", "currency"], shop_orders, ",", "utf-8")
write_csv(SHOP / "order_items.csv", ["order_id", "line", "sku", "qty", "unit_price_gross", "discount_rate"], shop_items, ",", "utf-8")

wb = openpyxl.Workbook()
def sheet(name, header, rows, first=False):
    ws = wb.active if first else wb.create_sheet()
    ws.title = name
    ws.append(header)
    for c in ws[1]: c.font = Font(bold=True)
    for r in rows: ws.append(r)
    for col in ws.columns:
        ws.column_dimensions[col[0].column_letter].width = min(40, max(10, max(len(str(c.value or "")) for c in col) + 2))
    return ws
ws = sheet("Kontakte", ["Kontakt-ID", "Name", "Typ", "Adresse", "E-Mail", "Telefon", "Geschlecht", "Geburtstag", "Segment", "Status", "Quelle", "Spielerprofil", "Verein", "Liga", "Newsletter", "Betreuer", "ERP-Kunden-Nr.", "Shop-Kunde", "Letzter Kontakt"], crm_kontakte, first=True)
for row in ws.iter_rows(min_row=2):
    row[18].number_format = "DD.MM.YYYY"
ws = sheet("Aktivitäten", ["Aktivitäts-ID", "Kontakt-ID", "Datum", "Typ", "Mitarbeiter", "Ergebnis", "Dauer (min)"], crm_akt)
for row in ws.iter_rows(min_row=2):
    row[2].number_format = "DD.MM.YYYY"
sheet("Kampagnen", ["Kampagnen-ID", "Bezeichnung", "Start", "Ende", "Budget EUR"], [list(k) for k in crm_kamp])
sheet("Kampagnenteilnahme", ["Kampagnen-ID", "Kontakt-ID", "Reaktion"], crm_teiln)
sheet("Mitarbeiter", ["Kürzel", "Name", "Abteilung"], [list(m) for m in CRM_MA])
wb.save(OUT / "CRM_Export.xlsx")
P("P63", "CRM", "Kontakte", "Letzter Kontakt / Geburtstag", "Echte Excel-Datumswerte neben Datums-Texten in derselben Datei → gemischte Spaltentypen")

write_csv(HELP / "Wechselkurse.csv", fx[0], fx[1:], ";", "utf-8")
write_csv(HELP / "PLZ_Bundesland.csv", plz_bl[0], plz_bl[1:], ";", "utf-8")

assert len({p[0] for p in PROBLEME})==len(PROBLEME), 'doppelte P-Nr'
PROBLEME.sort(key=lambda x: int(x[0][1:]))
write_csv(OUT / "Problemverzeichnis.csv", ["P-Nr", "System", "Tabelle", "Schlüssel/Zeile", "Eingebautes Problem"], PROBLEME, ";", "utf-8-sig")

print(f"ERP: {len(erp_kunde_rows(D(2026,10,31)))} Kunden, {len(erp_auftraege)} Aufträge ({import_count} aus Shop), {len(erp_pos)} Positionen, {len(erp_zahl)} Zahlungen")
print(f"Shop: {len(shop_customers)} Kunden, {len(SHOP_PRODUCTS)} Produkte, {len(shop_orders)} Bestellungen, {len(shop_items)} Positionen")
print(f"CRM: {len(crm_kontakte)} Kontakte, {len(crm_akt)} Aktivitäten, {len(crm_teiln)} Kampagnenteilnahmen")
print(f"{len(PROBLEME)} registrierte Probleme")
