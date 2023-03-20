# -*- coding: utf-8 -*-
# @Author : haowen.zhu
# @Time : 2023/3/18 23:21
# @File : ChatGPT.py
import logging
import requests
import json

logging.basicConfig(level=logging.DEBUG)


def get_chaggpt_ans(question):
    url = "https://api.openai.com/v1/chat/completions"

    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "user",
                "content": f"{question}"
            }
        ],
        "temperature": 0.7
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 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'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    # 将字符串解析为字典
    data = json.loads(response.text)
    if response.status_code == 200:
        logging.debug(f"chatGPT返回：{response.text}")
        # 访问content中的数据
        content = data["choices"][0]["message"]["content"]
    else:
        content = f"resp error: {response.status_code}"

    print(content)
    return content


def chat_multi_turn():
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    prompt = "Hello, how are you doing today?"
    chat_history = ['1']
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer "
    }
    for i in range(5):
        data = {
            "prompt": prompt,
            "max_tokens": 50,
            "temperature": 0.5,
            "stop": "\n",
            "n": 1,
            "context": chat_history
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        # print(response.text)
        json_data = json.loads(response.text)
        message = json_data["choices"][0]["text"]
        print(message)
        chat_history.append(prompt)
        chat_history.append(message)
        prompt = message


def start_conversation():
    print("Hi, I'm ChatGPT.")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Bye")
            break
        get_chaggpt_ans(question)


if __name__ == '__main__':
    start_conversation()
    # chat_multi_turn()
