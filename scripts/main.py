from logger import logger

from downloader import download_dataset
from validator import validate_dataset
from cleaner import clean_dataset
from transformer import transform_dataset
from sharepoint import upload_to_sharepoint


def main():

    logger.info("=" * 70)
    logger.info("AdventureWorks ETL Pipeline Started")
    logger.info("=" * 70)

    try:

        # --------------------------------------------------
        # Download Dataset
        # --------------------------------------------------

        if not download_dataset():
            raise Exception("Download Failed")

        # --------------------------------------------------
        # Validate Dataset
        # --------------------------------------------------

        validate_dataset()

        # --------------------------------------------------
        # Clean Dataset
        # --------------------------------------------------

        clean_dataset()

        # --------------------------------------------------
        # Transform Dataset
        # --------------------------------------------------

        transform_dataset()

        # --------------------------------------------------
        # Upload
        # --------------------------------------------------

        upload_to_sharepoint()

        logger.info("=" * 70)
        logger.info("Pipeline Completed Successfully")
        logger.info("=" * 70)

    except Exception as e:

        logger.exception(f"Pipeline Failed : {e}")


if __name__ == "__main__":
    main()