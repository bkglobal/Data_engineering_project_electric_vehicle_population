# Electric Vehicle Analysis 

## What is the problem describing here ?

The main problem is the lack of the public awareness to educate people about the benefits of EVs (Electric Vehicles), charging infrastructure and effeciency on price, emission control and lots more advantages.

## Here we solved the problem !!

This analytics reduce the following challanges.
1. *Increase public awareness*: Educate people about the benefits of EVs, such as reduced emissions and lower running costs. This can address range anxiety (fear of running out of battery) and encourage adoption.
2. *Expand charging infrastructure*: Build more charging stations, especially fast-charging stations, to reduce charging time and make long-distance travel with EVs more convenient.
3. *Provide incentives*: Offer tax breaks, rebates, or other financial incentives for purchasing or leasing EVs. This can offset the higher upfront cost compared to traditional gasoline vehicles.
4. *Develop efficient battery technology*: Research and development of batteries with longer range and shorter charging times can significantly improve the practicality of EVs.

By addressing these challenges, we can encourage more people to switch to EVs and reduce reliance on fossil fuels, leading to a cleaner environment.


# Setting up the Project.

## Clone the Project.
```
git@github.com:bkglobal/Data_engineering_project_electric_vehicle_population.git
cd Data_engineering_project_electric_vehicle_population
```

## Setting up environment variables and credentials.
Rename `dev.env` to `.env`
```
mv dev.env .env
```

Add your kaggle credentials to the following variables.
`KAGGLE_USERNAME=<Kaggle_username>`
`KAGGLE_API_TOKEN=<Kaggle_token>`

Add GCP Key file to folder `data-ingestion/gcp_credentials/key.json`


## Run Project

The project containg two parts which needs to run using Docker.

1. Data Ingestion
2. Data Analytics


### Run Data ingestion

It is using Mage with Postgres Database.

Go to Data Ingestion Folder.
```
cd data-ingestion
```

Start the Docker containers using `docker-compose.yml` file:
```
docker compose up
```
For running containers on background
```
docker compose up -d
```




### Run Data Analytics

It is using metabase.

Go to the Data Analytics Folder
```
cd data-analytics
```

Start the Docker containers using `docker-compose.yml` file:
```
docker compose up
```
For running containers on background
```
docker compose up -d
```
