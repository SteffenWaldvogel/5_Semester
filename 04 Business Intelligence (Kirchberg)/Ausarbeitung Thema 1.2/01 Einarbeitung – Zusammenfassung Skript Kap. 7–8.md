# Einarbeitung BI-Portfolio – Zusammenfassung Skript Kap. 7 + 8
Quelle: Kirchberg, Skript Business Intelligence v2.2 (01.10.2026), S. 137–174.
Zweck: Alles, was für Thema 1.2 (Datenintegration ERP / Online-Shop / CRM mit Power Query) relevant ist. Seitenzahlen = Skript-Seiten, damit du nachschlagen kannst.

---

## 0. Der große Bogen (Abb. 8.1, S. 145)

```
Quellsysteme ──Extraktion──▶ 1. Filterung ──▶ 2. Harmonisierung ──▶ 3. Verdichtung ──▶ 4. Anreicherung ──▶ DWH
   (Kap. 7)                  (8.1 Bereinigung)   (8.2 Schema- +           (optional)        (abgeleitete Werte)
                                                   Datenintegration)
```

Für die Ausarbeitung heißt das: Jede Power-Query-Abfrage lässt sich einer dieser Phasen zuordnen. Das ist ein gutes Gliederungsgerüst für den Umsetzungsteil.

---

## 1. Kapitel 7 – Extraktion aus Quellsystemen (S. 137–143)

### 1.1 Zwei Klassifikationen von Quellsystemen (S. 138)

**A) Nach Umfang der Extraktion**
| Variante | Idee | Voraussetzung / Problem |
|---|---|---|
| **Extraktion der Nettoänderungen (Delta)** | Nur seit dem letzten Lauf geänderte Sätze (neu, gelöscht; Änderung = löschen + neu einfügen) | Braucht Zeitstempel im Quellsystem; nachträglicher Einbau (Trigger) bei Standardsoftware oft nicht möglich |
| **Kompletter Abzug (Full Load)** | Gesamter Bestand | Wenn Delta technisch nicht geht oder sehr viele Änderungen |

**Informationsverlust** (S. 138, 140): Ändert sich ein Objekt zwischen zwei Läufen mehrfach, kommt nur der letzte Stand an. Lösung: Protokollierung aller Änderungen im Quellsystem, Log-Auswertung oder Replikation.

**B) Nach Kooperationsbereitschaft – „Monitore“ (Abb. 7.2, S. 139)**
| Quellentyp | Mechanismus |
|---|---|
| Replikationsquellen | Änderungen werden synchron direkt propagiert (engste Kopplung) |
| Trigger-basiert / aktive Quellen | DB-Trigger melden Änderungen (Oracle CDC synchron) |
| Snapshot-Quellen | Konsistente logische Kopie, ohne Sperren extrahierbar |
| Exportbasiert / zeitstempelbasiert | Database dump; Zeitstempel je Satz für Delta |
| Protokollierende Quellen (log-basiert) | Log sniffer liest Änderungen aus DB-Logs (proprietär!) |
| Nicht explizit unterstützende Quellen | Altsysteme → Adapter oder Individualsoftware |

**Aktualität** (S. 140): Üblich ist ein Lauf pro Tag → Daten vom Vortag. Für kritische Anwendungen: Near-Real-Time / Right-Time / Living DWH.

### 1.2 Zugriff auf heterogene Quellen (7.2, S. 140–141)
Abstraktionsebenen: Anwendungsdialog (Altsystem simulieren) → Anwendungsebene / API (z. B. SAP BAPI) → Datenbankebene (direkter DB-Zugriff) → Protokollierungsebene (Log-Dateien).

### 1.3 Export und Import (7.3, S. 141–143)
- **Zeitpunkt** (7.3.1): periodisch, anfragegesteuert, ereignisgesteuert (Zeit-, DB- oder externes Ereignis, z. B. n Änderungen), sofort (Replikation).
- **Interoperabel** (7.3.2): ASCII-/Textdateien als kleinster gemeinsamer Nenner; Trennzeichen (z. B. `|`, `;`, `,`); Ladeprogramme wie DB2 LOAD oder Oracle SQL*Loader mit Control File → Filter → *discard file* (Filter nicht erfüllt) / *bad file* (nicht interpretierbar oder Integritätsverletzung). Tabelle 7.1: Ladeprogramm vs. INSERT → automatische Commits, optionales Logging, Teilprüfung der Integrität, Trigger unterdrückt, Sperren.
- **Proprietär** (7.3.3): nur gleiche Plattform (DB2 IXF, Oracle transportable tablespaces); Vorteil: Metadaten kommen mit, viel schneller.
- Dazwischen optional: Netztransfer, Komprimierung, Verschlüsselung.

> **Für Power Query:** Alle drei Quellen werden als *exportbasierte, interoperable* Quellen behandelt (CSV/XLSX-Export, periodisch, Full Load). Delta nur, wo ein Zeitstempel existiert (ERP `Geaendert_am`). Das in der Arbeit zu begründen ist ein Pluspunkt – auch zu nennen, was dabei verloren geht (Mehrfachänderungen).

---

## 2. Kapitel 8.1 – Datenbereinigung / Datenqualität (S. 145–151)

**Grundsatz:** Der größte Fehler ist die ungeprüfte Übernahme von Quelldaten. Jede Filterung = Datenverlust → **protokollieren**.

### 2.1 Mängelklassifikation nach Kemper (Tab. 8.1, S. 146)
| | 1. Klasse: autom. erkennen + autom. korrigieren | 2. Klasse: autom. erkennen, manuell korrigieren | 3. Klasse: manuell erkennen + korrigieren |
|---|---|---|---|
| **Syntaktisch** (Form/Code) | bekannte Formatanpassungen (Datumsformate, Sonderzeichen) | erkennbare Formatinkompatibilitäten | – |
| **Semantisch** (Inhalt) | fehlende Werte (z. B. Planwert statt Istwert) | Ausreißer, unstimmige Wertekonstellationen | unerkannte Fehler in den Quellen |

### 2.2 Typische Fehlerarten (Abb. 8.3, S. 147 – Köppen)
Eindeutigkeit · unterschiedliche Repräsentation · Widersprüche · referenzielle Integrität · Unvollständigkeit · kodierte Default-Werte (999-999, 99999) · Dubletten · falsche/unzulässige Werte · Schreib-/Tippfehler.

### 2.3 Datenqualitätsprobleme nach Naumann (8.1.1.1, S. 147–148) – **die Kernliste**
1. **Fehlerhafte / unzulässige Werte** – Wertebereich verletzt, Quellsystem prüft nicht
2. **Zuverlässigkeit** – subjektive Erfassungsspielräume
3. **Genauigkeit** – Nachkommastellen, Tagesgenauigkeit
4. **Fehlende Werte / Nullwerte** – unterschiedlich kodiert: `-1`, `31.12.9999` (SAP), leer; Null kann auch Semantik haben
5. **Redundanz** – nicht normalisierte Quellen; Inkonsistenz bei redundanten Infos aus mehreren Quellen
6. **Unverständlichkeit / uneinheitliche Kodierung** – undokumentierte Codes
7. **Konsistenz** – Widerspruchsfreiheit über Systeme hinweg
8. **Schlüsseleindeutigkeit** – PKs müssen systemübergreifend eindeutig sein
9. **Referenzielle Integrität** – FK zeigt ins Leere
10. **Aktualität** – Zeitabstand seit Erzeugung; noch gültig?

### 2.4 Qualitätsmerkmale (8.1.1.2, S. 148–149)
Wang/Strong, 15 Merkmale in 4 Klassen: intrinsisch (Glaubhaftigkeit, Genauigkeit, Objektivität, Reputation), kontextuell (Mehrwert, Relevanz, Zeitnähe, Vollständigkeit, Datenmenge), repräsentationell (Interpretierbarkeit, Verständlichkeit, Konsistenz und Knappheit der Darstellung), Zugriff (Verfügbarkeit, Sicherheit). Hinrichs-Gruppierung für DWH: Glaubwürdigkeit, Nützlichkeit, Interpretierbarkeit, Schlüsselintegrität. Definition: *Datenqualität = Erfüllungsgrad der Anforderungen für einen Zweck* → ohne messbare Anforderungen keine Aussage.

### 2.5 Qualitätsverbesserung (8.1.2, S. 150–151)
Besser in den Quellsystemen (Fachabteilungen verantwortlich) als nachträglich im DWH. Richtlinien nach English: unternehmensweite Datendefinition, nur benötigte Daten (kein „Datenfriedhof“), Detaildaten übernehmen (Nachvollziehbarkeit), Metadaten ablegen. **Data Profiling**: Statistiken (Null-Anzahl, Min/Max, distinct) → Regeln ableiten. *(Power Query: Spaltenqualität/-verteilung/-profil!)*

### 2.6 Umgang mit fehlenden Werten (8.1.3, S. 151) – **pro Attribut entscheiden und begründen**
| Option | Wann |
|---|---|
| Attribut ignorieren | genug andere vollständige Attribute |
| Manuell nachtragen | kleine Mengen, interne Daten |
| Globale Konstante („unbekannt“) | Leer = Information oder viele fehlen |
| Klassen-Durchschnitt | numerisch, Werte liegen dicht |
| Wahrscheinlichster Wert (statistisch) | wenige Fälle, gute Anhaltspunkte, aufwändig |
| Satz als fehlerhaft markieren, ausschließen | genug vollständige Daten |

Jede Methode verändert den Bestand (Verteilung!) → nie informationsneutral, aber unvermeidbar.

---

## 3. Kapitel 8.2 – Daten- und Schemaintegration (S. 151–167)

### 3.1 Schematransformation (S. 151–152)
Exportschema → Staging-Schema. Von Formatkonvertierung (Datum → DATE) bis zur **Zerlegung sprechender Schlüssel** (Teilenummer = Werk + Produktgruppe + Variante …) in explizite Attribute. Einmalig beim Anbinden, aber laufend zu pflegen.

### 3.2 Drei Konfliktklassen (S. 153)
- **Semantik**: gleiche Gegenstände unterschiedlich erfasst → meist manuell (Ontologien, KI als Hilfe)
- **Struktur**: inkompatible Schemata → Schemaintegration
- **Daten**: dasselbe Objekt mit widersprüchlichen Werten

### 3.3 Anforderungen an das integrierte Schema (Conrad, S. 154)
**Vollständigkeit** (nichts geht verloren) · **Korrektheit** (Semantik erhalten, z. B. „Preis“ mit/ohne MwSt. einheitlich) · **Minimalität** (keine Redundanz, jeder Gegenstand einmal) · **Verständlichkeit** (dokumentiert).

### 3.4 Heterogenitätsarten (Abb. 8.6, S. 154–156, Hartmann)
Von gering zu hoch semantisch: Plattform/technisch → **syntaktisch** (Zahlenformate, Zeichenkodierung, Trennzeichen – per Parser lösbar) → Modellierungsheterogenität (**Datenmodell**, **strukturell**: gleiche Realität anders dargestellt, normalisiert/denormalisiert; **schematisch**: derselbe Sachverhalt als Entität *oder* Attribut *oder* Wert) → **semantisch** (Bedeutung der Begriffe, Kontext, Domänenwissen) → Anwendungsprogramm/funktional.

### 3.5 Prozess der Schemaintegration (8.2.2.2, S. 156–157)
Strategien: **binär** (leiterartig = left deep tree, balanciert) vs. **n-är** (One-Shot, iterativ). Reihenfolge = implizite Präferenz (erstes Schema prägt). Schritte nach Leser/Naumann: **Vorintegration** (Auswahl, Reihenfolge, Zusatzinfos) → **Schemavergleich** (Korrespondenzen, Konflikte) → **Schemaangleichung** (Namen, Typen vereinheitlichen, (de)normalisieren) → **Schemafusion + Umstrukturierung**.

### 3.6 Schemakonflikte (Abb. 8.8, S. 157–158) – **zweite Kernliste**
| Ebene | Konflikt |
|---|---|
| Tabelle/Tabelle | Benennung: **Synonyme**, **Homonyme**; Struktur: **fehlende Attribute**, **fehlende, aber implizierte Attribute** (z. B. Lieferweg „Luft“ nur implizit); **konfligierende Integritätsbedingungen** (Dimensionshierarchien → Hierarchieebenen einziehen / Parallelklassifikation) |
| Attribut/Attribut | Benennung (Synonyme/Homonyme); **Default-Wert-Konflikte**; konfligierende Integritätsbedingungen: **Datentypen**, **Bereichseinschränkungen** (NOT NULL, CHECK) |
| Attribut/Tabelle | Sachverhalt in A als Attribut, in B als eigene Tabelle/Entität |

**Schlüsselbehandlung** (S. 158): Quellschlüssel meist nicht global eindeutig → **künstlicher Schlüssel** + jederzeit mögliche Zuordnung Quellschlüssel ↔ DWH-Schlüssel (Mapping-Tabelle). **Objektidentifikation** ohne gemeinsamen Schlüssel über charakteristische Attribute (Name, Bezeichnung) → Tippfehler gefährlich → probabilistisches **Record Linkage** mit Ähnlichkeitsgewichten.

**Beispiel Abb. 8.9 (S. 159)** – prüfungsnah: Kundennummer wird String (weil ein System nicht-numerische Nummern hat); Titel aus Namensfeld abtrennen; nur auswertungsrelevante Attribute (Geburtsdatum weglassen, wenn zu selten gepflegt); Attribute, die nur in einem System existieren (Kundenwert, Risiko) → Belegungsregel für die anderen definieren (z. B. Durchschnitt). **Dokumentation der Integration = Transformationsregeln für ETL.**

### 3.7 Anpassung unterschiedlicher Modellierungen (8.2.2.4, S. 159–161)
- Attribut ↔ eigenständige Entität (1:n) sind äquivalent
- Kompositer PK (A,B) + X ↔ zwei Entitäten mit n:m-Beziehung, X an der Beziehung → **Grundlage des Star-Schemas** (ShopNr, ProduktNr, Anzahl)
- Redundante Beziehungen eliminieren (direkte n:m überflüssig, wenn über E1 abgebildet)
- Vereinfachung durch Generalisierung (Bareinlage + Überweisung → Kontobewegung)
- Lösungsansätze: zusicherungsbasiert, Upward Inheritance, formal objektorientiert, Generic Integration Model

### 3.8 Beispiel 8.2.2.5 (S. 161–163) – Vorgehensmuster
1. Entsprechungen finden (Kunden = Abnehmer, KName = Name …) 2. Namenswahl im Zielschema 3. keine Attribute verlieren (Branche mitnehmen) 4. Entität vs. Beziehung → Entität 5. **Preis an Entität (S1) vs. an Beziehung (S2) → allgemeinere Variante (an der Beziehung) wählen**, sonst nicht einspielbar 6. nur in einem Schema vorhandene Teile übernehmen und Befüllungsregel festlegen.

### 3.9 Datenzusammenführung (8.2.3, S. 163–164)
Vier **extensionale Beziehungen** (Jung): Äquivalenz · Einschluss/Teilmenge · **Überlappung** · Disjunktheit. Die ersten drei sind schwierig bei unterschiedlichen PKs → Gleichheitskriterien über Attribute, ggf. nur Wahrscheinlichkeit (Record Linkage). Tab. 8.3: Mythenmetz – Geschlecht `m` vs. `1`, Anrede widersprüchlich, Datum `22.10.88` vs. `1988-10-22`, verschiedene IDs → Redundanz. **Lösung: einheitliche Kodierung festlegen + Quellsysteme priorisieren + Regeln definieren.**

### 3.10 Harmonisierung (8.2.4, S. 164–165) – **dritte Kernliste**
1. **Anpassung von Datentypen** (Rechnungsnummer Zahl vs. String)
2. **Vereinheitlichung von Kodierungen** (1/0, J/N; Null-Kodierungen wie 31.12.9999)
3. **Vereinheitlichung von Zeichenketten** (Str. → Straße, systemspezifische Codes)
4. **Umrechnung von Maßeinheiten** (Währungen, cm/Zoll)
5. **Separierung von Attributwerten** (BLZ aus IBAN, Adresse zerlegen)

**Attributäquivalenz** (Larson, Abb. 8.17): **stark** (1:1 oder 1:0 → Werte vereinheitlichen), **schwach** (1:n → kleinster gemeinsamer Nenner), **disjunkt** (keine Regel nötig).

### 3.11 Phasen der Zusammenführung pro Datensatz (8.2.5, S. 165–167) – **Reihenfolge der Power-Query-Schritte**
1. **Elementizing** – zerlegen (Adresse → PLZ, Ort, Bundesland)
2. **Standardizing** – Standardform (Abkürzungen, Datumsformate, Geschlecht 0/1 – M/W – m/f, zweistellige Jahre → Jahrhundertregel, Monat/Jahr → Standardtag 1. oder 15., Zeitzonen, Maßeinheiten)
3. **Verification** – Plausibilität (PLZ 06120 ≠ Bayern) → verwerfen / korrigieren / Rückmeldung
4. **Matching** – Abgleich mit Bestand, Objekt ergänzen/aktualisieren
5. **Householding** – Gruppen bilden (Käuferklassen, Haushalt → Cross-Selling)

Danach optional **Verdichtung** (Wochensummen) und **Anreicherung** (Netto zusätzlich zu Brutto, Bundesland aus PLZ). Alles im **Metadaten-Repositorium** dokumentieren (Herkunft rekonstruierbar). Erkennen ≠ Lösen: Fehler sind Indikator für Handlungsbedarf in den Quellen.

---

## 4. Kapitel 8.3 – Datentransformation (S. 167–168)
- **Datensatzebene**: Filterung (mehr exportiert als nötig), Verknüpfung (Join) gemäß Schemazusammenführung – setzt bereinigte Daten voraus; nicht verknüpfbare Sätze manuell prüfen
- **Attributebene**: Konvertierungen + **Ableitung von Kennzahlen** (Umsatz = Preis × Menge)
- Abschluss: interne Aktualisierung/Propagierung in abhängige Datenbasen (Filter + Aggregation)

## 5. Kapitel 8.4 – Datenübernahmeprozess (S. 168–171)
- Explizit: `INSERT /*+APPEND*/ … SELECT`, **UPSERT/MERGE** (`WHEN MATCHED UPDATE / WHEN NOT MATCHED INSERT`), prozedural (PL/SQL, Cursor = langsam; inline SQL PL)
- Replikation: asymmetrisch (**Datenverteilung**, **Datenzusammenführung** = DWH-relevant, Konflikte bei Überlappung) vs. symmetrisch (update anywhere); synchron vs. asynchron (schwache Konsistenz)
> *Power Query lädt immer komplett neu (kein MERGE) – das ist ein Punkt für die Diskussion „Alternativen/Grenzen“.*

## 6. Kapitel 8.5 – Historisierung (S. 171–172) – **vierte Kernliste**
Warum: Änderungen nicht überschreiben, zeitlich korrekter Bezug (Beispiel **Kunde zieht um** → Einkäufe dürfen nicht zum neuen Wohnort „wandern“). Dimensionen ändern sich selten, Fakten oft. Verfahren:
| Verfahren | Mechanik |
|---|---|
| Überschreiben | nur aktueller Stand relevant |
| **Schlüsselerweiterung / Versionsnummer** + **Current Flag** (Abb. 8.19, Kemper) | Version je Änderung +1, Flag markiert aktuellen Satz, Hauptschlüssel bleibt |
| **Gültig-von/bis** (Abb. 8.20) | Erstladung: von = ETL-Zeitpunkt, bis = leer/31.12.9999; Änderung: alter Satz bis = ETL-Zeitpunkt, neuer Satz wie Neuzugang; Vergleich mit `<` |
| Je Attribut Gültigkeitszeitraum | sehr aufwändig, geringer Zusatznutzen |
Ggf. Fremdschlüssel mit Datumsbezug pflegen → Ladeprozess wird komplexer.

## 7. Kapitel 8.6 – Unstrukturierte Daten (S. 172–173) – Randthema
Texte sind „schmutzig“ (Rechtschreibung, Abkürzungen), Extraktoren, iterativer Prozess, Unsicherheit → für Thema 1.2 höchstens als Abgrenzung (z. B. CRM-Freitextnotizen bewusst nicht integriert).

---

## 8. Was Kirchberg bewertet (aus „Portfolio Themen + Rahmenbedingungen“)
- 8–12 Inhaltsseiten; **Einleitung, Themenbearbeitung, Zusammenfassung**. **Keine** theoretischen Grundlagen, keine kritische Reflexion, kein Ausblick. Literatur zählt nicht.
- Bewertung „wie ein Programmentwurf“: Weg zur Umsetzung, **Entscheidungen begründen, Alternativen nennen und diskutieren, eigene Leistung herausstellen**.
- Datenstrukturen und Daten selbst entwerfen, Besonderheiten der Branche (Dart-Zubehör) berücksichtigen. Befüllung per Skript oder KI ist erlaubt.
- **Alle im Skript genannten Probleme und Lösungsansätze müssen vorkommen und gelöst werden.** → siehe `02 Checkliste Integrationsprobleme.md`
- Alles minimalistisch umgesetzt = 20/30 P („befriedigend“). Mehr Punkte durch Tiefe bei Begründung/Alternativen, nicht durch Umfang.
- Abgabe **27.11.2026, 24:00**, PDF an kirchberg@dhbw-ravensburg.de **von der DHBW-Adresse**. Präsentation: 2 Folien, 5 Min., T-Laufwerk `Kirchberg/BI`.
