# Vital

| Modality   | Item                     | Description                                                                               | ItemType   | Required   | Values              |   Unnamed: 13 |
|:-----------|:-------------------------|:------------------------------------------------------------------------------------------|:-----------|:-----------|:--------------------|--------------:|
| Vital      | weight_kg                | in kg                                                                                     | numeric    | nullable   | (y>=20) & (y<=225)  |           nan |
| Vital      | height_cm                | in cm                                                                                     | numeric    | nullable   | (y>=100) & (y<=220) |           nan |
| Vital      | BMI                      | nan                                                                                       | numeric    | nullable   | (y>=10) & (y<=75)   |           nan |
| Vital      | heart_rate               | per minute                                                                                | numeric    | nullable   | (y>=35) & (y<=200)  |           nan |
| Vital      | systolic_blood_pressure  | in mmHg (use only if no information is given on sitting, standing, or supine positioning) | numeric    | nullable   | (y>=50) & (y<=250)  |           nan |
| Vital      | diastolic_blood_pressure | in mmHg (use only if no information is given on sitting, standing, or supine positioning) | numeric    | nullable   | (y>=30) & (y<=250)  |           nan |