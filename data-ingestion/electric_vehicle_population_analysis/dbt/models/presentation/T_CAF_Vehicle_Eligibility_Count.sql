{{
    config(
        materialized="table",
        alias="T_CAF_Vehicle_Eligibility_Count"
    )
}}

with STG_DATA as (
    select * from {{ source("ev_population", "stg_ev_population_data") }}
)

SELECT 
    clean_alternative_fuel_vehicle_cafv_eligibility as cafv_name,
    COUNT(*) AS cafv_count
FROM STG_DATA
GROUP BY clean_alternative_fuel_vehicle_cafv_eligibility
