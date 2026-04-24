# server/agent_card.py
AGENT_CARD = {
    "id":          "echo-agent-v1",
    "name":        "Echo Agent",
    "version":     "1.0.0",
    "description": "A simple agent that echoes back any text it receives.",
    "url":         "http://localhost:8000",   # updated at deploy time
    "contact":{
        "email": "idkplaceholder@gmail.com"
    },
    "capabilities": {
        "streaming": False,
        "pushNotifications": False
    },
    "defaultInputModes":  ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id":          "echo",
            "name":        "Echo",
            "description": "Returns the user message verbatim.",
            "inputModes":  ["text/plain"],
            "outputModes": ["text/plain"]
        },
        {
            "id": "summarise",
            "name": "Summarise",
            "description": "Returns a summary of the provided text.",
            "inputModes": ["text/plain"],
            "outputModes": ["text/plain"]
        }
    ]
}

REQUIRED_FIELDS = {
    "id",
    "name",
    "version",
    "description",
    "url",
    "capabilities",
    "defaultInputModes",
    "defaultOutputModes",
    "skills",
}

 
def validate_card(card: dict) -> bool:
    for field in REQUIRED_FIELDS:
        if field not in card:
            return False
    return True
