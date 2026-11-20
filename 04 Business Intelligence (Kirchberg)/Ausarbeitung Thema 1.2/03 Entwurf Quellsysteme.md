# Entwurf der Quellsysteme – DartPro Handel GmbH (fiktiv)

## 1. Szenario
**DartPro Handel GmbH**, Ravensburg: Händler für Dart-Zubehör (Steel-/Softdarts, Flights, Shafts, Boards, Zubehör, Bekleidung). Vertrieb über vier Außendienst-Verkäufer (Gebiete Süd/Nord/West/Ost: Privatkunden, Vereine, Fachhandel) und einen Online-Shop. Drei gewachsene Systeme:

| System | Produkt (fiktiv) | Technik / Export | Besonderheiten |
|---|---|---|---|
| **ERP** | „NAVIRA ERP“ – Warenwirtschaft der Lexware-/Sage-Klasse, on-premise auf einem Windows-Server | Export-Assistent (*Datei → Export → ASCII*): eine Datenquelle je Lauf, TXT/CSV, `;`-getrennt, Text in `"…"`, Feldnamen als Kopfzeile, Zeichensatz wahlweise **ASCII (MS-DOS, CP 850)** oder **ANSI (Windows-1252, Standard)**; Dezimalkomma, Datum `DD.MM.YYYY`, Preise **netto** | Zeitraumfilter „neu angelegte/geänderte Sätze“ → zeitstempelbasierte Delta-Extraktion (`Geaendert_am`); Exportprofile → periodisch wiederholbar; Kontaktpersonen werden nicht exportiert (fehlendes Attribut → nur im CRM); Shop-Aufträge werden täglich importiert (Kanal `SHOP`) |
| **Online-Shop** | „dartpro.shop“ – Cloud-Shopsystem der Shopware-/Shopify-Klasse (englisch) | CSV-Export aus dem Admin-Backend (alternativ REST-API), `,`-getrennt, **UTF-8**, Dezimalpunkt, ISO-8601 mit Uhrzeit (UTC), Preise **brutto**, Gewicht in kg | Eigene Kundenkonten mit numerischen IDs (kollidieren mit ERP), Währung EUR/CHF, kein Zeitstempelfilter im Export → Vollabzug |
| **CRM** | „KontaktPilot“ – kleines Vertriebs-CRM | **Excel**-Export (xlsx), 5 Blätter; kein API-/DB-Zugang → *nicht explizit unterstützende Quelle* (Abb. 7.2) | Freitextfelder (Name, Adresse), US-Datumsformate als Text, Kodierungen 1/2, x/Ja |

**Einordnung nach Skript Abb. 7.2 / 7.3:** ERP = exportbasierte, zeitstempelbasierte Quelle (Delta möglich); Shop = exportbasierte Quelle ohne Zeitstempel (Vollabzug; API wäre Zugriff auf Anwendungsebene, Kap. 7.2); CRM = nicht explizit unterstützende Quelle (Dateiexport). Alle drei: interoperabler Export (7.3.2), periodisch (täglich nachts, Stichtag 31.10.2026).

**Zeichensatz-Entscheidung:** Der ERP-Export wird mit „ANSI (Windows)“ ausgeführt, weil Power Query Codepage 1252 direkt lesen kann; die Alternative „ASCII (MS-DOS)“ (Codepage 850) würde Umlaute an anderen Codepositionen liefern und einen zusätzlichen Umsetzungsschritt erfordern (Skript 8.1: Zeichensatzumsetzung vor der Bereinigung). Beleg für die Exportoptionen: Lexware-Support-FAQ „Export von Kunden- und Lieferantenstammdaten“ bzw. „Export von Artikeln und Warengruppen“ (lexware.de/support, abgerufen 24.10.2026). Hinweis: Lexware exportiert Belege nur als Buchungsdaten auf Rechnungsebene; für die Aufgabenstellung („Bestellungen, Zahlungen und Lieferungen“) wird ein ERP angenommen, das diese drei Bereiche als Tabellen bereitstellt – daher „angelehnt an“, nicht „Lexware“.

**Auswertungsziel (Aufgabenstellung):** Verkäufe je **Verkäufer** in Bezug zu **Kundenmerkmalen** (Kundentyp, Segment, Region/Bundesland, Geschlecht/Altersklasse, Vereinszugehörigkeit, Spielerprofil, Newsletter) – über alle Kanäle, ohne Doppelzählung.

## 2. Tabellen

### 2.1 ERP (`Quelldaten/ERP_Export/`)
| Tabelle | Schlüssel | Spalten | Zweck / Heterogenität |
|---|---|---|---|
| `ERP_Kunde` (Stand 31.10.) + `ERP_Kunde_Stand_2026-09-30` | KdNr (int, 1001…) | Name1 („Titel Nachname, Vorname“ oder Firma), Name2, Strasse, PLZ, Ort, Land, KdGruppe (01/02/03), Anrede, Geb_Dat, Telefon, EMail, VkNr, Gesperrt (J/N), Angelegt_am, Geaendert_am | Zwei Stände → Delta + Historisierung (Umzug, Heirat, Gruppenwechsel, Sperre, Neukunde) |
| `ERP_Verkaeufer` | VkNr | Name („Nachname, Vorname“), Gebiet, Eintritt | V99 = Pseudo-Verkäufer Online-Shop |
| `ERP_Warengruppe` | WG | Bezeichnung | Code-Tabelle |
| `ERP_Artikel` | ArtNr (sprechend `KAT-MAT-LFD-Vn`) | Bezeichnung, WG, Gewicht_g, Preis_Netto, MwSt_Code (1 = 19 %, 2 = 7 %) | Listenpreis an der Entität |
| `ERP_Auftrag` | AufNr | KdNr, VkNr, AufDatum, Status (10/20/30/90), Zahlart (RE/VK/LS/PP/KK), Kanal (TEL/MESSE/AUSSEND/SHOP), Ext_Referenz (`WEB-<order_id>`), Lieferdatum | Shop-Importe erkennbar an Kanal + Ext_Referenz |
| `ERP_Auftragspos` | AufNr + Pos | ArtNr, Menge, EPreis_Netto, Rabatt_Pct (0–100) | Positionspreis ≠ Listenpreis möglich; Menge −1 = Rücknahme |
| `ERP_Zahlung` | ZahlNr | AufNr, Zahldatum, Betrag_Brutto, Zahlart | Zahlung als eigene Tabelle (Shop: Attribut) |
| `ERP_Lieferung` | LiefNr (`L<AufNr>-n`) | AufNr, Lieferdatum (leer bei offen), Versandart (DHL/DPD/ABH/SPED), Geliefert (0/1), Umfang („alle“ / „Pos 1-3“), Retoure (J/N) | 1:n zum Auftrag, Teillieferungen; Lieferdatum redundant in ERP_Auftrag; Retoure zu nicht exportiertem Auftrag |

Die drei von der Aufgabenstellung geforderten ERP-Bereiche sind damit abgedeckt: **Bestellungen** (`ERP_Auftrag`/`ERP_Auftragspos`), **Zahlungen** (`ERP_Zahlung`), **Lieferungen** (`ERP_Lieferung`). Bewusst weggelassen (nicht auswertungsrelevant für Verkäufer × Kundenmerkmale): Lieferanten, Bankverbindungen, Einkaufspreise, Lagerbestände – im Text als Entscheidung „Übernahme nur tatsächlich benötigter Daten“ (Skript S. 150) begründen.

### 2.2 Shop (`Quelldaten/Shop_Export/`)
| Tabelle | Schlüssel | Spalten | Heterogenität |
|---|---|---|---|
| `customers` | customer_id (int, 1001…) | email, first_name, last_name, gender (m/f/d/leer), birthdate (ISO/leer/1900-01-01), street, zip (teils ohne führende 0), city, country (Germany/Deutschland/DE/…), created_at (UTC), newsletter (true/false), customer_type (b2c/b2b), erp_customer_no (optional, unsauber) | Dubletten-Account, Titel im Nachnamen, ß→ss |
| `products` | sku (≈ ArtNr, aber Schreibvarianten) | name (engl./dt. gemischt), category (Text), weight_kg, price_gross, currency (EUR/CHF), active | Gutschein nur im Shop; CH-Variante in CHF |
| `orders` | order_id (90001…) | customer_id, order_date (UTC), status (paid/shipped/cancelled/refunded/pending), payment_method, coupon, shipping_cost, total_gross, currency | Kein Kanal, kein Verkäufer (implizit) |
| `order_items` | order_id + line | sku, qty, unit_price_gross, discount_rate (0–1, leer = 0) | Rabatt als Anteil |

### 2.3 CRM (`Quelldaten/CRM_Export.xlsx`)
| Blatt | Schlüssel | Spalten | Heterogenität |
|---|---|---|---|
| `Kontakte` | Kontakt-ID (`CRM-0001`) | Name (Freitext inkl. Titel), Typ (Privat/Verein/Fachhandel), Adresse (ein Feld), E-Mail, Telefon (4 Formate), Geschlecht (1/2), Geburtstag (Text: MM/DD/YYYY, DD.MM.YY, n/a, unbekannt), Segment (A-Kunde/A/B/C-Kunde/Lead), Status (aktiv/inaktiv/Lead), Quelle, Spielerprofil, Verein, Liga, Newsletter (x/Ja/leer), Betreuer (Name), ERP-Kunden-Nr. (Text, teils `1.012`), Shop-Kunde, Letzter Kontakt (echtes Datum) | Dublette mit Tippfehler, veraltete Adresse, Leads ohne ERP/Shop |
| `Aktivitäten` | Aktivitäts-ID | Kontakt-ID, Datum, Typ (Call/Telefonat/Mail/E-Mail/Besuch/Messe), Mitarbeiter (Name, auch „T. Mueller“), Ergebnis (Freitext), Dauer (min, −1 = unbekannt) | Synonyme, Null-Kodierung, FK-Verletzung |
| `Kampagnen` / `Kampagnenteilnahme` | Kampagnen-ID | Bezeichnung, Start, Ende, Budget / Kontakt-ID, Reaktion | optionale Kundenmerkmale |
| `Mitarbeiter` | Kürzel | Name („Nachname, Vorname“), Abteilung | Zuordnung zu ERP_Verkaeufer nur über Namen |

### 2.4 Hilfstabellen (`Quelldaten/Hilfstabellen/`)
`Wechselkurse.csv` (CHF→EUR), `PLZ_Bundesland.csv` (2-stelliger Präfix → Bundesland) für Anreicherung und Plausibilitätsprüfung.

## 3. Zielschema (Vorschlag) – Star-Schema im integrierten Datenbestand

```
Dim_Kunde (historisiert)         Dim_Artikel            Dim_Verkaeufer        Dim_Zeit (aus Datum)
 Kunde_Key (künstlich)            Artikel_Key            Verkaeufer_Key         Datum, Monat, Quartal, Jahr
 ERP_KdNr | Shop_ID | CRM_ID      ArtNr (bereinigt)      VkNr
 Name, Vorname, Titel             Kategorie, Material,   Name (Vor-/Nachname)
 Kundentyp (Privat/Verein/        LfdNr, Variante        Gebiet
   Fachhandel) ← E/S/C            Warengruppe            Ist_Online (Flag)
 Segment (A/B/C/Lead) ← C         Listenpreis_Netto_EUR
 Straße, Hausnr, PLZ, Ort,        Gewicht_g, MwSt_Satz
   Land (ISO), Bundesland         Quelle (ERP/Shop/beide)
 Geschlecht (m/w/d/unbek.)
 Geburtsdatum, Altersklasse
 Verein (normiert), Liga, Spielerprofil, Newsletter
 Gueltig_von, Gueltig_bis, Version, Ist_Aktuell

Fakt_Verkauf
 Verkauf_Key | Quelle (ERP/Shop) | Quell_Beleg (AufNr+Pos bzw. order_id+line)
 Kunde_Key (zur am Belegdatum gültigen Version) | Artikel_Key | Verkaeufer_Key | Datum
 Kanal (TEL/MESSE/AUSSEND/ONLINE) | Status (normiert) | Zahlart (normiert)
 Menge | EPreis_Netto_EUR | Rabatt_Anteil | Umsatz_Netto_EUR | Umsatz_Brutto_EUR
 Ist_Shop_Import_Dublette (Flag – Shop-Beleg, der auch als ERP-Auftrag existiert)

Map_Kunde (Kunde_Key ↔ ERP_KdNr ↔ Shop_ID ↔ CRM_ID, Trefferstufe 1–4)   Map_Artikel   Map_Verkaeufer
Protokoll_Verworfen (Quelle, Tabelle, Schlüssel, Regel, Grund)
Kodierungsverzeichnis (Attribut, Quellwert, Zielwert)
```

**Entscheidungen, die in der Arbeit zu begründen sind (jeweils mit Alternative):**
1. Preis an der Faktenzeile (allgemeiner) statt am Artikel – Alternative: nur Listenpreis → Sonderpreise gingen verloren.
2. Netto-EUR als einheitliche Preisbasis – Alternative: brutto; Netto, weil MwSt-Sätze differieren und Controlling netto rechnet.
3. Shop-Belege, die im ERP importiert sind, werden aus dem **ERP** gezählt (Kanal ONLINE, Verkäufer V99) – Alternative: aus dem Shop (originärer, mit Coupon-Info) → Entscheidung dokumentieren, Dublettenflag mitführen.
4. Kundentyp und Segment als zwei Attribute (Parallelklassifikation) statt einer erzwungenen Hierarchie.
5. Nur Dim_Kunde historisiert (Gültig-von/bis + Current Flag), Artikel überschrieben – Alternative: alles historisieren → Aufwand.
6. Leiterartige Integration ERP → Shop → CRM – Alternative: One-Shot.
7. Fakten mit unbekanntem Kunden an Dummy „Unbekannt“ statt verwerfen – Alternative: verwerfen → Umsatzsumme stimmt nicht mehr.
8. Geburtsdatum nur als Altersklasse (zu lückenhaft/widersprüchlich für tagesgenaue Auswertung) – Alternative: weglassen (Abb. 8.9).

## 4. Nächste Schritte
1. In Excel ein neues Arbeitsbuch `DartPro_Integration.xlsx` anlegen; Quellen per *Daten → Daten abrufen → Aus Datei* anbinden (ERP: Codepage 1252, Trennzeichen Semikolon; Shop: 65001/UTF-8, Komma; CRM: Arbeitsmappe).
2. Abfragen in Gruppen organisieren: `00 Quellen`, `10 Bereinigung`, `20 Harmonisierung`, `30 Mapping`, `40 Dimensionen`, `50 Fakten`, `90 Protokoll`.
3. Pro Checklistenpunkt den Schritt bauen, Screenshot machen, P-Nr im Abfragenamen oder in der Beschreibung vermerken → spätere Textarbeit wird Fleißarbeit.
4. Datengenerator (`generate_quellsysteme.py`) liegt bei – Daten können bei Bedarf angepasst und neu erzeugt werden; in der Arbeit erwähnen („Befüllung per Skript“, von Kirchberg ausdrücklich erlaubt).
