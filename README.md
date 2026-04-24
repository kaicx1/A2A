## Setup

```bash
pip install fastapi uvicorn pydantic httpx vertexai google-cloud-aiplatform cloudpickle
```

## Run local

```bash
cd server
uvicorn main:app --reload
```

## Run the client

```bash
cd client
python3 demo.py
```

## Deploy to Cloud Run

```bash
bash cloud/deploy_cloud_run.sh
```

## Deploy to Agent Engine

```bash
gcloud auth application-default login
python3 cloud/deploy_agent_engine.py
```

**Services STOPPED**

project-8e9cb3d7-1996-49fa-ad0

https://echo-a2a-agent-144286160544.us-central1.run.app
