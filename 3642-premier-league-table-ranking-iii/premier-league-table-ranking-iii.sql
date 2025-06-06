# Write your MySQL query statement below

WITH cte AS (
SELECT 
    season_id,
    team_id,
    team_name,
    (wins*3+draws*1+losses*0) AS points,
    (goals_for - goals_against) AS goal_difference
FROM SeasonStats
)
SELECT 
    *,
    DENSE_RANK()OVER(
        PARTITION BY season_id 
        ORDER BY points DESC, 
        goal_difference DESC, team_name
    )AS position
FROM cte