# edge-tts (Microsoft Edge Voices) ⭐ Recommended
# ✅ High-quality neural voices
# ✅ Free
# ✅ Many languages and accents
# ❌ Internet required

import asyncio  # Python's built-in library for asynchronous programming. It lets you run tasks that can wait for operations (like network requests) without blocking the program.
import edge_tts # A Python package that accesses Microsoft's Edge Text-to-Speech service.

async def main(): # an asynchronous function that will handle the text-to-speech conversion. The 'async' keyword allows the function to perform tasks that may take time (like network requests) without freezing the program.
    communicate = edge_tts.Communicate(
        "Hello! This voice sounds very natural.",
        "en-US-AriaNeural"
    )
    await communicate.save("speech.mp3")  # await is used to pause the function until the save operation is complete, ensuring that the audio file is fully written before proceeding.

asyncio.run(main())

print("audio saved successfully as speech.mp3")