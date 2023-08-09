import os
import azure.cognitiveservices.speech as speechsdk



def synthesize_text_to_speech(text):
    # 设置语音合成配置
    print('SPEECH_KEY', os.environ.get('SPEECH_KEY'))
    print('SPEECH_REGION', os.environ.get('SPEECH_REGION'))
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'),
                                           region=os.environ.get('SPEECH_REGION'))
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # The language of the voice that speaks.

    # speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'
    speech_config.speech_synthesis_voice_name = 'zh-CN-YunxiNeural'
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


# 调用函数并传入要转换为语音的文本
# print("Enter some text that you want to speak >")
# text = input()
# synthesize_text_to_speech(text)




