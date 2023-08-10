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

