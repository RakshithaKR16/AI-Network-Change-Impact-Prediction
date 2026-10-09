# AI-Based Network Change Impact Prediction and Automated Validation System

## Project Overview
This project predicts the potential impact of network changes using a Machine Learning model and performs basic connectivity validation using Python. Cisco Packet Tracer is used to simulate network topology, failure scenarios, and recovery.

## Objectives
- Predict network change impact as LOW, MEDIUM, or HIGH.
- Analyze network parameters such as latency, packet loss, bandwidth, and throughput.
- Test connectivity to a reachable network endpoint using Python.
- Simulate network failures and recovery in Cisco Packet Tracer.

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Random Forest Classifier
- Cisco Packet Tracer
- CSV for dataset and test-result storage

## Project Files
- `01_data_analysis.py` – Dataset analysis
- `02_preprocessing.py` – Data preprocessing
- `03_train_model.py` – Model training
- `04_save_model.py` – Saving the trained model and encoders
- `05_predict_impact.py` – Network impact prediction
- `06_network_testing.py` – Network testing experiments
- `07_ai_network_test.py` – Impact prediction and validation checks
- `08_auto_network_test.py` – Automated ping testing and result logging

## Dataset
The training dataset contains synthetic network scenarios, including normal operation, high latency, packet loss, and router failure. It is used to train and evaluate the Machine Learning model.

## Current Implementation
1. Train a Random Forest model using the prepared dataset.
2. Predict network impact from manually entered network parameters.
3. Run a Python ping test against a reachable endpoint.
4. Record automated ping-test results in a CSV file.
5. Use Cisco Packet Tracer to simulate network failures and recovery.

**Note:** Python ping testing and Cisco Packet Tracer simulation are currently separate. Direct automatic collection of Packet Tracer or physical Cisco device metrics has not been implemented.

## Future Scope
- Integrate with real network devices using SNMP, NETCONF, or telemetry.
- Automatically collect network metrics.
- Connect prediction and validation into a unified workflow.

## Disclaimer
Predictions depend on the training data and model. Since the current dataset is synthetic, results demonstrate a prototype rather than validated real-world network performance.