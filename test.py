from langchain.agents import create_agent
from langchain.chat_models import init_chat_model


model = init_chat_model(
    model="Qwen3.5-0.8B-MLX-4bit",
    base_url="http://localhost:8000/v1",
    api_key="omlx-12345678",
    model_provider="openai",
)


response = model.invoke("为什么鹦鹉有五颜六色的羽毛？")
print(response)
