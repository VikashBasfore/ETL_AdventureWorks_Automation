import os
import pandas as pd

from config import INPUT_FILE, VALIDATION_REPORT
from logger import logger


def validate_sheet(sheet_name, df, report):
    """
    Validate an individual worksheet.
    """

    report.write(f"\n{'='*60}\n")
    report.write(f"Sheet : {sheet_name}\n")
    report.write(f"{'='*60}\n")

    report.write(f"Rows    : {df.shape[0]}\n")
    report.write(f"Columns : {df.shape[1]}\n\n")

    # ------------------------------------------------------
    # Missing Values
    # ------------------------------------------------------

    report.write("Missing Values\n")
    report.write("-------------------------\n")
    report.write(df.isnull().sum().to_string())
    report.write("\n\n")

    # ------------------------------------------------------
    # Duplicate Rows
    # ------------------------------------------------------

    duplicates = df.duplicated().sum()

    report.write("Duplicate Rows\n")
    report.write("-------------------------\n")
    report.write(str(duplicates))
    report.write("\n\n")

    # ------------------------------------------------------
    # Business Validation
    # ------------------------------------------------------

    if "Sales Amount" in df.columns:

        negative_sales = (df["Sales Amount"] < 0).sum()

        report.write("Negative Sales Amount\n")
        report.write("-------------------------\n")
        report.write(str(negative_sales))
        report.write("\n\n")

    if "Order Quantity" in df.columns:

        invalid_qty = (df["Order Quantity"] <= 0).sum()

        report.write("Invalid Order Quantity\n")
        report.write("-------------------------\n")
        report.write(str(invalid_qty))
        report.write("\n\n")


def validate_dataset():
    """
    Validate the downloaded dataset.

    Returns
    -------
    bool
        True if validation succeeds.
    """

    try:

        logger.info("=" * 70)
        logger.info("Dataset Validation Started")
        logger.info("=" * 70)

        if not os.path.exists(INPUT_FILE):

            logger.error(f"Input file not found: {INPUT_FILE}")
            return False

        excel = pd.ExcelFile(INPUT_FILE)

        with open(VALIDATION_REPORT, "w", encoding="utf-8") as report:

            report.write("=" * 60 + "\n")
            report.write("AdventureWorks Validation Report\n")
            report.write("=" * 60 + "\n")

            for sheet in excel.sheet_names:

                logger.info(f"Validating Sheet : {sheet}")

                df = pd.read_excel(INPUT_FILE, sheet_name=sheet)

                validate_sheet(sheet, df, report)

            report.write("\nValidation Completed Successfully\n")

        logger.info("Validation Completed Successfully.")
        logger.info(f"Validation Report : {VALIDATION_REPORT}")

        logger.info("=" * 70)

        return True

    except Exception as e:

        logger.exception(f"Validation failed: {e}")

        return False


# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":

    success = validate_dataset()

    if success:

        logger.info("Validator Module Completed Successfully.")

    else:

        logger.error("Validator Module Failed.")