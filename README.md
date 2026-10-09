# AI/ML-Based Network Change Impact Prediction and Automated Validation System

## 1. Project Overview

The **AI/ML-Based Network Change Impact Prediction and Automated Validation System** is a Python-based project that uses Machine Learning to predict the potential impact of network changes and performs automated connectivity testing.

Network changes such as high latency, packet loss, and router failures can affect communication between network devices. This project uses a Random Forest classification model to predict the impact level as LOW, MEDIUM, or HIGH based on network parameters.

Cisco Packet Tracer is used to simulate the network topology, test failure scenarios, and observe network recovery. Python is used for Machine Learning prediction and connectivity validation.

## 2. Problem Statement

Network changes can cause connectivity issues, performance degradation, and service interruptions. Manually identifying the possible impact of these changes can take time.

This project demonstrates how Machine Learning can help classify the potential impact of network changes and how automated ping testing can check basic connectivity.

## 3. Objectives

- Predict the potential impact of network changes using Machine Learning.
- Classify network impact into LOW, MEDIUM, and HIGH.
- Analyze parameters such as latency, packet loss, bandwidth, and throughput.
- Perform automated ping testing using Python.
- Record connectivity test results in a CSV file.
- Simulate network failures and recovery using Cisco Packet Tracer.

## 4. Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Random Forest Classifier
- **Data Processing:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Network Simulation:** Cisco Packet Tracer
- **Data Storage:** CSV files
- **Model Storage:** Pickle (`.pkl`) files

## 5. System Architecture

The system consists of two main workflows.

### Machine Learning Workflow

Synthetic Network Dataset → Data Analysis → Preprocessing → Model Training → Saved Model → Impact Prediction

### Network Validation Workflow

Reachable Network Endpoint → Python Ping Test → Packet Statistics → Connectivity Status → CSV Result Logging

Cisco Packet Tracer is used separately to simulate a network containing PCs, a switch, a router, and a server. Interface shutdown and recovery operations help demonstrate network failure and restoration.

## 6. Dataset Description

The project uses a synthetic dataset created for training and testing the Machine Learning model.

The dataset contains the following parameters:

| Parameter | Description |
|---|---|
| `latency_ms` | Network latency in milliseconds |
| `packet_loss_percent` | Percentage of packets lost |
| `bandwidth_mbps` | Available or configured bandwidth in Mbps |
| `throughput_mbps` | Network throughput in Mbps |
| `device_status` | Indicates device availability |
| `link_status` | Indicates link availability |
| `change_type` | Type of network change or scenario |
| `impact` | Impact class used for model training |

The dataset represents scenarios such as normal operation, high latency, packet loss, and router failure.

**Note:** The training dataset is synthetic and does not represent measurements collected automatically from real network devices.

## 7. Machine Learning Methodology

A Random Forest Classifier is used to predict the potential impact of network changes.

### Steps

1. Load the synthetic network dataset.
2. Analyze the dataset and its parameters.
3. Preprocess the data and encode categorical values where required.
4. Train the Random Forest classification model.
5. Save the trained model and encoders as `.pkl` files.
6. Provide network parameters to the prediction program.
7. Predict the impact class and display the model's confidence score.

The model output is classified into three categories:

- **LOW:** Lower predicted impact.
- **MEDIUM:** Moderate predicted impact.
- **HIGH:** Higher predicted impact.

The prediction depends on the quality of the training dataset and the patterns learned by the model. A confidence score is not a guarantee of real-world accuracy.

## 8. Automated Network Validation

The Python connectivity testing script uses the system's ping command to test a specified reachable IP address or hostname.

It extracts available statistics, including:

- Packets sent
- Packets received
- Packet loss percentage
- Average latency
- Connectivity status

The script reports PASS when at least one reply is received and FAIL when no replies are received. The results are recorded in `auto_network_results.csv`.

The validation program also demonstrates rule-based checks using network parameters entered by the user. These checks are separate from the Machine Learning prediction.

## 9. Cisco Packet Tracer Simulation

Cisco Packet Tracer is used to create a basic network topology containing a PC, switch, router, and server.

The simulation demonstrates:

1. Normal connectivity between the PC and server.
2. Network failure after shutting down the router's relevant interface.
3. Ping failure during the simulated interruption.
4. Connectivity restoration after enabling the interface using `no shutdown`.

This demonstrates how network configuration changes can affect communication.

**Implementation limitation:** The Python ping script and Cisco Packet Tracer simulation currently operate independently. The Python script does not automatically collect live metrics from Packet Tracer. Direct integration with real network devices has not been implemented.

## 10. Project File Structure

| File | Purpose |
|---|---|
| `01_data_analysis.py` | Analyzes the dataset |
| `02_preprocessing.py` | Preprocesses data |
| `03_train_model.py` | Trains the Machine Learning model |
| `04_save_model.py` | Saves the trained model and encoders |
| `05_predict_impact.py` | Predicts network change impact |
| `06_network_testing.py` | Contains network testing experiments |
| `07_ai_network_test.py` | Combines impact prediction with validation checks |
| `08_auto_network_test.py` | Performs ping testing and logs results |
| `network_change_dataset.csv` | Synthetic training dataset |
| `network_impact_model.pkl` | Saved Random Forest model |
| `change_type_encoder.pkl` | Saved change-type encoder |
| `impact_encoder.pkl` | Saved impact encoder |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Excludes selected unnecessary files |

## 11. How to Run the Project

### Prerequisites

- Python 3.10 or later
- Required Python libraries
- Cisco Packet Tracer for the separate network simulation

### Installation

Install the dependencies from the project directory:

```bash
pip install -r requirements.txt
```

### Run the Machine Learning Workflow

Run the analysis, preprocessing, training, and model-saving scripts in the order required by their implementation:

```bash
python 01_data_analysis.py
python 02_preprocessing.py
python 03_train_model.py
python 04_save_model.py
```

After the model and encoder files are available, run the prediction or validation script:

```bash
python 07_ai_network_test.py
```

To run the automated ping test:

```bash
python 08_auto_network_test.py
```

Enter an IP address or hostname that is reachable from the computer running the script.

## 12. Results and Observations

The prototype has been tested using sample network scenarios.

- Normal scenario: the model predicted LOW impact, and the validation check reported PASS.
- Packet-loss scenario: the model predicted HIGH impact, and the validation check reported FAIL.
- Router-failure scenario: failure-related parameters were supplied to the prediction and validation program.
- Ping test: the script successfully received 4 out of 4 replies from the tested endpoint, reporting 0% packet loss and an average latency of 14 ms in one recorded run.
- Cisco Packet Tracer: shutting down the router interface interrupted the simulated PC-to-server communication; restoring the interface recovered connectivity.

These are prototype test observations. The Windows ping result is independent of the Cisco Packet Tracer simulation.

## 13. Advantages

- Demonstrates the application of Machine Learning to network management.
- Identifies potential network impact categories.
- Automates basic connectivity testing.
- Stores test results for later review.
- Supports controlled network failure and recovery experiments.

## 14. Limitations

- The training dataset is synthetic.
- Network parameters for impact prediction are entered manually.
- The Python ping test operates independently of Cisco Packet Tracer.
- Real-time data collection from physical network devices is not implemented.
- Model predictions require further evaluation using real network data.

## 15. Future Enhancements

- Integrate real network devices through SNMP, NETCONF, or supported telemetry interfaces.
- Collect network parameters automatically.
- Connect impact prediction and validation into a unified workflow.
- Evaluate the model using real network measurements.
- Add alerts for detected connectivity failures.

## 16. Conclusion

This project demonstrates a prototype for predicting network change impact using Machine Learning and validating basic network connectivity using Python. The Random Forest model classifies potential impact levels, while automated ping testing checks endpoint reachability. Cisco Packet Tracer provides a separate environment for simulating network failures and recovery.

The project provides a foundation for further development toward intelligent network monitoring and automated network change validation.
