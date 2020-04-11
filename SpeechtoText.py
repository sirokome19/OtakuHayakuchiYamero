import azure.cognitiveservices.speech as speechsdk
import json

# Reference
# https://docs.microsoft.com/ja-jp/azure/cognitive-services/speech-service/quickstarts/speech-to-text-from-microphone?tabs=dotnet%2Cx-android%2Clinux%2Cjava-runtime&pivots=programming-language-python

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
def speechtotext():
    with open("api_keys.json","r") as f:
        subscription_info=json.load(f)
    speech_key, service_region = subscription_info["key"], subscription_info["region"]
    speech_config = speechsdk.SpeechConfig(
        subscription=speech_key, region=service_region)

    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, language="ja-JP")

    print("喋ってください")


    # Starts speech recognition, and returns after a single utterance is recognized. The end of a
    # single utterance is determined by listening for silence at the end or until a maximum of 15
    # seconds of audio is processed.  The task returns the recognition text as result.
    # Note: Since recognize_once() returns only a single utterance, it is suitable only for single
    # shot recognition like command or query.
    # For long-running multi-utterance recognition, use start_continuous_recognition() instead.
    result = speech_recognizer.recognize_once()
    
    # Checks result.
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        sentence = result.text
        talking_time=result._duration*(10**-7) #100ns->1s
        print("Recognized: {}".format(sentence))
        return sentence, talking_time
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
    return "", 0
if __name__ == "__main__":
    speechtotext()