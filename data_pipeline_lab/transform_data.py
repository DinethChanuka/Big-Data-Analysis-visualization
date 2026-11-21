from datetime import datetime, timezone
import validate_data

#Work on a copy of the validated DataFrame

validated_df = validate_data.validated_df.copy()

# Add the ingestion timestamp
validated_df["ingestion_time"] = datetime.now(timezone.utc)

# Arrange the columns
validated_df = validated_df[
    ["id", "userId", "title", "body", "ingestion_time"]
]

