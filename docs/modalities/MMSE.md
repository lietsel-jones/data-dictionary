# MMSE

| Modality   | Item                       | Description                                                                                   | ItemType   | Required   | Values           |   Unnamed: 13 |
|:-----------|:---------------------------|:----------------------------------------------------------------------------------------------|:-----------|:-----------|:-----------------|--------------:|
| MMSE       | mmse_01_year               | MMSE 1 - year                                                                                 | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_02_season             | MMSE 2 - season                                                                               | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_03_date               | MMSE 3 - date                                                                                 | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_04_day                | MMSE 4 - day                                                                                  | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_05_month              | MMSE 5 - month                                                                                | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_orientation_time      | x[["mmse_01_year","mmse_02_season","mmse_03_date","mmse_04_day","mmse_05_month"]].sum(axis=1) | integer    | nullable   | (y>=0) & (y<=5)  |           nan |
| MMSE       | mmse_06_state              | MMSE 6 - state                                                                                | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_07_county             | MMSE 7 - county                                                                               | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_08_town               | MMSE 8 - town                                                                                 | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_09_hospital           | MMSE 9 - hospital                                                                             | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_10_floor              | MMSE 10 - floor                                                                               | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_orientation_place     | sum MMSE 6-10 orientation/place                                                               | integer    | nullable   | (y>=0) & (y<=5)  |           nan |
| MMSE       | mmse_11_immediate_recall_1 | MMSE 11 - immediate recall 1                                                                  | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_12_immediate_recall_2 | MMSE 12 - immediate recall 2                                                                  | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_13_immediate_recall_3 | MMSE 13 - immediate recall 3                                                                  | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_immediate_recall      | sum MMSE 11-13 recall                                                                         | integer    | nullable   | (y>=0) & (y<=3)  |           nan |
| MMSE       | mmse_14_serial7_1          | MMSE 14 - serial 7 item 1                                                                     | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_15_serial7_2          | MMSE 15 - serial 7 item 2                                                                     | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_16_serial7_3          | MMSE 16 - serial 7 item 3                                                                     | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_17_serial7_4          | MMSE 17 - serial 7 item 4                                                                     | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_18_serial7_5          | MMSE 18 - serial 7 item 5                                                                     | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_serial7               | sum MMSE 14-18 serial 7                                                                       | integer    | nullable   | (y>=0) & (y<=5)  |           nan |
| MMSE       | mmse_19_delayed_recall_1   | MMSE 19 - delayed recall item 1                                                               | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_20_delayed_recall_2   | MMSE 20 - delayed recall item 2                                                               | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_21_delayed_recall_3   | MMSE 21 - delayed recall item 3                                                               | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_delayed_recall        | sum MMSE 19-21 delayed recall                                                                 | integer    | nullable   | (y>=0) & (y<=3)  |           nan |
| MMSE       | mmse_22_naming_1           | MMSE 22 naming item 1                                                                         | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_23_naming_2           | MMSE 23 naming item 2                                                                         | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_naming                | sum MMSE 22-23 naming                                                                         | integer    | nullable   | y.isin([0,1, 2]) |           nan |
| MMSE       | mmse_24_repeating          | MMSE 24 - repetition                                                                          | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_25_oral_command_1     | MMSE 25 - oral command item 1                                                                 | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_26_oral_command_2     | MMSE 26 - oral command item 2                                                                 | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_27_oral_command_3     | MMSE 27 - oral command item 3                                                                 | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_comprehension         | sum MMSE 25-27 comprehension                                                                  | integer    | nullable   | (y>=0) & (y<=3)  |           nan |
| MMSE       | mmse_28_reading            | MMSE 28 - reading                                                                             | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_29_writing            | MMSE 29 - writing                                                                             | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_30_drawing            | MMSE 30 - drawing                                                                             | integer    | nullable   | y.isin([0,1])    |           nan |
| MMSE       | mmse_total_score           | MMSE total score                                                                              | integer    | nullable   | (y>=0) & (y<=30) |           nan |