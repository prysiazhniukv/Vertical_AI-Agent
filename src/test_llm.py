import asyncio
from llm_service import LLMService

async def test_llm():
    llm = LLMService()
    response = await llm.get_response("What is Python?")
    print(f"Response: {response}")

if __name__ == "__main__":
    # Ensure you have set OPENAI_API_KEY in .env file
    asyncio.run(test_llm()) 