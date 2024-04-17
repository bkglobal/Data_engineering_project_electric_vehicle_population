
  
    

  create  table "ev_population_db"."ev_population"."T_Distribution_By_Country_Count__dbt_tmp"
  
  
    as
  
  (
    

with STG_DATA as (
    select * from "ev_population_db"."ev_population"."stg_ev_population_data"
),
DISTRIBUTION_BY_COUNTRY as (
    SELECT 
        county as country,
        COUNT(*) AS vehicle_count
    FROM STG_DATA
    GROUP BY county
)

SELECT * FROM DISTRIBUTION_BY_COUNTRY
ORDER BY vehicle_count DESC
  );
  