# My First CI/CD Pipeline: Automated Python App Deployment to AWS EC2 🚀🎖️

> **Welcome! This is my very first CI/CD pipeline project.** I built this to master the core concepts of DevOps, cloud automation, and containerization.

This repository demonstrates a fully automated pipeline that packages a Python application into a Docker container and deploys it instantly to an **AWS EC2 instance** using **GitHub Actions** upon every code push.

---

## 🛠️ Tech Stack & Tools Used
*   **Application Framework:** Python (Flask / Web App)
*   **Containerization:** Docker & Docker Hub
*   **Automation (CI/CD):** GitHub Actions
*   **Cloud Provider:** Amazon Web Services (AWS) EC2
*   **Networking:** AWS Elastic IP (Static IP) & Security Groups

---

## 💻 How to Run and Test This Project Locally

If you want to clone this repository and run the entire setup on your local machine (without cloud deployment), follow these exact steps:

### Prerequisites
Make sure you have Git and Docker installed on your operating system (Ubuntu/Windows/Mac).

### Step-by-Step Local Setup

#### 1. Clone the Repository
Open your terminal and run the following command to download the project files:
```bash
git clone [https://github.com/itsmuji9t9/my-docker-app.git](https://github.com/itsmuji9t9/my-docker-app.git)
cd my-docker-app
docker build -t my-python-app .
docker run -d -p 8080:8080 --name my-running-app my-python-app
##  Verify Local Execution
Open your browser and navigate to: http://localhost:8080
You should see the live Python application running smoothly on your local machine!

## Stop the Local Container
Once you are done testing, you can stop and clean up the container using:
docker rm -f my-running-app

## 🏗️ How the Automated Cloud Workflow Works (CI/CD)

When code is pushed to the `main` branch, the pipeline triggers automatically:

1. **Continuous Integration (CI):** GitHub Actions fires up an isolated Ubuntu runner -> Logs into Docker Hub securely -> Builds the fresh production image -> Pushes it to Docker Hub with the :latest tag.
2. **Continuous Deployment (CD):** GitHub Actions securely connects to the **AWS EC2 instance** via SSH using a Private Key (.pem) -> Stops the old container -> Pulls the updated image from Docker Hub -> Runs the new container live on production port 80.

---

## 🔒 Required GitHub Secrets Configuration

To secure the automation without exposure, the following encrypted environment variables must be configured under `Settings -> Secrets and variables -> Actions`:

*   `DOCKERHUB_USERNAME`: Your Docker Hub profile name.
*   `DOCKERHUB_TOKEN`: Personal Access Token (PAT) from Docker Hub.
*   `EC2_HOST`: The AWS Elastic IP (Static Public IP) of your server.
*   `EC2_USERNAME`: Usually `ubuntu` for AWS Ubuntu servers.
*   `EC2_SSH_KEY`: The complete text inside your private key (.pem) file.

---

## 🌍 Live Production Access

Once the GitHub Actions workflow tab goes Green, the app is production-ready. You can access the live cloud deployment directly using the Static Elastic IP (no ports required):

```text
http://<YOUR_AWS_ELASTIC_IP>
