import requests
import streamlit as st
import datetime
import time
import pandas as pd
import json
import plotly.express as px
import boto3
import numpy as np
import matplotlib.pyplot as plt

city_df = pd.read_csv('city.csv')

client = boto3.client('s3')
result = client.get_object(Bucket="sagemaker-us-east-1-118600533013", Key="wind-notebook/data/batch-prediction/test.json.out")
csvcontent = result['Body'].read().decode('utf-8')

obj = client.get_object(Bucket='wind-data-team', Key='power_prd_0_19.csv')
data = pd.read_csv(obj['Body'], index_col=0, parse_dates=True)
data.index.name = None
for i in data.columns:
    data[i] = data[i].astype(float)
    
data_p = csvcontent.split("}")

lst_data = []

for i in list(range(0, 40, 2)):
    temp = data_p[i]+'}}'
    lst_data.append(json.loads(temp)['mean'])
    # d = data_p[0]+'}}'
    # e = data_p[2]+'}}'
    # id_1 = json.loads(d)['mean']
    # id_2 = json.loads(e)['mean']



    
### streamlit

today = datetime.date.today()

# construct UI layout

st.sidebar.subheader('Query parameters')

# Date Time


start_date = st.sidebar.date_input("Start date", datetime.date(2015, 1, 1))
from_date = time.mktime(start_date.timetuple())

end_date = st.sidebar.date_input("End date", datetime.date(2017, 4, 18))
to_date= time.mktime(end_date.timetuple())    
# print(start_date)
    
def main():
    page = st.sidebar.selectbox(
        "Select a Page",
        [
            "Wind Mill N:1",
            "Wind Mill N:2",
            "Wind Mill N:3",
            "Wind Mill N:4",
            "Wind Mill N:5",
            "Wind Mill N:6",
            "Wind Mill N:7",
            "Wind Mill N:8",
            "Wind Mill N:9",
            "Wind Mill N:10",
            "Wind Mill N:11",
            "Wind Mill N:12",
            "Wind Mill N:13",
            "Wind Mill N:14",
            "Wind Mill N:15",
            "Wind Mill N:16",
            "Wind Mill N:17",
            "Wind Mill N:18",
            "Wind Mill N:19",
            "Wind Mill N:20",
            
        ]
    )

    if page == "Wind Mill N:1":
        wind_mill_1()
    elif page == "Wind Mill N:2":
        wind_mill_2()
    elif page == "Wind Mill N:3":
        wind_mill_3()
    elif page == "Wind Mill N:4":
        wind_mill_4()
    elif page == "Wind Mill N:5":
        wind_mill_5()
    elif page == "Wind Mill N:6":
        wind_mill_6()
    elif page == "Wind Mill N:7":
        wind_mill_7()
    elif page == "Wind Mill N:8":
        wind_mill_8()
    elif page == "Wind Mill N:9":
        wind_mill_9()
    elif page == "Wind Mill N:10":
        wind_mill_10()
    elif page == "Wind Mill N:11":
        wind_mill_11()
    elif page == "Wind Mill N:12":
        wind_mill_12()
    elif page == "Wind Mill N:13":
        wind_mill_13()
    elif page == "Wind Mill N:14":
        wind_mill_14()
    elif page == "Wind Mill N:15":
        wind_mill_15()
    elif page == "Wind Mill N:16":
        wind_mill_16()
    elif page == "Wind Mill N:17":
        wind_mill_17()
    elif page == "Wind Mill N:18":
        wind_mill_18()
    elif page == "Wind Mill N:19":
        wind_mill_19()
    elif page == "Wind Mill N:20":
        wind_mill_20()

# Number of Hours to forcast

number_of_hours_forcast = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] 
hours_to_predict = st.sidebar.selectbox('Number of Hours to Forcast', number_of_hours_forcast) # Select coin

def wind_mill_1():
    st.write("""
        # Wind Power Production
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[0][:hours_to_predict])
    
def wind_mill_2():
    st.write("""
        # Wind Power Production
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[1][:hours_to_predict])
    
    
def wind_mill_3():
    st.write("""
        # Wind Power Production
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[2][:hours_to_predict])
    

def wind_mill_4():
    st.write("""
        # Wind Power Production N:4
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[3][:hours_to_predict])
    
def wind_mill_5():
    st.write("""
        # Wind Power Production N:5
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[4][:hours_to_predict])
    
    
def wind_mill_6():
    st.write("""
        # Wind Power Production N:6
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[5][:hours_to_predict])


def wind_mill_7():
    st.write("""
        # Wind Power Production N:7
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[6][:hours_to_predict])
    
def wind_mill_8():
    st.write("""
        # Wind Power Production N:8
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[7][:hours_to_predict])
    
    
def wind_mill_9():
    st.write("""
        # Wind Power Production N:9
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[8][:hours_to_predict])
    

def wind_mill_10():
    st.write("""
        # Wind Power Production N:10
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[9][:hours_to_predict])
    
def wind_mill_11():
    st.write("""
        # Wind Power Production N:11
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[10][:hours_to_predict])
    
    
def wind_mill_12():
    st.write("""
        # Wind Power Production N:12
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[11][:hours_to_predict])
    
def wind_mill_13():
    st.write("""
        # Wind Power Production N:13
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[12][:hours_to_predict])


def wind_mill_14():
    st.write("""
        # Wind Power Production N:14
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[13][:hours_to_predict])
    
def wind_mill_15():
    st.write("""
        # Wind Power Production N:15
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[14][:hours_to_predict])
    
    
def wind_mill_16():
    st.write("""
        # Wind Power Production N:16
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[15][:hours_to_predict])
    

def wind_mill_17():
    st.write("""
        # Wind Power Production N:17
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[16][:hours_to_predict])
    
def wind_mill_18():
    st.write("""
        # Wind Power Production N:17
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[17][:hours_to_predict])
    
    
def wind_mill_19():
    st.write("""
        # Wind Power Production N:19
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[18][:hours_to_predict])
    
def wind_mill_20():
    st.write("""
        # Wind Power Production N:20
        ### Shown are the generated electricity  by wind power ###
        #""")
    
    # tot = data.loc[start_date:end_date]['id_1']
    # tot = tot.append(id_1, ignore_index=True)
    st.line_chart(lst_data[19][:hours_to_predict])

# Total expected energy for requested timeframe
expected_total = []

for i in lst_data:
   expected_total.append(sum(i[:hours_to_predict]))
   
city_df['exp_total'] = expected_total


col         = 'exp_total'
threshold = city_df[col].mean()
conditions  = [ city_df[col] >= threshold, (city_df[col] < threshold) & (city_df[col]> threshold/2), city_df[col] <= threshold/2 ]
choices     = [ "high", 'medium', 'low' ]
    
city_df["category"] = np.select(conditions, choices, default=np.nan)


st.dataframe(city_df[['City','exp_total']])


# Multiselect to choose a subset of crimes to show in the map
enrgy_class = st.multiselect('Select the list of crimes you\'d like to filter by',
                            list(city_df.category.unique()), list(city_df.category.unique()))


# # Streamlit's integration with DeckGL. 



# Adding code so we can have map default to the center of the data
midpoint = (np.average(city_df['latitude']), np.average(city_df['longitude']))

st.deck_gl_chart(
            viewport={
                'latitude': midpoint[0],
                'longitude':  midpoint[1],
                'zoom': 4
            },
            layers=[{
                'type': 'ScatterplotLayer',
                'data': city_df[city_df['category'].isin(enrgy_class)],
                'radiusScale': 100,
                'radiusMinPixels': 5,
                'getFillColor': [0, 255, 0, 255],
            }]
        )

# Number of Days

number_of_days = [1,2,3,4,5] 
days = st.sidebar.selectbox('Number of Days to Forcast Weather', number_of_days) # Select coin

# Location

location_name = list(city_df['City'])
location = st.sidebar.selectbox('Name of Location', location_name) # Select currency

# Get Data

payload = {'location':location, 'days':days}
res = requests.get('http://localhost:8080', params=payload)
data = json.loads(res.json())

# Transform Data

df = pd.DataFrame.from_dict(data["wind_mph"])
df.columns = ['Time', 'wind_mph']

st.header('**Wind speed for {} on {}**'.format(location,today))
# fig = px.line(df, x='Time', y='wind_mph')
# st.write(fig)
st.line_chart(df['wind_mph'])

    
if __name__ == "__main__":
    main()