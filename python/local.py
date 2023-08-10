import time

from speech_chat import chatGptApi
from speech_recognition import recognize_from_microphone
from speech_synthesis import synthesize_text_to_speech


def loop_chat_voice(msgs):
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
    loop_chat_voice(msgs)


# 附带上下文的问答
loop_chat_voice([])
