import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from agent import ProfileAnalyzerAgent
from shared_core.memory.postgres import PostgresClient
from shared_core.memory.repository import MemoryRepository
from shared_core.memory.manager import MemoryManager

postgres = PostgresClient("postgresql://postgres:postgres@localhost:5432/ai_agents")
repository = MemoryRepository(postgres)
manager = MemoryManager(repository)
agent = ProfileAnalyzerAgent(memory_manager=manager)

print("Starting analysis...")
result = agent.analyze_profile("https://www.linkedin.com/in/yuvraj3905/")
print("Analysis done")
