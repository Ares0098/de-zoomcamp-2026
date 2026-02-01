import os
import time
import pyarrow.parquet as pq

from sqlalchemy import create_engine
from tqdm.auto import tqdm


def run_ingest_green_tripdata():
    dtype = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RatecodeID": "Int64",
        "store_and_fwd_flag": "string",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64",
    }

    table_name = "green_tripdata"

    parquet_file = pq.ParquetFile(
        "./raw_data/green_tripdata_2025-11.parquet"
    )

    db_url = (
        f"postgresql://{os.environ['DATABASE_USER']}:"
        f"{os.environ['DATABASE_PASSWORD']}@"
        f"{os.environ['DATABASE_HOST']}:"
        f"{os.environ['DATABASE_PORT']}/"
        f"{os.environ['DATABASE_NAME']}"
    )

    engine = create_engine(db_url)

    for _ in range(10):
        try:
            engine.connect()
            break
        except Exception:
            time.sleep(2)

    first = True

    for batch in tqdm(parquet_file.iter_batches(batch_size=100_000)):
        df_chunk = batch.to_pandas()

        # enforce pandas dtypes (optional but consistent with your CSV logic)
        df_chunk = df_chunk.astype(dtype)

        df_chunk.columns = [c.lower() for c in df_chunk.columns]

        if first:
            df_chunk.head(0).to_sql(
                name=table_name,
                con=engine,
                if_exists="replace",
            )
            first = False
            print("Table created")

        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
        )

        print("Inserted:", len(df_chunk))