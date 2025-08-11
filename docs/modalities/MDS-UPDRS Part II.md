# MDS-UPDRS Part II

| Modality          | Item                                            | Description                                                   | ItemType   | Required   | Values              |   Unnamed: 13 |
|:------------------|:------------------------------------------------|:--------------------------------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| MDS-UPDRS Part II | mds_updrs_part_ii_primary_info_source           | MDS-UPDRS Part II Primary Source Of Information               | string     | nullable   | nan                 |           nan |
| MDS-UPDRS Part II | code_upd2201_speech                             | 2.01 MDS-UPDRS - Speech (UPD2201)                             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2202_saliva_and_drooling                | 2.02 MDS-UPDRS - Saliva And Drooling (UPD2202)                | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2203_chewing_and_swallowing             | 2.03 MDS-UPDRS - Chewing And Swallowing (UPD2203)             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2204_eating_tasks                       | 2.04 MDS-UPDRS - Eating Tasks (UPD2204)                       | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2205_dressing                           | 2.05 MDS-UPDRS - Dressing (UPD2205)                           | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2206_hygiene                            | 2.06 MDS-UPDRS - Hygiene (UPD2206)                            | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2207_handwriting                        | 2.07 MDS-UPDRS - Handwriting (UPD2207)                        | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2208_doing_hobbies_and_other_activities | 2.08 MDS-UPDRS - Doing Hobbies And Other Activities (UPD2208) | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2209_turning_in_bed                     | 2.09 MDS-UPDRS - Turning In Bed (UPD2209)                     | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2210_tremor                             | 2.10 MDS-UPDRS - Tremor (UPD2210)                             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2211_get_out_of_bed_car_or_deep_chair   | 2.11 MDS-UPDRS - Get Out Of Bed, Car, Or Deep Chair (UPD2211) | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2212_walking_and_balance                | 2.12 MDS-UPDRS - Walking And Balance (UPD2212)                | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | code_upd2213_freezing                           | 2.13 MDS-UPDRS - Freezing (UPD2213)                           | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part II | mds_updrs_part_ii_summary_score                 | MDS-UPDRS Part II Summary Score                               | integer    | nullable   | (y>=0) & (y<=52)    |           nan |