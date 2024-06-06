# Hello World Application

This application broadcasts "Hello world" messages at random intervals and displays them on a web interface in real-time.

## Services

- **Broadcaster**: Sends "Hello world" messages at random intervals.
- **Receiver**: Receives the messages and provides an API to fetch them.
- **Web Interface**: Displays the messages in real-time.

## Setup

### Prerequisites

- Docker
- Minikube
- Kubernetes

### Instructions for Windows

1. Start Minikube:

   ```powershell
   minikube start --driver=docker
   ```

2. Ensure Docker is using the Minikube Docker daemon:

    ```powershell
    & minikube -p minikube docker-env --shell powershell | Invoke-Expression
    ```

3. Build Docker images:

    ```powershell
    docker build -t hello_broadcaster:latest -f broadcaster/Dockerfile broadcaster/
    docker build -t hello_receiver:latest -f receiver/Dockerfile receiver/
    docker build -t web_interface:latest -f web_interface/Dockerfile web_interface/
    ```

4. Apply Kubernetes deployments and services:

    ```powershell
    kubectl apply -f broadcaster/broadcaster-deployment.yaml
    kubectl apply -f receiver/receiver-deployment.yaml
    kubectl apply -f web_interface/web-interface-deployment.yaml

    kubectl apply -f services/broadcaster-service.yaml
    kubectl apply -f services/receiver-service.yaml
    kubectl apply -f services/web-interface-service.yaml

    ```

5. Access the web interface:

    ```powershell
    minikube service web-interface
    ```

    Open the provided URL in your web browser to view the "Hello world" messages in real-time.
