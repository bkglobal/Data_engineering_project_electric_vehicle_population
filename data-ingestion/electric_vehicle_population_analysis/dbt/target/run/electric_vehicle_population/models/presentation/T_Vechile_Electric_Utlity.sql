
  
    

  create  table "ev_population_db"."ev_population"."T_Vehicle_Electric_Utility__dbt_tmp"
  
  
    as
  
  (
    

with STG_DATA as (
    select * from "ev_population_db"."ev_population"."stg_ev_population_data"
)

SELECT 
    electric_utility as electric_utility,
    COUNT(*) AS eu_count
FROM STG_DATA
GROUP BY electric_utility
ORDER BY eu_count DESC
LIMIT 20
  );
  