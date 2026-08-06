# 🚀 AdventureWorks Automated ETL Pipeline

## 📌 Project Overview

This project is an automated ETL (Extract, Transform, Load) pipeline developed in Python. It downloads the AdventureWorks Sales dataset from the provided GitHub repository, validates the data, performs cleaning and transformation, generates a business-ready Excel file, and prepares it for SharePoint upload.

The pipeline is modular, reusable, and can be executed using a single Python script.

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
└── README.md
```

---

# ⚙ Technologies Used

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

The pipeline automatically downloads the AdventureWorks Sales Excel file from the provided GitHub repository.

### Tasks Performed

- Open the GitHub repository using Selenium.
- Navigate to the AdventureWorks Sales dataset.
- Download the Excel file.
- Verify successful download.

**Output**

```
downloads/
AdventureWorks Sales.xlsx
```

---

# Step 2 - Data Validation

The downloaded dataset is validated before processing.

### Validation Checks

- Missing values
- Duplicate rows
- Negative Sales Amount
- Invalid Order Quantity

A validation report is generated.

**Output**

```
logs/
validation_report.txt
```

---

# Step 3 - Data Cleaning

The cleaning module improves the quality of the dataset.

### Cleaning Performed

- Removed duplicate rows
- Trimmed leading and trailing spaces
- Replaced missing `ShipDateKey` values with **-1**
- Replaced missing `Color` values with **Unknown**

**Output**

```
output/
AdventureWorks_Sales_Cleaned.xlsx
```

---

# Step 4 - Data Transformation

The cleaned dataset is transformed into a business-ready dataset.

### New Columns Created

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

A SharePoint upload module has been implemented.

Since no SharePoint site or credentials were provided for this assignment, the module detects the placeholder configuration and skips the upload while recording the status in the log.

---

# Step 6 - Logging

The pipeline records every execution step.

The log contains:

- Pipeline Start
- Dataset Download
- Validation
- Cleaning
- Transformation
- SharePoint Status
- Pipeline Completion

**Output**

```
logs/
pipeline.log
```

---

# ▶ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the complete pipeline:

```bash
python scripts/main.py
```

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

# ✅ Features

- Automated dataset download
- Data validation
- Data cleaning
- Data transformation
- Business-ready Excel generation
- Logging and error handling
- Modular project structure
- Single-command pipeline execution

---

# 👨‍💻 Author

**Vikash Basfore**
