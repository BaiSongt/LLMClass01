#!/opt/homebrew/Caskroom/miniconda/base/envs/rag/bin/python

"""
web_tool.py

这是一个用于实现Google搜索工具的Python脚本。
该工具使用Google自定义搜索API，通过提供的查询关键词返回相关信息的摘要。

作者: baisongtao
日期: 2023-10-01
"""


from langchain.tools import BaseTool
import requests, os

class GoogleSearchTool(BaseTool):
  name = "google_search"
  description = "一个用于在Google上搜索信息的工具。"

  def __init__(self, api_key: str, cx: str):
    """
    使用Google API密钥和自定义搜索引擎ID初始化工具。
    """
    self.api_key = api_key
    self.cx = cx

  def _run(self, query: str) -> str:
    """
    使用给定的查询运行Google搜索工具。
    """
    try:
      # 发送HTTP GET请求到Google自定义搜索API
      response = requests.get(
        "https://www.google.com/customsearch/v1",
        params={
          "q": query,  # 查询关键词
          "key": self.api_key,  # API密钥
          "cx": self.cx  # 自定义搜索引擎ID
        }
      )
      response.raise_for_status()  # 检查HTTP响应状态
      data = response.json()  # 解析响应为JSON格式
      # 提取第一个搜索结果的摘要
      if "items" in data and len(data["items"]) > 0:
        return data["items"][0].get("snippet", "没有可用的摘要。")
      return "未找到相关信息。"
    except Exception as e:
      # 捕获并返回异常信息
      return f"发生错误: {e}"

  async def _arun(self, query: str) -> str:
    """
    Google搜索工具的异步运行方法。
    """
    raise NotImplementedError("此工具不支持异步操作。")

# 示例用法
if __name__ == "__main__":
  # 替换为您的实际Google API密钥和自定义搜索引擎ID
  API_KEY = os.getenv("GOOGLE_API_KEY")
  CX = "your_custom_search_engine_id"

  tool = GoogleSearchTool(api_key=API_KEY, cx=CX)
  query = "什么是LangChain？"
  result = tool.run(query)
  print(result)
