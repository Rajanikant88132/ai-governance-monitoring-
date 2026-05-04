def simple_agent(query):
    if "policy" in query.lower():
        return "Checking governance policies..."
    return f"Agent response to: {query}"