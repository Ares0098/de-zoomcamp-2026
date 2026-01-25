SELECT 
	COUNT(trip_distance) AS trip_distance_less_than_a_mile
FROM 
	green_tripdata
WHERE
	(lpep_pickup_datetime >= '2025-11-01' AND lpep_pickup_datetime < '2025-12-01') AND
	trip_distance <= 1
