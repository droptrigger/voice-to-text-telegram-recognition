[Russian](ruREADME.md)
<div align="center">

# Voice to text translator

Telegram bot, for recognizing text from voice messages or video messages.

</div>


## 📖 Description
The bot allows you to translate voice messages and video notes into text form.\
You just need to forward or record such messages.

The translation is carried out by a trained vosk model, which you can pump if you know how, of course __:)__

You can also add a text recognition function from the video, and in general, do what you go __xD__


## 🧐 Instruction

#### 0. First, you need to clone the repository to your computer;

#### 1. The next step is to install the necessary libraries (versions are written in [constants](main/constants.py));

```
pip install vosk
pip install soundfile 
pip install aiogram
pip install moviepy
pip install librosa
```
#### 2. Next, you need to download the vosk model for your language from the [official website](https://alphacephei.com/vosk/models);
* P.S: Personally, small models work better for me

#### 3. After installation, unzip the model to the root folder;

#### 4. Next, using https://t.me/BotFather create a bot and get its token;

#### 5. Enter the received token and the path to the vosk model in the file [constants](main/constants.py).


## ✅ That's it, now you can launch the bot

If you still want to upgrade your vosk model, try this method - https://habr.com/ru/articles/735480/