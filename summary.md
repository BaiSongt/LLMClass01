# 学习内容总结

## 01-Prompt
- **1_first_example.ipynb**: 介绍了如何使用 OpenAI API 和其他开源模型（如 BaiChuan、ChatGLM）进行基础调用。
- **2_prompt_template.ipynb**: 学习了如何使用 Prompt Template 来构建动态提示词。
- **3_LLMs的调用.ipynb**: 详细讲解了调用大型语言模型（LLMs）的方式，包括参数设置和模型选择。

## 02-RAG
- **01_Loader.ipynb**: 学习了如何加载多种文件格式（如 JSON、PDF、HTML、Excel）以供后续处理。
- **02_transform.ipynb**: 介绍了文档分割与精炼的技术，包括递归字符分割器和向量化处理。
- **03_lost_in_middle.ipynb**: 探讨了在长文本处理中避免信息丢失的策略。

## 03-ChatDoc
- **ChatDoc.ipynb**: 实现了对 PDF、DOC、XLSX 文件的读取与内容提取，并进行了分块和向量化存储。
- **ChatDocApp.ipynb**: 构建了一个应用程序，用于基于文档内容的问答。

## 04-Chain&Memory
- **Memory.ipynb**: 学习了短时记忆和长时记忆的实现方式，以及如何在对话中动态摘要。
- **MapReduce&Map.ipynb**: 介绍了 MapReduceChain 的原理及其在长文本摘要中的应用。
- **DocDeal.ipynb**: 深入探讨了网格算法的基础理论、生成方法及其在工程中的应用。

## 05-Agent
- **01_第一个Agents.ipynb**: 构建了第一个简单的 Agent，能够执行数学计算和搜索任务。
- **04_Agent与Tool之间共享记忆.ipynb**: 学习了如何在 Agent 和工具之间共享记忆以提高任务效率。
- **05_tool的加载与使用.ipynb**: 详细列举了常用工具的加载与使用方法，包括数据查询、图像处理和金融分析工具。

## 06-LCEL
- **02-LCEL_RAG_Search.ipynb**: 实现了基于 RAG 的搜索功能，支持多语言查询。
- **03-LCEL接口.ipynb**: 设计了多种接口格式，支持复杂的输入输出需求。

---

以上内容涵盖了从 Prompt 工程、文档处理、链式调用到智能 Agent 的完整学习路径，为构建基于 LLM 的应用提供了全面的技术支持。
