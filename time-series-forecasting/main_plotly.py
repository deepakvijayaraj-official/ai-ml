import pandas as pd
from fbprophet import Prophet
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Sample resource usage data (change this with your actual data)
data = pd.read_csv('resource_usage.csv')
data = data.rename(columns={'timestamp': 'ds', 'resource_usage': 'y'})
data['ds'] = pd.to_datetime(data['ds'])

# Initialize and fit the Prophet model
model = Prophet()
model.fit(data)

# Create a future dataframe for forecasting
future = model.make_future_dataframe(periods=24, freq='H')  # Forecasting 24 hours into the future

# Make predictions
forecast = model.predict(future)

# Create a Plotly figure
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)
fig.add_trace(go.Scatter(x=data['ds'], y=data['y'], mode='lines', name='Actual'), row=1, col=1)
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'), row=1, col=1)
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_lower'], fill='tonexty', mode='none', name='Uncertainty'), row=1, col=1)
fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='none', name='Uncertainty'), row=1, col=1)
fig.update_yaxes(title_text='Resource Usage', row=1, col=1)
fig.update_xaxes(title_text='Time', row=1, col=1)

# Additional plots or data can be added to the second row if needed

fig.update_layout(title_text='Resource Usage Forecast')
fig.show()
