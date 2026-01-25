SELECT 
	lpep_pickup_datetime AS longest_distance_pickup_date_less_than_hundred_mile
FROM 
	green_tripdata
WHERE
	trip_distance < 100
ORDER BY
	trip_distance DESC
LIMIT 1