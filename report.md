**Section 3**

26. Why does the request use a client-generated id rather than a server-generated one? What problem does this solve in distributed systems?

    If the client generates the ID before the sending it can retry failed requests without the server needed to do extra work.

27. The status.state can be 'working'. Under what circumstances would a server return this
    state in a non-streaming call, and how should a client react?
    
    when tasts take lonfer than a single http request. The client should keep polling until the state changes to completed/finished or a failed/error state.

29. What is the purpose of the sessionId field? Give a concrete example of two related tasks that should share a session.

    sessionId can group multiple tasks to one conversation. For example if a prompt like "what is c++?" is sent and another that prompts "what is that" or "give me an example code" the agent will know the conversation is still about c++ and not a new converation.

32. The parts array supports types text, file, and data. Describe a realistic multi-agent
    workflow where all three part types appear in a single conversation.
    
    A teacher can make an auto grading system with text being the prompt "grade this homework", the file would be the submitted file, and the data would be a something like {"score: ...?", "passed": true,}

**Section 4**

37. In report.md Section 4, describe: (a) what the --allow-unauthenticated flag does and its** security implications, (b) how Cloud Run scales to zero and what cold start latency means for A2A clients.

    --allow-unauthenticated cloud can allow users to attack without a signed token. this can allow attacks to gain access to tools or bring up the bill

    scaling to zero mean the cloud run shuts down until a request. cold start latency is time it takes to start a new container .

**Section 5**

42. explain: (a) the difference between deploying to Cloud Run vs Agent Engine in terms of operational burden and use-case fit

    Cloud run give you more control over containers, but with agent engine goolge handles most of the work. 



**Section 6**

GET https://echo-a2a-agent-144286160544.us-central1.run.app/.well-known/agent.json

200 name=Echo Agent

Agent : Echo Agent

Skills: ['Echo', 'Summarise']

Reply : Hello from the client!

46. If a client loses the network connection after sending the POST but before receiving the response, how could it safely retry? What field in the A2A protocol helps with idempotency?

    The ID field helps. The A2A will resent the original results instead of generating new results.
