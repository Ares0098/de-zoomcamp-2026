SELECT
	tzl.zone,
	SUM(gt.total_amount) AS total_amount_sum
FROM
	green_tripdata gt
LEFT JOIN
	taxi_zone_lookup tzl
		ON gt.pulocationid = tzl.locationid
WHERE
	gt.lpep_pickup_datetime >= TIMESTAMP '2025-11-18 00:00:00' AND gt.lpep_pickup_datetime <  TIMESTAMP '2025-11-19 00:00:00'
GROUP BY
	tzl.zone
ORDER BY total_amount_sum DESC