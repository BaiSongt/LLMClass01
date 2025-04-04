以下是LangChain中Agent工具的**具体使用示例**，按工具类型分类并附代码片段及说明：

---

### **1. 数据查询类工具示例：SQLDatabase**
**场景**：通过自然语言查询MySQL数据库
**代码示例**：
```python
from langchain_community.utilities import SQLDatabase

# 连接MySQL数据库
db = SQLDatabase.from_uri(
    "mysql+pymysql://root:password@localhost:3306/sales_db"
)

# 生成SQL查询链
query_chain = (
    RunnablePassthrough.assign(query=create_sql_query_chain(db))  # 自动生成SQL
    | QuerySQLDataBaseTool(db=db)  # 执行查询
    | StrOutputParser()  # 解析结果
)

result = query_chain.invoke("查询2024年Q2华北地区销售额最高的商品")
print(result)  # 输出：商品A，销售额580万元
```
**说明**：
- `create_sql_query_chain`根据自然语言生成SQL语句
- `QuerySQLDataBaseTool`执行查询并返回结构化数据
**适用场景**：金融报表生成、库存管理等需实时数据支持的任务

---

### **2. API与云服务类工具示例：Twilio短信通知**
**场景**：订单状态变更时自动发送短信通知
**代码示例**：
```python
from twilio.rest import Client
from langchain.agents import Tool

# 初始化Twilio客户端
twilio_client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_TOKEN"))

# 定义短信工具
def send_sms(to: str, message: str) -> str:
    try:
        twilio_client.messages.create(
            body=message,
            from_="+1234567890",
            to=to
        )
        return "短信发送成功"
    except Exception as e:
        return f"发送失败: {str(e)}"

sms_tool = Tool(
    name="sms_notifier",
    func=send_sms,
    description="发送短信通知"
)

# 在Agent中调用
agent = initialize_agent(tools=[sms_tool], llm=llm)
agent.invoke("通知用户13800138000订单已发货")
```
**说明**：
- 需配置Twilio账户密钥
- 工具自动处理API调用和错误捕获

---

### **3. 代码与系统管理类工具示例：Shell命令执行**
**场景**：自动化服务器日志清理
**代码示例**：
```python
from langchain.agents import Tool

# 定义Shell工具
def clean_logs(days: int = 7) -> str:
    import os
    result = os.system(f"find /var/log -mtime +{days} -exec rm {{}} \\;")
    return f"已清理{days}天前的日志文件"

log_cleanup_tool = Tool(
    name="log_cleaner",
    func=clean_logs,
    description="清理指定天数的服务器日志"
)

# 在安全环境中调用
agent = initialize_agent(tools=[log_cleanup_tool], llm=llm)
agent.invoke("清理30天前的系统日志")
```
**说明**：
- 需限制工具执行权限
- 可扩展为批量服务器管理

---

### **4. 图像与多媒体类工具示例：DALL-E图像生成**
**场景**：根据产品描述生成宣传图
**代码示例**：
```python
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool

# 初始化图像生成工具
search = SerpAPIWrapper(api_key=os.getenv("SERP_API_KEY"))
def generate_product_image(prompt: str) -> str:
    result = search.run(f"生成{prompt}的高清图片")
    return result["imageUrl"]

image_tool = Tool(
    name="image_generator",
    func=generate_product_image,
    description="根据文本生成产品宣传图"
)

# 在电商场景中使用
agent = initialize_agent(tools=[image_tool], llm=llm)
agent.invoke("生成智能手表产品宣传图，科技感风格")
```
**说明**：
- 依赖SerpAPI的图像搜索能力
- 可结合Stable Diffusion增强生成质量

---

### **5. 金融与商业类工具示例：Alpha Vantage股票分析**
**场景**：实时获取股票数据并分析
**代码示例**：
```python
from alpha_vantage.timeseries import TimeSeries
from langchain.agents import Tool

# 初始化金融工具
ts = TimeSeries(key=os.getenv("ALPHA_VANTAGE_KEY"), output_format="pandas")
def analyze_stock(symbol: str) -> str:
    data, _ = ts.get_daily(symbol=symbol, outputsize="full")
    return f"{symbol}过去一年涨幅：{data['4. close'].pct_change().sum()*100:.2f}%"

stock_tool = Tool(
    name="stock_analyzer",
    func=analyze_stock,
    description="获取股票历史数据与分析"
)

# 在投资决策中使用
agent = initialize_agent(tools=[stock_tool], llm=llm)
agent.invoke("分析腾讯控股（0700.HK）近一年表现")
```
**说明**：
- 需申请Alpha Vantage API密钥
- 可扩展技术指标计算（MACD、RSI等）

---

### **汇总对比表**
| 工具类型       | 示例工具          | 核心功能                          | 适用场景                  | 关键依赖              |
|----------------|-------------------|-----------------------------------|---------------------------|-----------------------|
| 数据查询       | SQLDatabase       | 自然语言转SQL查询                 | 数据库问答系统            | MySQL/PostgreSQL驱动  |
| API服务        | Twilio SMS        | 发送短信/WhatsApp通知             | 客服自动化                | Twilio账户            |
| 系统管理       | Shell命令执行     | 服务器命令行操作                  | 运维自动化                | 操作系统权限          |
| 图像处理       | DALL-E生成器      | 文生图创作                        | 营销素材生成              | SerpAPI图像搜索       |
| 金融分析       | Alpha Vantage     | 股票数据获取与分析                | 投资决策支持              | Alpha Vantage API密钥 |

---

### **扩展建议**
1. **安全加固**：对数据库/API工具添加执行频率限制和白名单控制
2. **链式调用**：组合多个工具实现复杂流程（如：数据查询→清洗→可视化）
3. **记忆增强**：通过`ConversationBufferMemory`记录工具调用历史
4. **异步支持**：对耗时操作（如大数据查询）使用异步工具调用

