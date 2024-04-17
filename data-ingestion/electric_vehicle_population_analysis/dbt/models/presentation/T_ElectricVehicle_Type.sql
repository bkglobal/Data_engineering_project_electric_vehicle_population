{{
    config(
        materialized="table",
        alias="T_ElectricVehicle_Type"
    )
}}

with STG_DATA as (
    select * from {{ source("ev_population", "stg_ev_population_data") }}
)

SELECT 
    electric_vehicle_type,
    COUNT(*) AS ev_type_count
FROM STG_DATA
GROUP BY electric_vehicle_type
