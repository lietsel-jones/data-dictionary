# Lifestyle

| Modality   | Item                    | Description                                                                           | ItemType   | Required   | Values                                                  |   Unnamed: 13 |
|:-----------|:------------------------|:--------------------------------------------------------------------------------------|:-----------|:-----------|:--------------------------------------------------------|--------------:|
| Lifestyle  | smoking_status          | Smoking status (Can ignore non-substantial smoking)                                   | string     | nullable   | ["Current smoker", "Former smoker", "Never", "Unknown"] |           nan |
| Lifestyle  | smoking_ever_smoker_yes | Smoking status 2 (Can ignore non-substantial smoking) Ever/Never distinction (Ever=1) | integer    | nullable   | y.isin([0,1])                                           |           nan |
| Lifestyle  | smoking_years           | Smoking years (Can ignore non-substantial smoking)                                    | numeric    | nullable   | (y>=0) & (y<=120)                                       |           nan |
| Lifestyle  | smoking_pack_years      | Smoking pack (20) x years                                                             | numeric    | nullable   | (y>=0) & (y<=10000)                                     |           nan |