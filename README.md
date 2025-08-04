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


docker tag flask-mongo-app-flask-app your-dockerhub-username/flask-mongo-app:latest

docker push your-dockerhub-username/flask-mongo-app:latest

minikube start --driver=docker
minikube ssh -n minikube

eval $(minikube docker-env)   # This switches Docker context to Minikube's internal one

# Rebuild your image inside Minikube

docker build -t flask-mongo-app:latest .

kubectl apply -f mongo-deployment.yaml             
kubectl apply -f mongo-service.yaml

kubectl apply -f flask-deployment.yaml         
kubectl apply -f flask-service.yaml

minikube service flask-service

kubectl logs <your-flask-pod-name>

minikube service flask-service

kubectl delete deployment flask-app
kubectl delete deployment mongo

kubectl get pods, services, deployments

minikube start --nodes 3 --driver=docker

minikube ssh -n minikube         # Master
minikube ssh -n minikube-m02     # Agent 1

how to work with argoCD
$ kubectl create namespace argocd
$ kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
$ kubectl get pods -n argocd
$ kubectl port-forward svc/argocd-server -n argocd 8080:443 for local 
$get password
$ kubectl get secret argocd-initial-admin-secret -n argocd -o yaml  
$ decode password  echo OXFzOTQwSzNFZVlWWmJjVw== | base64 --decode
$ user name admin   9qs940K3EeYVZbcW

==================================== Setup Kubernetes using eksctl =====================
# Install AWS CLI
Refer--https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
$ sudo su
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
$ apt install unzip,   $ unzip awscliv2.zip
$ sudo ./aws/install
         OR
$ sudo yum remove -y aws-cli
$ pip3 install --user awscli
$ sudo ln -s $HOME/.local/bin/aws /usr/bin/aws
$ aws --version

# Installing kubectl
Refer--https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
$ sudo su
$ curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.1/2023-04-19/bin/linux/amd64/kubectl
$ ll , $ chmod +x ./kubectl  //Gave executable permisions
$ mv kubectl /bin   //Because all our executable files are in /bin
$ kubectl version --output=yaml

# Installing  eksctl 
Refer--https://github.com/eksctl-io/eksctl/blob/main/README.md#installation
$ curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
$ cd /tmp
$ ll
$ sudo mv /tmp/eksctl /bin
$ eksctl version

# Setup Kubernetes using eksctl
Refer--https://github.com/aws-samples/eks-workshop/issues/734
eksctl create cluster --name virtualtechbox-cluster \
--region ap-south-1 \
--node-type t2.small \
--nodes 3 \

================================ ArgoCD Installation ==============================================
$ kubectl create namespace argocd
$ kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
$ kubectl get pods -n argocd
$ curl --silent --location -o /usr/local/bin/argocd https://github.com/argoproj/argo-cd/releases/download/v2.4.7/argocd-linux-amd64
$ chmod +x /usr/local/bin/argocd
$ kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
$ kubectl get svc -n argocd
$ kubectl get secret argocd-initial-admin-secret -n argocd -o yaml
$ echo XXXXXXX | base64 --decode

=============================== Add EKS Cluster to ArgoCD ========================================
kubectl port-forward svc/argocd-server -n argocd 8080:443
argocd login localhost:8080 --username admin --password 9qs940K3EeYVZbcW --insecure

$ argocd login a2255bb2bb33f438d9addf8840d294c5-785887595.ap-south-1.elb.amazonaws.com --username admin
argocd login <ARGOCD_SERVER> --username admin --password <ADMIN_PASSWORD> --insecure
argocd login localhost:8080 --username admin --password 9qs940K3EeYVZbcW --insecure

$ argocd cluster list
$ kubectl config get-contexts
$ argocd cluster add i-08b9d0ff0409f48e7@virtualtechbox-cluster.ap-south-1.eksctl.io --name virtualtechbox-eks-cluster


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

---

### **Beginner Level Projects**

### 1. **Simple To-Do App**

**Description:** Build a CRUD (Create, Read, Update, Delete) app where users can manage tasks.

* Create tasks with title and description.
* Store and retrieve them from MongoDB.
* Add routes for:

  * `GET /tasks` (list all tasks)
  * `POST /tasks` (create a task)
  * `PUT /tasks/<id>` (update a task)
  * `DELETE /tasks/<id>` (delete a task)
* Use **Postman** to test the API.

---

### 2. **User Registration API**

**Description:** Build an API for user signup with basic validation.

* Fields: `name`, `email`, `password`
* Hash passwords before storing (use `werkzeug.security`)
* Store in MongoDB
* Add route to get all users (excluding password)

---

### **Intermediate Level Projects**

### 3. **Blog Platform Backend**

**Description:** Backend API for a blogging system.

* Models: `User`, `Post`, `Comment`
* Features:

  * Users can create posts.
  * Users can comment on any post.
* Endpoints:

  * `/posts` → Get all posts
  * `/posts/<id>` → Get a single post with comments
  * `/posts` (POST) → Add new post
  * `/posts/<id>/comment` → Add comment

---

### 4. **Authentication System with JWT**

**Description:** Secure a Flask + MongoDB app with **JWT authentication**.

* Routes:

  * `/register` (save user)
  * `/login` (return token)
  * `/profile` (protected route)
* Use:

  * `PyJWT` or `flask-jwt-extended`
  * Password hashing

---

### 5. **Product Catalog API**

**Description:** Create an API for managing product listings.

* Product fields: `name`, `price`, `description`, `category`
* MongoDB collections: `products`, `categories`
* Add filtering route: `/products?category=shoes&min_price=100`
* Add pagination to `/products` route

---

### **Advanced Level Projects**

### 6. **Flask + MongoDB + Docker Compose Project**

**Description:** Containerize a Flask API app with MongoDB using `docker-compose`.

* Build the app from a Dockerfile.
* Define services in `docker-compose.yml`:

  * `web`: Flask app
  * `db`: MongoDB
* Connect Flask to MongoDB via container hostname.
* Use a volume to persist MongoDB data.
* Add healthcheck.

---

### 7. **Real-Time Chat App (Flask + Socket.IO + MongoDB)**

**Description:** A chat API where messages are stored in MongoDB.

* Flask with `flask-socketio`
* Users can join rooms and send messages
* Store chat history in MongoDB
* Emit new messages in real time
* Add REST API to fetch chat history

---

### 8. **Flask Admin Dashboard with MongoDB**

**Description:** Build a basic admin dashboard with:

* User login (with admin role)
* Add/view/delete products
* View orders (saved in MongoDB)
* Filter by status (Pending, Delivered)
* Optional: Add frontend with Bootstrap
---
## 🧠 Bonus: Add-ons for All Projects

* Use `Marshmallow` or `pydantic` for data validation.
* Use `dotenv` for storing sensitive info.
* Add Swagger UI for API docs (`flasgger`).
* Add unit tests with `pytest` and `mongomock`.
---


