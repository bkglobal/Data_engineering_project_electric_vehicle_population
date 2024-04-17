To run big query emulator.
docker run -it ghcr.io/goccy/bigquery-emulator:latest --project=test


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
