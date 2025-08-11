# MoCA

| Modality   | Item                                           | Description                                                      | ItemType   | Required   | Values                  |   Unnamed: 13 |
|:-----------|:-----------------------------------------------|:-----------------------------------------------------------------|:-----------|:-----------|:------------------------|--------------:|
| MoCA       | moca01_alternating_trail_making                | MOCA: 01. Alternating Trail Making                               | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca02_visuoconstr_skills_cube                 | MOCA: 02. Visuoconstructional Skills - Copy Cube                 | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca03_visuoconstr_skills_clock_cont           | MOCA: 03. Visuoconstructional Skills - Draw Clock Contour        | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca04_visuoconstr_skills_clock_num            | MOCA: 04. Visuoconstructional Skills - Draw Clock Numbers        | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca05_visuoconstr_skills_clock_hands          | MOCA: 05. Visuoconstructional Skills - Draw Clock Hands          | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca05_visuoconstr_skills_clock                | MOCA: Draw Clock Total                                           | integer    | nullable   | y.isin([0,1,2,3])       |           nan |
| MoCA       | moca_visuospatial_executive_subscore           | MOCA: Visuospatial And Executive Subscore                        | integer    | nullable   | y.isin([0,1,2,3,4,5])   |           nan |
| MoCA       | moca06_naming_lion                             | MOCA: 06. Naming - Lion                                          | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca07_naming_rhino                            | MOCA: 07. Naming - Rhino                                         | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca08_naming_camel                            | MOCA: 08. Naming - Camel                                         | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca_naming_subscore                           | MOCA: Naming Subscore                                            | integer    | nullable   | y.isin([0,1,2,3])       |           nan |
| MoCA       | moca09_attention_forward_digit_span            | MOCA: 09. Attention - Forward Digit Span                         | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca10_attention_backward_digit_span           | MOCA: 10. Attention - Backward Digit Span                        | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca_attention_digits_subscore                 | MOCA: Attention Forward-Backward Repeat Lists Of Digits Subscore | integer    | nullable   | y.isin([0,1,2])         |           nan |
| MoCA       | moca11_attention_vigilance                     | MOCA: 11. Attention - Vigilance                                  | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca12_attention_serial_7s                     | MOCA: 12. Attention - Serial 7s                                  | integer    | nullable   | y.isin([0,1,2,3])       |           nan |
| MoCA       | moca_attention_subscore                        | MOCA: Attention domain subscore                                  | integer    | nullable   | y.isin([0,1,2,3,4,5,6]) |           nan |
| MoCA       | moca13_sentence_repetition                     | MOCA: 13. Sentence Repetition                                    | integer    | nullable   | y.isin([0,1,2])         |           nan |
| MoCA       | moca13_sentence_repetition_1                   | MOCA: 13. Sentence Repetition 1                                  | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca13_sentence_repetition_2                   | MOCA: 13. Sentence Repetition 2                                  | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca14_verbal_fluency_number_of_words          | MOCA: 14. Verbal Fluency - Number Of Words                       | integer    | nullable   | (y>=0) & (y<=100)       |           nan |
| MoCA       | moca15_verbal_fluency                          | MOCA: 15. Verbal Fluency                                         | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca_language_subscore                         | MOCA: Language Subscore                                          | integer    | nullable   | y.isin([0,1,2,3])       |           nan |
| MoCA       | moca16_abstraction_1                           | MOCA: 16. Abstraction 1                                          | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca16_abstraction_2                           | MOCA: 16. Abstraction 2                                          | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca_abstraction_subscore                      | moca16_abstraction_1 + moca16_abstraction_2                      | integer    | nullable   | y.isin([0,1,2])         |           nan |
| MoCA       | moca17_delayed_recall_face                     | MOCA: 17. Delayed Recall - Face                                  | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca18_delayed_recall_velvet                   | MOCA: 18. Delayed Recall - Velvet                                | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca19_delayed_recall_church                   | MOCA: 19. Delayed Recall - Church                                | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca20_delayed_recall_daisy                    | MOCA: 20. Delayed Recall - Daisy                                 | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca21_delayed_recall_red                      | MOCA: 21. Delayed Recall - Red                                   | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca_delayed_recall_subscore_optnl_cat_cue     | MOCA: Delayed Recall Subscore Optional Category Cue              | integer    | nullable   | y.isin([0,1,2,3,4,5])   |           nan |
| MoCA       | moca_delayed_recall_subscore_optnl_mult_choice | MOCA: Delayed Recall Subscore Optional Multiple Choice Cue       | integer    | nullable   | y.isin([0,1,2,3,4,5])   |           nan |
| MoCA       | moca_delayed_recall_subscore                   | MOCA: Delayed Recall Subscore Uncued                             | integer    | nullable   | y.isin([0,1,2,3,4,5])   |           nan |
| MoCA       | moca22_orientation_date_score                  | MOCA: 22. Orientation - Date Score                               | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca23_orientation_month_score                 | MOCA: 23. Orientation - Month Score                              | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca24_orientation_year_score                  | MOCA: 24. Orientation - Year  Score                              | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca25_orientation_day_score                   | MOCA: 25. Orientation - Day Score                                | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca26_orientation_place_score                 | MOCA: 26. Orientation - Place Score                              | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca27_orientation_city_score                  | MOCA: 27. Orientation - City Score                               | integer    | nullable   | y.isin([0,1])           |           nan |
| MoCA       | moca_orientation_subscore                      | MOCA: Orientation Subscore                                       | integer    | nullable   | y.isin([0,1,2,3,4,5,6]) |           nan |
| MoCA       | moca_total_score                               | MOCA Total Score                                                 | integer    | nullable   | (y>=0) & (y<=30)        |           nan |
| MoCA       | moca_total_score_adjusted                      | MoCA Total Score adjusted for education                          | integer    | nullable   | (y>=0) & (y<=31)        |           nan |