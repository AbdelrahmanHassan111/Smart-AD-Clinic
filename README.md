# Smart Clinic - Alzheimer's Disease Diagnosis System

![Smart Clinic](https://img.shields.io/badge/Smart%20Clinic-Healthcare-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22+-red)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-1.5+-purple)

A comprehensive healthcare management system with a focus on Alzheimer's disease diagnosis and patient management. This application provides tools for doctors to analyze patient data, make predictions, and manage patient records efficiently.

## 📹 Demo Video

Check out our system in action!

https://github.com/user-attachments/assets/0f94079c-74ab-4496-9882-48b4c23a28bd

## 📑 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Key Components](#key-components)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [File Overview](#file-overview)
- [Data Visualization](#data-visualization)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## ✨ Features

### For Doctors 👨‍⚕️👩‍⚕️
- **🧑‍🤝‍🧑 Patient Management**: Add, view, and manage patient information with an intuitive interface.
- **🧠 Alzheimer's Analysis**: Run ML-based predictions on patient data for early disease detection.
- **📋 Medical Records**: Maintain comprehensive patient medical history with searchable entries.
- **🤖 AI Clinical Assistant**: Get AI-powered insights about patients using Google's Gemini API.
- **📊 Analytics Dashboard**: Visualize patient data and trends with interactive, compact charts.

### For Administrators 👨‍💼👩‍💼
- **👥 User Management**: Create and manage doctor accounts with role-based permissions.
- **🧑‍⚕️ Doctor Management**: Add and manage doctor profiles with specialization details.
- **👨‍👩‍👧‍👦 Patient Management**: Oversee all patient records with powerful search capabilities.
- **📈 Prediction Logs**: Monitor all Alzheimer's predictions with filtering and export options.
- **📅 Appointment Scheduling**: Manage patient appointments with status tracking.

## 🛠️ Technology Stack

- **🖥️ Frontend**: Streamlit
- **⚙️ Backend**: Python
- **🗄️ Database**: MySQL
- **🔮 Machine Learning**: XGBoost
- **🤖 AI Assistant**: Google Gemini API
- **📊 Data Visualization**: Matplotlib, Seaborn

## 📁 Project Structure

```
smart_clinic/
├── streamlit_app/           # Streamlit application files
│   ├── app.py               # Main application entry point
│   ├── admin_view.py        # Admin dashboard
│   ├── doctor_view.py       # Doctor dashboard
├── database/                # Database scripts and utilities
│   ├── db_creation.sql      # Database schema creation
├── model/                   # Machine learning models
│   └── XGBoost_grid_optimized.joblib  # Trained XGBoost model
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore file
```

## 🔑 Key Components

### 🧠 Machine Learning Model

The application uses an XGBoost model trained on Alzheimer's disease data to predict patient outcomes. The model analyzes various clinical features including:

- 📝 Cognitive test scores (MMSE, CDRSB, ADAS13)
- 🧠 Memory test results (RAVLT)
- 🔍 Brain measurements (Hippocampus volume)
- 🧬 Biomarkers (APOE4, TAU, ABETA)

### 🤖 AI Clinical Assistant

The AI assistant uses Google's Gemini API to provide intelligent insights about patients. It can:

- 📊 Interpret test results with clinical context
- 💊 Suggest treatment options based on patient data
- 📚 Provide research-backed recommendations
- ❓ Answer questions about patient data and test results

### 🗄️ Database Schema

The application uses a comprehensive database schema with tables for:

- 👨‍👩‍👧‍👦 Patients
- 🧑‍⚕️ Doctors
- 📋 Medical records
- 🧠 Alzheimer's analyses
- 📅 Appointments
- 💬 Chat logs

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- MySQL 8.0 or higher
- Streamlit 1.22.0 or higher
- XGBoost 1.5 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/smart-clinic.git
   cd smart-clinic
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   mysql -u root -p < database/db_creation.sql
   ```

5. **Set up environment variables**:
   Create a `.env` file in the root directory with your database credentials and Gemini API key:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=root
   DB_NAME=smart_clinic
   GEMINI_API_KEY=your_api_key_here
   ```

## 🖥️ Usage

1. **Start the Streamlit app**:
   ```bash
   streamlit run streamlit_app/app.py
   ```

2. **Access the application** at `http://localhost:8501`.

3. **Log in with the default credentials**:
   - Admin: username: `admin1`, password: `admin1`
   - Doctor: username: `dr.shaker`, password: `dr.shaker`

## 📄 File Overview

### app.py
The main entry point for the application. Handles:
- 🔐 User authentication
- 💾 Session management
- 🔄 Routing to appropriate views (admin or doctor)

### admin_view.py
The administrative interface providing functionality for:
- 👥 User management (add/delete users)
- 🧑‍⚕️ Doctor management (add/delete doctors)
- 👨‍👩‍👧‍👦 Patient overview and management
- 📊 Prediction logs monitoring
- 📅 Appointment scheduling and management

### doctor_view.py
The doctor interface providing tools for:
- 🧑‍🤝‍🧑 Patient management
- 🧠 Alzheimer's disease analysis and prediction
- 📋 Medical record management
- 🤖 AI-powered clinical assistant
- 📈 Data visualization and analytics

## 📊 Data Visualization

The application includes various visualizations:

- 📊 Feature importance plots
- 📈 Probability distribution charts
- 📉 Disease progression trends
- 📌 Patient analytics dashboards
- 🔄 Comparative analysis charts

## 🔒 Security

- 🔑 Role-based access control (Admin/Doctor)
- 🔐 Secure password authentication
- 🛡️ Database connection security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Alzheimer's Disease Neuroimaging Initiative (ADNI) for data
- Google Gemini for AI capabilities
- Streamlit for the web framework
- XGBoost for the machine learning model
