import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger import logger
from config import (
    GITHUB_URL,
    RAW_DOWNLOAD_URL,
    DOWNLOAD_FOLDER,
    DOWNLOAD_FILE_NAME,
    CHROMEDRIVER_PATH,
    DOWNLOAD_TIMEOUT,
)

# ==========================================================
# Chrome Driver Configuration
# ==========================================================

CHROMEDRIVER_PATH = (
    r"C:\Users\vikas\.wdm\drivers\chromedriver\win64"
    r"\151.0.7922.76\chromedriver-win64\chromedriver.exe"
)

# ==========================================================
# GitHub Raw File URL
# ==========================================================

RAW_DOWNLOAD_URL = (
    "https://raw.githubusercontent.com/"
    "microsoft/powerbi-desktop-samples/"
    "main/AdventureWorks%20Sales%20Sample/"
    "AdventureWorks%20Sales.xlsx"
)


def download_dataset():
    """
    Download the AdventureWorks Sales dataset from GitHub.

    Returns
    -------
    bool
        True if download is successful, otherwise False.
    """

    logger.info("=" * 70)
    logger.info("AdventureWorks Dataset Download Started")
    logger.info("=" * 70)

    # ------------------------------------------------------
    # Create Download Folder
    # ------------------------------------------------------

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    download_path = os.path.join(
        DOWNLOAD_FOLDER,
        DOWNLOAD_FILE_NAME
    )

    # ------------------------------------------------------
    # Remove Existing File
    # ------------------------------------------------------

    if os.path.exists(download_path):
        try:
            logger.info("Existing dataset found. Removing old file...")
            os.remove(download_path)
            logger.info("Old dataset removed successfully.")
        except Exception as e:
            logger.exception(f"Unable to delete old file: {e}")
            return False

    # ------------------------------------------------------
    # Chrome Options
    # ------------------------------------------------------

    chrome_options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": DOWNLOAD_FOLDER,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
    }

    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--start-maximized")

    driver = None

    try:

        logger.info("Launching Chrome Browser...")

        driver = webdriver.Chrome(
            service=Service(CHROMEDRIVER_PATH),
            options=chrome_options
        )

        wait = WebDriverWait(driver, 30)

        # ------------------------------------------------------
        # Open GitHub Repository
        # ------------------------------------------------------

        logger.info("Opening GitHub Repository...")

        driver.get(GITHUB_URL)

        # ------------------------------------------------------
        # Locate Excel File
        # ------------------------------------------------------

        logger.info("Searching for AdventureWorks Excel file...")

        excel_link = wait.until(
            EC.element_to_be_clickable(
                (
                    By.PARTIAL_LINK_TEXT,
                    DOWNLOAD_FILE_NAME
                )
            )
        )

        excel_link.click()

        logger.info("Excel file page opened successfully.")

        time.sleep(2)

        # ------------------------------------------------------
        # Download File
        # ------------------------------------------------------

        logger.info("Downloading dataset...")

        driver.get(RAW_DOWNLOAD_URL)

        timeout = 60

        while timeout > 0:

            if (
                os.path.exists(download_path)
                and
                not os.path.exists(download_path + ".crdownload")
            ):
                break

            time.sleep(1)
            timeout -= 1

        # ------------------------------------------------------
        # Verify Download
        # ------------------------------------------------------

        if not os.path.exists(download_path):
            logger.error("Dataset download failed.")
            return False

        file_size = os.path.getsize(download_path)

        if file_size < 1024 * 1024:
            logger.error("Downloaded file appears to be incomplete.")
            return False

        logger.info("Dataset downloaded successfully.")
        logger.info(f"File Location : {download_path}")
        logger.info(f"File Size : {round(file_size / (1024 * 1024), 2)} MB")

        return True

    except Exception as e:

        logger.exception(f"Downloader failed: {e}")
        return False

    finally:

        if driver:

            logger.info("Closing Chrome Browser...")

            driver.quit()

            logger.info("Browser closed.")

        logger.info("=" * 70)


# ==========================================================
# Execute Standalone
# ==========================================================

if __name__ == "__main__":

    if download_dataset():
        logger.info("Downloader module completed successfully.")
    else:
        logger.error("Downloader module failed.")