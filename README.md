# Redis_K8S
This repo will build and deploy Redis and python service in K8S

Redis deployment:

helm repo add bitnami https://charts.bitnami.com/bitnami

helm repo update

helm install my-redis bitnami/redis