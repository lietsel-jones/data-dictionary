# UPDRS Part IV

| Modality      | Item                                         | Description                              | ItemType   | Required   | Values              |   Unnamed: 13 |
|:--------------|:---------------------------------------------|:-----------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| UPDRS Part IV | code_upd132_time_spent_with_dyskinesias      | Complications:Dyskinesias Duration       | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part IV | code_upd133_functional_impact_of_dyskinesias | Complications:Dyskinesias Disable        | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part IV | code_upd134_painful_dyskinesias              | Complications:Dyskinesias Painful        | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part IV | code_upd135_early_morning_dystonia           | Complications:Dyskinesias Dystonia       | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | code_upd136_predictable_off                  | Complications:Fluct Predictable          | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | code_upd137_unpredictable_off                | Complications:Fluct Unpredictable        | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | code_upd138_sudden_off                       | Complications:Fluct Suddenly             | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | code_upd139_time_spent_in_the_off_state      | Complications:Proportion OFF             | integer    | nullable   | y.isin([0,1,2,3,4]) |           nan |
| UPDRS Part IV | code_upd140_anorexia                         | Complications:Anorexia, Nausea, Vomiting | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | code_upd141_sleep_disturbances               | Complications:Insomnia, Hypersomnolence  | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | code_upd142_symptomatic_orthostasis          | Complications:Symptomatic Orthostasis    | integer    | nullable   | y.isin([0,1])       |           nan |
| UPDRS Part IV | updrs_part_iv_summary_score                  | UPDRS Part IV Summary Score              | integer    | nullable   | (y>=0) & (y<=23)    |           nan |