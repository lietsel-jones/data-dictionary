# UPDRS Part II

| Modality      | Item                           | Description                        | ItemType   | Required   | Values              |   Unnamed: 13 |
|:--------------|:-------------------------------|:-----------------------------------|:-----------|:-----------|:--------------------|--------------:|
| UPDRS Part II | code_upd105_speech             | Activities:Speech                  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd106_salivation         | Activities:Salivation              | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd107_swallowing         | Activities:Swallowing              | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd108_handwriting        | Activities:Handwriting             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd109_eating_tasks       | Activities:Cut Food/Handle Utensil | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd110_dressing           | Activities:Dressing                | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd111_hygiene            | Activities:Hygiene                 | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd112_bed                | Activities:Turn Bed/Adj Clothes    | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd113_falling            | Activities:Falling                 | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd114_freezing_of_gait   | Activities:Freezing When Walking   | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd115_walking            | Activities:Walking                 | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd116_tremor             | Activities:Tremor                  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | code_upd117_sensory_complaints | Activities:Sensory Complaints      | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part II | updrs_part_ii_summary_score    | UPDRS Part II Summary Score        | integer    | nullable   | (y>=0) & (y<=52)    |           nan |