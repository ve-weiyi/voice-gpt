from flask import Flask, request, jsonify, send_file
import os

from speech_chat import chatGptApi
from speech_recognition import recognize_from_wavfile
from speech_synthesis import synthesize_text_to_file

app = Flask(__name__)


@app.route('/api/v1/upload', methods=['POST'])
def upload_file():
    # 检查是否有上传的文件
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # 检查文件名是否合法
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 检查文件扩展名是否为 .wav
    if file and file.filename.endswith('.wav'):
        # 将文件保存到指定路径
        print("filename", file.filename)
        file.save(os.path.join(file.filename))
        # 只能读取本地文件
        text = recognize_from_wavfile(file.filename).text
        print("input", text)
        msgs = []
        # 添加本次提问的消息
        msgs.append(
            {
                "role": "user",
                "content": text
            }
        )
        # 与gpt对话
        data = chatGptApi(msgs)

        # 提取回复文字
        choices = data['choices']
        out_text = choices[0]['message']['content']

        # 替换为您的本地 .wav 文件路径
        audio_file_path = './output.wav'
        # 文字转语音
        synthesize_text_to_file(out_text, audio_file_path)

        # 设置 MIME 类型为 audio/wav
        mimetype = 'audio/wav'

        # 使用 send_file 函数返回文件内容
        return send_file(audio_file_path, mimetype=mimetype)
        # return jsonify({'message': 'File uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
