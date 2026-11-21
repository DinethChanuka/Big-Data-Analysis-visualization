import os
import requests
import pandas as pd
import pandera.pandas as pa 
from datetime import datetime, timezone
from prefect import flow, task

API_URL = "https://jsonplaceholder.typicode.com/posts"

# TASK 1: INGEST DATA
@task
def ingest_data():
    print("Ingesting data from API...")
    response= requests.get(API_URL, timeout=30)
    response.raise_for_status()

    data=response.json()
    df = pd.DataFrame(data)
    print("Data ingestion completed successfully!")
    print("Records ingested:", len(df))
    return df

# TASK 2: VALIDATE DATA
@task
def validate_data(df):
    print("Validating dataset...")

    schema = pa.DataFrameSchema({
        "userId": pa.Column(
            int,
            checks=pa.Check.ge(1)
        ),
        "id": pa.Column(
            int,
            checks=pa.Check.ge(1),
            unique=True
        ),
        "title": pa.Column(
            str,
            nullable=False,
            checks=pa.Check.str_length(min_value=1)
        ),
        "body": pa.Column(
            str,
            nullable=False,
            checks=pa.Check.str_length(min_value=1)
        )
    })

    validated_df = schema.validate(df)
    print("Validation successful!")
    return validated_df

# TASK 3: TRANSFORM DATA
@task
def transform_data(df):
    print("Transforming dataset...")

    df = df.copy()
    df["ingestion_time"] = datetime.now(timezone.utc)

    df = df[
        ["id", "userId", "title", "body", "ingestion_time"]
    ]

    return df


# TASK 4: SAVE AS PARQUET
@task
def save_data(df):
    os.makedirs("data", exist_ok=True)

    file_path = "data/posts.parquet"

    df.to_parquet(
        file_path,
        engine="pyarrow",
        index=False
    )

    print("Parquet file saved:", file_path)
    return file_path


# MAIN PREFECT FLOW
@flow(name="API Data Ingestion Pipeline")
def data_pipeline():
    raw_data = ingest_data()
    valid_data = validate_data(raw_data)
    transformed_data = transform_data(valid_data)
    save_data(transformed_data)

    print("Pipeline completed successfully!")


# RUN THE FLOW
if __name__ == "__main__":
    data_pipeline()

