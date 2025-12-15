from google.adk.agents.llm_agent import Agent
from .openapi_tools import petstore_toolset


def get_current_time(city: str) -> dict:
    return {
        "status": "success",
        "city": city,
        "time": "10:30 AM",
    }


def get_weather(city: str) -> dict:
    return {
        "status": "success",
        "city": city,
        "temperature": "25°C",
        "condition": "Sunny",
    }


root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="Agent that answers time, weather, and pet-related questions.",
    instruction=(
        "You are a helpful agent.\n"
        "- Answer time and weather questions directly.\n"
        "- Use OpenAPI tools for pet-related questions."
    ),
    tools=[
        get_weather,
        get_current_time,
        petstore_toolset,  # ✅ Pass the toolset directly
    ],
)