#%% Load Libraries
import pandas as pd

#%% Load Data Sources from OHANA
url = 'https://raw.githubusercontent.com/ohana-project/StandardChargesData/master/chargelevel.csv'
sources = pd.read_csv(url)

#%% Select Sources and Load
sources_to_load = sources.query('State=="AL"')
mdf = pd.DataFrame()
for index, row in sources_to_load.iterrows():
    print(f"Loaded {row['Hospital']}")
    incoming_data = pd.read_csv(row['Url'])
    incoming_data = incoming_data.assign(State = row['State'])
    incoming_data = incoming_data.assign(County = row['County'])
    incoming_data = incoming_data.assign(City = row['City'])
    incoming_data = incoming_data.assign(Hospital = row['Hospital'])
    mdf = mdf.append(incoming_data)
mdf = mdf.reindex(fill_value='**MISSING**')

#%% Search Data
match = mdf['Charge'].str.contains('^ACETAMIN|^IBUPRO.*200', na=False)
print(mdf[match])

#%%
for index, row in mdf[match].iterrows():
    print(row)

#%% Drop Contents To CSV
# mdf.to_csv("Output-Sample.csv")
