# 🚀 Day 2: EC2 Web App Deployment

## 📌 Overview

This project demonstrates deploying a Python Flask web application on an AWS EC2 instance using a production-style setup with Gunicorn and Nginx.

---

## ⚙️ Tech Stack

* AWS EC2 (Ubuntu)
* Python 3
* Flask
* Gunicorn (WSGI Server)
* Nginx (Reverse Proxy)

---

## 🔧 Steps Performed

### 1. Launch EC2 Instance

* Created Ubuntu EC2 instance
* Configured security group (allowed ports 22, 80, 5000)

### 2. Connect via SSH

```bash
ssh web-app
```

### 3. Setup Project

```bash
git clone <your-repo-url>
cd AWS-Portfolio/DAY2
```

### 4. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Run Flask App (Development)

```bash
python3 webapp.py
```

---

## 🚀 Production Deployment

### 6. Run using Gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 webapp:app
```

### 7. Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/default
```

Paste:

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Restart Nginx:

```bash
sudo systemctl restart nginx
```

---

## 🌐 Access Application

```
http://43.205.242.111/

```

---

## 📂 Project Structure

* `webapp.py` → Flask application
* `requirements.txt` → Dependencies
* `Screenshot/` → Deployment screenshots

---

## 🎯 Key Learnings

* Difference between development server and production server
* Using Gunicorn as WSGI server
* Configuring Nginx as reverse proxy
* Deploying apps on AWS EC2

---

## ⚠️ Note

* This was a practice deployment
* EC2 instance may be terminated after use to avoid charges

---




✨ This project demonstrates hands-on experience with cloud deployment and basic DevOps practices.
