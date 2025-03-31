## LangChain
### 01 Prompt 提示词工程
- `PromptTemplate`
- `ChatPromptTemplate`
- `ChatMassagePromptTemplate`
  - SystemMessagePromptTemplate
  - HumanMessagePromptTemplate
  - AIMessagePromptTemplate
  - ChatMessagePromptTemplate
- `StringPromptTemplate` `CustomPromptTemplate`
- `FewShotPromptTemplate` 少量例子
- `OneShotPromptTemplate` 单个例子
- 提示词的设计方法： 组合提示词  多层提示词
```text
template = "{content}" --> PromptTemplate.from_template(template)
```
### 02 OutputFormatter
- JSON LIST DICT ...
```python
from langchain.schema import BaseOutputParser
from langchain.output_parsers import PydanticOutputParser
```
### 03 示例选择器 LengthBasedExampleSelector

- `MaxMarginalRelevanceExampleSelector`
- 根据长度要求智能选择  字符长度
- 根据输入相似度选择示例 最大边际相似度 MMR
- 根据输入相似度选择    最大余弦相似度

### 04 LLMs 和 ChatModels
- LLMs 和 ChatModels 的区别， 有角色和无角色
- 流式输出 getStream

### 05 Token 消耗的追踪

___

