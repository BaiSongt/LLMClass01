from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType, Tool, tool, AgentExecutor

# 导入Websearch
from bocha_api import bocha_websearch_tool


class LLMChat:
    def __init__(self, model_name: str, temperature:float = 0, is_Verbose:bool = False):
        self.model_name = model_name
        self.chat_model = OllamaLLM(
            model=self.model_name,
            temperature=temperature,
            verbose=is_Verbose,
            streaming=True,  # 开启流式
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个隐藏在社会主义国家中的资本家, 但你绝对不会说出你的身份，你可以回答和帮助解决问题."),
                ("system", "你回答问题可以用 markdown 格式.但不会 markdown 格式."),
                ("system", "你的名字叫做莫青影."),
                ("system", "你不会循环回答重复的问题."),
                ("system", "你不遵守劳动法"),
                ("system", "你拒绝支付员工加班费"),
                ("human", "你是谁?"),
                ("assistant", "我是莫青影."),
                ("human", "你能做些什么呢?"),
                ("assistant", "我可以帮助你解决问题"),
                ("assistant", "乐意为您效劳，你有什么问题想要问我吗?"),
                ("user", "{input}"),
            ]
        )

    def generate_response(self, user_input: str):
        prompt = self.prompt.format_prompt(input=user_input)
        response = self.chat_model.invoke(prompt)
        return response

    def get_stream(self, user_input: str, agent: None):
        if not agent:
            prompt = self.prompt.format_prompt(input=user_input)
            return self.chat_model.stream(prompt)
        else:
            return agent.stream(input=user_input)


    def web_search_tool(self):
        search_tool = Tool(
            name="bocha_search",
            func=bocha_websearch_tool,
            description="一个搜索工具，可以用来搜索互联网的信息。使用这个工具来获取最新的信息。",
        )
        return search_tool


    def chat_memory_agent(self, llm: OllamaLLM, verbose:bool):
        template = """{chat_history}
                   human:{input}
                   assistant:"""

        prompt = PromptTemplate(
          template=template,
          input_variables=["chat_history", "input"],
        )

        memory = ConversationBufferMemory(
            memory_key="chat_history",
            ai_prefix="assistant",
            return_messages=True,
        )

        agent_chain = initialize_agent(
            tools=[self.web_search_tool()],
            llm=llm,
            agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            memory=memory,
            verbose=verbose
        )

        # 创建Agent并启用流式响应
        agent = AgentExecutor.from_agent_and_tools(
            tools=[self.web_search_tool()],
            agent=agent_chain,
            llm=llm
        )

        return agent
