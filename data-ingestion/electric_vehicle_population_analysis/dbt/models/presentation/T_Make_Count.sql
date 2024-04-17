{{
    config(
        materialized="table",
        alias="T_Make_Count"
    )
}}

with STG_DATA as (
    select * from {{ source("ev_population", "stg_ev_population_data") }}
)

SELECT 
    make,
    COUNT(*) AS make_count
FROM STG_DATA
GROUP BY make
