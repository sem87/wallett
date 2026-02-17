import os
from dotenv import load_dotenv
import dashscope
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv
from wallett.logi import logi
load_dotenv('.env.wallet')
# Устанавливаем API-ключ (хранится в переменной окружения)
api_key = os.getenv("deepii")

# Подключаемся к модели Qwen
client = InferenceClient("Qwen/Qwen2.5-7B-Instruct", token=api_key)


def intelligence_def(text: str, client: InferenceClient) -> str:
    """Анализирует текст через Qwen с чёткими инструкциями."""
    # Системное сообщение задаёт роль и правила
    system_prompt = ("Отвечай полностью на русском языке"
                     "Нужно руководство к действию"
                     "Отвечай только обработанным текстом, без комментариев.")
    messages = [{"role": "system", "content": system_prompt}, {"role": "user", "content": text}]
    try:
        response = client.chat_completion(messages=messages, max_tokens=500, extra_body={
                "temperature": 0.3,
                "top_p": 0.85,
                "repetition_penalty": 1.2
            })
        return response.choices[0].message.content.strip()
    except Exception as e:
        logi.err.info(f"do_list() в папке handlers/handler_message.py , Exception as e : {e}")


if __name__ == "__main__":
    # ...
    intelligence = "сегодня заседание ЦБ по ставки.какую ставку выберут? Это не иир"
    print(intelligence_def(text=intelligence,client=client))
