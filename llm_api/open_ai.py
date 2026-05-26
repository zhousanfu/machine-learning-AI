from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def create_model(model, **kwargs):
    temperature = kwargs.get("temperature", 1.0)

    llm = ChatOpenAI(
        model=model,
        api_key=os.environ["OPENAI_API_KEY"],
        base_url=os.environ["OPENAI_API_BASE"],
        temperature=0.8
    )
    llm = ChatGoogleGenerativeAI(
        model=os.environ["GAMINI_MODEL_BASE"],
        api_key=os.environ["GAMINI_API_KEY"],
        client_args={"proxy": "socks5://127.0.0.1:7890"},
        temperature=temperature
    )
    llm = ChatOpenAI(
        model=os.environ["GROQ_MODEL_BASE"],
        api_key=os.environ["GROQ_API_KEY"],
        base_url=os.environ["GROQ_API_BASE"],
        temperature=temperature
    )

    return llm

if __name__=="__main__":
    llm = create_model(model=os.environ["OPENAI_MODEL_COMPLEX"], temperature=0.8)
    rqw = llm.ainvoke("你是谁")