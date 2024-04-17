

with STG_DATA as (
    select * from "ev_population_db"."ev_population"."stg_ev_population_data"
)

SELECT 
    make,
    COUNT(*) AS make_count
FROM STG_DATA
GROUP BY make