# Current Medication Status

| Modality                  | Item                          | Description                                                       | ItemType   | Required   | Values              |   Unnamed: 13 |
|:--------------------------|:------------------------------|:------------------------------------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| Current Medication Status | medication_data_availability  | Is the medication data available? Yes or no for the dataset       | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | levodopa_mg_daily             | Levodopa Dosage per day                                           | numeric    | nullable   | (y>=0) & (y<=10000) |           nan |
| Current Medication Status | ledd_daily                    | Levodopa Equivalent Dosage (LEDD) per day (including all PD meds) | numeric    | nullable   | (y>=0) & (y<=10000) |           nan |
| Current Medication Status | levodopa_use                  | Usage of levodopa                                                 | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | dopamine_agonist_use          | Usage of dopamine agonist                                         | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | anticholinergics_use          | Usage of anticholinergics                                         | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | brain_surgery                 | Usage of DBS/Brain surgery                                        | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | cholin_esterase_inhibitor_use | Usage of cholinesterase Inhibitors                                | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | anti_depressant_use           | Usage of anti-depressant drugs                                    | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | sleeping_pills_use            | Usage of sleeping pills                                           | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | stomach_medicines_use         | Usage of stomach medicines (including for nausea, GERD)           | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | laxatives_use                 | Usage of laxatives (not fibers)                                   | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | NSAIDs_use                    | Usage of NSAIDs                                                   | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | morphines_use                 | Usage of morphines                                                | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | anti_psychotics_use           | Usage of anti-psychotics                                          | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | insulin_use                   | Usage of insulin                                                  | string     | nullable   | ["Yes", "No"]       |           nan |
| Current Medication Status | hormone_replacement_therapy   | Usage of sex hormones replacement therapy                         | string     | nullable   | ["Yes", "No"]       |           nan |