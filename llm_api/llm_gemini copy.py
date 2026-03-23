import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

env_path = Path('.') / '.env'          # 或者 Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)      # 读取文件并把变量写入 os.environ

client = genai.Client(api_key=os.getenv('GENAI_API_KEY'))
prompt = "Explain the concept of Occam's Razor and provide a simple, everyday example."
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print(response.text)