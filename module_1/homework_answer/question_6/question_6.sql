SELECT
	do_tzl.zone AS drop_off_zone,
	gt.tip_amount
FROM
	green_tripdata gt
LEFT JOIN
	taxi_zone_lookup pu_tzl ON gt.pulocationid = pu_tzl.locationid
LEFT JOIN
	taxi_zone_lookup do_tzl ON gt.dolocationid = do_tzl.locationid
WHERE
	(gt.lpep_pickup_datetime >= TIMESTAMP '2025-11-01 00:00:00' AND gt.lpep_pickup_datetime <  TIMESTAMP '2025-12-01 00:00:00') AND
	pu_tzl.zone = 'East Harlem North'
ORDER BY gt.tip_amount DESC