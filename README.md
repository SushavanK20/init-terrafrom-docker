# 🇮🇳 init-terrafrom-docker

A Python Flask application demonstrating a complete local DevOps workflow using **Flask, Pytest, Docker, Terraform, Git, and GitHub Actions**.

The project uses Terraform to manage the Docker image and container, while GitHub Actions automates CI and CD.

---

## 🏗️ Architecture

```text
                    Developer
                        │
                        ▼
                      GitHub
                        │
            ┌───────────┴───────────┐
            │                       │
       release branch            main branch
            │                       │
            ▼                       ▼
           CI                      CD
            │                       │
     ┌──────┴──────┐                │
     │             │                │
 Python Tests  Terraform           │
               Validation          │
               + Plan              │
     │             │                │
     └──────┬──────┘                │
            │                       │
           PASS                     │
            │                       │
            └──── PR ────► Merge ──┘
                                    │
                                    ▼
                              Terraform
                                    │
                                    ▼
                              Docker Provider
                               │          │
                               ▼          ▼
                         Docker Image  Container
                               │          │
                               └────┬─────┘
                                    ▼
                              Flask :5000
```

---

## 🛠️ Technology Stack

| Category               | Technology      |
| ---------------------- | --------------- |
| Language               | Python 3.12     |
| Web Framework          | Flask 3.1.2     |
| Testing                | Pytest          |
| Containerization       | Docker          |
| Infrastructure as Code | Terraform       |
| Terraform Provider     | Docker Provider |
| CI/CD                  | GitHub Actions  |
| Version Control        | Git / GitHub    |

---

## 📁 Project Structure

```text
init-terrafrom-docker/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── tests/
│   └── test_app.py
│
├── terraform/
│   └── main.tf
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
│
├── Dockerfile
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

---

# 🌐 Flask Application

The application is a simple India-themed Flask web application.

## Endpoints

### Home

```text
GET /
```

Displays the application landing page.

### Health Check

```text
GET /health
```

Example response:

```json
{
    "status": "healthy",
    "service": "india-devops-platform"
}
```

### Application Status

```text
GET /api/status
```

Example response:

```json
{
    "application": "init-terrafrom-docker",
    "environment": "local",
    "version": "1.0.0",
    "status": "running"
}
```

---

# 🐍 Run Flask Locally

Create a virtual environment:

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the application:

```powershell
python run.py
```

Open:

```text
http://localhost:5000
```

Health endpoint:

```text
http://localhost:5000/health
```

---

# 🧪 Testing

The project uses Pytest for automated testing.

Run:

```powershell
python -m pytest
```

Current tests cover:

* Home page
* Health endpoint
* Application status endpoint

Example:

```text
3 passed
```

---

# 🐳 Docker

The application is containerized using Docker.

## Build Image

```powershell
docker build -t india-devops-platform:1.0.0 .
```

## Run Container

```powershell
docker run -d `
  --name india-devops-platform `
  -p 5000:5000 `
  india-devops-platform:1.0.0
```

Application:

```text
http://localhost:5000
```

## Check Container

```powershell
docker ps
```

## View Logs

```powershell
docker logs india-devops-platform
```

## Stop Container

```powershell
docker stop india-devops-platform
```

## Remove Container

```powershell
docker rm india-devops-platform
```

---

# 🏗️ Terraform

Terraform manages the Docker infrastructure.

The current Terraform configuration uses the:

```text
kreuzwerker/docker
```

provider.

Terraform manages:

```text
Docker Image
     │
     ▼
Docker Container
     │
     ▼
Flask Application
```

---

## Terraform Commands

Navigate to the Terraform directory:

```powershell
cd terraform
```

Initialize Terraform:

```powershell
terraform init
```

Format configuration:

```powershell
terraform fmt
```

Validate configuration:

```powershell
terraform validate
```

Create an execution plan:

```powershell
terraform plan
```

Apply infrastructure:

```powershell
terraform apply
```

Destroy infrastructure:

```powershell
terraform destroy
```

Return to project root:

```powershell
cd ..
```

---

# 🔄 Terraform Deployment

Terraform is responsible for creating the Docker image and Docker container.

```text
terraform apply
       │
       ▼
Docker Provider
       │
       ├── Create Docker Image
       │
       └── Create Docker Container
                    │
                    ▼
              Flask :5000
```

The Docker image is built from the project's Dockerfile using the project root as the build context.

---

# ⚙️ CI/CD

GitHub Actions is used to automate the development and deployment workflow.

The current branch strategy is:

```text
feature/*
     │
     ▼
Pull Request
     │
     ▼
release
     │
     ▼
CI
     │
     ▼
Pull Request
     │
     ▼
main
     │
     ▼
CD
```

---

# ✅ Continuous Integration

CI runs when code is pushed to the `release` branch.

```text
Push → release
       │
       ▼
GitHub Actions
       │
       ├── Checkout code
       │
       ├── Setup Python
       │
       ├── Install dependencies
       │
       ├── Run Pytest
       │
       ├── Terraform fmt -check
       │
       ├── Terraform init
       │
       ├── Terraform validate
       │
       └── Terraform plan
```

### CI validates

* Python application tests
* Terraform formatting
* Terraform initialization
* Terraform configuration
* Terraform execution plan

CI must pass before changes are promoted toward `main`.

---

# 🚀 Continuous Deployment

CD runs when changes are merged into the `main` branch.

The current CD workflow uses Terraform to deploy the Docker infrastructure.

```text
Merge → main
     │
     ▼
GitHub Actions
     │
     ├── Checkout code
     │
     ├── Check Docker
     │
     ├── Setup Terraform
     │
     ├── Terraform init
     │
     ├── Terraform validate
     │
     ├── Terraform plan
     │
     ├── Terraform apply
     │
     ├── Verify Docker container
     │
     └── Test /health
```

Terraform performs the actual Docker deployment:

```text
GitHub Actions
      │
      ▼
terraform apply
      │
      ▼
Docker Provider
      │
      ├──────────────┐
      ▼              ▼
Docker Image    Docker Container
                     │
                     ▼
                Flask App
                     │
                     ▼
                Port 5000
```

---

# 🔐 Current Workflow

The complete workflow implemented so far is:

```text
Developer
    │
    ▼
feature/*
    │
    ▼
Pull Request
    │
    ▼
release
    │
    ▼
CI
 ├── Pytest
 ├── Terraform fmt
 ├── Terraform init
 ├── Terraform validate
 └── Terraform plan
    │
    ▼
Pull Request
    │
    ▼
main
    │
    ▼
CD
 ├── Terraform init
 ├── Terraform validate
 ├── Terraform plan
 └── Terraform apply
    │
    ▼
Docker Image
    │
    ▼
Docker Container
    │
    ▼
Flask Application
```

---

# 📊 Project Status

| Component                   | Status        |
| --------------------------- | ------------- |
| Flask Application           | ✅ Complete    |
| India-themed UI             | ✅ Complete    |
| Health API                  | ✅ Complete    |
| Status API                  | ✅ Complete    |
| Pytest                      | ✅ Complete    |
| Dockerfile                  | ✅ Complete    |
| Docker Image                | ✅ Complete    |
| Docker Container            | ✅ Complete    |
| Terraform Docker Provider   | ✅ Complete    |
| Terraform Validation        | ✅ Complete    |
| Terraform Plan              | ✅ Complete    |
| Git Repository              | ✅ Complete    |
| GitHub Repository           | ✅ Complete    |
| GitHub Actions CI           | ✅ Complete    |
| GitHub Actions CD           | ✅ Complete    |
| Terraform Docker Deployment | ✅ Implemented |

---

# 🎯 DevOps Workflow

The project currently demonstrates:

```text
SOURCE CONTROL
      ↓
    GitHub
      ↓
CONTINUOUS INTEGRATION
      ↓
Python Tests
      ↓
Terraform Validation
      ↓
Terraform Plan
      ↓
CONTINUOUS DEPLOYMENT
      ↓
Terraform Apply
      ↓
Docker Image
      ↓
Docker Container
      ↓
Flask Application
```

This provides a complete working **local DevOps CI/CD workflow** using Python, Docker, Terraform, and GitHub Actions.

```

This version documents **only what we've actually built so far** and removes the future-scope sections.
```
