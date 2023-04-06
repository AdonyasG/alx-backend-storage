-- select number of fans
-- 
-- select country by number of fans
-- non unique fans (sum)
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY SUM(fans) DESC;