import pandas as pd
from sklearn.ensemble import IsolationForest

# Load your log data (replace 'log_data.csv' with the path to your log data file)
data = pd.read_csv('log_data.csv')

# Assuming your log data has a 'timestamp' and 'log_value' column
# You may need to adapt column names and data preprocessing according to your dataset

# Create a DataFrame with only the 'log_value' column for the Isolation Forest model
log_data = data[['log_value']]

# Initialize the Isolation Forest model
model = IsolationForest(contamination=0.05)  # Adjust the contamination parameter as needed

# Fit the model to your log data
model.fit(log_data)

# Predict anomalies
anomalies = model.predict(log_data)

# Add the anomaly predictions to the original data
data['anomaly'] = anomalies

# Filter out the anomalies
anomaly_data = data[data['anomaly'] == -1]

# Print or analyze the anomaly_data DataFrame as needed
print("Anomalies detected:")
print(anomaly_data)

# You can save the anomaly_data to a file or perform further analysis on the detected anomalies
# anomaly_data.to_csv('anomalies.csv', index=False)
