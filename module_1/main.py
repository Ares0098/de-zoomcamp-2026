from pipeline.ingest_green_tripdata import run_ingest_green_tripdata
from pipeline.ingest_taxi_zone_lookup import run_ingest_taxi_zone_lookup

def main():
    run_ingest_green_tripdata()
    run_ingest_taxi_zone_lookup()

if __name__ == "__main__":
    main()
