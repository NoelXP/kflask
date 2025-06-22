# kflask

A minimal Flask application designed for cloud-native deployment on Kubernetes clusters, with a modern CI/CD pipeline using GitHub, Quay, and Flux.

---

## Features
- **Flask** web app (`app.py`)
- **Dockerized** for container builds (`Dockerfile`)
- **Kubernetes manifests** for deployment (`manifests/app/`)
- **Flux** for GitOps-based deployment (`manifests/flux-system/`)
- **Quay** for container image hosting
- **Ingress** for external access (`ingress.yaml`)
---

## File Structure

```
app.py                # Flask application
Dockerfile            # Container build instructions
requirements.txt      # Python dependencies
manifests/
  app/
    deployment.yaml   # Kubernetes Deployment
    service.yaml      # Kubernetes Service
  flux-system/
    gotk-sync.yaml    # Flux sync configuration
    kustomization.yaml# Flux kustomization
application.yaml      # (Optional) App config
ingress.yaml          # Ingress resource
```

---

## Quick Start

### 1. Build and Run Locally
```sh
pip install -r requirements.txt
python app.py
```
App will be available at http://localhost:5000

### 2. Build Docker Image
```sh
docker build -t quay.io/<your-namespace>/kflask:latest .
```

### 3. Push to Quay
```sh
docker push quay.io/<your-namespace>/kflask:latest
```

### 4. Deploy to Kubernetes (with Flux)
- Ensure Flux is installed and configured.
- Update image references in `deployment.yaml` if needed.
- Apply manifests:
```sh
kubectl apply -k manifests/app/
```
- Or let Flux sync from GitHub automatically.

### 5. Access via Ingress
- Update your `/etc/hosts` if using the sample host:
  ```
  127.0.0.1 flask-app.local
  ```
- Visit http://flask-app.local

---

## CI/CD Pipeline

- ✅ **GitHub**: Stores code and manifests
- ✅ **Quay**: Builds and hosts container images
- ✅ **Flux**: Deploys to Kubernetes cluster
- ✅ **Ingress**: Exposes app externally


