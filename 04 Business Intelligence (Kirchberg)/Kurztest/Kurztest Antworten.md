# Kurztest BI (Kirchberg) – Aufgaben und Antworten

Dokumentation aller Aufgaben der Kurztest-Seite mit richtiger Antwort, Begründung und Quelle.
Seitenangaben = gedruckte Seitenzahl im BI Skript v2.2 (PDF-Seite = gedruckte Seite + 1).

---

# Thema 1: Umfang und Einsatzmöglichkeiten von BI (Kapitel 1)

## Aufgabe 1 – Perspektiven einer BI-Strategie (Zuordnung)
**Frage:** Begriffe den Perspektiven Architektur/Technologie, Fachlichkeit, Organisation zuordnen.

| Begriff | Zuordnung |
|---|---|
| Prozesse | Organisation |
| Informationsbedarf | Fachlichkeit |
| Flexibilität | Architektur/Technologie |
| Governance | Organisation |
| Performance | Architektur/Technologie |
| Rollen | Organisation |
| Kennzahlen | Fachlichkeit |
| Integrationsgrad | Fachlichkeit |
| Komplexität | Architektur/Technologie |
| Standardisierung | Architektur/Technologie |

**Begründung:** Technologie = Infrastruktur/Systeme (Performance …), Organisation = Prozesse, Funktionen, Rollen, Fachlichkeit = fachliche Inhalte, Kennzahlen, Informationsbedarf. Die übrigen Begriffe stehen nur in der Abbildung. Achtung: Integrationsgrad gehört zur Fachlichkeit, nicht zur Technologie.
**Quelle:** S. 20, Abb. 1.11 (siehe Bild im Ordner). Zuordnung von Flexibilität, Integrationsgrad, Komplexität, Standardisierung aus der Abbildung abgeleitet, auf der Testseite noch nicht bestätigt.

## Aufgabe 2 – Fragestellungen und Analyseformen (Drag & Drop)
| Frage | Antwort |
|---|---|
| Was soll geschehen? | Prescriptive Analytics |
| Was könnte geschehen? | Predictive Analytics |
| Was geschieht gerade? | Monitoring |
| Warum ist etwas geschehen? | OLAP |
| Was ist geschehen? | Reporting |

**Begründung:** Reporting beschreibt Vergangenes, Monitoring liefert aktuelle Daten, OLAP dient der Ursachenanalyse, Predictive betrachtet die Zukunft, Prescriptive liefert Steuerungsmaßnahmen.
**Quelle:** S. 8, Abb. 1.4.

## Aufgabe 3 – Mobile Offline-BI (Single Choice)
**Frage:** Welche zusätzliche Komponente ist erforderlich, um auch mobil Offline-BI-Lösungen nutzen zu können?
**Antwort:** Synchronisation
**Begründung:** Offline braucht lokale Datenhaltung auf dem Mobilgerät. Änderungen am zentralen Datenbestand müssen regelmäßig übertragen werden, dafür ist eine Synchronisationskomponente nötig.
**Quelle:** S. 33–34.

## Aufgabe 4 – Transaktionale vs. analytische Systeme (Zuordnung)
| Merkmal | Zuordnung |
|---|---|
| Periodische Aktualisierung | Analytische Informationssysteme |
| Bereichsanfragen | Analytische Informationssysteme |
| Verdichtete Daten | Analytische Informationssysteme |
| Lange Leseoperationen | Analytische Informationssysteme |
| Einzelsatzzugriffe | Transaktionale Systeme |
| Detaillierte Einzeldaten | Transaktionale Systeme |
| Aktualisierung durch Geschäftsvorfälle | Transaktionale Systeme |
| Durchgängig sehr schnelle Antwortzeiten | Transaktionale Systeme |

**Quelle:** S. 7, Tabelle 1.1. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 5 – Analyseorientiertes BI-Verständnis nach Kemper (Multiple Choice, 4 richtig)
**Antwort:** Data Mining, OLAP, Text Mining, Ad-hoc-Reporting
**Nicht dazu:** Data Warehouse, ETL-Prozess, Standard-Reporting (gehören erst zum weiten BI-Verständnis).
**Begründung:** ETL und DWH sind technische Aspekte. Standard-Reporting ist kein analytischer Vorgang mit Aktionen eines Analysten.
**Quelle:** S. 11, Abb. 1.6.

## Aufgabe 6 – Kompetenzen Data Scientist vs. BI-Analyst (Zuordnung)
| Kompetenz | Zuordnung |
|---|---|
| Statistische Modellierung | Data Scientist |
| Leistungsstarke Hardware | Data Scientist |
| Programmierkenntnisse | Data Scientist |
| Usability | BI-Analyst |
| Geschäftsverständnis | BI-Analyst |
| OLAP-Werkzeuge | BI-Analyst |
| Kommunikative Fähigkeiten | BI-Analyst |

**Quelle:** S. 16–17, Abschnitt 1.3.3. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 7 – Maschinelles Lernen (Lückentext)
1. Das **überwachte** Lernen ist ein Lernen aus Beispielen.
2. … über ein in der Datenanalyse erstelltes **Modell** Zusammenhänge zu beschreiben
3. … und **Vorhersagen** auf Daten durchzuführen, bei denen zusammenhängende Werte nicht bekannt sind.
4. **Unüberwachte** Methoden ermitteln Muster, die zuvor nicht bekannt sind.
5. Bei **semi-überwachten** Methoden handelt es sich um eine Mischform.

**Quelle:** S. 17, Abschnitt 1.3.4.

## Aufgabe 8 – Analysearten (Lückentext)
1. **Descriptive** Analytics: Dokumentation und Beschreibung, was in der Vergangenheit geschehen ist.
2. **Diagnostic** Analytics: Ursachenanalyse, Frage nach dem Warum.
3. **Real-Time** Analytics: aktuelle Situation, Analyse innerhalb zeitlicher Schranken.
4. **Predictive** Analytics: Vorhersagen für die Zukunft und von unbekannten Werten.
5. **Prescriptive** Analytics: mit welchen Handlungen ein Ziel am besten erreicht wird, höchste Form der Entscheidungsunterstützung.

**Quelle:** S. 8, Abschnitt 1.1.2.

## Aufgabe 9 – Aufgaben einer BI-Strategie (Multiple Choice, 2 richtig)
**Antwort:**
- Sicherung des langfristigen Erfolgs beim Einsatz von BI-Lösungen.
- Festlegung der unternehmensrelevanten Kennzahlen.

**Falsch:** „Informationsangebot ausreichend dokumentiert“ und „Kosten im Betrieb und Wartung kontrollieren“. Beides sind Aufgaben der BI-Governance, nicht der Strategie.
**Quelle:** S. 20 (Strategie), S. 22 (Governance-Liste).

## Aufgabe 10 – Hierarchie der BI-Strategie (Abbildung, Dropdowns)
- (1) IT-Strategie (linker Pfeil, Gegenstück zur Business-Strategie)
- (2) BI (Pyramidenspitze)
- (3) Vision
- (4) Grundsätze
- (5) Strategie
- (6) Operative Ziele

**Quelle:** S. 19, Abb. 1.10.

## Aufgabe 11 – Data Science vs. Data Mining (Single Choice)
**Antwort:** Data Mining ist ein möglicher Teilschritt von Data Science.
**Begründung:** Data Science integriert Datenanalysen in einen strukturierten Analyseprozess, in dem Data Mining und andere Analysetechniken zielorientiert eingesetzt werden.
**Quelle:** S. 15–16, Abschnitt 1.3.

## Aufgabe 12 – Personenbezogene Daten im Data Warehouse (Multiple Choice, 2 richtig)
**Antwort:**
- Wenn eine Einverständniserklärung der Betroffenen vorliegt.
- Wenn die Daten anonymisiert sind.

**Falsch:** „Wenn daraus KPIs ermittelt werden können“, „Wenn über Zugriffsrechte die Verwendung verhindert wird“.
**Begründung:** Anonyme Daten dürfen immer verarbeitet werden. Ohne Anonymisierung/Pseudonymisierung und ohne Notwendigkeit für den Geschäftszweck braucht man das Einverständnis.
**Quelle:** S. 34, Abschnitt 1.4.6.

## Aufgabe 13 – Fragen: klassisches BI vs. Data Science (Zuordnung)
| Frage | Zuordnung |
|---|---|
| Was ist passiert? | Business Intelligence |
| Wann ist etwas passiert? | Business Intelligence |
| Wer ist der wichtigste Kunde? | Business Intelligence |
| Wie viel Umsatz wurde in einem Bereich gemacht? | Business Intelligence |
| Was sagen uns die Daten, was wir nicht gefragt haben? | Data Science |
| Was wird passieren, wenn man etwas ändert? | Data Science |
| Wird etwas wieder passieren? | Data Science |
| Warum ist etwas passiert? | Data Science |

**Quelle:** S. 16, Tabelle 1.2. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 14 – Übertragbarkeit gefundener Zusammenhänge (Multiple Choice, 2 richtig)
**Frage:** Wieso lässt sich nicht jeder über Datenanalysen gefundene Zusammenhang auf neue Daten übertragen?
**Antwort:**
- Gefundene Modelle sind manchmal zu sehr auf die Ausgangsdaten ausgelegt und nicht übertragbar (Überanpassung/Overfitting).
- Daten aus der Vergangenheit sind nicht immer auf die Zukunft übertragbar.

**Quelle:** Erläuterung der Testseite; Overfitting siehe S. 256, Abschnitt 10.4.5. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 15 – Bereiche im Self-Service-BI (Multiple Choice, 4 richtig)
**Antwort:**
- Eigenständige Datenbeschaffung
- Eigenständige Datenmodellierung
- Persönliche Datenaufbereitung
- Persönliche Datenverfügbarkeit

**Falsch:** Persönliche Datenspeicherung (individuelles Speichern soll verhindert werden), Eigenständiges Data Mining (zu komplex für Fachabteilungen), Cloud-Anbindung (kann, muss aber nicht).
**Quelle:** S. 27–28, Abb. 1.17.

## Aufgabe 16 – Unternehmensaufgaben für BI-Lösungen (Multiple Choice, 3 richtig)
**Antwort:**
- Analyse des Kundenverhaltens
- Optimierung von Vorgängen
- Vergleich von Daten mit Wettbewerbern

**Falsch:** Verbuchung von Wareneingängen, Erfassung von Bestellungen, Prüfung von Rechnungsangaben (operative Aufgaben, kein Mehrwert durch BI).
**Quelle:** Erläuterung der Testseite; Competitive Intelligence S. 8–9.

---

# Thema 2/3: Data Warehouse – Merkmale und Architektur (Kapitel 2 und 3)

## Aufgabe 17 – Geschäftsprozessorientierte Metadaten (Multiple Choice, 3 richtig)
**Frage:** Welche Metadaten lassen sich den geschäftsprozessorientierten Metadaten zuordnen?
**Antwort:**
- Informationen zur Herkunft der Daten
- Dokumentation, wo welche Informationen zu finden sind
- Erläuterungen zur Bedeutung der Attribute

**Falsch:** Zugriffsrechte, Transformationsregeln (technische Aspekte, für den Geschäftsprozessaspekt nicht relevant).
**Begründung:** Geschäftsprozessorientierte Metadaten beschreiben, wie die Daten fachlich zu interpretieren sind (Semantik), erleichtern die Navigation und vermitteln die Herkunft der Daten.
**Quelle:** S. 53, Abschnitt 3.1 (Metadaten), Abb. 3.4. Die dritte Antwort ist aus Erläuterung und Skript hergeleitet, auf der Testseite noch nicht bestätigt.

## Aufgabe 18 – Merkmale bei der Gestaltung eines Data Warehouse (Multiple Choice, 2 richtig)
**Antwort:**
- nicht-flüchtig
- integriert

**Falsch:** redundanzfrei (Redundanzen können für die Performance nützlich sein), multidimensional (entsteht erst innerhalb der Auswertungen).
**Begründung:** Ein Data Warehouse integriert Daten aus verschiedenen Quellen, eingebrachte Daten werden nicht verändert oder gelöscht (Inmon-Merkmale).
**Quelle:** S. 42–43, Abschnitt 2.2 (Definition nach Inmon).

## Aufgabe 19 – Definition Data Warehouse (Lückentext)
1. Ein Data Warehouse ist im Kern nur ein **Datenspeicher**,
2. der Daten aus verschiedenen Quellen in einer **einheitlichen**, zusammengefassten Form zur Verfügung stellt.
3. Zwei zentrale Merkmale: die **Integration**
4. und der **einheitliche** Zugriff.
5. Der Zweck liegt nicht mehr auf der Funktionsorientierung, sondern auf der **fachorientierten** (themenorientierten) Darstellung der Datensammlung.
6. Die **Integration** ermöglicht einen einheitlichen Zugang zu den Daten,
7. die **Heterogenität** der Datenstrukturen und Kodierungen der Quellsysteme verschwindet.
8. **Nicht flüchtige** Datenbasis: einmal geladene Daten stehen dauerhaft für Analysezwecke zur Verfügung.
9. **Zeitraumbezug**: Daten, die zu verschiedenen Zeiten erfasst wurden, sollen später vergleichbar sein.

**Quelle:** S. 42–43, Abschnitt 2.2.

## Aufgabe 20 – Einsatz von Data Marts (Multiple Choice, 3 richtig)
**Frage:** In welchen Situationen kann der Einsatz von Data Marts nützlich sein?
**Antwort:**
- Mobilität
- Performance
- Datentrennung

**Falsch:** Historisierung, Vereinfachte Administration, Erweiterte Auswertungsmöglichkeiten.
**Begründung:** Gründe für Data Marts: Eigenständigkeit (z. B. Mobilität), Datenschutz durch Teilsicht auf die Daten, organisatorische Aspekte (z. B. Datentrennung von Abteilungen), Verringerung des Datenvolumens, Performancegewinn durch Aggregation, Verteilung der Last, Unabhängigkeit von den Aktualisierungszyklen des Data Warehouse.
**Quelle:** S. 52, Abschnitt 3.1 (Data Marts).

## Aufgabe 21 – Referenzarchitektur eines Data-Warehouse-Systems (Abbildung, Freitext)
- (1) Analyse
- (2) Data Mart
- (3) DW-Manager (auch: Data-Warehouse-Manager)
- (4) Repositorium (auch: Repository)
- (5) Basisdatenbank
- (6) Arbeitsbereich
- (7) Extraktion
- (8) Monitor

**Merkhilfe (Datenfluss von unten nach oben):** Datenquelle → Extraktion → Arbeitsbereich (mit Transformation) → Laden → Basisdatenbank → Laden → Data Warehouse → Ableiten → Data Mart → Analyse. Der Monitor beobachtet die Datenquellen, der DW-Manager steuert alles (Kontrollfluss), der Metadaten-Manager verwaltet das Repositorium.
**Quelle:** S. 48–51, Abb. 3.1 (Referenzmodell für die Architektur von DW-Systemen).

## Aufgabe 22 – Architekturvarianten (Drag & Drop)
| Architekturvariante | Beschreibung |
|---|---|
| Föderiertes Data-Warehouse-System | Zusammenschluss mehrerer DW-Systeme |
| Unabhängige Data Marts | Analysen auf isolierten Teilbereichen des Unternehmens |
| Hub-and-Spoke-Architektur | Ein Data Warehouse mit Data Marts |
| Virtuelles Data Warehouse | Analyse direkt auf Quellsystemen |
| Operational Data Store | Datenanalysen auf Datenkopie eines Produktivsystems |

**Begründung:** Hub-and-Spoke = Grundaufbau mit einem DW und mehreren Data Marts. ODS arbeitet auf den Daten eines einzelnen Quellsystems. Das virtuelle DW hat keine eigene Analysedatenbank, die Analysen laufen direkt auf den Quellsystemen. Unabhängige Data Marts sind kleine, getrennt betriebene DW-Lösungen für je einen Teilbereich. Im föderierten System werden lokale DW-Systeme zu einem Verbund zusammengeschlossen.
**Quelle:** S. 54–55, Abschnitt 3.1.2 (Architekturvarianten).

## Aufgabe 23 – Analysearten nach Flexibilität ordnen (Reihenfolge)
**Frage:** Analysearten so anordnen, dass die Analyseart höchster Flexibilität ganz oben steht.
**Antwort:**
1. OLAP
2. Ad-hoc-Reporting
3. CRM-Analysen
4. Data Mining
5. Standard-Reporting

**Quelle:** Lösung der Testseite; im Skript S. 59, Abschnitt 3.3, Abb. 3.9 (Analysemethoden).

## Aufgabe 24 – Analysearten nach Komplexität ordnen (Reihenfolge)
**Frage:** Analysearten so anordnen, dass die Analyseart höchster Komplexität ganz oben steht.
**Antwort:**
1. CRM-Analysen
2. Datenvisualisierung
3. Data Mining
4. OLAP
5. Ad-hoc-Reporting
6. Standard-Reporting

**Hinweis:** Nicht mit Aufgabe 23 verwechseln. Bei der Flexibilität steht OLAP oben, bei der Komplexität CRM-Analysen. Standard-Reporting ist in beiden Fällen ganz unten.
**Quelle:** Lösung der Testseite; im Skript S. 59, Abschnitt 3.3, Abb. 3.9 (Analysemethoden).

## Aufgabe 25 – Aktivitäten der Transformation im ETL-Prozess (Multiple Choice, 5 richtig)
**Frage:** Welche Aktivitäten können im Rahmen der Transformation im ETL-Prozess durchgeführt werden?
**Antwort:**
- Filterung (Bereinigung inhaltlicher und syntaktischer Fehler)
- Vorabberechnungen (Bildung betriebswirtschaftlicher Kennzahlen)
- Vorabverdichtungen (Aggregation, Kombination bzw. Separierung von Attributwerten)
- Anreicherung (von Attributen durch Hintergrundwissen)
- Harmonisierung

**Falsch:** Replizieren, Synchronisieren, Historisierung (die Historisierung geschieht erst beim Laden).
**Quelle:** S. 50, Abschnitt 3.1 (Transformation); vertiefend S. 164–167.

---

# Thema 4: Reporting (Kapitel 4)

## Aufgabe 26 – Reporting-Arten (Lückentext)
1. Das **Standard**-Reporting setzt eine exakt geplante Bereitstellung von vordefinierten Informationen um.
2. Wird ein Bericht aufgrund einer atypischen Situation erstellt, bezeichnet man dies als **Exception**-Reporting.
3. Explorative Vorgehensweisen innerhalb von Berichten ermöglicht das **Analyse**-Reporting,
4. wobei eine freie Definition der Inhalte der Berichte zum **Ad-hoc**-Reporting führt.

**Hinweis:** Ad-hoc ist nicht der Bericht bei einer atypischen Situation (das ist Exception), sondern die freie Definition der Berichtsinhalte.
**Quelle:** S. 67–68, Kapitel 4 (Reporting).

## Aufgabe 27 – Absolute Kennzahlen (Multiple Choice, 2 richtig)
**Frage:** Welche der folgenden Kennzahlen sind absolute Kennzahlen?
**Antwort (wahrscheinlich, noch nicht bestätigt):**
- Arbeitsaufwand in Stunden in einem Projekt (Summe)
- Durchschnittseinkommen in Euro (Mittelwert)

**Falsch:** Auslastung der Mitarbeiter (Gliederungszahl), Ranglistenposition, vermutlich Umsatz je Jahr in Euro („je“ = Beziehungszahl, wie „Herstellungskosten pro Stück“ im Skript).
**Unsicherheit:** Der Versuch mit Umsatz + Arbeitsaufwand + Durchschnittseinkommen ergab „2/2 korrekt, 1 falsch“. Eine der drei ist also falsch. Die Erläuterung nennt Mittelwerte ausdrücklich als absolut, Arbeitsaufwand ist eine eindeutige Summe, daher fällt am ehesten „Umsatz je Jahr“ heraus. Beim nächsten Durchlauf prüfen.
**Begründung:** Einzelwerte, Summen, Mittelwerte und Differenzen sind absolute Kennzahlen. Gliederungs-, Beziehungs- und Indexzahlen sind Verhältniszahlen.
**Quelle:** S. 65, Abschnitt 4.1.2, Abb. 4.2.

## Aufgabe 28 – Reportansätze nach Prozessschwerpunkt und Flexibilität (Abbildung, Dropdowns)
- (1) Dashboards (Informationsbereitstellung, geringste Flexibilität, geringe Komplexität)
- (2) Standard-Reporting
- (3) Ad-hoc-Reporting
- (4) OLAP (Informationsauswertung, höchste Flexibilität, hohe Komplexität)

**Hinweis:** Dashboards stehen noch vor dem Standard-Reporting, OLAP ist flexibler als Ad-hoc-Reporting.
**Quelle:** S. 79, Abb. 4.12 (Klassifikation von Reporting-Ansätzen).

## Aufgabe 29 – Merkmale der Dashboardarten (Zuordnung)
| Merkmal | Dashboardart |
|---|---|
| Kommunikation/Kollaboration | Strategisch |
| Bereichsspezifische Kennzahlen | Analytisch |
| Monitoring | Operativ |
| Echtzeitaktualisierung | Operativ |
| Individuelles Informationsspektrum | Operativ |
| Inhalte vorwiegend grafisch | Analytisch |
| Monatliche Aktualisierung | Strategisch |
| Prozessspezifisch | Operativ |

**Merkhilfe:** Strategisch = Kommunikation/Kollaboration, monatliche Aktualisierung. Analytisch = bereichsspezifische Kennzahlen, vorwiegend grafisch. Operativ = alles Zeitnahe und Prozessbezogene (Monitoring, Echtzeit, prozessspezifisch, individuelles Informationsspektrum).
**Quelle:** S. 72, Abb. 4.6 (Dashboardarten).

## Aufgabe 30 – Visualisierungskriterien und ihre Ziele (Drag & Drop)
| Kriterium | Ziel |
|---|---|
| Expressivität | Unverfälschte Darstellung |
| Effektivität | Berücksichtigung der Fähigkeiten des Betrachters |
| Angemessenheit | Berücksichtigung des Berechnungsaufwands |

**Hinweis:** Angemessenheit meint hier den Aufwand (Berechnung), nicht den Betrachter. Der Betrachter gehört zur Effektivität.
**Quelle:** S. 70, Kapitel 4 (Visualisierung).

## Aufgabe 31 – SUCCESS-Regeln der Diagrammgestaltung (Drag & Drop)
| Regel | Erläuterung |
|---|---|
| **S**ay | Ein Diagramm sollte Einsichten oder Botschaften vermitteln. |
| **U**nify | Ein Diagramm sollte Teil eines einheitlichen Darstellungskonzepts sein. |
| **C**ondense | Ein Diagramm sollte eine hohe Informationsdichte bieten. |
| **C**heck | Wichtige Qualitätsaspekte sollten berücksichtigt werden. |
| **E**nable | Die organisatorische und technische Diagrammrealisierung sollte gute Ergebnisse ermöglichen. |
| **S**implify | Einfachheit ist ein wichtiger Aspekt des Darstellungskonzepts. |
| **S**tructure | Die Diagramminhalte sollten richtig strukturiert sein. |

**Quelle:** S. 75, Kapitel 4 (SUCCESS-Regeln nach Hichert). (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 32 – Schritte des Reporting-Prozesses (Reihenfolge)
**Antwort:**
1. Bedarf ermitteln
2. Quellen ermitteln
3. Informationsgewinnung
4. Informationsaufbereitung
5. Informationsspeicherung
6. Informationsübermittlung
7. Einsatzprotokollierung
8. Einsatz und Betreuung

**Hinweis:** Die Übermittlung kommt erst nach Gewinnung, Aufbereitung und Speicherung (Position 6, nicht 3).
**Quelle:** S. 66, Abb. 4.3 (Reporting-Prozess).

## Aufgabe 33 – Kennzahlen den Kennzahlenarten zuordnen (Drag & Drop)
| Kennzahlenart | Kennzahl |
|---|---|
| Beziehungszahl | Herstellkosten je Stück |
| Einzelwert | Rechnungsbetrag zur Rechnung 88256 |
| Differenz | Anstieg des Stundensatzes für Wartung |
| Gliederungszahl | Frauenquote |
| Mittelwert | Durchschnittspreis zum Produkt Peck im Januar 2026 |
| Indexzahl | Prozentuales Umsatzwachstum 2026 im Vergleich zu 2025 |
| Summe | Gesamtumsatz im Januar 2026 |

**Begründung:** Gliederungszahl = Teilmenge im Verhältnis zur Gesamtmenge (Frauenquote). Beziehungszahl = unterschiedliche Ausgangsmengen in Bezug zueinander (Kosten je Stück). Indexzahl = prozentuale Abweichung zu einem festen Vergangenheitswert (Wachstum gegenüber 2025). Alle anderen sind absolute Zahlen, die Zuordnung ergibt sich aus der Berechnungsart.
**Quelle:** S. 65, Abschnitt 4.1.2, Abb. 4.2. Aus der Erläuterung hergeleitet (Einzelwert, Mittelwert, Summe waren bereits korrekt), auf der Testseite noch nicht als Ganzes bestätigt.

## Aufgabe 34 – Berichtsmerkmale und Berichtskriterien (Zuordnung)
| Berichtsmerkmal | Berichtskriterium |
|---|---|
| Berichtsintervall | Berichtszeit |
| Darstellungsart | Berichtsform |
| Genauigkeit | Berichtsinhalt |
| Empfänger | Berichtsinstanz |
| Dokumentation | Berichtszweck |
| Struktur | Berichtsform |
| Kontrolle | Berichtszweck |
| Detaillierung | Berichtsinhalt |
| Gegenstand | Berichtsinhalt |

**Merkhilfe:** Berichtsinhalt = Gegenstand, Detaillierung, Genauigkeit. Berichtsinstanz = Empfänger, Ersteller. Berichtszweck = Dokumentation, Kontrolle. Berichtszeit = Berichtsintervall. Berichtsform = Darstellungsart, Struktur.
**Quelle:** S. 64, Abb. 4.1 (Kennzeichnungskriterien eines Reports).

## Aufgabe 35 – Hauptgruppen von Kennzahlen (Lückentext)
1. Bei Einzelwerten, Summen, Mittelwerten und Differenzen handelt es sich um **absolute** Kennzahlen.
2. Gliederungszahlen, Beziehungszahlen und Indexzahlen werden den **Verhältniszahlen** zugeordnet.

**Quelle:** S. 65, Abschnitt 4.1.2, Abb. 4.2.

---

# Thema 5: OLAP und multidimensionale Modellierung (Kapitel 5)

## Aufgabe 36 – OLAP-Modellierungsansätze und Modellierungsebene (Zuordnung)
| Modellierungsansatz | Ebene |
|---|---|
| Multidimensionales Modell | Logisches Datenmodell |
| UML | Semantisches Datenmodell |
| Star-Schema | Logisches Datenmodell |
| ADAPT | Semantisches Datenmodell |

**Begründung:** Für das semantische (konzeptionelle) Datenmodell nutzt man den ER-basierten Ansatz oder Methoden wie mE/R, mUML oder ADAPT. Dieser Entwurf wird dann auf das vom System implementierte multidimensionale Datenmodell übertragen (logische Ebene), relational z. B. als Star-Schema.
**Quelle:** S. 87, Abschnitt 5.2, Abb. 5.9. Aus der Erläuterung hergeleitet, auf der Testseite noch nicht bestätigt.

## Aufgabe 37 – Definition von Dimensionen für OLAP-Auswertungen (Lückentext)
1. Das Schema einer Dimension D besteht aus einer **partiell** geordneten Menge
2. von **Kategorienattributen** {D1,…,Dn, TopD},
3. wobei TopD ein generisches **maximales** Element
4. in Bezug auf die **funktionale** Abhängigkeit darstellt,
5. so dass TopD von allen Attributen **funktional** bestimmt wird.
6. Genau ein Di bestimmt alle anderen Kategorienattribute und gibt somit die **feinste** Granularität einer Dimension vor,
7. man bezeichnet es auch als **Primärattribut** (oder das kleinste Element der Dimension).
8. Werte der Klassifikationsattribute werden **Kategorien** genannt.

**Zusatz:** Die Kategorie bezeichnet ein Mitglied einer Ebene, einen konkreten fachlichen Begriff oder Wert.
**Quelle:** S. 105–106, Kapitel 5 (Schema einer Dimension).

## Aufgabe 38 – GROUPING SETS (SQL-Ergebnis ausfüllen)
**Gegeben:** Tabelle Auftraege

| Staat | Stadt | Jahr | Umsatz |
|---|---|---|---|
| Deutschland | Stuttgart | 2025 | 100 |
| Frankreich | Reimes | 2025 | 200 |
| Deutschland | Heilbronn | 2026 | 250 |
| Frankreich | Nantes | 2026 | 350 |

```sql
SELECT Staat, Jahr, SUM(Umsatz) as S
FROM Auftraege
GROUP BY GROUPING SETS ((Staat), (Jahr), ());
```

**Antwort (S ist auf der Testseite vorgegeben):**

| Staat | Jahr | S | Rechnung |
|---|---|---|---|
| Deutschland | NULL | 350 | 100 + 250 |
| Frankreich | NULL | 550 | 200 + 350 |
| NULL | 2025 | 300 | 100 + 200 |
| NULL | 2026 | 600 | 250 + 350 |
| NULL | NULL | 900 | Gesamtsumme |

**Begründung:** Jede Gruppierungsmenge wird einzeln ausgewertet: (Staat) liefert die Summe je Land mit Jahr NULL, (Jahr) die Summe je Jahr mit Staat NULL, () die Gesamtsumme mit beidem NULL. Es gibt keine Zeile, in der Staat und Jahr gleichzeitig gefüllt sind.
**Quelle:** S. 132–133 (GROUPING SETS). Selbst nachgerechnet, auf der Testseite noch nicht bestätigt.

## Aufgabe 39 – Sinnvolle ROLLUP-Anfrage (Single Choice)
**Gegeben:** dieselbe Tabelle Auftraege wie in Aufgabe 38.
**Frage:** Welche der folgenden Anfragen ist sinnvoll?
**Antwort:** Möglichkeit 1

```sql
SELECT Staat, Jahr, SUM(Umsatz) as S
FROM Auftraege
GROUP BY ROLLUP (Staat, Stadt);
```

**Falsch:** ROLLUP (Stadt, Staat), ROLLUP (Jahr, Stadt), ROLLUP (Staat, Jahr).
**Begründung:** ROLLUP aggregiert schrittweise von rechts nach links entlang einer Hierarchie. Nur Staat – Stadt bildet eine Dimensionshierarchie in angemessener Ordnung (vom Groben zum Feinen). Stadt, Staat hat die falsche Reihenfolge, Jahr und Stadt bzw. Staat und Jahr gehören zu verschiedenen Dimensionen.
**Quelle:** S. 133–135 (ROLLUP).

## Aufgabe 40 – Einsatz von MOLAP-Technologien (Multiple Choice, 2 richtig)
**Frage:** In welchen Situationen empfiehlt sich der Einsatz von MOLAP-Technologien zur Bereitstellung von OLAP-Analysemöglichkeiten?
**Antwort (teilweise unsicher, noch nicht bestätigt):**
- Hohe Performanceansprüche (sicher)
- Einsatz OLAP-fixierter Data Marts (wahrscheinlich) ODER Mobile BI im Offline-Betrieb

**Falsch:** Verringerung des Administrationsaufwands (MOLAP erzeugt einen höheren administrativen Aufwand).
**Unsicherheit:** Der Versuch mit „Mobile BI im Offline-Betrieb“ + „Einsatz OLAP-fixierter Data Marts“ ergab „1/2 korrekt, 1 falsch“. Eine der beiden ist also falsch, und da der Administrationsaufwand sicher falsch ist, muss „Hohe Performanceansprüche“ richtig sein. Die Erläuterung nennt aber sowohl Mobilgeräte als auch Data Marts. Zuerst Performance + Data Marts probieren, sonst Performance + Mobile BI.
**Begründung:** MOLAP speichert die Aggregate direkt mehrdimensional und ist dadurch performanter, wovon auch leistungsschwächere Mobilgeräte profitieren. Für einen speziell für OLAP-Analysen geschaffenen Data Mart bietet sich ebenfalls MOLAP an.
**Quelle:** Erläuterung der Testseite; MOLAP/ROLAP/HOLAP im Skript S. 115 (Kapitel 6, Einleitung).

## Aufgabe 41 – Eigenschaft von Dimensionen (Single Choice)
**Frage:** Dimensionen sind …
**Antwort:** Diskret
**Falsch:** Summierbar, Quantifizierend, Kontinuierlich (das sind Eigenschaften von Kennzahlen, nicht von Dimensionen).
**Begründung:** Dimensionen sind diskret, da bezüglich der Werte gruppiert wird.
**Quelle:** Erläuterung der Testseite; Kapitel 5 (Elemente der multidimensionalen Modellierung, ab S. 87).

---

# Thema 6: Relationales OLAP (Kapitel 6)

## Aufgabe 42 – Star-Schema statt Snowflake-Schema (Multiple Choice, 3 richtig)
**Frage:** In welchen Situationen ist ein Star-Schema einem Snowflake-Schema zu bevorzugen?
**Antwort:**
- Anfragen werden meist auf höherer Granularität definiert.
- Das Datenvolumen der Dimensionstabellen ist relativ gering.
- Änderungen an den Klassifikationen treten selten auf.

**Falsch:** Der Würfel hat wenige Dimensionen; Anfragen meist auf niederer Granularität; Datenvolumen der Faktentabelle relativ gering.
**Begründung:** Bei Anfragen auf höherer Granularität spart die Denormalisierung aufwändige Verbundoperationen zwischen den Tabellen einer Dimension. Die Dimensionstabellen sind klein im Vergleich zur Faktentabelle, die Redundanz erhöht das Datenvolumen also kaum. Bei seltenen Änderungen an den Klassifikationen lassen sich Änderungsanomalien einfach vermeiden.
**Quelle:** S. 121, Kapitel 6 (Star-Schema vs. Snowflake-Schema).

## Aufgabe 43 – Vorteile des Snowflake-Schemas gegenüber dem Star-Schema (Multiple Choice, 2 richtig)
**Antwort:**
- Verringerung des Datenvolumens
- Unterstützung des Fact-Constellation-Ansatzes

**Falsch:** Einfachere Aggregation auf höheren Verdichtungsstufen einer Dimensionshierarchie; Höhere Performance (beides spricht eher für das Star-Schema, siehe Aufgabe 42).
**Begründung:** Das Snowflake-Schema unterstützt den Fact-Constellation-Ansatz und verringert das Datenvolumen, da weniger Redundanzen gespeichert werden.
**Quelle:** S. 121–122, Kapitel 6 (Snowflake-Schema, Fact Constellation).

## Aufgabe 44 – Akronym FASMI (Freitext)
**Frage:** Wofür steht das Akronym FASMI im Rahmen der Definition von OLAP-Analysen?
**Antwort:**
- F: **Fast**
- A: **Analysis**
- S: **Shared**
- M: **Multidimensional**
- I: **Information**

Ausgeschrieben: Fast Analysis of Shared Multidimensional Information. (Die Testseite schreibt „Multidimenional“ mit Tippfehler; falls die korrekte Schreibweise nicht akzeptiert wird, diese Variante probieren.)
**Quelle:** S. 81, Kapitel 5 (OLAP-Definition, FASMI).

## Aufgabe 45 – Qualifizierende vs. quantifizierende Informationen (Zuordnung)
| Datenart | Zuordnung |
|---|---|
| Prozessdurchlaufzeit | quantifizierend |
| Bruttopreis | quantifizierend |
| Kundenkategorie | qualifizierend |
| Produkt | qualifizierend |
| Prozesskennung | qualifizierend |
| Lieferdauer | quantifizierend |

**Begründung:** Qualifizierende Informationen sind alle Daten, die dem Benutzer als Navigationsraster zur Verfügung stehen (Dimensionen). Quantifizierende Informationen spiegeln den Gegenstand der Auswertung wider (Kennzahlen).
**Quelle:** S. 85, Kapitel 5. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 46 – Roll-up bei OLAP-Analysen (Single Choice)
**Frage:** Was bewirkt ein Roll-up im Rahmen von OLAP-Analysen?
**Antwort:** Die Daten werden innerhalb einer Dimensionshierarchie auf eine stärker verdichtete Ebene aggregiert dargestellt.
**Falsch:** Dimensionsebene wird durch eine Ebene einer höher priorisierten Dimension getauscht; in einer Dimension höherliegende Daten werden herausgefiltert; die Granularität wird erhöht (das wäre Drill-down).
**Quelle:** S. 111–112, Kapitel 5 (OLAP-Operationen).

## Aufgabe 47 – GROUP BY mit CASE: Anzahl Ergebniszeilen (Zahleneingabe)
**Gegeben:** dieselbe Tabelle Auftraege wie in Aufgabe 38.

```sql
SELECT (CASE
           WHEN Stadt IN ('Stuttgart','Reimes')
              THEN Stadt
        END),
       SUM(Umsatz)
FROM Auftraege
GROUP BY (CASE
           WHEN Stadt IN ('Stuttgart','Reimes')
              THEN Stadt
        END);
```

**Frage:** Wie viele Ergebniszeilen erzeugt die Anfrage?
**Antwort:** 3

| Gruppe | SUM(Umsatz) |
|---|---|
| Stuttgart | 100 |
| Reimes | 200 |
| NULL | 600 (Heilbronn 250 + Nantes 350) |

**Begründung:** Für Stuttgart und Reimes gibt es individuelle Summen. Bei allen anderen Städten liefert das CASE ohne ELSE den Wert NULL, sie werden zu einer gemeinsamen Gruppe zusammengefasst. Diese NULL-Gruppe ist die dritte Zeile.
**Quelle:** Erläuterung der Testseite; selbst nachgerechnet.

## Aufgabe 48 – CUBE (SQL-Ergebnis ausfüllen)
**Gegeben:** dieselbe Tabelle Auftraege wie in Aufgabe 38.

```sql
SELECT Staat, Jahr, SUM(Umsatz) as S
FROM Auftraege
GROUP BY CUBE (Staat, Jahr);
```

**Antwort (Reihenfolge und S wie auf der Testseite):**

| Staat | Jahr | S |
|---|---|---|
| Deutschland | 2025 | 100 |
| Deutschland | 2026 | 250 |
| Deutschland | NULL | 350 |
| Frankreich | NULL | 550 |
| Frankreich | 2025 | 200 |
| Frankreich | 2026 | 350 |
| NULL | 2025 | 300 |
| NULL | 2026 | 600 |
| NULL | NULL | 900 |

**Begründung:** CUBE bildet alle Kombinationen: Summen für jede Staat/Jahr-Kombination, für jedes Land einzeln, für jedes Jahr einzeln und die Gesamtsumme. Nicht beteiligte Merkmale sind NULL. Die Zeile mit 550 ist die Landessumme Frankreich (200 + 350), nicht NULL/NULL.
**Quelle:** S. 133–134 (CUBE). Die 550-Zeile ist nachgerechnet, die übrigen neun Felder waren auf der Testseite korrekt.

## Aufgabe 49 – Vorteile der Modellierungsansätze mE/R, mUML, ADAPT (Drag & Drop)
| Ansatz | Vorteil |
|---|---|
| mE/R | Vertrauter Ansatz bei der Modellierung von Datenbanken. |
| mUML | Standard-Modellierungswerkzeuge können weiter verwendet werden. |
| ADAPT | Umfassender Pool an Notationselementen. |

**Begründung:** ADAPT ist speziell für OLAP-Auswertungen definiert und umfasst einen großen Pool an hierfür nützlichen Elementen. mUML kann mit evtl. schon vorhandenen Werkzeugen zur Modellierung genutzt werden. mE/R baut auf dem bekannten und etablierten ER-Ansatz auf.
**Quelle:** S. 87–95, Kapitel 5 (mE/R, mUML, ADAPT). (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 50 – Multidimensionale Operatoren und ihre Umsetzung (Drag & Drop)
| Operator | Umsetzung |
|---|---|
| Drill-down | Aufspaltung in die eingehenden Teilsummen |
| Drill-through | Wechsel der Datenquelle |
| Roll-up | Zahlen bzgl. einer höheren Dimensionsgranularität |
| Slicing | Ausschnittsbildung gemäß den in dimensionalen Strukturen (vordefinierten Begriffswelten) |
| Drill-across | Wechsel zwischen verschiedenen Würfeln |
| Pivotierung | Drehen des Würfels um seine Achsen |

**Begründung:** Pivotierung rotiert die Dimensionen durch Drehen des Würfels. Slicing bildet Ausschnitte. Drill-through wechselt die Datenquelle (z. B. von multidimensionaler zu relationaler Speicherform). Drill-across wechselt zwischen Würfeln auf Basis einer gemeinsamen Dimension. Roll-up ist die inverse Operation zu Drill-down und zeigt Zahlen einer höheren Dimensionsgranularität. Drill-down spaltet Ergebnisse höherer Granularität in die eingehenden Teilsummen auf.
**Hinweis:** Die Testseite nennt beim Roll-up die verdichtete Ebene „höhere Dimensionsgranularität“. Drill-down = Aufspaltung, Roll-up = Verdichtung (vgl. Aufgabe 46).
**Quelle:** S. 111–113, Kapitel 5 (OLAP-Operationen).

## Aufgabe 51 – Geeignete Dimensionen bei Warenentnahmen aus einem Lager (Multiple Choice, 3 richtig)
**Frage:** Welche Attribute sind in einer Relation zur Speicherung von Warenentnahmen aus einem Lager als Dimensionen im Rahmen einer OLAP-Analyse geeignet?
**Antwort:**
- Entnommenes Produkt
- Entnahmedatum
- Person, die die Entnahme durchgeführt hat

**Falsch:** Entnommene Stückzahl (das ist die Kennzahl).
**Begründung:** Stückzahlen werden in Kennzahlenberechnungen verwendet, alle anderen Attribute eignen sich für eine Gruppierung (vgl. Aufgabe 41: Dimensionen sind diskret, und Aufgabe 45: qualifizierend vs. quantifizierend).
**Quelle:** Erläuterung der Testseite; Kapitel 5, S. 85.

---

# Thema 7/8: Datenqualität, ETL und physische Optimierung

## Aufgabe 52 – Modellierungselemente im ANSI/SPARC-Ebenenmodell (Zuordnung)
| Modellierungselement | Ebene |
|---|---|
| Indizes | Interne Ebene |
| Star-Schema | Konzeptionelle Ebene |
| Materialisierte Views | Interne Ebene |
| Partitionierungen | Interne Ebene |
| Snowflake-Schema | Konzeptionelle Ebene |

**Begründung:** Zur internen Ebene gehören Indizes, materialisierte Views und Partitionierungen. Star- und Snowflake-Schema finden sich auf der konzeptionellen Ebene. Die externe Ebene bleibt hier leer.
**Hinweis:** Materialisierte Views sind trotz des Namens „View“ keine externe Sicht, sondern eine physische Optimierung (interne Ebene).
**Quelle:** S. 177 (ANSI/SPARC-Ebenenmodell).

## Aufgabe 53 – Partitionierung: logische und physische Ebene (Lückentext)
1. Die **logische** Ebene beschreibt die Aufteilung
2. anhand eines **Prädikats**. Es wird definiert, wie eine Partitionierung vorgenommen wird (Partitionierung im engeren Sinn).
3. Die **physische** Ebene wird durch die Definition des physischen Speicherungsorts einer Partition beschrieben (wo die Partitionen gespeichert werden).
4. Dies wird als **Allokation** bezeichnet.

**Quelle:** S. 178 (Partitionierung).

## Aufgabe 54 – Programmanpassungen für materialisierte Views (Single Choice)
**Frage:** Welche Anpassungen sind in einem Programm notwendig, dass dieses vom Einsatz materialisierter Views profitiert?
**Antwort:** Keine
**Falsch:** Refresh vor jedem Select; View in der FROM-Klausel ansprechen; Zugriff über eine vordefinierte Stored Procedure.
**Begründung:** Materialisierte Summendaten können komplett transparent ohne Programmanpassungen verwendet werden (das DBMS schreibt die Anfrage selbst um). Refreshs sind optional und können unabhängig erfolgen.
**Quelle:** S. 185–187 (Materialisierte Sichten).

## Aufgabe 55 – Historisierung mit Gültig_von / Gültig_bis (Multiple Choice, 3 richtig)
**Frage:** Welche Attributwerte sind nach der Änderung eines Datensatzes durch den Lade-Prozess beim Laden der neuen Version des Datensatzes zu belegen?
**Antwort:**
- Gültig_bis der neuesten schon im Data Warehouse vorhandenen Version des Datensatzes (wird mit aktuellem Zeitpunkt belegt)
- Gültig_bis des zu ladenden Datensatzes (wird auf unbegrenzt gesetzt)
- Gültig_von des zu ladenden Datensatzes (wird mit aktuellem Zeitpunkt belegt)

**Falsch:** Gültig_von der neuesten vorhandenen Version; Gültig_von aller vorhandenen Versionen; Gültig_bis aller vorhandenen Versionen.
**Merkhilfe:** Nur die bisher aktuelle Version wird „geschlossen“ (Gültig_bis = jetzt), die neue Version wird „geöffnet“ (Gültig_von = jetzt, Gültig_bis = unbegrenzt). Ältere Versionen bleiben unverändert.
**Quelle:** S. 171–172 (Historisierung).

## Aufgabe 56 – Datentyp für integrierte Bestellnummer (Multiple Choice, 2 richtig)
**Frage:** Quellsystem A nutzt für die Bestellnummer einen 32-Bit-Integer, Quellsystem B eine Ziffernfolge der Länge 6 als Zeichenkette. Welche Datentypen sind in einer integrierten Tabelle möglich?
**Antwort:**
- Zeichenkette der Länge 10
- 32-Bit-Integer

**Falsch:** Zeichenkette der Länge 6 (zu kurz für die Integer-Werte), Double (überdimensioniert).
**Begründung:** Der Datentyp muss Werte aus beiden Quellsystemen akzeptieren, darf aber nicht überdimensioniert sein. Ein 32-Bit-Integer nimmt Werte bis ca. 2 Mrd. an (10 Stellen), daher braucht ein String die Länge 10. Die 6-stelligen Ziffernfolgen passen umgekehrt problemlos in einen 32-Bit-Integer.
**Quelle:** Erläuterung der Testseite; Datenintegration/Harmonisierung im Skript S. 164–167.

## Aufgabe 57 – Qualitätskriterien und Qualitätskategorien für DW-Systeme (Zuordnung)
| Qualitätskriterium | Qualitätskategorie |
|---|---|
| Relevanz | Nützlichkeit |
| Konsistenz | Glaubwürdigkeit |
| Eindeutigkeit | Interpretierbarkeit |
| Referentielle Integrität | Schlüsselintegrität |
| Zeitnähe | Nützlichkeit |
| Einheitlichkeit | Interpretierbarkeit |

**Merkhilfe:** Nützlichkeit = Relevanz, Zeitnähe. Interpretierbarkeit = Eindeutigkeit, Einheitlichkeit. Glaubwürdigkeit = Konsistenz. Schlüsselintegrität = Referentielle Integrität.
**Quelle:** S. 148–150 (Datenqualität).

## Aufgabe 58 – Definition Datenqualität (Lückentext)
1. Datenqualität bezeichnet den **Erfüllungsgrad**
2. der Gesamtheit der **Anforderungen**
3. an die für einen bestimmten **Zweck** benötigten Daten.

**Quelle:** S. 147 (Definition Datenqualität).

## Aufgabe 59 – Kategorien der Datenqualität (Drag & Drop)
| Kriterium | Kategorie |
|---|---|
| Reputation | Intrinsische Datenqualität |
| Relevanz | Kontextuelle Datenqualität |
| Verständlichkeit | Repräsentationelle Datenqualität |
| Verfügbarkeit | Zugriffsqualität |

**Merkhilfe:** Intrinsisch = Eigenschaft der Daten selbst (Reputation, Glaubwürdigkeit). Kontextuell = abhängig vom Verwendungszweck (Relevanz). Repräsentationell = Darstellung (Verständlichkeit). Zugriff = Erreichbarkeit (Verfügbarkeit).
**Quelle:** S. 149 (Kategorien der Datenqualität).

---

# Thema: Data Mining – Überanpassung und Modellbewertung

## Aufgabe 60 – Kreuzvalidierung und Regularisierung (Lückentext)
1. Die **Kreuzvalidierung** ist ein gängiges experimentelles Verfahren, eine einzelne Datenmenge so aufzuteilen, dass mehrere Beurteilungen der Leistung möglich sind.
2. Die allgemeine Methode zur Steuerung der Komplexität zur Vermeidung einer Überanpassung wird als **Regularisierung** bezeichnet.
3. Bei linearen Funktionen wird die Komplexität zur Reduzierung der Überanpassung in Form eines **Strafterms** in die zu optimierende Funktion integriert.

**Quelle:** Erläuterung der Testseite. Die Begriffe Kreuzvalidierung, Regularisierung und Strafterm stehen im Skript nicht wörtlich; Überanpassung (Overfitting) siehe S. 256–258, Abschnitt 10.4.5.

## Aufgabe 61 – Überwachte vs. unüberwachte Data-Mining-Verfahren (Zuordnung)
| Verfahren | Ansatz |
|---|---|
| Ausreißererkennung | Unüberwacht |
| Entscheidungsbäume | Überwacht |
| Support Vector Machines | Überwacht |
| Assoziationsanalysen | Unüberwacht |
| Clustering | Unüberwacht |
| Logistische Regression | Überwacht |
| Lineare Regression | Überwacht |

**Begründung:** Überwachtes Lernen ist Lernen aus Beispielen, bei denen die Zuordnungen schon bekannt sind (Klassifikation, Regression). Unüberwachte Methoden ermitteln Muster, die zuvor nicht bekannt sind (Cluster, Assoziationen, Ausreißer).
**Quelle:** S. 17, Abschnitt 1.3.4; Kapitel 10, S. 202–203. Aus der Erläuterung hergeleitet, auf der Testseite noch nicht bestätigt.

## Aufgabe 62 – Datenanalysetechnologien bei der Geschäftsanalyse (Lückentext)
1. Zu den bei Datenanalysen verwendeten Ansätzen gehört die **Statistik**, die Methoden zur Berechnung bestimmter Kennzahlen zur Verfügung stellt.
2. Grundinformationen zu bestimmten Objekten können aus einem **Datenbanksystem** über Datenbankabfragen (SQL) ermittelt werden.
3. Manuelle und visuelle Untersuchungsmöglichkeiten auf großen Datenmengen mit frei wählbaren Gruppierungskriterien sind über **OLAP**-Analysen möglich.
4. Die Daten hierzu kommen beispielsweise aus einem **Data Warehouse**, in dem auswertungsrelevante Daten homogen zusammengeführt werden.

**Quelle:** S. 39 (Geschäftsanalyse).

## Aufgabe 63 – Phasen des CRISP-Vorgehensmodells (Reihenfolge)
**Antwort:**
1. Aufgabenverständnis
2. Datenverständnis
3. Datenaufbereitung
4. Modellbildung
5. Beurteilung
6. Deployment

**Quelle:** S. 198–199 (CRISP-DM).

## Aufgabe 64 – Passendes Hotel vorschlagen: einsetzbare Algorithmen (Multiple Choice, 3 richtig)
**Frage:** Ein Reiseanbieter bietet drei Hotels an und möchte Kunden anhand erfasster Merkmale das passende vorschlagen. Welche Data-Mining-Algorithmen sind einsetzbar?
**Antwort:**
- Logistische Regression
- Support Vector Machines
- Entscheidungsbäume

**Falsch:** K-Means (Clustering, keine Klassifikation), Regressionsanalysen (für stetige Werte).
**Begründung:** Die Fragestellung verlangt eine Klassifikation von Kunden, also Klassifikationsverfahren.
**Quelle:** Erläuterung der Testseite; Klassifikationsverfahren im Skript S. 202–203.

## Aufgabe 65 – Equal-frequency Binning (Zahleneingabe)
**Frage:** Obergrenze des ersten Intervalls bei Diskretisierung von M = (1, 2, 6, 7, 8, 9, 10, 14, 20, 35, 40, 50) mittels Equal-frequency Binning mit vier Intervallen?
**Antwort:** 6
**Rechnung:** 12 Werte / 4 Intervalle = 3 Werte pro Intervall. Erstes Intervall: 1, 2, 6. Es endet bei 6. (Die weiteren Intervalle: 7–9, 10–20, 35–50.)
**Quelle:** S. 205 (Equal-frequency Binning).

## Aufgabe 66 – Verfahren auf stetigen Werten (Multiple Choice, 2 richtig)
**Antwort:**
- Clusteranalysen
- Regression

**Falsch:** Assoziationsanalysen, Klassifikation (siehe Aufgabe 69).
**Begründung:** Regression und Clusteranalysen führen direkt Berechnungen auf den Attributen der Objekte aus und benötigen damit stetige Werte.
**Quelle:** Erläuterung der Testseite. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 67 – Daten für die Verbesserung ermittelter Modelle (Single Choice)
**Antwort:** Validierungsdaten
**Falsch:** Rohdaten, Testdaten, Trainingsdaten.
**Merkhilfe:** Trainingsdaten = Modell erstellen, Validierungsdaten = Modell verbessern, Testdaten = Modell abschließend bewerten.
**Quelle:** Erläuterung der Testseite; der Begriff „Validierungsdaten“ steht im Skript nicht wörtlich.

## Aufgabe 68 – Qualitative, stetige und diskrete Merkmale (Zuordnung)
| Merkmal | Art |
|---|---|
| Gewicht | Stetig |
| Religionszugehörigkeit | Qualitativ |
| Geschwindigkeit | Stetig |
| Urlaubstage | Diskret |
| Beruf | Qualitativ |

**Quelle:** Lösung der Testseite; Merkmalsarten im Skript ab S. 209.

## Aufgabe 69 – Verfahren auf diskreten Werten (Multiple Choice, 2 richtig)
**Antwort:**
- Klassifikation
- Assoziationsanalysen

**Falsch:** Clusteranalysen, Regression (siehe Aufgabe 66).
**Begründung:** Klassifikation und Assoziationsanalysen benötigen für die Regeln zur Vorhersage einen diskreten Vorhersagewert.
**Quelle:** Erläuterung der Testseite.

## Aufgabe 70 – Ziele der Datenanalyse und passende Methode (Drag & Drop)
| Ziel | Methode |
|---|---|
| Abweichungsanalysen | Ausreißertests |
| Klassifikation | Entscheidungsbäume |
| Segmentierung | Clusteranalysen |
| Prognose stetiger Werte | Regressionsanalysen |
| Abhängigkeitsanalysen | Assoziationsregeln |

**Quelle:** S. 202–203 (Aufgaben und Methoden des Data Mining).

## Aufgabe 71 – Methoden und Aufgaben im Data Mining (Zuordnung)
| Methode | Aufgabe |
|---|---|
| Gerichtete Bayessche Netze | Abhängigkeiten |
| Fallbasiertes Schließen | Klassifikation |
| Clusteranalysen | Segmentierung |
| Assoziationsregeln | Abhängigkeiten |
| Ausreißertests | Abweichungsanalysen |
| Entscheidungsbäume | Klassifikation |
| K-nächste-Nachbarn | Klassifikation |
| Diskriminanzanalyse | Klassifikation |
| Unüberwachte neuronale Netze | Segmentierung |
| Überwachte neuronale Netze | Klassifikation |

**Merkhilfe:** Klassifikation = Entscheidungsbäume, Diskriminanzanalyse, K-nächste-Nachbarn, Fallbasiertes Schließen, überwachte neuronale Netze. Segmentierung = Clusteranalysen, unüberwachte neuronale Netze. Abhängigkeiten = Assoziationsregeln, Gerichtete Bayessche Netze. Abweichungsanalysen = Ausreißertests.
**Quelle:** S. 203 (Methoden des Data Mining).

## Aufgabe 72 – Arten der Korrelation (Drag & Drop)
| Bedeutung | Art |
|---|---|
| Zufälliges zeitliches oder räumliches Zusammentreffen von Ereignissen | Koinzidenz |
| Subjektiv wahrgenommener Zusammenhang, der objektiv nicht existiert | Illusorische Korrelation |
| Logischer Fehlschluss aufgrund einer Korrelation | Scheinkausalität |
| Korrelation ohne inhaltlichen Zusammenhang | Scheinkorrelation |

**Quelle:** Lösung der Testseite; die Begriffe stehen im Skript nicht wörtlich.

## Aufgabe 73 – Repräsentativität und Überanpassung (Lückentext)
1. Die für das Data Mining eingesetzten Daten müssen bzgl. der möglichen Einsatzszenarien **repräsentativ** sein.
2. Auch dann ist bei einem gefundenen Modell die **Verallgemeinerungsfähigkeit** nicht immer gegeben.
3. Man bezeichnet dies auch als **Überanpassung** des Modells
4. auf die **Trainingsdaten**.
5. Diese kann mittels einer **Fitfunktion** analysiert werden,
6. die die Genauigkeit eines Modells als Funktion der **Komplexität** darstellt.

**Quelle:** Erläuterung der Testseite; Überanpassung im Skript S. 256–258.

## Aufgabe 74 – Fragestellungen und Aufgabentypen im Data Mining (Drag & Drop)
| Fragestellung | Aufgabentyp |
|---|---|
| Untersuchung von Kaufabhängigkeiten | Assoziationsregeln |
| Untersuchung typischer Verhaltensmuster | Profiling |
| Berechnung einer Unfallwahrscheinlichkeit | Regression |
| Vorschlag für Produktempfehlungen anhand Erfahrungen mit anderen Kunden | Ähnlichkeitstests |
| Vorhersage der Kreditwürdigkeit | Klassifikation |
| Vorhersage der Kundenreaktion auf bestimmte Werbung | Kausalmodellbildung |

**Begründung:** Kreditwürdigkeit = Zuordnung zu einer Klasse. Numerische Vorhersagen (Wahrscheinlichkeit) = Regression. Vorhersagen mit genauen Bezügen aus der Vergangenheit (andere Kunden) = Ähnlichkeitstests. Daraus abgeleitete Regeln = Assoziationsverfahren. Profiling untersucht Muster. Vorhersagen aufgrund durchgeführter Aktionen (Werbung) = Kausalmodelle.
**Quelle:** Erläuterung der Testseite. Aus der Erläuterung hergeleitet (die ersten beiden Zeilen waren bereits korrekt), auf der Testseite noch nicht als Ganzes bestätigt.

---

# Thema: Clustering (Kapitel 10)

## Aufgabe 75 – Euklidischer Abstand (Zahleneingabe)
**Frage:** Euklidischer Abstand zwischen X = (3, 7, 2, 11) und Y = (5, 7, 1, 9)?
**Antwort:** 3
**Rechnung:** Differenzen 2, 0, 1, 2 → Quadrate 4 + 0 + 1 + 4 = 9 → Wurzel aus 9 = 3.
**Quelle:** S. 211–212 (Abstandsmaße).

## Aufgabe 76 – Ergebnis eines Clusterings veranschaulichen (Multiple Choice, 3 richtig)
**Antwort:**
- Entscheidungsbaum
- Angabe der Clustergrenzen
- Zentroid mit Radius

**Falsch:** Fitfunktion, Nächste-Nachbar-Analyse.
**Begründung:** Die Clustergrenzen lassen sich absolut oder bei sphärischen Clustern über ihr Zentrum mit dem Radius beschreiben. Nach dem Clustering kann ein Entscheidungsbaumverfahren Regeln finden, über die die Clusterzugehörigkeit ermittelt wird.
**Quelle:** Erläuterung der Testseite; Clustering im Skript ab S. 217.

## Aufgabe 77 – Merkmale verschiedener Clustering-Verfahren (Lückentext)
1. **Partitionierende** Verfahren liefern eine Einteilung der Objekte in eine bestimmte Anzahl von Clustern.
2. **Hierarchische** Verfahren bauen dagegen einen Baum über Verschmelzungsebenen auf,
3. der sich in einem **Dendrogramm** darstellen lässt.
4. **Disjunkte** Methoden weisen ein Objekt nur genau einem Cluster zu.
5. Werden alle Objekte mindestens einem Cluster zugeordnet, handelt es sich um ein **exhaustives** Verfahren.
6. Objekte, die sich keinem Cluster zuordnen lassen, werden häufig als **Rauschen** bezeichnet.

**Quelle:** S. 219 (Einteilung der Clustering-Verfahren), S. 223–224 (Dendrogramm).

## Aufgabe 78 – Datenarten beim Clustering (Drag & Drop)
| Datenart | Beispiel |
|---|---|
| Kontinuierlich | Gewicht |
| Quantitativ-Diskret | Bestellmenge |
| Nominal | Studiengang |
| Binär | Erlaubnis für Cookies durch einen Online-Kunden |
| Ordinal | Anforderungspriorität |

**Begründung:** Quantitativ-diskret = natürliche Zahlen, fest definierte Zustände. Kontinuierlich = reelle Zahlen. Ordinal = qualitativ mit Reihenfolge. Nominal = qualitativ ohne Reihenfolge. Binär = Sonderfall nominal mit nur zwei Ausprägungen.
**Quelle:** S. 210 (Datenarten). Aus der Erläuterung hergeleitet, auf der Testseite noch nicht bestätigt.

## Aufgabe 79 – Manhattan-Metrik (Zahleneingabe)
**Frage:** Abstand nach Manhattan-Metrik zwischen X = (3, 7, 2, 11) und Y = (5, 7, 1, 9)?
**Antwort:** 5
**Rechnung:** Beträge der Differenzen: 2 + 0 + 1 + 2 = 5.
**Quelle:** S. 212 (Manhattan-Metrik).

## Aufgabe 80 – Grundkonzept der Clusteranalyse (Lückentext)
1. Ziel ist eine möglichst hohe Intra-Cluster-**Homogenität** der Objekte in einem Cluster.
2. Bei **hierarchischen** Verfahren ist die Anzahl der Cluster nicht vorzugeben,
3. verschiedene Ebenen möglicher Einteilungen werden in Form eines **Dendrogramms** dargestellt.
4. Das Verfahren k-Means clustert die Objekte um einen **Zentroiden**.

**Quelle:** S. 217 (Homogenität), S. 220 (Zentroid), S. 223–224 (Dendrogramm).

## Aufgabe 81 – Clusteringalgorithmen und Konfigurationsparameter (Zuordnung)
| Algorithmus | Parameter |
|---|---|
| k-Means | Clusteranzahl |
| k-Medoid | Clusteranzahl |
| Hierarchische Verfahren | Parameterlos |
| Dichtebasierte Verfahren | Mindestabstand |

**Begründung:** Bei k-Means und k-Medoid muss die Clusteranzahl vorgegeben werden. Dichtebasierte Verfahren benötigen einen Mindestabstand für die Aufnahme eines Objekts in ein Cluster. Hierarchische Verfahren arbeiten parameterlos.
**Quelle:** Erläuterung der Testseite; Skript S. 220–229.

## Aufgabe 82 – k-Means: verschobene Objekte vor Neuberechnung (Single Choice)
**Frage:** Wie viele Objekte werden bei k-Means maximal vor einer Neuberechnung der Clusterzentren verschoben?
**Antwort:** 1
**Begründung:** Bei k-Means werden nach dem Verschieben eines jeden einzelnen Objekts die Zentren neu berechnet.
**Quelle:** Erläuterung der Testseite; k-Means im Skript S. 220–223.

---

# Thema: Klassifikation, Entscheidungsbäume und Assoziationsregeln (Kapitel 10)

## Aufgabe 83 – Verfahrensmerkmale C5.0, CART, CHAID (Tabelle, Dropdowns)
| | C5.0 | CART | CHAID |
|---|---|---|---|
| Splitanzahl | multiple | binär | multiple |
| Split-Gütemaß | Informationsgewinn | Gini-Koeffizient | Chi-Quadrat-Maß |
| Pruning | Pruning | Pruning | Kein Pruning |

**Merkhilfe:** Nur CART splittet binär, nur CHAID hat kein Pruning. „unär“ kommt nie vor.
**Quelle:** S. 254–256 (Entscheidungsbaumverfahren).

## Aufgabe 84 – Anzahl Regeln eines Entscheidungsbaums (Zahleneingabe)
**Frage:** Wie viele Regeln entstehen durch den abgebildeten Entscheidungsbaum (Sicherheiten → Bestehende Verschuldung → Einkommen)?
**Antwort:** 5
**Begründung:** Jeder Weg zu einem Blatt führt zu einer Regel. Der Baum hat 5 Blätter: Niedriges Risiko (Sicherheiten ja), Hohes Risiko (Verschuldung ja), Hohes Risiko (Einkommen niedrig), Mittleres Risiko (Einkommen mittel), Niedriges Risiko (Einkommen hoch).
**Quelle:** Erläuterung der Testseite; selbst gezählt.

## Aufgabe 85 – Klassifikation auf Basis einer mathematischen Funktion (Multiple Choice, 2 richtig)
**Antwort:**
- Logistische Regression
- Support Vector Machines

**Falsch:** Regressionsanalysen (keine Klassifikation), Entscheidungsbäume (Regeln statt Funktion).
**Begründung:** Sowohl die logistische Regression als auch Support Vector Machines suchen Trennebenen zwischen Klassen, die über eine mathematische Funktion beschrieben werden.
**Quelle:** Erläuterung der Testseite.

## Aufgabe 86 – Multivariate Entscheidungsbäume (Single Choice)
**Antwort:** Bäume, die mehr als eine Variable in einem Knoten nutzen.
**Falsch:** Bäume ohne Pruning; mehrere Bäume zu unterschiedlichen Trainingsdaten; Bäume mit mehr als zwei Ebenen; Bäume mit nicht-binären Knoten.
**Quelle:** S. 255, S. 259–261 (Multivariate Entscheidungsbäume).

## Aufgabe 87 – Pruning bei Klassifikationsverfahren (Single Choice)
**Frage:** Bei welchen Klassifikationsverfahren wird Pruning zur Verbesserung der Verallgemeinerungsfähigkeit eingesetzt?
**Antwort:** Entscheidungsbäume
**Begründung:** Beim Pruning werden Bäume zurückgeschnitten.
**Quelle:** S. 256–258, Abschnitt 10.4.5. (Auf der Testseite als korrekt bestätigt.)

## Aufgabe 88 – Attributabhängigkeit vs. Regelqualitätskriterium (Zuordnung)
| Maß | Zuordnung |
|---|---|
| Lift | Regelqualitätskriterium |
| Support | Regelqualitätskriterium |
| Konfidenz | Regelqualitätskriterium |
| Gini-Index | Attributabhängigkeit |
| Chi-Quadrat-Unabhängigkeit | Attributabhängigkeit |
| Entropie | Attributabhängigkeit |

**Begründung:** Chi-Quadrat-Unabhängigkeit, Gini-Index und Entropie bewerten Abhängigkeiten bei Attributen (Split-Maße der Entscheidungsbäume). Lift, Support und Konfidenz bewerten die Qualität von Regeln (Assoziationsregeln).
**Quelle:** S. 254–256 (Split-Maße), S. 271–274 (Support, Konfidenz, Lift).

## Aufgabe 89 – Warum wird Pruning verwendet? (Single Choice)
**Antwort:** Zur Vermeidung eines Overfitting.
**Falsch:** Homogenisierung von Klassen; Verbesserung der Entropie; Überführung von Regeln in Programmcode.
**Begründung:** Pruning schneidet Entscheidungsbäume zurück, so dass die Überanpassung an die Trainingsdaten zurückgenommen bzw. verhindert wird.
**Quelle:** S. 256, Abschnitt 10.4.5.

## Aufgabe 90 – Ende des Wachstums eines Pfads bei Entscheidungsbäumen (Multiple Choice, 3 richtig)
**Antwort:**
- Die Menge der Datensätze in einem Knoten unterschreitet eine bestimmte Mindestanzahl.
- Alle Datensätze in einem Knoten haben dieselbe Klassenzugehörigkeit.
- Alle Datensätze in einem Knoten sind in ihren Merkmalsausprägungen identisch (aber nicht unbedingt derselben Klasse zugeordnet).

**Falsch:** Der Baum führt zu zu vielen Regeln; der Baum hat eine Maximalhöhe erreicht; das Post-Pruning beginnt. Die Baumgröße hat keinen Einfluss.
**Quelle:** Erläuterung der Testseite; Skript S. 256–258.

## Aufgabe 91 – Qualitätsmerkmale von Regeln (Drag & Drop)
| Aussage | Maß |
|---|---|
| Relevanz | Support |
| Güte | Lift |
| Stärke | Konfidenz |

**Quelle:** S. 271–274 (Assoziationsregeln).

---

# Thema: Assoziationsregeln (Kapitel 10)

## Aufgabe 92 – Konfidenz einer Assoziationsregel (Zahleneingabe)
**Gegeben:** fünf Einkäufe
- K1: {USB-Speicherstick, SIM-Karte, Kopierpapier, Toner}
- K2: {Kopierpapier, WLAN-Karte}
- K3: {Smartphone, Handyhülle, Kopierpapier}
- K4: {Toner, Drucklabels, Kopierpapier}
- K5: {Toner, Tablet}

**Frage:** Wie hoch ist die Konfidenz der Regel „Kopierpapier → Toner“ in Prozent?
**Antwort:** 50
**Rechnung:** Kopierpapier kommt in 4 Einkäufen vor (K1, K2, K3, K4), davon enthalten 2 auch Toner (K1, K4). Konfidenz = 2 / 4 = 0,5 = 50 %.
**Quelle:** S. 271–274 (Support und Konfidenz).

## Aufgabe 93 – Anzahl möglicher Regeln aus einem Itemset (Zahleneingabe)
**Frage:** Itemset {Honig, Senf, Bier}. Wie viele mögliche Regeln lassen sich daraus bei der Regelfindung im Apriori-Algorithmus finden?
**Antwort:** 6
**Rechnung:** Drei Regeln mit einem Wert links und zwei Werten rechts (Honig → Senf, Bier; Senf → Honig, Bier; Bier → Honig, Senf) und drei Regeln mit zwei Werten links und einem Wert rechts (Honig, Senf → Bier; Honig, Bier → Senf; Senf, Bier → Honig).
**Quelle:** S. 274–279 (Apriori-Algorithmus, Regelgenerierung).

## Aufgabe 94 – Support einer Assoziationsregel (Zahleneingabe)
**Gegeben:** dieselben fünf Einkäufe wie in Aufgabe 92.
**Frage:** Wie hoch ist der Support der Regel „Kopierpapier → Toner“ in Prozent?
**Antwort:** 40
**Rechnung:** Die Kombination Kopierpapier + Toner kommt in 2 von 5 Einkäufen vor (K1, K4). Support = 2 / 5 = 0,4 = 40 %.
**Merkhilfe:** Support teilt durch alle Transaktionen, Konfidenz nur durch die Transaktionen mit der linken Seite der Regel.
**Quelle:** S. 271–274 (Support und Konfidenz).
