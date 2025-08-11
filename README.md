# CDE Version Control
This is a test repository for version control and public access to a data dictionary. Only select columns from the live document are actually published here.

## Update Schedule
* Updates run daily at 6AM UTC via GitHub Actions.
* Updates can also be triggered manually in the GitHub Actions tab.

## Latest Version
You can use this link in your code to get the most recent version of the data dictionary:
https://raw.githubusercontent.com/lietsel-jones/data-dictionary/main/docs/latest_data_dictionary.csv

For example, in Python:
```python
import pandas as pd

url = "https://raw.githubusercontent.com/lietsel-jones/data-dictionary/main/docs/latest_data_dictionary.csv"
df = pd.read_csv(url)
print(df.head())
```

## Latest Version
**Curent version:** v2025.08.11-2202

## Versioning
* Each update is tagged with a version number based on the date/time of the update.
* Historical versions can be browsed in the Releases page,

## Documentation
You can browse the data dictionary here: https://lietsel-jones.github.io/data-dictionary/
