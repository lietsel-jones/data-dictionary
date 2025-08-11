# UMSARS part I

| Modality      | Item                             | Description                                         | ItemType   | Required   | Values              |   Unnamed: 13 |
|:--------------|:---------------------------------|:----------------------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| UMSARS part I | umsars_i_02_swallowing           | Swallowing                                          | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_03_handwriting          | Handwriting                                         | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_04_food_utensils        | Cutting food and handling utensils                  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_05_dressing             | Dressing                                            | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_06_hygiene              | Hygiene                                             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_07_walking              | Walking                                             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_08_falling_rate         | Falling (past month)                                | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_09_orthostatic_symptoms | Orthostatic symptoms                                | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_10_urinary_function     | Urinary function (symptoms not due to other causes) | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_11_sexual_function      | Sexual function                                     | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_12_bowel_function       | Bowel function                                      | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part I | umsars_i_summary_score           | UMSARS part I summary score                         | integer    | nullable   | (y>=0) & (y<=48)    |           nan |