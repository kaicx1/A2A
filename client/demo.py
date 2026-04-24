from client import A2AClient

with A2AClient('CHANGE TO YOUR CLOUD RUN') as client:
    card = client.fetch_agent_card()
    print(f"Agent : {card['name']}")
    print(f"Skills: {[s['name'] for s in client.get_skills()]}")

    response = client.send_task('Hello from the client!')
    print(f"Reply : {client.extract_text(response)}")
