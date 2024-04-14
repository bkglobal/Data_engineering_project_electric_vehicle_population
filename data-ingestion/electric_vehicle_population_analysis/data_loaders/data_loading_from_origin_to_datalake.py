import io
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# Set environment variables from Docker secrets (optional)
# os.getenv("KAGGLE_USERNAME")
# os.getenv("KAGGLE_API_TOKEN")
KAGGLE_USERNAME = ""
KAGGLE_API_TOKEN = ""
kaggle_credentials = {
    "username": KAGGLE_USERNAME,
    "key": KAGGLE_API_TOKEN
}

@data_loader
def load_data_from_api(*args, **kwargs):
    # Authenticate to Kaggle using environment variables
    api = KaggleApi()
    api.authenticate()

    # Download the dataset
    api.dataset_download_files("sahirmaharajj", "electric-vehicle-population")

    # Get downloaded file name
    downloaded_file_path = os.listdir()[0]

    #     # Upload the downloaded file to GCS
    # client = storage.Client()
    # bucket = client.bucket(gcs_bucket_name)
    # blob = bucket.blob(gcs_file_path)
    # blob.upload_from_filename(downloaded_file_path)

    # os.remove(downloaded_file_path)  # Clean up the downloaded file


    """
    Template for loading data from API
    """
    url = ''
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
