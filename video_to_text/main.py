import whisper

"""
1 tiny → smallest and fastest

2 base → small with good accuracy

3 small → better accuracy

4 medium even better accuracy

5 large → highest accuracy, but requires more resources

"""

model = whisper.load_model("base")

result = model.transcribe("##")

print(result["text"])