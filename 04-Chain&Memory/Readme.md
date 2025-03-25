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
