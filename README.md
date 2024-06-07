# Infrastructure HW

## Project Overview

This project sets up an infrastructure for a small application with the following services:
1. **Hello Broadcaster Service**: Broadcasts "Hello world" at random intervals between 1 to 10 seconds.
2. **Hello Receiver Service**: Receives and stores "Hello world" broadcasts along with their timestamps.
3. **Web Service**: Displays the received "Hello world" broadcasts in a web browser, with the newest messages at the top.

The solution uses Docker to containerize the services and Minikube to orchestrate them locally. It has been tested on a Windows 11 machine using git bash.

## Prerequisites

- Docker
- Minikube
- kubectl

## Setup Instructions

### Automated Setup

To set up the infrastructure automatically, you can use the provided `setup.sh` script.

1. **Run the Setup Script**

    ```sh
    ./setup.sh
    ```

This script will:
1. Start Minikube.
2. Set up Minikube Docker environment.
3. Build Docker images.
4. Tag Docker images.
5. Apply Kubernetes configurations.
6. Access the web service and provide the URL.

### Teardown Instructions

To clean up the environment automatically, you can use the provided `teardown.sh` script.

1. **Run the Teardown Script**

    ```sh
    ./teardown.sh
    ```

This script will:
1. Delete project-specific Kubernetes deployments.
2. Delete project-specific Kubernetes services.
3. Optionally stop Minikube (commented out by default).
4. Optionally delete the Minikube cluster (commented out by default).
5. Optionally reset the Docker environment (commented out by default).

### Manual Setup

#### Step 1: Start Minikube

Start Minikube to create a local Kubernetes cluster:

```sh
minikube start
```

#### Step 2: Set Up Minikube Docker Environment

Configure your shell to use Minikube's Docker daemon:

```sh
eval $(minikube -p minikube docker-env)
```

#### Step 3: Build Docker Images

Navigate to the project directory where `docker-compose.yml` is located and build the Docker images

```sh
docker-compose build
```

#### Step 4: Tag Docker Images

Tag the Docker images correctly:

```sh
docker tag machina-infrastructure-hw-broadcaster-service:latest hello_broadcaster:latest
docker tag machina-infrastructure-hw-receiver-service:latest hello_receiver:latest
docker tag machina-infrastructure-hw-web-service:latest web_service:latest
```

#### Step 5: Apply Kubernetes Configurations

Apply the Kubernetes configuration files to deploy the services:

```sh
kubectl apply -f k8s/
```

#### Step 6: Access the Web Service

Get the URL to access the web service using Minikube:

```sh
minikube service web-service-service
```

Open the provided URL in a web browser to see the "Hello world" broadcasts.