import os 
import requests 
import pandas as pd
from dotenv import load_dotenv
import time

load_dotenv()
# API_KEY = os.getenv("API_KEY")
APP_TOKEN = os.getenv("APP_TOKEN")
PAGE_NUMBER = 1
PAGE_SIZE = 1000
NUM_OF_PAGES = 29_700//PAGE_SIZE

for pn in range(1 , NUM_OF_PAGES + 1):
   url = (
      f"https://data.cityofnewyork.us/api/v3/views/833y-fsy8/query.json?"
      f"app_token={APP_TOKEN}"
      f"&pageNumber={pn}&pageSize={PAGE_SIZE}"
      f"&query=SELECT%20incident_key%2C%20occur_date%2C%20occur_time%2C%20boro%2C%20loc_of_occur_desc%2C%20precinct%2C%20jurisdiction_code%2C%20loc_classfctn_desc%2C%20location_desc%2C%20statistical_murder_flag%2C%20perp_age_group%2C%20perp_sex%2C%20perp_race%2C%20vic_age_group%2C%20vic_sex%2C%20vic_race%2C%20x_coord_cd%2C%20y_coord_cd%2C%20latitude%2C%20longitude%2C%20geocoded_column"
   )

   response = requests.get(url)
   print(response.status_code)
   data = response.json()
   df = pd.DataFrame(data)
   # df.to_csv(f"../data/raw/nyc-shooting-incidents-{pn}.csv")
   time.sleep(5)



