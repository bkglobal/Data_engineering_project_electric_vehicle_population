{{
    config(
        materialized="table",
        alias="T_Vehicle_Electric_Utility"
    )
}}

with STG_DATA as (
    select * from {{ source("ev_population", "stg_ev_population_data") }}
)

SELECT 
    electric_utility as electric_utility,
    COUNT(*) AS eu_count
FROM STG_DATA
GROUP BY electric_utility
ORDER BY eu_count DESC
LIMIT 20