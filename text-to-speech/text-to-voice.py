from gtts import gTTS

text = "नमस्ते, यह एक उदाहरण है कि कैसे आप टेक्स्ट को हिंदी में ऑडियो में बदल सकते हैं।"

tts = gTTS(text=text, lang='hi') # we can use en for english or hi for hindi

tts.save("output.mp3")

print("audio saved successfully as output.mp3")