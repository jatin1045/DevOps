# Flask Web App with Automated CI/CD Pipeline on AWS EC2

This project demonstrates a simple CI/CD pipeline using Jenkins to build a Docker image of a Flask app,
transfer the image to an AWS EC2 instance via SCP, and deploy it there by loading the image and running a container.

## Contents
- `app.py` - simple Flask app
- `requirements.txt` - Python deps
- `Dockerfile` - builds the Flask app image
- `Jenkinsfile` - Declarative Jenkins pipeline to build, save, transfer and trigger deploy on EC2
- `deploy/deploy_ec2.sh` - script that runs on EC2 to load image and run container
- `README.md` - this file

## Prerequisites
- AWS EC2 instance (Ubuntu 20.04+) with Docker installed and user in `docker` group or using `sudo` for docker
- SSH access to EC2 via key pair
- Jenkins server with:
  - Docker CLI available (either Jenkins host has Docker or use Docker-in-Docker)
  - Credentials configured:
    - `ec2_user` (Username string, e.g., ubuntu)
    - `ec2_host` (Host/IP string)
    - `ec2_ssh_key` (SSH private key, store as "Secret file" in Jenkins credentials)
  - Optional: Docker registry credentials if you prefer pushing images instead of SCP

## How it works
1. Jenkins builds Docker image and saves it as a tarball.
2. Jenkins SCPs tarball and deploy script to EC2 and SSHs to run the deploy script.
3. EC2 loads the Docker image tar, stops old container, and runs the new container.

## Run locally (for testing)
1. Build image:
   ```bash
   docker build -t flask-app:local .
   ```
2. Run container:
   ```bash
   docker run -d --name flask_app -p 5000:5000 flask-app:local
   ```
3. Visit `http://localhost:5000`

## Notes & Security
- Using SCP and SSH is simple and works well for small deployments, but for larger infra consider using ECR + ECS or Kubernetes.
- Ensure your EC2 security group allows inbound traffic on port 5000 (or use a reverse proxy / load balancer).
- Jenkins needs network access to the EC2 host and the SSH key should be stored securely in Jenkins credentials.
# flask_ec2_cicd
