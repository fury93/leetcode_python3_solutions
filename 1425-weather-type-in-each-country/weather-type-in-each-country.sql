# Write your MySQL query statement below
SELECT a.country_name,
CASE WHEN AVG(weather_state)<=15 THEN "Cold"
WHEN AVG(weather_state)>=25 THEN "Hot"
ELSE "Warm" END as weather_type FROM Countries as a
JOIN Weather as b
ON a.country_id=b.country_id
WHERE b.day BETWEEN "2019-11-01" AND "2019-11-30"
GROUP BY a.country_id;