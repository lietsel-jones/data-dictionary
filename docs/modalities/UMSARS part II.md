# UMSARS part II

| Modality       | Item                                  | Description                          | ItemType   | Required   | Values              |   Unnamed: 13 |
|:---------------|:--------------------------------------|:-------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| UMSARS part II | umsars_ii_01_facial_expression        | Facial expression                    | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_02_speech                   | Speech                               | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_03_oculomotor_dysfunction   | Ocular motor dysfunction             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_04_resting_tremor           | Tremor at rest (most affected limb)  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_05_action_tremor            | Action tremor                        | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_06_increased_tone           | Increased tone (most affected limb)  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_07_rapid_alt_hand_movements | Rapid alternating movements of hands | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_08_finger_taps              | Finger taps                          | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_09_leg_agility              | Leg agility                          | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_10_heel_knee_shin_test      | Heel-knee-shin test                  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_11_arise_chair              | Arising from chair                   | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_12_posture                  | Posture                              | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_13_body_sway                | Body sway                            | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_14_gait                     | Gait                                 | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UMSARS part II | umsars_ii_summary_score               | UMSARS part II summary score         | integer    | nullable   | (y>=0) & (y<=56)    |           nan |