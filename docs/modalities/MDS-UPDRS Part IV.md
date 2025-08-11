# MDS-UPDRS Part IV

| Modality          | Item                                           | Description                                                  | ItemType   | Required   | Values              |   Unnamed: 13 |
|:------------------|:-----------------------------------------------|:-------------------------------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| MDS-UPDRS Part IV | code_upd2401_time_spent_with_dyskinesias       | 4.01 MDS-UPDRS - Time Spent With Dyskinesias (UPD2401)       | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part IV | code_upd2402_functional_impact_of_dyskinesias  | 4.02 MDS-UPDRS - Functional Impact Of Dyskinesias (UPD2402)  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part IV | code_upd2403_time_spent_in_the_off_state       | 4.03 MDS-UPDRS - Time Spent In The Off State (UPD2403)       | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part IV | code_upd2404_functional_impact_of_fluctuations | 4.04 MDS-UPDRS - Functional Impact Of Fluctuations (UPD2404) | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part IV | code_upd2405_complexity_of_motor_fluctuations  | 4.05 MDS-UPDRS - Complexity Of Motor Fluctuations (UPD2405)  | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part IV | code_upd2406_painful_off_state_dystonia        | 4.06 MDS-UPDRS - Painful Off-State Dystonia (UPD2406)        | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| MDS-UPDRS Part IV | mds_updrs_part_iv_summary_score                | MDS-UPDRS Part IV Summary Score                              | integer    | nullable   | (y>=0) & (y<=24)    |           nan |
| MDS-UPDRS Part IV | upd2406_1_total_hours_off                      | 4.06.1 MDS-UPDRS - Total Hours OFF                           | numeric    | nullable   | (y>=0) & (y<=1440)  |           nan |
| MDS-UPDRS Part IV | upd2406_2_off_hours_wo_dystonia                | 4.06.2 MDS-UPDRS - Total OFF Hours with Dystonia             | numeric    | nullable   | (y>=0) & (y<=1440)  |           nan |
| MDS-UPDRS Part IV | upd2406_3_pct_off_dystonia                     | 4.06.3 MDS-UPDRS - % OFF Dystonia = ((2/1)*100)              | numeric    | nullable   | (y>=0) & (y<=100)   |           nan |