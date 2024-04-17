import io
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from google.cloud import storage
import pandas as pd
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    dataset_file_name = 'Electric_Vehicle_Population_Data.csv'
    
    bucket_name = 'dev-adscore-dataingestion'
    object_key = dataset_file_name


    def fetch_object_from_gcs(bucket_name, blob_name):
        """
        Fetches an object from a Google Cloud Storage bucket and returns its content as a string.
        """
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        content = blob.download_as_string().decode('utf-8')
        return content
    
    # Fetch object from GCS
    csv_content = fetch_object_from_gcs(bucket_name, object_key)

    # Convert CSV content to DataFrame
    df = pd.read_csv(io.StringIO(csv_content))


    return df



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