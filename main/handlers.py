import tempfile
import wave
import json
import io
import librosa
import soundfile as sf

from moviepy.editor import VideoFileClip
from vosk import Model, KaldiRecognizer, SetLogLevel
from aiogram import Router, Bot
from aiogram.types import Message

from constants import token, path_model, FRAME_RATE

router = Router()
bot = Bot(token)

SetLogLevel(0)

model = Model(path_model)
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)


async def read(voice_file):
    """translation to voice"""

    result = ""
    last_n = False

    wf = wave.open(voice_file, "rb")

    while True:
        data = wf.readframes(32000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())

            if res['text'] != '':
                result += f" {res['text']}"
                last_n = False
            elif not last_n:
                result += '\n'
                last_n = True

    res = json.loads(rec.FinalResult())
    result += f"{res['text']}"

    return result.capitalize()


async def print_result(file, message):
    y, sr_ = librosa.load(file, sr=16000)
    file.close()

    voice_file = io.BytesIO()
    sf.write(voice_file, y, sr_, format='WAV', subtype='PCM_16')
    voice_file.seek(0)

    result = await read(voice_file)

    if len(result) > 0:
        await message.reply(result.capitalize())
    else:
        await message.reply("У меня не получилось, хочется плакать :(")


@router.message()
async def general(message: Message):
    """Eating all messages"""

    if message.voice is not None:
        voice_file = io.BytesIO()
        await bot.download(message.voice.file_id, voice_file)
        await print_result(voice_file, message)

    if message.video_note is not None:
        input_video_byte_io = io.BytesIO()
        await bot.download(message.video_note.file_id, input_video_byte_io)

        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_video_file:
            temp_video_file.write(input_video_byte_io.read())
            temp_video_path = temp_video_file.name

        video_clip = VideoFileClip(temp_video_path)
        audio_clip = video_clip.audio

        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_audio_file:
            temp_audio_path = temp_audio_file.name
            audio_clip.write_audiofile(temp_audio_path)

        video_clip.close()
        audio_clip.close()

        with open(temp_audio_path, 'rb') as audio_file:
            audio_byte_io = io.BytesIO(audio_file.read())

        temp_video_file.close()
        temp_audio_file.close()

        await print_result(audio_byte_io, message)
