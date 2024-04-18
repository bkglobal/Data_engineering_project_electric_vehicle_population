import io
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from google.cloud import storage
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


KAGGLE_USERNAME = os.environ.get('KAGGLE_USERNAME')
KAGGLE_API_TOKEN = os.environ.get('KAGGLE_API_TOKEN')

# Mount point for service account key file (adjust path if needed)
SERVICE_ACCOUNT_KEY_PATH = "kaggle_credentials/kaggle.json"

@data_loader
def load_data_from_api(*args, **kwargs):
    # Set your Kaggle API credentials using environment variables
    os.environ["KAGGLE_USERNAME"] = KAGGLE_USERNAME
    os.environ["KAGGLE_KEY"] = KAGGLE_API_TOKEN
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_credentials/key.json"

    # Authenticate to Kaggle using environment variables
    api = KaggleApi()
    api.authenticate()

    dataset_name = 'sahirmaharajj/electric-vehicle-population'
    dataset_file_name = 'Electric_Vehicle_Population_Data.csv'
    # Setting download directory here..
    download_dir = "datasets/"

    # Download the dataset
    api.dataset_download_files(dataset_name, path=download_dir, unzip=True)
    print('dataset downloaded successfully')


    # Upload to GCS Bucket Part..
    # ###########################
    # Upload dataset to Google Cloud Storage (GCS)
    def upload_to_gcs(local_file, bucket_name, destination_blob_name):
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file)
        print(f"File {local_file} uploaded to GCS bucket {bucket_name} as {destination_blob_name}")

    # Set up Google Cloud Storage credentials using environment variable (for authentication)

    # Specify your GCS bucket name, destination blob name, and file name
    bucket_name = "ev_population"
    destination_blob_name = dataset_file_name
    file_name = dataset_file_name

    # Upload dataset to GCS
    local_zip_file = os.path.join(download_dir, file_name)
    upload_to_gcs(local_zip_file, bucket_name, destination_blob_name)


    # Read it on pandas dataframe..
    data = pd.read_csv(f"{download_dir}/{dataset_file_name}")

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    # Check if the output is a DataFrame
    assert isinstance(output, pd.DataFrame), 'The output should be a DataFrame'
    
    # Check number of rows and columns
    num_rows, num_columns = output.shape
    assert num_rows == 177866, 'The number of rows should be 177866'
    assert num_columns == 17, 'The number of columns should be 17'