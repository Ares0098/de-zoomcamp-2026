import os
import time
import pandas as pd

from sqlalchemy import create_engine

def run_ingest_taxi_zone_lookup() :

    dtype = {
        "LocationID": "Int64",
        "Borough": "string",
        "Zone": "string",
        "service_zone": "string"
    }

    table_name = "taxi_zone_lookup"

    df = pd.read_csv(
        'raw_data/taxi_zone_lookup.csv',
        dtype=dtype
    )

    df.columns = [c.lower() for c in df.columns]

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

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )