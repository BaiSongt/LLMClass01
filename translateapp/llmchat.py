from langchain_ollama.llms import OllamaLLM
from langchain.prompts import ChatPromptTemplate


class LLMChat:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.chat_model = OllamaLLM(model=self.model_name)
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个AI助手,你可以回答和帮助解决问题.你回答问题都用markdown格式."),
                ("human", "你是谁?"),
                ("assistant", "我是一个人工智能助手."),
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

    def getStream(self, user_input: str):
        prompt = self.prompt.format_prompt(input=user_input)
        response = self.chat_model.stream(prompt)
        return response
