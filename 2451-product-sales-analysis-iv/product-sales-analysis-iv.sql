# Write your MySQL query statement below
SELECT 
    user_id, 
    product_id
FROM (SELECT 
        user_id, 
        product_id, 
        RANK() OVER (
            PARTITION BY user_id 
            ORDER BY SUM(price * quantity) DESC
        ) AS rnk 
      FROM Sales JOIN Product USING (product_id) 
      GROUP BY 1, 2) a 
WHERE rnk = 1