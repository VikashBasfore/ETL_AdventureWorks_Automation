import os

from logger import logger
from config import (
    FINAL_OUTPUT_FILE,
    SHAREPOINT_SITE,
    DOCUMENT_LIBRARY,
    TARGET_FOLDER,
    USERNAME,
    PASSWORD,
)

try:
    from office365.runtime.auth.user_credential import UserCredential
    from office365.sharepoint.client_context import ClientContext
    OFFICE365_AVAILABLE = True
except ImportError:
    OFFICE365_AVAILABLE = False


def upload_to_sharepoint():
    """
    Upload the final dataset to SharePoint.

    Returns
    -------
    bool
    """

    logger.info("=" * 60)
    logger.info("SharePoint Upload Started")
    logger.info("=" * 60)

    # ----------------------------------------------------
    # Check Output File
    # ----------------------------------------------------

    if not os.path.exists(FINAL_OUTPUT_FILE):

        logger.error("Final output file not found.")
        logger.error(FINAL_OUTPUT_FILE)

        return False

    # ----------------------------------------------------
    # Placeholder Configuration
    # ----------------------------------------------------

    if (
        SHAREPOINT_SITE.startswith("https://yourcompany")
        or USERNAME == "your_email@company.com"
        or PASSWORD == "your_password"
    ):

        logger.warning("SharePoint configuration not provided.")
        logger.info("Upload skipped (Assignment Mode).")
        logger.info("File Ready For Upload:")
        logger.info(FINAL_OUTPUT_FILE)

        logger.info("=" * 60)

        return True

    # ----------------------------------------------------
    # Office365 Library
    # ----------------------------------------------------

    if not OFFICE365_AVAILABLE:

        logger.error("Office365 Python library is not installed.")

        return False

    try:

        logger.info("Connecting to SharePoint...")

        ctx = ClientContext(
            SHAREPOINT_SITE
        ).with_credentials(
            UserCredential(
                USERNAME,
                PASSWORD
            )
        )

        folder_path = (
            f"{DOCUMENT_LIBRARY}/{TARGET_FOLDER}"
        )

        folder = ctx.web.get_folder_by_server_relative_url(
            folder_path
        )

        logger.info("Uploading file...")

        with open(FINAL_OUTPUT_FILE, "rb") as file:

            folder.upload_file(
                os.path.basename(FINAL_OUTPUT_FILE),
                file.read()
            ).execute_query()

        logger.info("Upload Successful")
        logger.info(folder_path)

        logger.info("=" * 60)

        return True

    except Exception as e:

        logger.exception(f"Upload failed: {e}")

        return False


if __name__ == "__main__":

    success = upload_to_sharepoint()

    if success:

        logger.info("SharePoint Module Completed Successfully.")

    else:

        logger.error("SharePoint Module Failed.")