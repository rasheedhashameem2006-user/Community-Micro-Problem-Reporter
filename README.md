# 🏙️ Community Micro-Problem Reporter

## 📌 Project Overview

**Community Micro-Problem Reporter** is a web-based application designed to help people report small but important problems in their local communities.

The system allows users to submit reports about community issues such as garbage, potholes, roadway flooding, and street-light problems. Submitted reports are stored in a database and can be monitored and managed through a separate Admin Dashboard.

The project provides a simple digital platform for collecting, organizing, analyzing, and managing community-level problems.

---

## 🎯 Objectives

* Provide an easy way for citizens to report local community problems.
* Store submitted reports in a structured database.
* Categorize different types of community issues.
* Automatically assign the relevant department.
* Assign priority and severity levels.
* Detect potentially duplicate reports.
* Allow administrators to monitor submitted reports.
* Track the status of reported problems.
* Provide statistics and visualizations.
* Support future AI-based problem detection.

---

## 🚀 Features

### 👤 User Reporting

Users can:

* Submit a community problem.
* Select the problem category.
* Enter the location.
* Describe the problem.
* Select priority.
* Select severity.
* Submit the report through the Streamlit interface.

After submission, the report is stored in the database.

---

### 🔐 Admin Dashboard

The project includes a **separate Admin Dashboard** for managing submitted reports.

Administrators can:

* View submitted reports.
* Search reports.
* Filter reports.
* Monitor problem categories.
* View priority and severity information.
* Monitor report status.
* Analyze reports using charts.
* Manage community problem information.

The Admin Dashboard is implemented in:

```text
admin_dashboard.py
```

---

### 🔎 Duplicate Report Detection

The system performs a basic duplicate-report check before saving a new report.

It compares:

* Problem type
* Location
* Description similarity

If a sufficiently similar report already exists, the system displays a warning to help reduce duplicate submissions.

---

### 📊 Analytics Dashboard

The application provides analytical information about submitted reports.

The dashboard includes:

* Total reports
* High-priority reports
* High-severity reports
* Resolved reports
* Most reported problem
* Problem-wise reports
* Severity-wise reports
* Priority-wise reports
* Department-wise reports
* Status-wise reports
* Location-wise reports

---

### 🔍 Search and Filtering

Reports can be searched using:

* Report ID
* Problem type
* Location
* Description

Reports can also be filtered by:

* Problem
* Department
* Priority
* Severity
* Status

---

### ⬇️ Report Export

Filtered reports can be exported as a CSV file for further analysis and record keeping.

---

## 🧩 Problem Categories

The current project supports categories such as:

* 🗑️ Garbage
* 🕳️ Pothole
* 🌧️ Roadway Flooding
* 💡 Street Light
* 🔧 Other

Additional categories can be added in future versions.

---

## 🗂️ Project Structure

```text
Community_Micro_Problem_Reporter/
│
├── app.py
├── admin_dashboard.py
├── database.py
├── view_reports.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── train/
│   └── Dataset files
│
├── test/
│   └── Dataset files
│
└── processed_data/
    └── Processed dataset files
```

> **Note:** Large datasets and generated/processed files should not be uploaded to GitHub. They can be downloaded or generated separately when required.

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **SQLite**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Ultralytics YOLO** *(for AI/ML experimentation and future development)*

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone 
```

### 2. Navigate to the Project

```bash
cd Community_Micro_Problem_Reporter
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

### User Application

Run:

```bash
streamlit run app.py
```

The application opens in a web browser and allows users to submit community problem reports.

### Admin Dashboard

Run the separate admin dashboard using:

```bash
streamlit run admin_dashboard.py
```

The Admin Dashboard allows administrators to view, analyze, and manage submitted reports.

---

## 🗄️ Database

The project uses **SQLite** to store community reports.

A report can contain information such as:

| Field       | Description               |
| ----------- | ------------------------- |
| Report ID   | Unique report identifier  |
| Problem     | Type of community problem |
| Confidence  | Classification confidence |
| Department  | Responsible department    |
| Priority    | Priority level            |
| Severity    | Severity level            |
| Location    | Reported location         |
| Description | Details of the problem    |
| Status      | Current report status     |

The database is created locally by the application.

---

## 🔄 Report Status

Reports can be tracked using statuses such as:

```text
Pending
In Progress
Resolved
```

This allows administrators to monitor the progress of reported community problems.

---

## 🤖 AI Component

The project is designed to support AI-based community problem detection.

The initial development can use image datasets for experimentation and classification.

Future AI functionality can include:

* 📷 Image-based problem classification
* 🤖 Automatic problem identification
* 🔎 Duplicate image detection
* 🚨 Problem severity estimation
* 🏷️ Automatic report categorization

The current system focuses primarily on the reporting, database, analytics, and administration workflow.

---

## 📈 Future Enhancements

Possible future improvements include:

* 📷 Image upload with reports
* 🤖 AI-based image classification
* 🗺️ Interactive map integration
* 📍 Automatic location detection
* 🔔 Notifications for report updates
* 👥 User authentication
* 🔐 Improved administrator authentication
* 📱 Mobile-friendly interface
* 📊 Advanced analytics
* 🚨 Automatic severity detection
* ☁️ Cloud database integration
* 🏛️ Integration with local-authority workflows

---

## 🌱 Social Impact

Small community problems can sometimes remain unnoticed because there is no simple way to report and track them.

The **Community Micro-Problem Reporter** provides a digital platform for collecting and organizing information about such problems.

The system can help communities:

* Report local issues systematically.
* Identify frequently occurring problems.
* Track unresolved reports.
* Analyze common problem categories.
* Organize reports for administrative review.

---

## 🎓 Project Purpose

This project was developed as an **academic and learning-oriented project** to explore:

* Python application development
* Streamlit web application development
* SQLite database management
* Data analysis
* Data visualization
* Basic AI/ML integration
* Duplicate report detection
* Community-focused technology solutions

---

## 📋 Requirements

The main Python dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🚫 Files Excluded from GitHub

The following files and folders should not be uploaded:

```text
venv/
__pycache__/
*.pyc
*.db
community_reports.db
processed_data/
train/
test/
.vscode/
.env
```

These files are either generated locally, contain large datasets, or are not required for the source-code repository.

---

## 📜 License

This project is intended primarily for educational and academic purposes.

The project may be modified and extended for learning and development.

---

## 👩‍💻 Author

**Community Micro-Problem Reporter**

An academic project focused on using Python, data analysis, databases, and AI-based techniques to support community problem reporting and management.
