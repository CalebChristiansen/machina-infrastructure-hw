#!/bin/bash

# Step 1: Delete specific Kubernetes deployments
echo "Deleting project-specific Kubernetes deployments..."
kubectl delete deployment hello-broadcaster-deployment
kubectl delete deployment hello-receiver-deployment
kubectl delete deployment web-service-deployment

# Step 2: Delete specific Kubernetes services
echo "Deleting project-specific Kubernetes services..."
kubectl delete service hello-receiver-service
kubectl delete service web-service-service

# Step 3: Optionally stop Minikube (commented out by default)
# echo "Stopping Minikube..."
# minikube stop

# Step 4: Optionally delete Minikube cluster (commented out by default)
# echo "Deleting Minikube cluster..."
# minikube delete

# Step 5: Reset Docker environment (optional, only if Minikube was stopped)
# echo "Resetting Docker environment..."
# eval $(minikube -p minikube docker-env -u)

echo "Teardown complete."
