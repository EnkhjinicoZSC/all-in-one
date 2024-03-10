
import pandas as pd


def fetch_simplify():
  url = 'https://github.com/SimplifyJobs/New-Grad-Positions'
  tables = pd.read_html(url) # Returns list of all tables on page
  df = pd.DataFrame(tables[1])
  df = df.drop('Application/Link', axis=1)

  print(df)

  df.to_csv("data/simple.csv", index=False) 

  return df

fetch_simplify()
