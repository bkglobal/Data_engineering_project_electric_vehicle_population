
  
    

  create  table "ev_population_db"."ev_population"."T_CAF_Vehicle_Eligibility_Count__dbt_tmp"
  
  
    as
  
  (
    

with STG_DATA as (
    select * from "ev_population_db"."ev_population"."stg_ev_population_data"
)

SELECT 
    clean_alternative_fuel_vehicle_cafv_eligibility as cafv_name,
    COUNT(*) AS cafv_count
FROM STG_DATA
GROUP BY clean_alternative_fuel_vehicle_cafv_eligibility
  );
  