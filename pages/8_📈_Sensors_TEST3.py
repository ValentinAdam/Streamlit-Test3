import streamlit as st

st.set_page_config(
    page_title="Sensors Predictions",
    page_icon="📈",
)

st.write("# Predictions for pollution data 📈")

st.sidebar.header("Sensors Predictions")

st.markdown(
    """
Predictions page for sensors in Brasov
"""
)


import logging
import numpy as np
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly, plot_components_plotly
from plotly import graph_objs as go
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


import pandas as pd
import streamlit as st 
import plotly.graph_objects as go

from PIL import Image
 

@st.cache(allow_output_mutation=True)
def get_data(path:str)->pd.DataFrame:
    data_frame = pd.read_csv(
        path,
    )
    return data_frame

@st.cache(allow_output_mutation=True)
def get_image(path:str)->Image:
    image = Image.open(path)
    return image


import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth('elastic', 'AWbtmGda2Q7BI2bYpdjyF4qd')
url = 'https://8f9677360fc34e2eb943d737b2597c7b.us-east-1.aws.found.io:9243/brasov-dev/_search?size=10000&q=*&sort=TimeStamp:desc'
response = requests.get(url=url, auth=auth)
import json
data = json.loads(response.text)
from pandas import json_normalize
dataframe = json_normalize(data['hits']['hits'])
dataframe_size = len(dataframe.index)

dataframe.rename(columns = {'_source.Source':'Source', '_source.Sensor':'Sensor', '_source.Value':'Value', '_source.LocationLat':'Latitude', '_source.LocationLong':'Longitude', '_source.TimeStamp':'Timestamp', '_source.Measurement':'Measurement'}, inplace = True)

dataframe['LocationId'] = dataframe['Latitude']*10000000 + dataframe['Longitude']*10000000
dataframe['LocationName'] = ""
dataframe.loc[dataframe['LocationId'] == 712668900.0, 'LocationName'] = 'Toamnei' 
dataframe.loc[dataframe['LocationId'] == 712196290.0, 'LocationName'] = 'Carierei'
dataframe.loc[dataframe['LocationId'] == 712209000.0, 'LocationName'] = 'Brintex'
dataframe.loc[dataframe['LocationId'] == 712240750.0, 'LocationName'] = 'Avantgarden'
dataframe.loc[dataframe['LocationId'] == 708361730.0, 'LocationName'] = 'Bucegi'
dataframe.loc[dataframe['LocationId'] == 712682018.0, 'LocationName'] = 'Carrefour'
dataframe.loc[dataframe['LocationId'] == 712307300.0, 'LocationName'] = 'Centru'
dataframe.loc[dataframe['LocationId'] == 712422000.0, 'LocationName'] = 'Cetatuie'
dataframe.loc[dataframe['LocationId'] == 712485560.0, 'LocationName'] = 'Basarab'
dataframe.loc[dataframe['LocationId'] == 712532529.0, 'LocationName'] = 'Patria'
dataframe.loc[dataframe['LocationId'] == 711435090.0, 'LocationName'] = 'Codlea1'
dataframe.loc[dataframe['LocationId'] == 711587690.0, 'LocationName'] = 'Codlea2'
dataframe.loc[dataframe['LocationId'] == 712526000.0, 'LocationName'] = 'Colina1'
dataframe.loc[dataframe['LocationId'] == 712485000.0, 'LocationName'] = 'Colina2'
dataframe.loc[dataframe['LocationId'] == 711054930.0, 'LocationName'] = 'Cristian'
dataframe.loc[dataframe['LocationId'] == 712743216.0, 'LocationName'] = 'Gara'
dataframe.loc[dataframe['LocationId'] == 713825580.0, 'LocationName'] = 'Harman1'
dataframe.loc[dataframe['LocationId'] == 714030800.0, 'LocationName'] = 'Harman2'
dataframe.loc[dataframe['LocationId'] == 712560910.0, 'LocationName'] = 'Racadau'
dataframe.loc[dataframe['LocationId'] == 710537170.0, 'LocationName'] = 'Rasnov'
dataframe.loc[dataframe['LocationId'] == 713449870.0, 'LocationName'] = 'Sanpetru1'
dataframe.loc[dataframe['LocationId'] == 713500000.0, 'LocationName'] = 'Sanpetru2'
dataframe.loc[dataframe['LocationId'] == 712475170.0, 'LocationName'] = 'Saturn'
dataframe.loc[dataframe['LocationId'] == 712500331.0, 'LocationName'] = 'Stupini1'
dataframe.loc[dataframe['LocationId'] == 712571580.0, 'LocationName'] = 'Stupini2'
dataframe.loc[dataframe['LocationId'] == 712804610.0, 'LocationName'] = 'Tractorul'
dataframe.loc[dataframe['LocationId'] == 713218270.0, 'LocationName'] = 'TriajH'
dataframe.loc[dataframe['LocationId'] == 712783320.0, 'LocationName'] = 'Vlahuta1'
dataframe.loc[dataframe['LocationId'] == 712797770.0, 'LocationName'] = 'Vlahuta2'
dataframe.loc[dataframe['LocationId'] == 708839110.0, 'LocationName'] = 'Zarnesti'
dataframe.loc[dataframe['LocationId'] == 712247880.0, 'LocationName'] = 'Saguna'
dataframe.loc[dataframe['LocationId'] == 712352710.0, 'LocationName'] = 'Livada'


dataframe_v2 = dataframe[[i for i in list(dataframe.columns) if i != '_index']]
dataframe_v2 = dataframe_v2[[i for i in list(dataframe_v2.columns) if i != '_type']]
dataframe_v2 = dataframe_v2[[i for i in list(dataframe_v2.columns) if i != '_id']]
dataframe_v2 = dataframe_v2[[i for i in list(dataframe_v2.columns) if i != '_score']]
dataframe_v2 = dataframe_v2[[i for i in list(dataframe_v2.columns) if i != 'sort']]
cho2 = dataframe_v2[dataframe_v2.get('Sensor') == 'cho2']
co2 = dataframe_v2[dataframe_v2.get('Sensor') == 'co2']
no2 = dataframe_v2[dataframe_v2.get('Sensor') == 'no2']
o3 = dataframe_v2[dataframe_v2.get('Sensor') == 'o3']
pm1 = dataframe_v2[dataframe_v2.get('Sensor') == 'pm1']
pm10 = dataframe_v2[dataframe_v2.get('Sensor') == 'pm10']
pm25 = dataframe_v2[dataframe_v2.get('Sensor') == 'pm25']
so2 = dataframe_v2[dataframe_v2.get('Sensor') == 'so2']

SENSORS = dataframe_v2['Sensor'].unique()
SENSORS_SELECTED = st.sidebar.multiselect('Select sensors', SENSORS)
mask_sensors = dataframe_v2['Sensor'].isin(SENSORS_SELECTED)
dataframe_v2 = dataframe_v2[mask_sensors]

st.dataframe(dataframe_v2)


pd.options.mode.chained_assignment = None
# data = get_data("82000278_Toamnei_2022_05.csv")
# data = get_data("../82000278_Toamnei_2022_05.csv")
# data = pd.read_csv("82000278_Toamnei_2022_05.csv")
data = dataframe_v2
data['day'] = ' '
st.dataframe(data)

# drop Nan columns and indexes
data.dropna(axis='columns', how='all', inplace=True)
data.dropna(axis='index', how='all', inplace=True)

# convert to date format
# dataframe.loc[dataframe['LocationId'] == 712668900.0, 'LocationName'] = 'Toamnei' 
# data.loc[data['Timestamp'], 'day'] = pd.to_datetime('Timestamp')
data['day'] = pd.to_datetime(data['Timestamp'], dayfirst=True)
# data['day'] = data['Timestamp'].dt.date

# modify name with any sensor name from df
sensor_name = mask_sensors

# sort dates by day
data = data.sort_values(by=['day'])
group_by_df = pd.DataFrame(
    [name, group.mean()[sensor_name]] for name, group in data.groupby('day')
)
group_by_df.columns = ['day', sensor_name]

# group df by day
grp_date = data.groupby('day')
# calculate mean value  for every given day
data = pd.DataFrame(grp_date.mean())

# select needed data
data = data[[sensor_name]]

# boxplot values to eliminate outliers
upper_quartile = np.percentile(data[sensor_name], 75)
lower_quartile = np.percentile(data[sensor_name], 25)
iqr = upper_quartile - lower_quartile
upper_whisker = data[sensor_name][data[sensor_name] <= upper_quartile + 1.5 * iqr].max()
lower_whisker = data[sensor_name][data[sensor_name] >= lower_quartile - 1.5 * iqr].min()

# start using prophet
logging.getLogger().setLevel(logging.ERROR)

# create df for prophet
df = data.reset_index()
df.columns = ['ds', 'y']

X = group_by_df[['day']].values
y = group_by_df[[sensor_name]].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, shuffle=False)

# create dataframe containing only train values
dff = pd.DataFrame(index=range(0, len(y_train)))
dff['ds'] = group_by_df['day'][:len(y_train)]
dff['y'] = group_by_df[sensor_name][:len(y_train)]

m = Prophet()
# fit train values to prophet
m.fit(dff)

# predict whole month
future = m.make_future_dataframe(periods=len(y_test))
forecast = m.predict(future)

# plot predictions
fig = plot_plotly(m, forecast)
fig.update_layout(
    title=sensor_name + ' forecast for May 2022',
    xaxis_title="Day",
    yaxis_title=sensor_name)
# fig.show()
st.plotly_chart(fig)

# check if there is seasonality+trend
fig2 = plot_components_plotly(m, forecast)
fig2.update_layout(
    title=sensor_name + " seasonality"
)
# fig.show()
st.plotly_chart(fig2)

# define a function to make a df containing the prediction and the actual values
def make_comparison_dataframe(historical, forecast):
    return forecast.set_index('ds')[['yhat', 'yhat_lower', 'yhat_upper']].join(historical.set_index('ds'))

# modify dff so that mse can be calculated for each value of the dataframe
dff['ds'] = group_by_df['day']
dff['y'] = group_by_df[sensor_name]

cmp_df = make_comparison_dataframe(df, forecast)

# add new column with default value
cmp_df['outlier_detected'] = 0
for i in range(len(cmp_df)):
    # detect outliers
    if (cmp_df['y'][i] > cmp_df['yhat_upper'][i] or cmp_df['y'][i] < cmp_df['yhat_lower'][i]):
        cmp_df['outlier_detected'][i] = 1
    else:
        cmp_df['outlier_detected'][i] = 0

# plot forecast with upper and lower bound
fig3 = go.Figure()

# predicted value
fig3.add_trace(go.Scatter(
    x=group_by_df['day'],
    y=cmp_df['yhat'],
    name='yhat(predicted value)',
    mode='lines+markers',
    line=dict(
        color='rgb(95,158,160)'),
    marker=dict(
        color='rgb(95,158,160)')
))

fig3.update_layout(title='pm10 values for May 2022', yaxis_title=sensor_name, xaxis_title='Day',
                  showlegend=True)
# fig.show()
st.plotly_chart(fig3)


# actual value
fig3.add_trace(go.Scatter(
    x=group_by_df['day'],
    y=cmp_df['y'],
    name='y(actual value)',
    mode='lines+markers',
    line=dict(
        color='rgb(75,0,130)'),
    marker=dict(color=np.where(cmp_df['outlier_detected'] == 1, 'red', 'rgb(75,0,130)'))))

fig3.update_layout(title='pm10 values for May 2022 and prediction values', yaxis_title=sensor_name, xaxis_title='Day',
                  showlegend=True)
# fig.show()
st.plotly_chart(fig3)


# lower bound of predicted value
fig3.add_trace(go.Scatter(
    x=group_by_df['day'],
    y=cmp_df['yhat_lower'],
    name='yhat_lower',
    mode='lines+markers',
    line=dict(
        color='rgb(205,92,92)'),
    marker=dict(
        color='rgb(205,92,92)')

))


# upper bound of predicted value
fig3.add_trace(go.Scatter(
    x=group_by_df['day'],
    y=cmp_df['yhat_upper'],
    name='yhat_upper',
    mode='lines+markers',
    line=dict(
        color='rgb(65,105,225)'),
    marker=dict(
        color='rgb(65,105,225)')
))

fig3.update_layout(title='Comparison between predicted values and real ones, including upper and lower values', yaxis_title=sensor_name, xaxis_title='Day',
                  showlegend=True)
# fig.show()
st.plotly_chart(fig3)