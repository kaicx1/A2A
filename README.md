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
