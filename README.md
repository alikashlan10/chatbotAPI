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




