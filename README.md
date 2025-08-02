docker ps,images, volume ls, network ls

docker network create flask-mongo-net

docker network connect flask-mongo-net 2642e063914d

docker-compose up -d --build

docker exec -it 2642e063914d mongosh

show dbs           // list all databases

use testdb         // switch to your DB (used in your Flask app)

show collections   // list collections

db.items.find()    // show documents in "items" collection

docker inspect d47eecb34216

docker inspect 2642e063914d | grep -i "NetworkMode"

docker exec -it d47eecb34216 sh

environment:
  - MONGO_URI=${MONGO_URI}

If we want to chang the code 
docker-compose build        # Rebuild image from Dockerfile
docker-compose down         # Stop and remove old containers
docker-compose up -d        # Start with updated containers

1. **Check Docker version installed on your system.**
   * What command do you use?
2. **List all Docker containers (running and stopped).**
3. **Start a new Ubuntu container in interactive mode.**

   * Make sure it opens a terminal inside the container.
4. **Check the logs of a running container.**
5. **List all Docker images on your system.**
6. **Pull the latest version of the `nginx` image.**
7. **Remove a stopped container.**
8. **Remove an unused image.**
9. **Run a container in the background and expose port 80.**
10. **Check running container stats in real time.**

11. **Create a Dockerfile for a simple Node.js or Python app. Build the image and run it.**
12. **Run a container with a mounted volume to persist data.**
13. **Inspect the details (IP, env variables) of a running container.**
14. **Tag an image and push it to Docker Hub.**
15. **Restart a stopped container.**
16. **Execute a command inside a running container (e.g., `ls`, `top`, `ps aux`).**
17. **Create and use a Docker bridge network to connect two containers.**
18. **Use environment variables in Docker when starting a container.**
19. **Build an image using a custom Dockerfile and assign a specific tag.**
20. **Run a container that auto-removes itself after stopping.**


21. **Write a `docker-compose.yml` file for a multi-container app (e.g., Node.js + MongoDB).**
22. **Use Docker volumes to share data between multiple containers.**
23. **Limit CPU and memory usage of a container.**
24. **Create a custom user and run the container with it.**
25. **Bind mount your local code to the container and live-edit.**
26. **Build and run a multi-stage Dockerfile.**
27. **Clean up all stopped containers, unused networks, dangling images with one command.**
28. **Scan your Docker image for vulnerabilities using `docker scan`.**
29. **Check container health using `HEALTHCHECK` in Dockerfile.**
30. **Use `docker save` and `docker load` to move an image to another system.**
.
