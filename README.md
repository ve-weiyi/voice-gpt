## 按照python 语音sdk
pip install azure-cognitiveservices-speech
pip install requests
pip install flask

## 在/python目录下新建config.py文件
写入相关key

## 在/python目录下运行，启动服务，监听8080端口  
python api.py

## 调用接口，上传音频文件
post http://127.0.0.1:8080/api/v1/upload    
请求参数格式form-data     
file: 上传的音频文件(.wav格式)

