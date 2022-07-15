import streamlit as st

st.set_page_config(
    page_title="Sensors Predictions",
    page_icon="📈",
)

st.write("# Predictions for pollution data! 📈")

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
 
# st.set_page_config(page_title="Predicție poluare", page_icon=":bar_chart:", layout="wide")

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

# sales_data = get_data("Superstore_Orders.csv")
# image = get_image("supermarket.jpeg")

# # ---- MAINPAGE ----
# st.title(":bar_chart: Metode de analiză și predicție a poluării aerului")
# st.markdown("##")

# st.markdown("""---""")

# st.plotly_chart(fig)




pd.options.mode.chained_assignment = None
data = get_data("82000278_Toamnei_2022_05.csv")
# data = get_data("../82000278_Toamnei_2022_05.csv")
# data = pd.read_csv("82000278_Toamnei_2022_05.csv")

# drop Nan columns and indexes
data.dropna(axis='columns', how='all', inplace=True)
data.dropna(axis='index', how='all', inplace=True)

# convert to date format
data['day'] = pd.to_datetime(data['day'], dayfirst=True)

# modify name with any sensor name from df
sensor_name = 'pm10'

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