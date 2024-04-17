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



Run Data ingestion Part..

docker compose build

Finally, start the Docker container:
docker compose up

On background..
docker compose up -d


docker run -it ghcr.io/goccy/bigquery-emulator:latest --project=ev_population_bigquery

[bigquery-emulator] REST server listening at 0.0.0.0:9050
[bigquery-emulator] gRPC server listening at 0.0.0.0:9060


 Could not find kaggle.json. Make sure it's located in /root/.kaggle. Or use the environment method.

 
 docker run --name pgadmin-container -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=user@domain.com -e PGADMIN_DEFAULT_PASSWORD=catsarecool -d dpage/pgadmin4
