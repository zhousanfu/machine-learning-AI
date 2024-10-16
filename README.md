<!--
 * @Author: Sanfor Chow
 * @Date: 2023-11-30 11:25:52
 * @LastEditors: courageux_san WX
 * @LastEditTime: 2024-10-17 04:57:28
 * @FilePath: /machine-learning-AI/README.md
-->
# NLP
bilstm_crf命名实体：[bert_bilstm_crf_ner](https://github.com/zhousanfu/machine-learning-demo/blob/master/nlp/nlp_entity_recognize_bert4keras_crf.ipynb)

百度UIE通用信息抽取：[paddlenlp](https://github.com/zhousanfu/machine-learning-demo/blob/master/nlp/my_paddlenlp.ipynb)

关系抽取：[triple_extraction](https://github.com/zhousanfu/machine-learning-demo/blob/master/nlp/关系抽取_GPLinker_torch.ipynb)

# LLM

## llm api 调用
llm_api文件夹, 使用示例
```python
from llm_api.llm_groq import llm_groq

prompt = "你是谁"
r = llm_groq(text=prompt)
```

## 实例
Langchain构建私有知识库智能问答 https://github.com/zhousanfu/machine-learning-demo/blob/master/llm/langchain_demo.ipynb

Langchain知识图谱 https://github.com/zhousanfu/machine-learning-demo/blob/master/llm/Llama_2_Knowledge_Graphs.ipynb



# 比赛
科大讯飞 基于论文摘要的文本分类与关键词抽取挑战赛 https://github.com/zhousanfu/machine-learning-demo/blob/master/比赛/科大讯飞_基于论文摘要的文本分类与关键词抽取挑战赛.ipynb
