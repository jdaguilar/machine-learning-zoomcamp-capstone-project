# Machine Learning Zoomcamp Capstone Project

## Overview

An important financial service company, based on German, is trying to grow up the credit portfolio. They're find out many people are interested in acquire a credit with them. However, there are some bottlenecks in their process, becoming it slow and inefficient. The company has decided to make an investment in infrastructure to digitalize many of the process they made since a credit is requested until it's given to the client.

The goal is build a service able to predict how risky is a client, to help sales representatives to make a choice to give a credit or not.

## EDA

You can find EDA in the `EDA/` directory.

It was explored relationship between target variables and the numerical and categorical features, and correlations between variables.

## Model Training

Due to it's a classification problem, training was made with some of the most common classification models.

In this problem, It's really important to optimize recall, that's we want to avoid people with "Bad" creditability may be classified as "Good".

Logistic Regression was chosen.

## Deployment

## How to reproduce

### Install Kubectl

To install kubectl, follow steps described [here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/):

### Install Minikube

To install Minikube, follow steps described [here](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download):

Start Minikube with the following command:

```sh
minikube start
```

Verify that Minikube is running.

```sh
minikube status
```

Once Minikube is installed and running, you can proceed with the following commands to build and deploy your application.

### Deploy Churn App in Minikube

To deploy the Churn App in Minikube, we have to follow these steps:

1. Set the docker-daemon from Minikube:

```sh
eval $(minikube -p minikube docker-env)
```

2. Build Docker Image:

```sh
docker build -t churn-app:1.0.0 .
```

3. Apply Kubernetes Manifest:

```sh
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

4. Verify Deployment:

```sh
kubectl get pods
kubectl get services
```

5. Find the Node IP:

```sh
kubectl get nodes -o wide
```

Example Output:
```
NAME           STATUS   ROLES                  AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION     CONTAINER-RUNTIME
minikube       Ready    control-plane,master   10d   v1.20.2   192.168.49.2   <none>        Ubuntu 20.04.1 LTS   5.4.0-58-generic   docker://20.10.2
```

In this example, the Node IP is `192.168.49.2`.

The `NodePort` for the churn-app-service is `30007`, so you can access your application through the following link:

```sh
http://192.168.49.2:30007
```
