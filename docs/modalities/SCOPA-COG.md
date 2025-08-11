# SCOPA-COG

| Modality   | Item                           | Description                            | ItemType   | Required   | Values                    |   Unnamed: 13 |
|:-----------|:-------------------------------|:---------------------------------------|:-----------|:-----------|:--------------------------|--------------:|
| SCOPA-COG  | scopa_cog1_verbal_recall       | SCOPA-COG item 1 - verbal recall       | integer    | nullable   | y.isin([0,1,2,3,4,5])     |           nan |
| SCOPA-COG  | scopa_cog2_digit_span_backward | SCOPA-COG item 2 - digit span backward | integer    | nullable   | y.isin([0,1,2,3,4,5,6,7]) |           nan |
| SCOPA-COG  | scopa_cog3_cube                | SCOPA-COG item 3 - indicate cubes      | integer    | nullable   | y.isin([0,1,2,3,4,5])     |           nan |
| SCOPA-COG  | scopa_cog4_count_backwards     | SCOPA-COG item 4 - counting backwards  | integer    | nullable   | y.isin([0,1,2])           |           nan |
| SCOPA-COG  | scopa_cog5_months_backward     | SCOPA-COG item 5 - months backwards    | integer    | nullable   | y.isin([0,1,2])           |           nan |
| SCOPA-COG  | scopa_cog6_fist_edge_palm      | SCOPA-COG item 6 - fist-edge-palm      | integer    | nullable   | y.isin([0,1,2,3])         |           nan |
| SCOPA-COG  | scopa_cog7_semantic_fluency    | SCOPA-COG item 7 - semantic fluency    | integer    | nullable   | y.isin([0,1,2,3,4,5,6])   |           nan |
| SCOPA-COG  | scopa_cog8_dice                | SCOPA-COG item 8 - dice                | integer    | nullable   | y.isin([0,1,2,3])         |           nan |
| SCOPA-COG  | scopa_cog9_assembling_figures  | SCOPA-COG item 9 - assembling patterns | integer    | nullable   | y.isin([0,1,2,3,4,5])     |           nan |
| SCOPA-COG  | scopa_cog10_delayed_recall     | SCOPA-COG item 10 - delayed recall     | integer    | nullable   | y.isin([0,1,2,3,4,5])     |           nan |
| SCOPA-COG  | scopa_cog_total_score          | SCOPA-COG Total Score                  | integer    | nullable   | (y>=0) & (y<=43)          |           nan |