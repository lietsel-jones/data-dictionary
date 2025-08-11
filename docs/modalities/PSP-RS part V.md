# PSP-RS part V

| Modality      | Item                       | Description                | ItemType   | Required   | Values              |   Unnamed: 13 |
|:--------------|:---------------------------|:---------------------------|:-----------|:-----------|:--------------------|--------------:|
| PSP-RS part V | psp_rs_v_01_limb_rigidity  | psp_rs_v_01_limb_rigidity  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part V | psp_rs_v_02_limd_dystonia  | psp_rs_v_02_limd_dystonia  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| PSP-RS part V | psp_rs_v_03_finger_tapping | psp_rs_v_03_finger_tapping | integer    | nullable   | y.isin([0,1,2])     |           nan |
| PSP-RS part V | psp_rs_v_04_toe_tapping    | psp_rs_v_04_toe_tapping    | integer    | nullable   | y.isin([0,1,2])     |           nan |
| PSP-RS part V | psp_rs_v_05_hand_apraxia   | psp_rs_v_05_hand_apraxia   | integer    | nullable   | y.isin([0,1,2])     |           nan |
| PSP-RS part V | psp_rs_v_06_tremor         | psp_rs_v_06_tremor         | integer    | nullable   | y.isin([0,1,2])     |           nan |
| PSP-RS part V | psp_rs_v_summary_score     | psp_rs_v_summary_score     | integer    | nullable   | (y>=0) & (y<=16)    |           nan |