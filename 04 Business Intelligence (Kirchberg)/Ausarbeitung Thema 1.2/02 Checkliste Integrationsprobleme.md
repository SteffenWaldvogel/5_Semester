# Checkliste – Integrationsprobleme aus Skript Kap. 7–8 → Quellsysteme → Lösung in Power Query

Kirchbergs Vorgabe: *„Achten Sie bei Ihrem Entwurf der Ausgangssysteme, dass alle im Skript genannten Probleme und Lösungsansätze, die im Rahmen einer Datenintegration auftreten können, auch bei Ihnen vorkommen und gelöst werden.“*

Diese Liste ist die Prüfmatrix dafür. Spalte **P-Nr** verweist auf `Quelldaten/Problemverzeichnis.csv` (dort steht die konkrete Zeile/der Schlüssel). Spalte **PQ-Lösung** = was im Power-Query-Schritt passiert. Die letzte Spalte hakst du beim Umsetzen ab.

Legende Systeme: **E** = ERP (NAVIRA), **S** = Shop (dartpro.shop), **C** = CRM (KontaktPilot), **H** = Hilfstabellen

---

## A. Extraktion (Kap. 7)

| Skript-Thema | S. | Eingebaut (P-Nr) | PQ-Lösung / Begründung in der Arbeit | ✓ |
|---|---|---|---|---|
| Extraktion Nettoänderungen vs. Vollabzug | 138 | P10, P62 – E hat `Geaendert_am`; S/C nur Vollabzug | Zwei ERP-Stände laden; Delta = Anti-Join/Merge über KdNr + Vergleich `Geaendert_am`. Begründen: Shop-/CRM-Export hat keinen Zeitstempel → Full Load. | ☐ |
| Informationsverlust bei Mehrfachänderung | 138/140 | P10 | Kann nicht gelöst, nur benannt werden (Grenze des Verfahrens) – 1 Satz in der Arbeit. | ☐ |
| Monitor-Typen / nicht unterstützende Quelle | 139 | P62 – CRM = Excel-Export (nicht explizit unterstützend) | Einordnung der drei Quellen in Abb. 7.2 (exportbasiert, zeitstempelbasiert, nicht unterstützend). | ☐ |
| Zeitpunkt des Exports | 141 | – (Annahme) | Annahme: periodisch, täglich nachts; Stichtag 31.10.2026. | ☐ |
| Interoperabler Export: ASCII, Trennzeichen, Zeichensatz | 141–143 | P61 – E: `;`, cp1252, Dezimalkomma; S: `,`, UTF-8, Dezimalpunkt; C: xlsx | `Csv.Document` mit Encoding 1252 bzw. 65001, Delimiter, Spaltentypen mit Gebietsschema (`de-DE` vs. `en-US`) setzen. ERP-Export-Assistent bietet „ASCII (MS-DOS)“ oder „ANSI (Windows)“ → Entscheidung ANSI begründen (Zeichensatzumsetzung S. 146). | ☐ |
| Lieferungen als eigene Tabelle / Teillieferungen | – (Aufgabenstellung) | P64, P65 | 1:n Auftrag→Lieferung; Shop hat nur `status = shipped` → Attribut/Tabelle-Konflikt; Retoure zu fehlendem Auftrag → Anti-Join ins Protokoll; Lieferdatum: ERP_Lieferung führend, Spalte in ERP_Auftrag ignorieren (Redundanz). | ☐ |
| Discard/Bad File (SQL*Loader-Prinzip) | 142 | alle Fehlersätze | Eigene Abfrage „Protokoll_Verworfen“: jeder Filter schreibt ausgefilterte Zeilen mit Grund in eine Protokolltabelle (Nachvollziehbarkeit!). | ☐ |

## B. Datenqualität / Bereinigung (8.1)

| Skript-Thema (Naumann-Liste + Abb. 8.3) | S. | Eingebaut (P-Nr) | PQ-Lösung | ✓ |
|---|---|---|---|---|
| Fehlerhafte / unzulässige Werte | 147 | P06 PLZ 99999 · P25 Menge −1 · P31 Geburtsdatum 1900 / Zukunft · P37 qty 0 | Bedingte Spalten/Filter mit Regel je Attribut; Menge −1 als Rücknahme interpretieren (Semantik!), nicht löschen. | ☐ |
| Genauigkeit | 148 | P15 Gewicht g vs. kg · Preise 2 Nachkommastellen | Umrechnung auf g; Rundung nach Netto/Brutto-Umrechnung begründen. | ☐ |
| Fehlende Werte / unterschiedliche Null-Kodierung | 148 | P03 `31.12.9999` · P04 `000` · P46 `n/a`/`unbekannt` · P58 `-1` · P38 leer statt 0 | `Table.ReplaceValue` → echte `null`; danach pro Attribut eine der sechs Strategien aus 8.1.3 (Tabelle in der Arbeit: Attribut → Strategie → Begründung). | ☐ |
| Default-Werte | 147 (Abb. 8.3) | P04 `000` · P31 `1900-01-01` · P51 `999-999` | Wie Null behandeln, im Protokoll kennzeichnen. | ☐ |
| Redundanz | 148 | P45 Adresse in C redundant zu E · P35/P53 Verein in E, S, C | Eine Quelle als führend festlegen (Priorisierung, S. 164). | ☐ |
| Uneinheitliche / undokumentierte Kodierung | 148 | P09 KdGruppe 01/02/03 · P14 MwSt-Code · P22 Status-Codes · P30/P47 Geschlecht · P52 Newsletter · P05/P29 Land | Mapping-Tabellen (eigene Abfragen) + Merge; alle Codes in einem „Kodierungsverzeichnis“ dokumentieren (Metadaten). | ☐ |
| Konsistenz / Widersprüche | 148 | P30 Shop `m` vs. ERP `Frau` · P43 CRM Geschlecht 2 vs. `Herr` · P49 alte Adresse im CRM | Regel: ERP führend für Stammdaten, Shop für E-Mail, CRM für Segment/Verein; Widersprüche ins Protokoll. | ☐ |
| Schlüsseleindeutigkeit | 148 | P01 KdNr 1001… = customer_id 1001… | Künstlicher Schlüssel (Index-Spalte) + Mapping-Tabelle `Map_Kunde` (DWH-Key ↔ ERP-KdNr ↔ Shop-ID ↔ CRM-ID); Quellpräfix „E-“, „S-“, „C-“ als Zwischenschritt. | ☐ |
| Referenzielle Integrität | 148 | P24 ArtNr fehlt · P26 KdNr 1099 · P36 customer_id 1099 · P57 CRM-0999 · P42 Betreuer ohne ERP-Pendant | Left-Anti-Join → Protokoll; Fakten mit unbekanntem Kunden auf Dummy „Unbekannt“ (Key −1) mappen statt verwerfen (Umsatz bleibt erhalten). | ☐ |
| Aktualität | 148 | P49, P54 | Vergleich `Letzter Kontakt` / `Geaendert_am`; Regel „jüngster Stand gewinnt“ pro Attribut. | ☐ |
| Dubletten | 147 | P27 Anna/Ann Berg (S) · P43 Mythenmetz/Mythenmez (C) | Matching-Schlüssel: E-Mail (lower/trim) → sonst Nachname + PLZ (+ Vorname-Initial); Fuzzy-Merge als Alternative diskutieren. | ☐ |
| Schreib-/Tippfehler, Repräsentation | 147 | P07 Nuernberg · P33 Gross/Dr. Berg · P43 Mythenmez · P53 „DC Oberschwaben“ | Normalisierung (ß→ss, Umlaute, Trim, Lower) vor dem Matching; Fuzzy-Merge mit Schwellwert. | ☐ |
| Data Profiling | 151 | alle Quellen | Spaltenqualität/-verteilung/-profil im PQ-Editor als Screenshot → Begründung der Regeln. | ☐ |
| Protokollierung von Filterungen | 147 | – | Siehe „Protokoll_Verworfen“ (A). | ☐ |

## C. Schema- und Datenintegration (8.2)

| Skript-Thema | S. | Eingebaut (P-Nr) | PQ-Lösung | ✓ |
|---|---|---|---|---|
| Datumsformate / Datentyp DATE | 152 | P34 ISO-UTC · P46 MM/DD/YYYY, DD.MM.YY · E DD.MM.YYYY · P63 Excel-Datum + Text gemischt | `Date.FromText` mit Culture, `DateTimeZone` → lokale Zeit, Jahrhundertregel (yy ≤ 30 → 20xx). | ☐ |
| Sprechende Schlüssel zerlegen | 152 | P12 ArtNr `KAT-MAT-LFD-Vn` | `Splitter.SplitTextByDelimiter("-")` → Kategorie, Material, LfdNr, Variante als Dimensionsattribute. | ☐ |
| Konfliktklassen Semantik/Struktur/Daten | 153 | Gliederung des Umsetzungsteils | Jede Lösung einer der drei Klassen zuordnen. | ☐ |
| Vollständigkeit, Korrektheit, Minimalität, Verständlichkeit | 154 | Zielschema | Abschnitt „Prüfung des integrierten Schemas gegen die vier Eigenschaften“. Korrektheit: Preis einheitlich **netto EUR** definieren. | ☐ |
| Heterogenitätsarten (Abb. 8.6) | 154–156 | syntaktisch P61 · strukturell P45/P18/P40 · schematisch P23/P39 · semantisch P22/P56 | Tabelle: Heterogenitätsart → Beispiel aus den Quellen → Lösung. | ☐ |
| Integrationsstrategie binär/n-är, Reihenfolge = Präferenz | 156–157 | Entscheidung | **Leiterartig**: ERP (vollständigstes Schema) → + Shop → + CRM. Begründen, Alternative One-Shot nennen. | ☐ |
| Vorintegration → Schemavergleich → Angleichung → Fusion | 157 | Vorgehen | Korrespondenztabelle (Spalte E ↔ S ↔ C ↔ Ziel) = Schemavergleich; Umbenennen/Typisieren = Angleichung; Append/Merge = Fusion. | ☐ |
| Synonyme | 157 | KdNr / customer_id / Kunden-Nr. · Preis_Netto / price_gross · Geb_Dat / birthdate / Geburtstag · P59 Call/Telefonat | Korrespondenztabelle + Umbenennung. | ☐ |
| Homonyme | 157 | P22/P56 „Status“ · P02 „Name1“ (Person vs. Firma) · „Typ“ (CRM Kontakt-Typ vs. Aktivitätstyp) | Präfixe im Zielschema (`Auftrag_Status`, `Kontakt_Status`). | ☐ |
| Fehlende Attribute | 157 | ERP ohne Geschlecht/Newsletter · Shop ohne Verkäufer · CRM ohne Umsatz | Belegungsregel je Attribut (z. B. Geschlecht aus Anrede ableiten, Verkäufer = „Online-Shop“). | ☐ |
| Fehlende, aber implizierte Attribute | 157 | P39 Kanal/Verkäufer im Shop implizit „Online“ · ERP `Kanal` explizit | Konstante Spalte `Kanal = "Online"` beim Shop ergänzen. | ☐ |
| Konfligierende Integritätsbedingungen – Datentypen | 158 | P28 PLZ als Zahl · P50 `1.012` · P32 `" 1009 "`/führende Null · KdNr numerisch vs. Text | Alles auf **Text** (wie Abb. 8.9: Kundennummer wird String); PLZ `Text.PadStart(5,"0")` nur für DE. | ☐ |
| – Bereichseinschränkungen | 158 | P21/P38 Rabatt 0–100 vs. 0–1 · P19 E-Mail NOT NULL nur im Shop | Vereinheitlichen auf Anteil 0–1; E-Mail optional im Ziel. | ☐ |
| – Default-Wert-Konflikte | 158 | P04/P31/P51 | Siehe B. | ☐ |
| – Dimensionshierarchien | 157 | P09/P48 KdGruppe vs. Segment vs. b2c/b2b | Zwei getrennte Attribute (Kundentyp, Segment) statt Zwang in eine Hierarchie → **Parallelklassifikation**. | ☐ |
| Attribut/Tabelle-Konflikt | 157 | P18 Warengruppe Tabelle vs. category Text · P40 Zahlung Tabelle vs. payment_method · P45 Adresse Feld vs. Spalten | Richtung „Tabelle“ (allgemeiner): Warengruppe-Mapping, Zahlart-Mapping; Adresse zerlegen. | ☐ |
| Schlüsselbehandlung: künstlicher Schlüssel + Mapping | 158 | P01 | `Map_Kunde`, `Map_Artikel`, `Map_Verkaeufer` als eigene Abfragen. | ☐ |
| Objektidentifikation ohne Schlüssel / Record Linkage | 158, 163 | P27, P33, P35, P42, P43 | Mehrstufig: 1) explizite Referenz (`erp_customer_no`, `ERP-Kunden-Nr.`) 2) E-Mail 3) Name+PLZ 4) Fuzzy. Trefferstufe als Spalte mitführen (Qualität). | ☐ |
| Beispiel Abb. 8.9: Titel abtrennen, Attribute weglassen, Belegungsregel | 159 | P02/P33/P44 Titel · Geburtsdatum selten gepflegt | Titel per Liste („Dr.“, „Dr. med.“, „Prof.“) extrahieren; entscheiden, ob Geburtsdatum → Altersklasse oder weglassen. | ☐ |
| Preis an Entität vs. Beziehung | 160–163 | P20 Listenpreis vs. Positionspreis | Zielschema: Preis **an der Faktenzeile** (allgemeiner), Listenpreis zusätzlich in Dim_Artikel. | ☐ |
| Kompositer PK → n:m / Star-Schema | 160 | AufNr+Pos, order_id+line | Fakt_Verkauf mit Surrogat-Key, Dimensionen Kunde/Artikel/Verkäufer/Zeit/Kanal. | ☐ |
| Redundante Beziehungen eliminieren / Generalisierung | 160–161 | Shop `orders` + ERP `Auftrag` → **Verkauf**; CRM Call/Mail/Besuch → **Kontaktaktivität** | Append zu einer Faktentabelle mit `Quelle`-Spalte (Generalisierung). | ☐ |
| Extensionale Beziehungen (Äquivalenz/Teilmenge/Überlappung/Disjunkt) | 163 | P17 Artikel überlappend · P35/P55 Kunden überlappend, Leads nur CRM · P41 **Fakten überlappend** (Shop-Importe im ERP) | Kunden: Full Outer Join über Mapping. Fakten: Shop-Auftrag mit `Ext_Referenz = "WEB-"&order_id` im ERP → **nur einmal** zählen; Regel + Zahl der Dubletten dokumentieren. | ☐ |
| Tabelle 8.3 (Mythenmetz) | 164 | P43 nachgebaut | Explizit als Beispiel in der Arbeit zeigen (Dozent kennt es). | ☐ |
| Quellsysteme priorisieren | 164 | Entscheidung | Prioritätstabelle je Attribut (Name/Adresse: E > C > S; E-Mail: S > C > E; Segment/Verein: C). | ☐ |
| Harmonisierung 1: Datentypen | 164 | P28, P50, P32 | s. o. | ☐ |
| Harmonisierung 2: Kodierungen | 164 | P05/P29 Land · P30/P47 Geschlecht · P52 Newsletter · P59 Aktivitätstyp · P14 MwSt | Mapping-Tabellen. | ☐ |
| Harmonisierung 3: Zeichenketten | 165 | P08 Str./Straße · P07 Umlaute · P33 ß | `Text.Replace`-Kette, Trim/Clean/Proper. | ☐ |
| Harmonisierung 4: Maßeinheiten | 165 | P15 g/kg · P15 netto/brutto · P16 CHF | Umrechnung mit Hilfstabelle `Wechselkurse`; Brutto→Netto über MwSt-Code des Artikels. | ☐ |
| Harmonisierung 5: Separierung | 165 | P45 Adresse · P02/P44 Name · P12 ArtNr | Spalte teilen nach Trennzeichen/Position. | ☐ |
| Attributäquivalenz stark/schwach/disjunkt | 165 | stark: Land, Geschlecht · schwach: P09/P48 Kundengruppe↔Segment · disjunkt: Spielerprofil | Je ein Beispiel benennen; bei schwach: kleinster gemeinsamer Nenner (Kundentyp Privat/Verein/Händler). | ☐ |
| Phasen: Elementizing → Standardizing → Verification → Matching → Householding | 165–167 | Reihenfolge der Abfrageschritte | Abfragen so benennen (`10_Elementize_CRM`, `20_Standardize_…`). Verification: PLZ↔Land (P06, P60), PLZ↔Ort (P07/P28). Householding: P53 Verein, P27/P03 Haushalt Berg (gleiche Adresse). | ☐ |
| Verdichtung | 167 | optional | Monatsumsatz je Verkäufer × Kundentyp als Beispiel-Pivot. | ☐ |
| Anreicherung | 167 | P60 Bundesland aus PLZ · Netto zusätzlich zu Brutto · Altersklasse | Merge mit `PLZ_Bundesland`; berechnete Spalten. | ☐ |
| Metadaten-Repositorium / Dokumentation | 167 | – | Abfrage-Beschreibungen in PQ + Korrespondenz- und Kodierungstabellen im Anhang. | ☐ |

## D. Transformation, Übernahme, Historisierung (8.3–8.5)

| Skript-Thema | S. | Eingebaut (P-Nr) | PQ-Lösung | ✓ |
|---|---|---|---|---|
| Datensatzebene: Filterung, Verknüpfung, nicht verknüpfbare Sätze | 167 | P22 Storno 90 / cancelled · P24/P26/P36 | Filter + Protokoll; Anti-Join-Liste „manuell prüfen“. | ☐ |
| Attributebene: Kennzahlen ableiten | 168 | – | `Umsatz_Netto = Menge × EPreis × (1 − Rabatt)`; Brutto über MwSt. | ☐ |
| INSERT APPEND / UPSERT-MERGE / Replikation | 168–171 | Grenze von PQ | PQ lädt vollständig neu (kein MERGE) → als Alternative/Grenze diskutieren; Lösung mit Datenbank nennen. | ☐ |
| Historisierung: Umzug-Beispiel | 171 | P11 Steiner 1005 zieht um, Aufträge vor/nach Umzug | Zeigen, dass Umsatz vor 15.10. zur alten Adresse/PLZ gehört. | ☐ |
| Verfahren: Überschreiben / Versionsnr. + Current Flag / Gültig-von-bis | 171–172 | zwei ERP-Stände (P10) | `Dim_Kunde` mit `Gueltig_von`, `Gueltig_bis` (31.12.9999 für aktuell), `Version`, `Ist_Aktuell`; Aufbau: Stand 1 = Erstladung (von = 30.09.), geänderte Sätze aus Stand 2 → alter Satz bis = 31.10., neuer Satz von = 31.10. Fakten über Datum an gültige Version anbinden (Fremdschlüssel mit Datumsbezug). | ☐ |
| Dimensionen ändern sich selten, Fakten oft | 171 | – | Nur Dim_Kunde historisieren, Dim_Artikel überschreiben – begründen. | ☐ |
| Unstrukturierte Daten (8.6) | 172 | CRM `Ergebnis`-Freitext | Bewusst **nicht** integriert → 1 Satz Abgrenzung. | ☐ |

---

## Zählung
65 registrierte Einzelprobleme (P01–P65) decken alle oben gelisteten Skript-Themen ab. Für die Arbeit reicht es, pro Skript-Thema **ein** Beispiel sauber zu zeigen und die restlichen in einer Anhangstabelle zu listen – Kirchberg bewertet Begründung und Alternativen, nicht Masse.

## Vorschlag Gliederung „Themenbearbeitung“ (8–12 Seiten)
1. Szenario und Auswertungsziel (½ S.) – Verkäufer × Kundenmerkmale
2. Entwurf der drei Quellsysteme (1½ S.) – Tabellen, bewusst eingebaute Heterogenität (Verweis auf Problemverzeichnis)
3. Zielschema (1 S.) – Star-Schema, Prüfung gegen Vollständigkeit/Korrektheit/Minimalität/Verständlichkeit
4. Extraktionsstrategie (½ S.)
5. Integrationsablauf in Power Query (4–5 S.) – entlang der Phasen Filterung → Harmonisierung → Verdichtung → Anreicherung; je Phase: Problem, Entscheidung, Alternative, Umsetzung (Screenshot/M-Code-Ausschnitt)
6. Historisierung (1 S.)
7. Ergebnis mit Beispieldaten (1 S.) – Auswertung Verkäufer × Kundentyp × Bundesland
