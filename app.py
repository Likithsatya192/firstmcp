import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def chat_with_agent(agent):
    print("\nWelcome to the MCP Chatbot! Type 'bye' to exit.")
    print("You can ask me anything, and I'll help you find information using Google search.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day!")
            break
            
        if not user_input:
            print("Please enter a valid query.")
            continue
            
        print("\nThinking...")
        try:
            result = await agent.run(
                user_input,
                max_steps=30,
            )
            print(f"\nAssistant: {result}")
        except Exception as e:
            print(f"\nSorry, I encountered an error: {str(e)}")

async def main():
    # Load environment variables
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"

    print("Initializing chat...")

    # Create MCPClient from config file
    client = MCPClient.from_config_file(config_file)

    # Create LLM
    llm = ChatGroq(model="qwen-qwq-32b")
    # Alternative models:
    # llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    # llm = ChatGroq(model="llama3-8b-8192")

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30, memory_enabled=True)

    # Start the chat session
    await chat_with_agent(agent)

if __name__ == "__main__":
    asyncio.run(main())