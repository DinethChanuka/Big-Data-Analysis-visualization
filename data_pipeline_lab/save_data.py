import os
import transform_data as td


# Create the output folder if it does not already exist
os.makedirs("data", exist_ok=True)

# Save the DataFrame as a Parquet file
td.validated_df.to_parquet(
    "data/posts.parquet",
    engine="pyarrow",
    index=False
)
