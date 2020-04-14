# temperature_gauge
This coding exercise exposes a GraphQL interface
to a mock temperature sensor backed by a random number generator. Queries are
served over http and subscriptions are served over websockets.

This project uses the Django web framework with
graphene-django and graphene-subscriptions for the GraphQL implementation.

## Schema
```gql
schema {
  query: Query
  subscription: Subscription
}

type Query {
  currentTemperature(unit: TemperatureUnit): TemperatureReadingGQLType
}

type Subscription {
  currentTemperatureSubscribe(unit: TemperatureUnit): TemperatureReadingGQLType
}

type TemperatureReadingGQLType {
  timestamp: Float
  value: Float
  unit: TemperatureUnit
}

enum TemperatureUnit {
  CELSIUS
  KELVIN
  FAHRENHEIT
}
```
## Running queries
### Setup
Build the docker image. In the root of the project where the Dockerfile
and docker-compose.yml file live:
```shell script
docker-compose build
docker-compose up
```
The service will now be running on port 8000. Navigate to [http://localhost:8000/graphql/]()
to access the graphiql playground.
### Executing a query
In the [graphiql playground](http://localhost:8000/graphql/) or any other client
issue a query such as
```gql
query
{
    currentTemperature
    {
        timestamp
        value
        unit
    }
}
```
### Executing a subscription
The graphiql playground does not support subscriptions. You will need to use
a client such as [graphqurl](https://github.com/hasura/graphqurl) to test
subscriptions. The server uses websockets for the network layer for subscriptions.

Once you have a client configured, try issuing the following query:
```gql
subscription
{
    currentTemperatureSubscribe
    {
        temperature
        {
            timestamp
            value
            unit
        }
    }
}
```
## Development and testing
For development, you'll want to setup a python virtual environment.
In the project root where the requirements.txt file lives:
```shell script
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
The python base directory is in `$PROJECTROOT/temperature_gauge` where `manage.py` lives.
```shell script
cd temperature_gauge
```
### Running tests
```shell script
pytest
```
### Running the server without docker:
```shell script
./manage.py runserver
```
### Generate the GraphQL schema to share with client developers
Graphene-django, helpfully, has a management command to produce and format the
schema.
```shell script
./manage.py graphql_schema --schema temperature_gauge.schema.schema --out=schema.graphql -v 0
```
