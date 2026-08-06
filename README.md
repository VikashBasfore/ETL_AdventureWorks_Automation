# 🚀 AdventureWorks Automated ETL Pipeline

## 📌 Project Overview

This project is an automated ETL (Extract, Transform, Load) pipeline developed in Python. It downloads the AdventureWorks Sales dataset from the provided GitHub repository, validates the extracted data, cleans and transforms it, generates a business-ready Excel file, and prepares it for SharePoint upload.

The pipeline is modular and can be executed using a single Python script.

---

# 📂 Project Structure

```
AdventureWorks_Automation
│
├── downloads/
├── logs/
├── output/
├── scripts/
│   ├── config.py
│   ├── downloader.py
│   ├── validator.py
│   ├── cleaner.py
│   ├── transformer.py
│   ├── sharepoint.py
│   ├── logger.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Technologies Used

- Python
- Selenium
- Pandas
- OpenPyXL
- Office365 REST Python Client
- Logging

---

# 🔄 Pipeline Workflow

```
GitHub Repository
        │
        ▼
Download Dataset
        │
        ▼
Validate Dataset
        │
        ▼
Clean Dataset
        │
        ▼
Transform Dataset
        │
        ▼
Generate Final Output
        │
        ▼
SharePoint Module
```

---

# Step 1 - Download Dataset

The `downloader.py` module automates the download of the AdventureWorks Sales dataset.

### Operations Performed

- Opens the GitHub repository using Selenium.
- Navigates to the AdventureWorks Sales dataset.
- Downloads the Excel workbook.
- Verifies successful download.
- Saves the file in the **downloads** folder.

**Output**

```
downloads/
AdventureWorks Sales.xlsx
```

---

# Step 2 - Data Validation

The `validator.py` module validates the downloaded dataset.

### Validation Performed

- Missing Values
- Duplicate Rows
- Negative Sales Amount
- Invalid Order Quantity

A validation report is generated after processing all worksheets.

**Output**

```
logs/
validation_report.txt
```

---

# Step 3 - Data Cleaning

The `cleaner.py` module performs data cleaning.

### Cleaning Operations

- Removed duplicate rows
- Removed leading and trailing spaces
- Replaced missing `ShipDateKey` values with **-1**
- Replaced missing `Color` values with **Unknown**

**Output**

```
output/
AdventureWorks_Sales_Cleaned.xlsx
```

---

# Step 4 - Data Transformation

The `transformer.py` module creates additional business columns.

### New Columns Added

- Profit
- Profit Margin %
- Shipment Status
- Order Date
- Order Year
- Order Month
- Order Quarter

**Output**

```
output/
AdventureWorks_Sales_Final.xlsx
```

---

# Step 5 - SharePoint Module

The `sharepoint.py` module checks the SharePoint configuration.

Since no SharePoint site or credentials were provided for this project, the upload is skipped and the status is recorded in the pipeline log.

---

# Step 6 - Logging

The `logger.py` module records every stage of pipeline execution.

The log includes:

- Pipeline Started
- Dataset Download Completed
- Validation Completed
- Cleaning Completed
- Transformation Completed
- SharePoint Status
- Pipeline Completed

**Output**

```
logs/
pipeline.log
```

---

# Step 7 - Pipeline Execution

The `main.py` module controls the complete ETL workflow.

Run the pipeline using:

```bash
python scripts/main.py
```

This automatically executes:

1. Dataset Download
2. Data Validation
3. Data Cleaning
4. Data Transformation
5. SharePoint Module
6. Pipeline Completion

---

# 📁 Output Files

### Downloaded Dataset

```
downloads/
AdventureWorks Sales.xlsx
```

### Validation Report

```
logs/
validation_report.txt
```

### Cleaned Dataset

```
output/
AdventureWorks_Sales_Cleaned.xlsx
```

### Final Dataset

```
output/
AdventureWorks_Sales_Final.xlsx
```

### Pipeline Log

```
logs/
pipeline.log
```

---

# ✅ Project Features

- Automated dataset download
- Automated data validation
- Automated data cleaning
- Automated data transformation
- Business-ready Excel generation
- Logging
- Error handling
- Modular project structure
- Single-command pipeline execution

---

# 👨‍💻 Author

**Vikash Basfore**
