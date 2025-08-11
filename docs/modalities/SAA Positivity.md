# SAA Positivity

| Modality       | Item             | Description                              | ItemType   | Required   | Values                                                                            |   Unnamed: 13 |
|:---------------|:-----------------|:-----------------------------------------|:-----------|:-----------|:----------------------------------------------------------------------------------|--------------:|
| SAA Positivity | saa_assay        | Name of SAA assay used (free text)       | string     | nullable   | nan                                                                               |           nan |
| SAA Positivity | saa_results      | SAA results (categorical)                | string     | nullable   | ["MSA","DLB","PD","DLB/PD","Inconclusive","Negative","Positive (no distinction)"] |           nan |
| SAA Positivity | saa_fmax         | Max fluorescence (average of replicates) | numeric    | nullable   | nan                                                                               |           nan |
| SAA Positivity | saa_ttt          | Average time to threshold                | numeric    | nullable   | nan                                                                               |           nan |
| SAA Positivity | saa_auc          | Average area under the curve             | numeric    | nullable   | nan                                                                               |           nan |
| SAA Positivity | saa_smax         | Max slope (average of replicates)        | numeric    | nullable   | nan                                                                               |           nan |
| SAA Positivity | saa_tsmax        | Average time to max slope                | numeric    | nullable   | nan                                                                               |           nan |
| SAA Positivity | saa_n_replicates | Number of replicates                     | numeric    | nullable   | nan                                                                               |           nan |
| SAA Positivity | ssa_n_positive   | Number of positive replicates (wells)    | numeric    | nullable   | nan                                                                               |           nan |