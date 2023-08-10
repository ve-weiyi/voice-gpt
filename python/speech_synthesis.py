import io
import os
import azure.cognitiveservices.speech as speechsdk

import config

# 设置语音合成配置
speech_config = speechsdk.SpeechConfig(subscription=config.speech_key, region=config.speech_region)
# 设置语音合成语言和声音
# speech_config.speech_synthesis_language = "en-US"
# speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'
speech_config.speech_synthesis_voice_name = 'zh-CN-YunxiNeural'


# 将语音输出到麦克风
def synthesize_text_to_speech(text):
    # 将语音输出到麦克风
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    # 创建语音合成器
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    try:
        # 合成文本为语音
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
    except Exception as e:
        print("Error:", str(e))


# 将语音输出到文件
def synthesize_text_to_file(text, filename):
    # 将语音输出到麦克风
    # audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
    # 创建一个内存字节流作为输出流
    # output_stream = io.BytesIO()
    # audio_config = speechsdk.audio.AudioOutputConfig(stream=speechsdk.audio.AudioOutputStream(handle=output_stream))
    # 创建语音合成器
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    try:
        # 合成文本为语音
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
    except Exception as e:
        print("Error:", str(e))
