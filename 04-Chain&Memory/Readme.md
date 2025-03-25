以下是LangChain中几种基础Chain的详细介绍，结合源代码、参数、使用场景及代码示例：

---

### 一、**LLMChain（语言模型链）**
**核心功能**：直接与大型语言模型（如GPT-4、ChatGLM）交互，用于生成或理解自然语言。
**参数**：
- `llm`：语言模型实例（如`OpenAI()`或`ChatZhipuAI()`）。
- `prompt`：提示模板（`PromptTemplate`），定义输入格式和生成规则。
**使用场景**：
- 简单问答、文本生成、代码编写等单步任务。
**代码示例**：
```python
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 初始化模型和提示模板
llm = OpenAI(temperature=0.7)
prompt = PromptTemplate(
    input_variables=["question"],
    template="你是一个Python专家，请解释{question}。"
)

# 创建LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)

# 调用链生成回答
response = llm_chain.invoke({"question": "装饰器的作用"})
print(response)
```
**输出**：
```
你是一个Python专家，请解释装饰器的作用。
...
```

---

### 二、**SequentialChain（顺序链）**
**核心功能**：按顺序串联多个步骤，前一步输出作为下一步输入。
**参数**：
- `chains`：子链列表（如`[LLMChain, ToolChain]`）。
- `input_variables`：输入变量名称（需与子链输入匹配）。
**使用场景**：
- 多步骤任务，如先生成问题再验证答案、文本处理流水线。
**代码示例**：
```python
from langchain.chains import SequentialChain
from langchain.agents import Tool
from langchain.prompts import PromptTemplate

# 定义子链：生成问题 + 调用工具查询
question_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        input_variables=["topic"],
        template="请为{topic}生成5个相关问题。"
    )
)
search_tool = Tool(
    name="GoogleSearch",
    func=lambda q: f"搜索结果：{q}"
)
validation_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate(
        input_variables=["answer"],
        template="验证答案：{answer}是否正确？"
    )
)

# 组合顺序链
full_chain = SequentialChain(
    chains=[question_chain, search_tool, validation_chain],
    input_variables=["topic"],
    output_variables=["final_answer"]
)

# 执行链
result = full_chain.invoke({"topic": "LangChain基础链"})
print(result)
```
**输出**：
```
请为LangChain基础链生成5个相关问题。
...
验证答案：...是否正确？
```

---

### 三、**MapReduceChain（映射-归约链）**
**核心功能**：将数据分块处理后合并结果，适用于大规模数据集。
**参数**：
- `map_chain`：处理每个数据块的子链。
- `reduce_chain`：合并结果的子链。
**使用场景**：
- 处理长文本、表格数据或分布式计算任务。
**代码示例**：
```python
from langchain.chains import MapReduceChain
from langchain.prompts import PromptTemplate

# 定义分块处理逻辑
def process_chunk(chunk):
    return LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            template="总结以下段落：{chunk}"
        )
    ).invoke({"chunk": chunk})

# 定义合并逻辑
def merge_results(results):
    return LLMChain(
        llm=llm,
        prompt=PromptTemplate(
            template="综合所有结果：{results}"
        )
    ).invoke({"results": results})

# 创建MapReduce链
chain = MapReduceChain(
    map_chain=process_chunk,
    reduce_chain=merge_results
)

# 执行链
output = chain.invoke({"data": ["段落1", "段落2", "段落3"]})
print(output)
```
**输出**：
```
总结段落1：...
总结段落2：...
综合所有结果：...
```

---

### 四、**ConditionalChain（条件链）**
**核心功能**：根据输入动态选择执行路径。
**参数**：
- `cases`：条件-链映射（如`{"条件A": chain_A, "条件B": chain_B}`）。
**使用场景**：
- 多模态任务（如文本+图像）、动态决策场景。
**代码示例**：
```python
from langchain.chains import ConditionalChain

# 定义条件分支
cases = {
    "text": LLMChain(llm=llm, prompt=PromptTemplate("解释文本...")),
    "image": LLMChain(llm=llm, prompt=PromptTemplate("描述图像..."))
}

# 创建条件链
conditional_chain = ConditionalChain(cases=cases)

# 根据输入类型选择链
result = conditional_chain.invoke({"input_type": "text", "content": "LangChain原理"})
print(result)
```
**输出**：
```
解释文本：LangChain原理...
```

---

### 五、**TextPromptChain（提示模板链）**
**核心功能**：通过组合提示模板实现复杂交互逻辑。
**参数**：
- `prompts`：提示模板列表（如`[PromptTemplate1, PromptTemplate2]`）。
**使用场景**：
- 需要多轮对话引导或结构化输入的任务。
**代码示例**：
```python
from langchain.chains import TextPromptChain
from langchain.prompts import PromptTemplate

# 定义提示模板
prompt1 = PromptTemplate(
    template="你是一个学生，请回答以下问题：{question}"
)
prompt2 = PromptTemplate(
    template="请用{style}风格总结答案：{answer}"
)

# 创建提示链
chain = TextPromptChain(prompts=[prompt1, prompt2])

# 执行链
response = chain.invoke({
    "question": "LangChain的SequentialChain如何工作？",
    "style": "诗歌"
})
print(response)
```
**输出**：
```
你是一个学生，请回答以下问题：LangChain的SequentialChain如何工作？
请用诗歌风格总结答案：...
```

---

### 总结
以上基础Chain覆盖了LangChain的核心功能：
1. **LLMChain**：直接调用大模型，适合单步任务。
2. **SequentialChain**：顺序执行多步骤，构建复杂流程。
3. **MapReduceChain**：处理大规模数据，分块合并结果。
4. **ConditionalChain**：动态选择路径，适应多模态场景。
5. **TextPromptChain**：通过模板实现结构化交互。

建议结合具体需求选择链类型，并参考[LangChain官方网页](https://python.langchain.com/docs/)深入学习高级用法。

______

## **RouterChain**

`RouterChain` 是 LangChain 中用于**动态路由请求**的高级链式结构，根据输入内容或上下文自动选择匹配的子链（Sub-chain）进行处理。它通过路由规则（如关键词匹配、意图识别、模态判断等）实现灵活的任务分发，适用于多模态、多步骤或复杂对话场景。

---

### **核心功能**
1. **动态路由**：根据输入内容（文本、图片、文件等）或上下文自动选择对应的子链。
2. **多模态支持**：可结合文本、图像、表格等多种数据类型进行路由决策。
3. **灵活配置**：支持基于规则（Rule-Based）、基于意图（Intent-Based）或混合路由策略。

---

### **关键参数**
1. **`router`**：路由器配置，定义匹配规则和对应的子链。
   - 例如：`{"text": text_chain, "image": image_chain}`。
2. **`interpreter`**（可选）：解释器（如 `TextInterpreter`），用于解析输入内容并提取路由关键信息。
3. **`input_variables`**：输入变量名称，需与子链的输入匹配。

---

### **使用场景**
1. **多模态任务**：根据输入类型（文本/图片/文件）自动路由到不同处理链。
   ```python
   # 用户上传图片或文本时，路由到对应处理链
   ```
2. **复杂对话系统**：根据用户意图（如“解释”、“生成”、“分析”）分配不同对话流程。
3. **动态任务分配**：根据问题复杂度、领域自动选择专家级子链。
4. **A/B测试路由**：按特定条件将请求分发到不同模型或服务。

---

### **代码示例**
#### 场景1：多模态路由（文本/图片）
```python
from langchain import OpenAI, LLMChain
from langchain.chains.router import RouterChain
from langchain.prompts import PromptTemplate
from langchain.interpreters import TextInterpreter

# 定义子链：文本处理链和图像处理链
text_chain = LLMChain(
    llm=OpenAI(temperature=0.5),
    prompt=PromptTemplate(
        template="分析以下文本内容：{text}",
        input_variables=["text"]
    )
)

image_chain = LLMChain(
    llm=OpenAI(temperature=0.5),
    prompt=PromptTemplate(
        template="描述以下图片内容：{image}",
        input_variables=["image"]
    )
)

# 定义路由规则（关键词匹配）
router_config = {
    "text": {"chain": text_chain, "interpreter": TextInterpreter()},
    "image": {"chain": image_chain}
}

# 创建 RouterChain
router_chain = RouterChain(
    router=router_config,
    interpreter=TextInterpreter()  # 解析输入类型（文本/图片）
)

# 调用链（自动路由）
response = router_chain.invoke({
    "input": "这是一张猫的图片.jpg",  # 实际使用需解析文件类型
    "type": "image"  # 或通过 interpreter 自动识别
})

print(response)
```

#### 场景2：意图路由（问答/生成/分析）
```python
from langchain.chains.router import IntentRouter

# 定义意图映射
intent_router = IntentRouter(
    {
        "question": {
            "chain": LLMChain(
                llm=OpenAI(),
                prompt=PromptTemplate("回答以下问题：{question}")
            )
        },
        "generate": {
            "chain": LLMChain(
                llm=OpenAI(),
                prompt=PromptTemplate("生成一段关于{topic}的文案：{topic}")
            )
        },
        "analyze": {
            "chain": LLMChain(
                llm=OpenAI(),
                prompt=PromptTemplate("分析以下数据：{data}")
            )
        }
    },
    intent_classifier=LLMChain(llm=OpenAI())  # 使用LLM判断意图
)

# 调用链（自动识别意图）
response = intent_router.invoke({
    "input": "帮我写一篇关于环保的演讲稿"
})

print(response)  # 自动路由到 "generate" 链
```

---

### **RouterChain vs 其他链**
| **特性**          | **RouterChain**                     | **ConditionalChain**         |
|---------------------|---------------------------------------|--------------------------------|
| **路由逻辑**        | 动态匹配（规则/意图/模态）            | 静态条件分支（预定义条件）     |
| **灵活性**          | 支持复杂路由策略（如正则表达式）       | 仅支持简单的键值对条件         |
| **适用场景**        | 多模态、意图识别、动态任务分配         | 简单的多步骤流程控制           |
| **性能开销**        | 较高（需解析输入并匹配规则）           | 较低（直接按条件分支执行）     |

---

### **常见错误与注意事项**
1. **路由规则冲突**：确保不同路由规则的匹配条件互斥。
   ```python
   # 错误示例：同时匹配 "cat" 和 "animal"
   {"text": ..., "cat": ...}  # 优先级问题可能导致覆盖
   ```
2. **输入解析依赖**：使用 `interpreter` 时需确保输入格式标准化。
3. **子链兼容性**：所有子链的输入变量需与 `input_variables` 一致。

---

### **进阶用法**
- **混合路由策略**：结合关键词匹配和意图识别。
  ```python
  router_config = {
      "rule1": {"pattern": r"分析(.*)", "chain": analysis_chain},
      "intent": {"intent": "generate", "chain": generate_chain}
  }
  ```
- **默认路由**：为未匹配的请求设置默认处理链。
  ```python
  router_config = {
      "default": {"chain": default_chain}
  }
  ```

---

### **总结**
`RouterChain` 是 LangChain 中实现**智能化任务分发**的核心组件，通过动态路由机制显著提升复杂系统的扩展性和灵活性。适用于需要：
- 多模态输入处理的场景（如 ChatGPT+DALL-E 集成）。
- 根据用户意图或上下文动态调整响应的对话系统。
- 分布式任务队列或 A/B 测试架构。

建议结合具体业务需求设计路由规则，并通过单元测试验证覆盖所有可能的输入路径。
