# 🏙️ Community Micro-Problem Reporter

## 📌 Project Overview

**Community Micro-Problem Reporter** is a simple AI-assisted web application designed to help people report small but important problems in their local communities.

The system allows users to submit reports about issues such as garbage, road problems, flooding, and street-light problems. The submitted reports are stored in a database and can be viewed and managed through an admin dashboard.

The project aims to provide a simple digital platform for collecting, organizing, and monitoring community-level problems.

---

## 🎯 Objectives

* Provide an easy way for users to report community problems.
* Store submitted reports in a structured database.
* Categorize different types of community issues.
* Allow administrators to view and manage reports.
* Track the status of reported problems.
* Provide statistics and visualizations about reported issues.
* Detect potentially duplicate reports.
* Create a foundation that can be extended with AI-based image classification in the future.

---

## 🚀 Features

### 👤 User Features

* Submit a community problem report.
* Select the problem category.
* Enter the location of the problem.
* Add a description of the issue.
* Receive confirmation after submitting a report.
* Get a warning when a similar report may already exist.

### 🔐 Admin Features

* View all submitted reports.
* Search and filter reports.
* View report statistics.
* Visualize problem categories using charts.
* Monitor report status.
* Manage community problem information.

### 📊 Dashboard

The application provides statistics and visualizations such as:

* Total number of reports.
* Number of reports by problem type.
* Number of reports by status.
* Location-based report information.
* Distribution of different community problems.

---

## 🧩 Problem Categories

The project can work with categories such as:

* 🗑️ Garbage
* 🕳️ Pothole
* 🌧️ Roadway Flooding
* 💡 Street Light Problems
* 🌳 Other Community Problems

The categories can be expanded as the project develops.

---

## 🤖 AI Component

The project is designed to support AI-based community problem detection.

The initial development uses a small image dataset for experimentation and classification.

Possible future AI functionality includes:

* Image-based problem classification.
* Automatic identification of community problems.
* Duplicate image/report detection.
* Severity estimation.
* Automatic report categorization.

The current application focuses mainly on the reporting and management workflow.

---

## 🗂️ Project Structure

```text
Community_Micro_Problem_Reporter/
│
├── app.py
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

> Large datasets and generated files should not be uploaded to GitHub. The dataset can be downloaded separately when required.

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **SQLite**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Scikit-learn**
* **Ultralytics YOLO** *(for future/experimental AI functionality)*

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Community_Micro_Problem_Reporter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 🗄️ Database

The project uses **SQLite** for storing community reports.

The database can contain information such as:

* Report ID
* Problem type
* Location
* Description
* Report status
* Date/time of submission

The database is created and managed locally by the application.

---

## 🔎 Duplicate Report Detection

The application includes a basic duplicate detection mechanism.

It compares:

* Problem type
* Location
* Description similarity

If a newly submitted report is sufficiently similar to an existing report, the application displays a warning to help reduce duplicate reports.

---

## 📈 Future Enhancements

The project can be further improved by adding:

* 📷 Image upload for problem reporting.
* 🤖 AI-based image classification.
* 🗺️ Interactive map integration.
* 📍 Automatic location detection.
* 🔔 Notifications for report updates.
* 👥 User authentication.
* 🏛️ Separate authority/admin accounts.
* 📱 Mobile-friendly interface.
* 📊 Advanced analytics.
* 🚨 Problem severity detection.
* 🔄 Real-time report status updates.
* ☁️ Cloud database integration.

---

## 🌱 Social Impact

Small community problems can often remain unnoticed because there is no simple way to report and track them.

This project provides a basic digital platform for making such problems visible and organized.

It can help communities:

* Identify frequently occurring problems.
* Organize complaints systematically.
* Track unresolved issues.
* Analyze common problem areas.
* Support better community management.

---

## 🎓 Project Purpose

This project was developed as an **academic and learning-oriented project** to explore:

* Python application development.
* Streamlit web applications.
* Database management.
* Data analysis and visualization.
* Basic AI/ML integration.
* Community-focused technology solutions.

---

## 📜 License

This project is intended for educational and study purposes.

You may modify and extend the project for learning and development.

---

## 👩‍💻 Author

**Community Micro-Problem Reporter**

Developed as an academic project focused on using technology to identify, report, and organize small community problems.
