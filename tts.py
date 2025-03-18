from espeakng import ESpeakNG

esng_cfg = {
    "voice": 'es-419',
    "audio_dev": 0,
    "pitch": 90,
    "word_gap": 1,
    "speed": 180,
}

_esng = ESpeakNG(**esng_cfg)

def say(text):
    print("tts:", text)
    _esng.say(text, sync=True)

