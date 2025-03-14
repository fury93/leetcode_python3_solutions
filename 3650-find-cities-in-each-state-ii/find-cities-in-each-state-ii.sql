# Write your MySQL query statement below
SELECT
  state,
  GROUP_CONCAT(city ORDER BY city ASC separator ', ') AS cities,
  SUM(IF(LEFT(city, 1) = LEFT(state, 1), 1, 0)) AS matching_letter_count
FROM cities
GROUP BY 1
HAVING COUNT(city) > 2 AND matching_letter_count > 0
ORDER BY matching_letter_count DESC, state ASC