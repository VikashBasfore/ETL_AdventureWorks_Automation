import pandas as pd

from config import INPUT_FILE, OUTPUT_FILE
from logger import logger


def clean_dataset():
    """
    Cleans the AdventureWorks dataset.

    Returns
    -------
    bool
        True if cleaning succeeds.
        False otherwise.
    """

    try:

        logger.info("=" * 60)
        logger.info("AdventureWorks Data Cleaning Started")
        logger.info("=" * 60)

        # Load workbook
        excel = pd.ExcelFile(INPUT_FILE)

        # Create cleaned workbook
        with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:

            for sheet in excel.sheet_names:

                logger.info(f"Processing Sheet : {sheet}")

                df = pd.read_excel(INPUT_FILE, sheet_name=sheet)

                original_rows = len(df)

                # ---------------------------------
                # Remove Duplicate Rows
                # ---------------------------------

                df.drop_duplicates(inplace=True)

                duplicates_removed = original_rows - len(df)

                # ---------------------------------
                # Remove Leading / Trailing Spaces
                # ---------------------------------

                for column in df.select_dtypes(include=["object", "string"]).columns:
                    df[column] = df[column].str.strip()

                # ---------------------------------
                # Sheet Specific Cleaning
                # ---------------------------------

                if sheet == "Sales_data":

                    if "ShipDateKey" in df.columns:
                        df["ShipDateKey"] = df["ShipDateKey"].fillna(-1)

                elif sheet == "Product_data":

                    if "Color" in df.columns:
                        df["Color"] = df["Color"].fillna("Unknown")

                # ---------------------------------
                # Save Sheet
                # ---------------------------------

                df.to_excel(
                    writer,
                    sheet_name=sheet,
                    index=False
                )

                logger.info(f"Rows Written        : {len(df)}")
                logger.info(f"Duplicates Removed  : {duplicates_removed}")

        logger.info("=" * 60)
        logger.info("Cleaning Completed Successfully")
        logger.info(f"Cleaned File Saved : {OUTPUT_FILE}")
        logger.info("=" * 60)

        return True

    except Exception as e:

        logger.exception(f"Cleaning failed: {e}")

        return False


if __name__ == "__main__":

    success = clean_dataset()

    if success:
        logger.info("Cleaner Module Completed Successfully.")

    else:
        logger.error("Cleaner Module Failed.")