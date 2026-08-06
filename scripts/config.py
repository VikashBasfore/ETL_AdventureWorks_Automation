import os

# ==========================================================
# Base Directory
# ==========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ==========================================================
# Folder Paths
# ==========================================================

DOWNLOAD_FOLDER = os.path.join(BASE_DIR, "downloads")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")
LOG_FOLDER = os.path.join(BASE_DIR, "logs")

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(LOG_FOLDER, exist_ok=True)

# ==========================================================
# File Paths
# ==========================================================

DOWNLOAD_FILE_NAME = "AdventureWorks Sales.xlsx"

INPUT_FILE = os.path.join(
    DOWNLOAD_FOLDER,
    DOWNLOAD_FILE_NAME
)

OUTPUT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "AdventureWorks_Sales_Cleaned.xlsx"
)

FINAL_OUTPUT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "AdventureWorks_Sales_Final.xlsx"
)

VALIDATION_REPORT = os.path.join(
    LOG_FOLDER,
    "validation_report.txt"
)

LOG_FILE = os.path.join(
    LOG_FOLDER,
    "pipeline.log"
)

# ==========================================================
# Source Website Configuration
# ==========================================================

GITHUB_URL = (
    "https://github.com/microsoft/"
    "powerbi-desktop-samples/tree/main/"
    "AdventureWorks%20Sales%20Sample"
)

RAW_DOWNLOAD_URL = (
    "https://raw.githubusercontent.com/"
    "microsoft/powerbi-desktop-samples/"
    "main/AdventureWorks%20Sales%20Sample/"
    "AdventureWorks%20Sales.xlsx"
)

# ==========================================================
# Selenium Configuration
# ==========================================================

CHROMEDRIVER_PATH = (
    r"C:\Users\vikas\.wdm\drivers\chromedriver\win64"
    r"\151.0.7922.76\chromedriver-win64\chromedriver.exe"
)

DOWNLOAD_TIMEOUT = 60

# ==========================================================
# SharePoint Configuration
# ==========================================================

SHAREPOINT_SITE = "https://yourcompany.sharepoint.com/sites/DataEngineering"

DOCUMENT_LIBRARY = "Shared Documents"

TARGET_FOLDER = "Processed Files"

USERNAME = "your_email@company.com"

PASSWORD = "your_password"