from fastapi import FastAPI, HTTPException, Header, Request, Depends
from typing import Optional
import requests

# 中间件配置
OLLAMA_URL = "http://localhost:11434"  # Ollama 默认地址
API_KEYS = {"OLLAMA_DEEPSEEK_API_KEY"}     # 自定义合法 API Key

app = FastAPI()

def verify_api_key(api_key: Optional[str] = Header(None, alias="X-API-Key")):
    """验证 API Key 的依赖函数"""
    if not api_key or api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True

@app.post("/v1/chat/completions")
async def chat_completion(
    request: Request,
    _: bool = Depends(verify_api_key)  # 依赖验证
):
    """将请求转发到 Ollama 的 DeepSeek 模型"""
    try:
        # 获取客户端请求数据
        data = await request.json()

        # 调用本地 Ollama 接口
        response = requests.post(
            f"{OLLAMA_URL}/v1/chat/completions",
            json={
                "model": "deepseek-r1:7b",  # 确保 Ollama 中模型名正确
                "messages": data.get("messages", []),
                "stream": True       # 示例关闭流式传输
            }
        )
        response.raise_for_status()  # 检查 HTTP 错误
        return response.json()

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {str(e)}")
