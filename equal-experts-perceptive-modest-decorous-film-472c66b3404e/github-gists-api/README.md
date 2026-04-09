# GitHub Gists API

## What is this?

This is a simple web application that shows public code snippets (called *gists*) from GitHub for any user.

👉 Example:
Open this in your browser:
http://localhost:8080/octocat

You will see a list of code snippets shared by that user (octocat).

---

## What do you need before starting?

You need the following installed on your computer:

1. **Python (version 3.10 or above)**
2. Internet connection (to fetch data from GitHub)

👉 To check Python is installed, run:

python --version

---

## How to run the application (step-by-step)

### Step 1: Open the project folder

Download or extract the project.
Open a terminal (Command Prompt / PowerShell / Terminal) in that folder.

---

### Step 2: Install required libraries

Run the following command:

pip install -r requirements.txt

👉 This installs all required components automatically.

---

### Step 3: Start the application

Run:

uvicorn app.main:app --port 8080

👉 You should see a message like:
“Application running on [http://127.0.0.1:8080”](http://127.0.0.1:8080”)

---

### Step 4: Open in your browser

Open:

http://localhost:8080/octocat

👉 You should now see the result.

---

## How to test if everything is working

Run this command:

python -m pytest -v

👉 What this does:

* It runs automated checks
* Confirms the application works correctly

👉 Expected result:

* All tests should pass

---

## Running using Docker

Docker allows you to run the application without installing Python.

---

### Step 1: Install Docker

Download and install Docker Desktop.

---

### Step 2: Build the application

Run:

docker build -t github-gists-api .

👉 What this command does:

Docker reads the Dockerfile in your project
It installs Python and all required dependencies
It copies your application code into the container
It creates a ready-to-run image (like a packaged app)

👉 After it completes, you should see something like:

Successfully built <image-id>
Successfully tagged github-gists-api

---

### Step 3: Run the application

Run:

docker run -p 8080:8080 github-gists-api

What this command does:

Starts your application inside a container
Maps port 8080 on your computer → 8080 inside the container
Makes your app accessible in the browser

👉 You should see logs like:

Uvicorn running on http://0.0.0.0:8080

👉 Important:

Keep this terminal open while the app is running
Press Ctrl + C to stop the container

---

### Step 4: Open in browser

http://localhost:8080/octocat

---

## What happens when you use this?

1. You enter a GitHub username
2. The application connects to GitHub
3. It retrieves public gists
4. It shows them in a simple format

---

## Possible issues and solutions

### ❌ “Command not found”

👉 Make sure Python or Docker is installed correctly

---

### ❌ “Port already in use”

👉 Try another port:
uvicorn app.main --port 8081

---

### ❌ No data shown

👉 Check your internet connection

---

## Summary

* Easy to run in a few steps
* Works locally or via Docker
* Includes automated tests
* Designed to be simple and clear

---

Thank you for reviewing this project 🙂
