import os
import time

import azure.cognitiveservices.speech as speechsdk
import requests
import json

import config
from speech_synthesis import synthesize_text_to_speech
from speech_recognition import recognize_from_microphone


def chatGptApi(msg):
    # 定义本地接口的地址
    # url = "http://localhost:9999/api/v1/ai/chat"  # 替换为你的本地接口地址
    url = config.gpt_url

    # 设置请求头
    headers = {
        'Content-Type': 'application/json',  # 指定请求的内容类型为 JSON
        'api-key': config.api_key,  # 添加您的授权令牌
    }

    data = {
        'model': config.model,
        'messages': msg,
    }
    # 发送 POST 请求到本地接口
    response = requests.post(url, headers=headers, json=data)
    print("gpt response:", response.json())
    return response.json()


def voice(msgs):
    # 读取语言转文字
    text = recognize_from_microphone().text
    print("input:", text)

    # 添加本次提问的消息
    msgs.append(
        {
            "role": "user",
            "content": text
        }
    )
    # 文字转语音
    data = chatGptApi(msgs)
    choices = data['choices']

    synthesize_text_to_speech(choices[0]['message']['content'])
    time.sleep(1)
    # 添加gpt回答的消息
    msgs.append(choices[0]['message'])

    # 递归调用 voice()，传入新的 msgs 列表
    voice(msgs)

# 附带上下文的问答
# voice([])
# print("data:", data)
# print("data 1:", data['choices'])
# print("data 2:", data['choices'][0])
# print("data 3:", data['choices'][0]['message'])
# print("data 3:", data['choices'][0]['message']['content'])
