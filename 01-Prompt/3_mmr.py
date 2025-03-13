from langchain.prompts.example_selector import MaxMarginalRelevanceExampleSelector
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
# from langchain.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain.prompts import FewShotPromptTemplate

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

OLLAMA_URL = "http://localhost:11434"  # Ollama 默认地址
API_KEYS = {"OLLAMA_DEEPSEEK_API_KEY"}     # 自定义合法 API Key


# 定义示例数据
examples = [
  {"input":"happy","output":"sad"},
  {"input":"sad","output":"happy"},
  {"input":"tall","output":"short"},
  {"input":"short","output":"tall"},
  {"input":"angry","output":"excited"},
  {"input":"excited","output":"angry"},
  {"input":"开心","output":"悲伤"},
  {"input":"悲伤","output":"开心"},
]

# 创建提示词模板
example_prompt = PromptTemplate(
  input_variables=["input","output"],
  template="原词: {input} \n反义: {output}",
)

# 调用 Ollama API
embed = OllamaEmbeddings(
    model="deepseek-r1:1.5b",
    base_url=OLLAMA_URL,
)
# 创建一个示例选择器
example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
  # 传入示例
  examples=examples,
  # 相似性搜索
  embeddings=embed,
  # 使用的向量存储
  vectorstore_cls=FAISS,
  # 结果条数
  k=2,
)

mmr_prompt = FewShotPromptTemplate(
  example_selector=example_selector,
  example_prompt=example_prompt,
  prefix="给出每一个输入词的反义词: ",
  suffix="原词: {adjective} \n反义: ",
  input_variables=["adjective"]
)

# 当我们输入一个词时，我们会得到一个提示，提示我们输入这个词的反义词
prompt = mmr_prompt.format(adjective="担心")
print(prompt)
