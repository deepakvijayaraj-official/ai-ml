import pandas as pd
from fbprophet import Prophet
import matplotlib.pyplot as plt

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

# Plot the forecast
fig = model.plot(forecast)
plt.title('Resource Usage Forecast')
plt.xlabel('Time')
plt.ylabel('Resource Usage')
plt.show()
