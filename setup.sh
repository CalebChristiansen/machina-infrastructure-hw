#!/bin/bash

# Step 1: Start Minikube
echo "Starting Minikube..."
minikube start

# Step 2: Set Up Minikube Docker Environment
echo "Setting up Minikube Docker environment..."
eval $(minikube -p minikube docker-env)

# Step 3: Build Docker Images
echo "Building Docker images..."
docker-compose build

# Step 4: Tag Docker Images
echo "Tagging Docker images..."
docker tag machina-infrastructure-hw-broadcaster-service:latest hello_broadcaster:latest
docker tag machina-infrastructure-hw-receiver-service:latest hello_receiver:latest
docker tag machina-infrastructure-hw-web-service:latest web_service:latest

# Step 5: Apply Kubernetes Configurations
echo "Applying Kubernetes configurations..."
kubectl apply -f k8s/

# Step 6: Wait for the Pods to be Ready
echo "Waiting for pods to be ready..."
while [[ $(kubectl get pods -l app=web-service -o 'jsonpath={..status.conditions[?(@.type=="Ready")].status}') != "True" ]]; do
  echo "Waiting for web-service pod to be ready (this will take a moment)..." && sleep 5
done

# Step 7: Access the Web Service
echo "Accessing the web service..."
minikube service web-service-service

echo "Setup complete. Open the provided URL in a web browser to see the 'Hello world' broadcasts."
