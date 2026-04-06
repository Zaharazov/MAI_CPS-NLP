import requests

def send(text_request):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "qwen2.5:0.5b",
        "prompt": text_request,
        "stream": False
    }
    response = requests.post(url, json = data)
    return response.json()["response"]

text_requests = [
    "Какая столица у России?",
    "Какая столица у Москвы?",
    "Посчитай: 987-789=?",
    "Переведи слово 'слово' на английский",
    "Жи-Ши пиши с буквой _ ?",
    "Расскажи анекдот про улитку",
    "В чем смысл жизни?",
    "Сколько сантиметров в 1 метре?",
    "Какая твоя любимая песня?",
    "Лучшее имя для мальчика?"
]

for r in text_requests:
    ans = send(r)
    print("•", r, " -> ", ans)
