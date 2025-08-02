docker network ls

docker ps

docker network create flask-mongo-net

docker network connect flask-mongo-net 2642e063914d

docker-compose up -d --build

docker exec -it 2642e063914d mongosh

show dbs           // list all databases
use testdb         // switch to your DB (used in your Flask app)
show collections   // list collections
db.items.find()    // show documents in "items" collection
