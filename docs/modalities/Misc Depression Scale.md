# Misc Depression Scale

| Modality              | Item               | Description                                                                    | ItemType   | Required   | Values                 |   Unnamed: 13 |
|:----------------------|:-------------------|:-------------------------------------------------------------------------------|:-----------|:-----------|:-----------------------|--------------:|
| Misc Depression Scale | is_depressed       | Does the patient have depression based on the cut-off score of the scale used? | string     | nullable   | ["Yes","No","Unknown"] |           nan |
| Misc Depression Scale | depress_test_name  | Test used for depression screening (e.g. GDS15, HDRS, BDI, PHQ9 (DPUK), GHQ)   | string     | nullable   | nan                    |           nan |
| Misc Depression Scale | depress_test_score | Total score on the depression scale used                                       | numeric    | nullable   | (y>=0) & (y<=100)      |           nan |