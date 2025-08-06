# Student-Enrollment-System

# IMPORTANT COST WARNING
* Using managed Kubernetes services like **AWS EKS**, **Google GKE**, or **Azure AKS** typically **incurs costs** beyond the free tier (e.g., EKS control plane costs ~$0.10/hour + worker node costs).
* You can build this app **locally and for free** using Minikube or Docker Desktop.

## Instructions for setting up the local Kubernetes environment (Minikube or Docker Desktop).
* Install **Minikube** ([Installation Guide](https://minikube.sigs.k8s.io/docs/start/)). For consistency, we recommend using Minikube with the Docker driver for this assignment. Alternatively, Docker Desktop's Kubernetes can be used.
    Example start command: `$ minikube start --driver=docker`
* **`kubectl`**: Install the Kubernetes command-line tool ([Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)).
* **Helm**: Install Helm v3+ ([Installation Guide](https://helm.sh/docs/intro/install/)).

## Instructions on how to add the required health check endpoint to the Django application if not already present.

In your `myapp/views.py`, you could add:
```python
      from rest_framework.views import APIView
      from rest_framework.response import Response
      from rest_framework import status
      class HealthCheckView(APIView):
          def get(self, request, *args, **kwargs):
              return Response({"status": "ok"}, status=status.HTTP_200_OK)
```
    
And in your `myapp/urls.py` (or project `urls.py` under an API path):
```python
      from django.urls import path
      from .views import HealthCheckView # Assuming HealthCheckView is in the same views.py
      urlpatterns = [
          # ... other urls
          path('health/', HealthCheckView.as_view(), name='health_check'),
      ]
```            

## Instructions for creating necessary secrets using `kubectl create secret --from-env-file`

Create local files (e.g., `k8s-app-secrets.env`, `k8s-pg-secrets.env`) specifically for Kubernetes secrets. **Crucially, update the database host in the `DATABASE_URL` within `k8s-app-secrets.env` to match the Kubernetes service name you will create for Postgres** (e.g., `postgres-service` or `postgres-service.default.svc.cluster.local` if using default namespace).
```dotenv
    # k8s-pg-secrets.env (Example for creating K8s postgres-secret)
    POSTGRES_PASSWORD=your_actual_db_password
```
```dotenv
    # k8s-app-secrets.env (Example for creating K8s app-secret)
    SECRET_KEY=your_production_django_secret_key_here
    DATABASE_URL=postgres://your_db_user:your_actual_db_password@postgres-service:5432/your_db_name 
    GOOGLE_CLIENT_ID=your_google_client_id
    GOOGLE_CLIENT_SECRET=your_google_client_secret
```

## Guidance on local image management for Minikube

```bash
    minikube start # Or ensure Kubernetes is enabled in Docker Desktop
    # If using Minikube & a local Docker image (not ECR), ensure Minikube's Docker daemon can see it:
    # Option A: Build with Minikube's Docker daemon: eval $(minikube -p minikube docker-env) && docker build -t your-local-image-name:latest .
    # Option B: Load an existing image into Minikube: minikube image load your-local-image-name:latest
```

## The command(s) to apply all Kubernetes manifests

```bash
    # Apply deployments, services, configmaps, pvcs etc.
    kubectl apply -f k8s/postgres-pvc.yaml -f k8s/postgres-deployment.yaml -f k8s/postgres-service.yaml -f k8s/app-configmap.yaml -f k8s/app-deployment.yaml -f k8s/app-service.yaml
    # Expected output: pvc created, deployment created, service created, configmap created...
```

## Helm commands used to install the `kube-prometheus-stack`

```bash
    helm repo add prometheus-community [https://prometheus-community.github.io/helm-charts](https://prometheus-community.github.io/helm-charts)
    helm repo update
```
```bash
    # Example using version 75.15.1 (replace with the latest stable version found on ArtifactHub for kube-prometheus-stack):
    helm install prom-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --version 75.15.1 
```

## Instructions on how to access the deployed application

**If using Minikube with NodePort**: Get the URL.
```bash
        minikube service app-service --url
        # Open the printed URL in your browser
```
**If using Docker Desktop (or other LoadBalancer provider)**: The `EXTERNAL-IP` for `app-service` might show `localhost` or an IP.
```bash
        kubectl get svc app-service
        # Access via http://localhost:80 (if EXTERNAL-IP is localhost and port is 80)
```
**Fallback using port-forwarding (works for any service type)**:
```bash
        # Forward local port 8000 to the service's port 80
        kubectl port-forward service/app-service 8000:80
        # Access via http://localhost:8000
```
            
## Instructions on how to access Grafana
* The Grafana service is typically named `<release-name>-grafana` (e.g., `prom-stack-grafana`). Find the exact name:
```bash
        kubectl get svc -n monitoring
```
* Get the default admin password (stored in a secret):
```bash
        kubectl get secret --namespace monitoring prom-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```
* Port-forward to the Grafana service (usually runs on port 80 or 3000 inside the cluster):
```bash
        # Forward local port 3000 to the Grafana service's port (assuming it's 80)
        kubectl port-forward --namespace monitoring svc/prom-stack-grafana 3000:80
```
* Open `http://localhost:3000` in your browser.
* Log in with username `admin` and the password retrieved above.

## Command to run database migrations
`$ kubectl exec <your-app-pod-name-here> -- python manage.py migrate`

## Commands used to demonstrate scaling and rolling updates.
**Scale Deployment**: Increase the number of replicas for your web application.
```bash
    kubectl scale deployment app-deployment --replicas=3
    kubectl get pods # Observe new pods being created
```
**Perform Rolling Update** (Simulated):
* Edit your `k8s/app-deployment.yaml` file. Change the `image:` tag to a different (even non-existent) tag, e.g., `:v2`.
* Apply the change:
```bash
        kubectl apply -f k8s/app-deployment.yaml
```
* Watch the rollout status:
```bash
        kubectl rollout status deployment/app-deployment
        # Observe pods terminating and new ones attempting to start
        kubectl get pods
```
* *(Roll back if needed: `kubectl rollout undo deployment/app-deployment`)*


# Screenshots
Screenshot showing the output of `kubectl get pods -n default`
<img width="1036" height="85" alt="image" src="https://github.com/user-attachments/assets/7272797a-3538-4eb4-9169-057f9dfcc0a3" />
Screenshot showing the application's health check endpoint
<img width="841" height="578" alt="image" src="https://github.com/user-attachments/assets/d48335b7-bc3d-40d7-b623-a91b62c7da69" />
Screenshot showing the output of `kubectl get pods -n monitoring`
<img width="1092" height="139" alt="image" src="https://github.com/user-attachments/assets/3ebfa9db-c274-451d-842e-58b03514f953" />
Screenshot of a Grafana dashboard
<img width="2232" height="821" alt="image" src="https://github.com/user-attachments/assets/beb22bd7-edda-4c23-a26e-b4051c69baa3" />

