
from langchain_ollama.chat_models  import ChatOllama
from langchain.agents import (
  load_tools, initialize_agent, AgentType
)
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool

from bocha_tool import bocha_websearch_tool as tool_func

# 必须有记忆的组件 memory
memory = ConversationBufferMemory(
  memory_key="chat_history",
)

bocha_web_tool = Tool(
  name="BochaWebSearch",
  func=tool_func,
  description="使用Bocha Web Search API 进行搜索互联网网页，输入应为搜索查询字符串，\
                输出将返回搜索结果的详细信息，包括网页标题、网页URL、网页摘要、网站名称"
)

llm = ChatOllama(model="qwen2.5:latest", temperature=0)
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(
  tools=[bocha_web_tool, *tools],
  llm=llm,
  agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
  memory=memory, # 记忆组件
  verbose=True
)

##  这样是可以正常运行的

