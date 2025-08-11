# PSP-RS part IV

| Modality       | Item                                    | Description                             | ItemType   | Required   | Values              |   Unnamed: 13 |
|:---------------|:----------------------------------------|:----------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| PSP-RS part IV | psp_rs_iv_01_volunt_upward_movement     | psp_rs_iv_01_volunt_upward_movement     | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part IV | psp_rs_iv_02_volunt_downward_movement   | psp_rs_iv_02_volunt_downward_movement   | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part IV | psp_rs_iv_03_volunt_left_right_movement | psp_rs_iv_03_volunt_left_right_movement | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part IV | psp_rs_iv_04_eyelid dysfunction         | psp_rs_iv_04_eyelid dysfunction         | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part IV | psp_rs_iv_summary_score                 | psp_rs_iv_summary_score                 | integer    | nullable   | (y>=0) & (y<=16)    |           nan |