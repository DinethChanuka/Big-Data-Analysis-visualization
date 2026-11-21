import pandera.pandas as pa
import pipeline

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

# Validate the DataFrame
validated_df = schema.validate(pipeline.df)

print("Data validation successful!")
