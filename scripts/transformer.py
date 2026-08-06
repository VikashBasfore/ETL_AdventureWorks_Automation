import pandas as pd

from config import OUTPUT_FILE, FINAL_OUTPUT_FILE
from logger import logger


def transform_dataset():
    """
    Transform the cleaned AdventureWorks dataset.

    Returns
    -------
    bool
        True if transformation succeeds, False otherwise.
    """

    try:

        logger.info("=" * 70)
        logger.info("AdventureWorks Data Transformation Started")
        logger.info("=" * 70)

        # ------------------------------------------------------
        # Read Cleaned Workbook
        # ------------------------------------------------------

        excel = pd.ExcelFile(OUTPUT_FILE)

        with pd.ExcelWriter(
            FINAL_OUTPUT_FILE,
            engine="openpyxl"
        ) as writer:

            for sheet in excel.sheet_names:

                logger.info(f"Processing Sheet : {sheet}")

                df = pd.read_excel(
                    OUTPUT_FILE,
                    sheet_name=sheet
                )

                # --------------------------------------------------
                # Sales Data Transformations
                # --------------------------------------------------

                if sheet == "Sales_data":

                    # Profit
                    df["Profit"] = (
                        df["Sales Amount"]
                        - df["Total Product Cost"]
                    )

                    # Profit Margin %
                    df["Profit Margin %"] = (
                        df["Profit"]
                        / df["Sales Amount"].replace(0, pd.NA)
                    ) * 100

                    # Shipment Status
                    df["Shipment Status"] = df["ShipDateKey"].apply(
                        lambda x: (
                            "Not Shipped"
                            if x == -1
                            else "Shipped"
                        )
                    )

                    # Convert Order Date
                    order_date = pd.to_datetime(
                        df["OrderDateKey"].astype(str),
                        format="%Y%m%d"
                    )

                    df["Order Date"] = order_date.dt.date
                    df["Order Year"] = order_date.dt.year
                    df["Order Month"] = order_date.dt.strftime("%B")
                    df["Order Quarter"] = (
                        "Q"
                        + order_date.dt.quarter.astype(str)
                    )

                # --------------------------------------------------
                # Save Sheet
                # --------------------------------------------------

                df.to_excel(
                    writer,
                    sheet_name=sheet,
                    index=False
                )

                logger.info(f"Rows Written : {len(df)}")

        logger.info("=" * 70)
        logger.info("Transformation Completed Successfully")
        logger.info(f"Final File : {FINAL_OUTPUT_FILE}")
        logger.info("=" * 70)

        return True

    except Exception as e:

        logger.exception(f"Transformation failed: {e}")

        return False


# ==========================================================
# Run Independently
# ==========================================================

if __name__ == "__main__":

    success = transform_dataset()

    if success:

        logger.info("Transformer Module Completed Successfully.")

    else:

        logger.error("Transformer Module Failed.")