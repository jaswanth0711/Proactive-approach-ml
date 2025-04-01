

import twilio
file_path = "/mount/src/proactive-approach-ml/model.py"

# Read file and remove invalid lines
with open(file_path, "r") as f:
    lines = f.readlines()

# Keep only valid Python lines
cleaned_lines = [line for line in lines if not line.strip().startswith("<!--")]

# Write back the cleaned file
with open(file_path, "w") as f:
    f.writelines(cleaned_lines)

print("Cleaned model.py successfully!")
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, GRU, Dense, Dropout, Bidirectional
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    mean_squared_error, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from google.colab import files
import io

# Upload the dataset
uploaded = files.upload()

# Load the dataset
uploaded = files.upload()  # Upload the file again
df = pd.read_csv(io.BytesIO(uploaded[list(uploaded.keys())[0]]))  # Read dynamically


# Convert categorical variables to numerical (except target)
df = pd.get_dummies(df, columns=['Vehicle_Type', 'Route_Info', 'Weather_Conditions', 'Road_Conditions'])

print(df.dtypes)  # Check data types
print(df.select_dtypes(include=['object']).head())  # Show first few rows of non-numeric columns

df = df.drop(columns=['Make_and_Model'])  # ✅ Remove the column

df = pd.get_dummies(df, drop_first=True)  # ✅ Convert categorical data into numerical format

print(df.dtypes)  # ✅ Should show only numeric data types
print(df.head())  # ✅ Check if all values are numbers

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = df.drop(columns=['Maintenance_Required'])  # Features
y = df['Maintenance_Required']  # Target

X = scaler.fit_transform(X.astype(float))  # ✅ Convert to float before scaling

print(X.shape)  # Should be (samples, features)
print(y.shape)  # Should be (samples,)



# Encode the target column 'Maintenance_Required'
label_encoder = LabelEncoder()
df['Maintenance_Required'] = label_encoder.fit_transform(df['Maintenance_Required'])

# Handle missing values
df = df.fillna(0)

# Separate features and target
X = df.drop('Maintenance_Required', axis=1)
y = df['Maintenance_Required']

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Reshape data for LSTM/GRU (samples, timesteps, features)
X = X.reshape((X.shape[0], 1, X.shape[1]))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X = X.reshape((X.shape[0], 1, -1))  # ✅ Automatically adjusts features dimension




print("Data preprocessing completed successfully!")

# LSTM Model
lstm_model = Sequential()
lstm_model.add(Bidirectional(LSTM(100, return_sequences=True), input_shape=(X_train.shape[1], X_train.shape[2])))
lstm_model.add(Dropout(0.3))
lstm_model.add(Bidirectional(LSTM(50)))
lstm_model.add(Dropout(0.3))
lstm_model.add(Dense(1, activation='sigmoid'))

lstm_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the LSTM model
history_lstm = lstm_model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test),
    verbose=1
)

# GRU Model
gru_model = Sequential()
gru_model.add(Bidirectional(GRU(100, return_sequences=True), input_shape=(X_train.shape[1], X_train.shape[2])))
gru_model.add(Dropout(0.3))
gru_model.add(Bidirectional(GRU(50)))
gru_model.add(Dropout(0.3))
gru_model.add(Dense(1, activation='sigmoid'))

gru_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the GRU model
history_gru = gru_model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test),
    verbose=1
)

# Evaluate LSTM Model
lstm_predictions = lstm_model.predict(X_test)
lstm_predictions = (lstm_predictions > 0.5).astype(int)

# Evaluate GRU Model
gru_predictions = gru_model.predict(X_test)
gru_predictions = (gru_predictions > 0.5).astype(int)

# Metrics for LSTM
print("LSTM Model Evaluation:")
print("Confusion Matrix:\n", confusion_matrix(y_test, lstm_predictions))
print("Classification Report:\n", classification_report(y_test, lstm_predictions))
print("Precision:", precision_score(y_test, lstm_predictions))
print("Recall:", recall_score(y_test, lstm_predictions))
print("F1-Score:", f1_score(y_test, lstm_predictions))
print("ROC-AUC Score:", roc_auc_score(y_test, lstm_predictions))

# Metrics for GRU
print("\nGRU Model Evaluation:")
print("Confusion Matrix:\n", confusion_matrix(y_test, gru_predictions))
print("Classification Report:\n", classification_report(y_test, gru_predictions))
print("Precision:", precision_score(y_test, gru_predictions))
print("Recall:", recall_score(y_test, gru_predictions))
print("F1-Score:", f1_score(y_test, gru_predictions))
print("ROC-AUC Score:", roc_auc_score(y_test, gru_predictions))

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, GRU, Bidirectional
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.model_selection import KFold

# Callbacks for efficient training
early_stopping = EarlyStopping(monitor='val_loss', patience=2, min_delta=0.001, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=1, min_delta=0.001, verbose=0)

# K-Fold Cross-Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

def build_model(cell_type='LSTM'):
    """ Builds an optimized LSTM or GRU model. """
    model = Sequential([
        Bidirectional(LSTM(32, return_sequences=True) if cell_type == 'LSTM' else GRU(32, return_sequences=True),
                      input_shape=(X.shape[1], X.shape[2])),
        Dropout(0.3),
        Bidirectional(LSTM(16) if cell_type == 'LSTM' else GRU(16)),
        Dropout(0.3),
        Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Function to Train and Evaluate using K-Fold
def train_and_evaluate(cell_type='LSTM'):
    scores = []
    with tf.device('/GPU:0'):  # Use GPU if available
        for train_idx, val_idx in kfold.split(X):
            X_train_fold, X_val_fold = X[train_idx], X[val_idx]
            y_train_fold, y_val_fold = y.iloc[train_idx], y.iloc[val_idx]

            model = build_model(cell_type)
            model.fit(
                X_train_fold, y_train_fold,
                epochs=10, batch_size=64,  # Fewer epochs, larger batch size
                validation_data=(X_val_fold, y_val_fold),
                callbacks=[early_stopping, reduce_lr],
                verbose=0
            )
            scores.append(model.evaluate(X_val_fold, y_val_fold, verbose=0)[1])
    return np.mean(scores)

# Run Optimized Training
lstm_acc = train_and_evaluate('LSTM')
gru_acc = train_and_evaluate('GRU')

print(f"LSTM Accuracy: {lstm_acc:.4f}")
print(f"GRU Accuracy: {gru_acc:.4f}")

# Save the best model based on validation accuracy
if lstm_acc > gru_acc:
    best_model = build_model('LSTM')  # Recreate the best model
    best_model.save('best_predictive_maintenance_model.h5')
    print("LSTM Model Saved as Best Model.")
else:
    best_model = build_model('GRU')  # Recreate the best model
    best_model.save('best_predictive_maintenance_model.h5')
    print("GRU Model Saved as Best Model.")

# Plot training and validation accuracy for LSTM
plt.plot(history_lstm.history['accuracy'], label='LSTM Training Accuracy')
plt.plot(history_lstm.history['val_accuracy'], label='LSTM Validation Accuracy')
plt.title('LSTM Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Plot training and validation accuracy for GRU
plt.plot(history_gru.history['accuracy'], label='GRU Training Accuracy')
plt.plot(history_gru.history['val_accuracy'], label='GRU Validation Accuracy')
plt.title('GRU Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

import sqlite3
from datetime import datetime, timedelta
import time

# Initialize database
def init_db():
    conn = sqlite3.connect(':memory:')  # Using in-memory database for Colab
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        next_maintenance_date DATE,
        maintenance_interval_days INTEGER NOT NULL,
        status TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id INTEGER NOT NULL,
        message TEXT NOT NULL,
        severity TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        resolved BOOLEAN DEFAULT 0,
        FOREIGN KEY (asset_id) REFERENCES assets (id)
    )
    ''')

    # Add some sample assets
    today = datetime.now().date()
    cursor.executemany(
        'INSERT INTO assets (name, next_maintenance_date, maintenance_interval_days, status) VALUES (?, ?, ?, ?)',
        [
            ('HVAC System', today + timedelta(days=2), 30, 'operational'),
            ('Generator', today - timedelta(days=5), 90, 'operational'),
            ('Elevator', today + timedelta(days=30), 180, 'operational')
        ]
    )

    conn.commit()
    return conn

# Alerting and maintenance check function
def check_maintenance(conn):
    cursor = conn.cursor()
    today = datetime.now().date()

    print("\nRunning maintenance check...")

    # Check for overdue maintenance
    cursor.execute(
        'SELECT * FROM assets WHERE next_maintenance_date < ? AND status = "operational"',
        (today,)
    )
    overdue_assets = cursor.fetchall()

    for asset in overdue_assets:
        print(f"ALERT: Maintenance overdue for {asset[1]} (was due on {asset[2]})")
        cursor.execute(
            'INSERT INTO alerts (asset_id, message, severity) VALUES (?, ?, ?)',
            (asset[0], f'Maintenance overdue for {asset[1]}', 'high')
        )

    # Check for upcoming maintenance (within 7 days)
    seven_days_later = today + timedelta(days=7)
    cursor.execute(
        'SELECT * FROM assets WHERE next_maintenance_date BETWEEN ? AND ? AND status = "operational"',
        (today, seven_days_later)
    )
    upcoming_assets = cursor.fetchall()

    for asset in upcoming_assets:
        print(f"INFO: Maintenance coming up for {asset[1]} on {asset[2]}")
        cursor.execute(
            'INSERT INTO alerts (asset_id, message, severity) VALUES (?, ?, ?)',
            (asset[0], f'Maintenance scheduled for {asset[1]} on {asset[2]}', 'medium')
        )

    conn.commit()

    # Display current alerts
    cursor.execute('SELECT * FROM alerts WHERE resolved = 0 ORDER BY created_at DESC')
    active_alerts = cursor.fetchall()

    if active_alerts:
        print("\nActive Alerts:")
        for alert in active_alerts:
            print(f"[{alert[4]}] {alert[2]} (Severity: {alert[3]})")
    else:
        print("\nNo active alerts")

    return active_alerts

# Main simulation loop
def run_cmms_simulation():
    conn = init_db()

    try:
        # Simulate 30 days of operation with daily checks
        for day in range(30):
            print(f"\n=== Day {day + 1} ===")
            current_date = datetime.now().date() + timedelta(days=day)
            print(f"System date: {current_date}")

            # Run maintenance check
            alerts = check_maintenance(conn)

            # Resolve some alerts automatically (simulation)
            if alerts:
                cursor = conn.cursor()
                cursor.execute(
                    'UPDATE alerts SET resolved = 1 WHERE id = ?',
                    (alerts[0][0],)
                )
                conn.commit()
                print(f"Resolved alert ID {alerts[0][0]}")

            # Advance time (in simulation)
            time.sleep(1)  # Just for visualization in Colab

    finally:
        conn.close()

# Run the simulation
run_cmms_simulation()


import sqlite3
from datetime import datetime, timedelta
from twilio.rest import Client  # For SMS alerts

# ===== CONFIGURATION =====
TWILIO_ACCOUNT_SID = 'ACde33f7ef6b3ce42cc34696f0502d6ffc'  # Replace with your Twilio SID
TWILIO_AUTH_TOKEN = '3a5478300f322442df47490cbf9f0a32'    # Replace with your Twilio token
TWILIO_PHONE_NUMBER = '+19414156754'             # Your Twilio phone number
OWNER_PHONE_NUMBER = '6301272493'                # Indian phone number (without +91)

# ===== SAMPLE VEHICLE DATA =====
VEHICLES = [
    {"name": "Toyota Camry", "last_service": "2023-10-01", "service_interval_days": 30, "owner_phone": OWNER_PHONE_NUMBER},
    {"name": "Ford F-150", "last_service": "2023-09-15", "service_interval_days": 60, "owner_phone": OWNER_PHONE_NUMBER},
    {"name": "Tesla Model 3", "last_service": "2023-11-01", "service_interval_days": 90, "owner_phone": OWNER_PHONE_NUMBER},
]

# ===== FORMAT PHONE NUMBERS TO E.164 =====
def format_phone_number(phone):
    """Ensure phone number is in E.164 format for India."""
    phone = phone.strip().replace(" ", "")
    if not phone.startswith("+"):
        phone = "+91" + phone  # Append India country code if missing
    return phone

# ===== DATABASE SETUP =====
def setup_database():
    conn = sqlite3.connect(':memory:')  # Temporary DB for testing
    cursor = conn.cursor()

    # Create VEHICLES table
    cursor.execute('''
    CREATE TABLE vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_service_date DATE,
        next_service_date DATE,
        service_interval_days INTEGER,
        owner_phone TEXT
    )
    ''')

    # Insert sample vehicles
    today = datetime.now().date()
    for vehicle in VEHICLES:
        last_service = datetime.strptime(vehicle["last_service"], "%Y-%m-%d").date()
        next_service = last_service + timedelta(days=vehicle["service_interval_days"])

        cursor.execute('''
        INSERT INTO vehicles (name, last_service_date, next_service_date, service_interval_days, owner_phone)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            vehicle["name"],
            last_service,
            next_service,
            vehicle["service_interval_days"],
            format_phone_number(vehicle["owner_phone"])
        ))

    conn.commit()
    return conn

# ===== SMS ALERT FUNCTION =====
def send_sms(to_number, message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=format_phone_number(to_number)  # Ensure correct format
        )
        print(f"📲 SMS sent to {to_number}")
        return True
    except Exception as e:
        print(f"❌ SMS failed: {e}")
        return False

# ===== CHECK FOR DUE SERVICES =====
def check_vehicle_service(db):
    with db:  # Ensures commit and close
        cursor = db.cursor()
        today = datetime.now().date()

        # Get vehicles due for service
        cursor.execute('''
        SELECT name, next_service_date, owner_phone
        FROM vehicles
        WHERE next_service_date <= ?
        ''', (today,))

        due_vehicles = cursor.fetchall()

        for name, due_date, phone in due_vehicles:
            alert_msg = f"🔧 SERVICE REQUIRED: {name} is overdue for service! (Due on: {due_date})"
            print(f"🚨 {alert_msg}")

            # Send SMS alert
            send_sms(phone, alert_msg)

            # Update next service date (for simulation)
            new_due_date = today + timedelta(days=30)  # Reset for next interval
            cursor.execute('''
            UPDATE vehicles
            SET last_service_date = ?, next_service_date = ?
            WHERE name = ?
            ''', (today, new_due_date, name))

# ===== RUN THE SYSTEM =====
def main():
    print("🚘 Starting Vehicle Maintenance Alert System...\n")
    db = setup_database()

    # Simulate a maintenance check
    print("🔍 Checking vehicle service status...\n")
    check_vehicle_service(db)

    print("\n✅ Done! Check your phone for SMS alerts.")

if __name__ == "__main__":
    main()

import sqlite3
from datetime import datetime, timedelta
from twilio.rest import Client  # For SMS alerts

# ===== CONFIGURATION =====
TWILIO_ACCOUNT_SID = 'ACde33f7ef6b3ce42cc34696f0502d6ffc'  # Replace with your Twilio SID
TWILIO_AUTH_TOKEN = '3a5478300f322442df47490cbf9f0a32'    # Replace with your Twilio token
TWILIO_PHONE_NUMBER = '+19414156754'             # Your Twilio phone number
OWNER_PHONE_NUMBER = '6301272493'                # Indian phone number (without +91)

# ===== SAMPLE VEHICLE DATA =====
VEHICLES = [
    {"name": "Toyota Camry", "last_service": "2025-05-01", "service_interval_days": 30, "owner_phone": OWNER_PHONE_NUMBER},
    {"name": "Ford F-150", "last_service": "2025-05-15", "service_interval_days": 60, "owner_phone": OWNER_PHONE_NUMBER},
    {"name": "Mahindra XUV-700", "last_service": "2025-06-01", "service_interval_days": 90, "owner_phone": OWNER_PHONE_NUMBER},
]

# ===== FORMAT PHONE NUMBERS TO E.164 =====
def format_phone_number(phone):
    '''Ensure phone number is in E.164 format for India.'''
    phone = phone.strip().replace(" ", "")
    if not phone.startswith("+"):
        phone = "+91" + phone  # Append India country code if missing
    return phone

# ===== DATABASE SETUP =====
def setup_database():
    conn = sqlite3.connect(':memory:')  # Temporary DB for testing
    cursor = conn.cursor()

    # Create VEHICLES table
    cursor.execute('''
    CREATE TABLE vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_service_date DATE,
        next_service_date DATE,
        service_interval_days INTEGER,
        owner_phone TEXT
    )
    ''')

    # Insert sample vehicles
    today = datetime.now().date()
    for vehicle in VEHICLES:
        last_service = datetime.strptime(vehicle["last_service"], "%Y-%m-%d").date()
        next_service = last_service + timedelta(days=vehicle["service_interval_days"])

        cursor.execute('''
        INSERT INTO vehicles (name, last_service_date, next_service_date, service_interval_days, owner_phone)
        VALUES (?, ?, ?, ?, ?)
        ''', (
            vehicle["name"],
            last_service,
            next_service,
            vehicle["service_interval_days"],
            format_phone_number(vehicle["owner_phone"])
        ))

    conn.commit()
    return conn

# ===== SMS ALERT FUNCTION =====
def send_sms(to_number, message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=format_phone_number(to_number)  # Ensure correct format
        )
        print(f"📲 SMS sent to {to_number}")
        return True
    except Exception as e:
        print(f"❌ SMS failed: {e}")
        return False

# ===== CHECK FOR DUE SERVICES =====
def check_vehicle_service(db):
    with db:  # Ensures commit and close
        cursor = db.cursor()
        today = datetime.now().date()

        # Get vehicles due for service
        cursor.execute('''
        SELECT name, next_service_date, owner_phone
        FROM vehicles
        WHERE next_service_date <= ?
        ''', (today,))

        due_vehicles = cursor.fetchall()

        for name, due_date, phone in due_vehicles:
            alert_msg = f"🔧 SERVICE REQUIRED: {name} is overdue for service! (Due on: {due_date})"
            print(f"🚨 {alert_msg}")

            # Send SMS alert
            send_sms(phone, alert_msg)

            # Update next service date (for simulation)
            new_due_date = today + timedelta(days=30)  # Reset for next interval
            cursor.execute('''
            UPDATE vehicles
            SET last_service_date = ?, next_service_date = ?
            WHERE name = ?
            ''', (today, new_due_date, name))

# ===== RUN THE SYSTEM =====
def main():
    print("🚘 Starting Vehicle Maintenance Alert System...\n")
    db = setup_database()

    # Simulate a maintenance check
    print("🔍 Checking vehicle service status...\n")
    check_vehicle_service(db)

    print("\n✅ Done! Check your phone for SMS alerts.")

if __name__ == "__main__":
    main()
