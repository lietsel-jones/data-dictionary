# UPDRS Part I

| Modality     | Item                                | Description                       | ItemType   | Required   | Values              |   Unnamed: 13 |
|:-------------|:------------------------------------|:----------------------------------|:-----------|:-----------|:--------------------|--------------:|
| UPDRS Part I | code_upd101_intellectual_impairment | Mentation:Intellectual Impairment | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part I | code_upd102_thought_disorder        | Mentation:Thought Disorder        | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part I | code_upd103_depression              | Mentation:Depression              | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part I | code_upd104_motivation              | Mentation:Motivation/Initiative   | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part I | updrs_part_i_summary_score          | UPDRS Part I Summary Score        | integer    | nullable   | (y>=0) & (y<=16)    |           nan |