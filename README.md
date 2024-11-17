# FastAPI Chatbot Server

This is a FastAPI-based server that interacts with a Rasa chatbot model to handle user inputs and return appropriate responses.

---

## Prerequisites

Ensure you have the following installed on your system:

- **Python 3.10 or above**  
- **Docker** (if deploying via Docker)  
- **Rasa Model**: A trained Rasa model file (e.g., `20241113-104357-bone-chalet.tar.gz`) is required for the chatbot.

---

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-repo-url.git
cd your-repo-directory
```

### 2. Install dependencies
```bash
pip install -r reqs.txt
```

### 3. Start the server
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```
replace "8000" to specify your desired port 

---

## Docker

### you can find the docker image in the following repository in docker hub 
```txt
https://hub.docker.com/repository/docker/alio141/chatbot/general
```

### Clone docker image
```bash
docker pull alio141/chatbot
```

### Run docker image

to run docker image properly and start the server you can use the following command

```bash
docker run -p 4000:8000 alio141/chatbot
```
you can replace port "4000" with your desired port to host the server

---

## Endpoints

this server has only one post endpoint that communicates with the chatbot

```txt
http://localhost:4000/chatbot/
```

Ensure the JSON payload matches the expected format
```json
{
    "message": "Your message here"
}

```



