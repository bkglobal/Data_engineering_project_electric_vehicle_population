
  
    

  create  table "ev_population_db"."ev_population"."T_ElectricVehicle_Type__dbt_tmp"
  
  
    as
  
  (
    

with STG_DATA as (
    select * from "ev_population_db"."ev_population"."stg_ev_population_data"
)

SELECT 
    electric_vehicle_type,
    COUNT(*) AS ev_type_count
FROM STG_DATA
GROUP BY electric_vehicle_type
  );
  