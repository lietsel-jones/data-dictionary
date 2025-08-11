# PSP-RS part I

| Modality      | Item                                   | Description                            | ItemType   | Required   | Values              |   Unnamed: 13 |
|:--------------|:---------------------------------------|:---------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| PSP-RS part I | psp_rs_i_01_withdrawl                  | psp_rs_i_01_withdrawl                  | integer    | nullable   | y.isin([0,1,2])     |           nan |
| PSP-RS part I | psp_rs_i_02_irritability               | psp_rs_i_02_irritability               | integer    | nullable   | y.isin([0,1,2])     |           nan |
| PSP-RS part I | psp_rs_i_03_solid_dysphagia            | psp_rs_i_03_solid_dysphagia            | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part I | psp_rs_i_04_use_fork_buttoning_washing | psp_rs_i_04_use_fork_buttoning_washing | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part I | psp_rs_i_05_falls                      | psp_rs_i_05_falls                      | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part I | psp_rs_i_06_urinary_incontinence       | psp_rs_i_06_urinary_incontinence       | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part I | psp_rs_i_07_sleep_difficulty           | psp_rs_i_07_sleep_difficulty           | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part I | psp_rs_i_summary_score                 | psp_rs_i_summary_score                 | integer    | nullable   | (y>=0) & (y<=24)    |           nan |