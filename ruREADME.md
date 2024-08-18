[English](README.md)
<div align="center">

# Переводчик голоса в текст


Telegram-бот для распознавания текста из голосовых сообщений или видеосообщений.

</div>


## 📖 Описание

Бот позволяет переводить голосовые сообщения и видеозаписи в текстовую форму.\
Вам просто нужно переслать или записать такие сообщения.

Перевод осуществляется обученной моделью vosk, которую вы можете прокачать, если знаете как, конечно __:)__

Также вы можете добавить функцию распознавания текста из видео, и вообще, делайте, что хотите __xD__


## 🧐 Инструкция

#### 0. Во-первых, вам нужно клонировать репозиторий на свой компьютер;

#### 1. Следующим шагом будет установка необходимых библиотек (версии написаны в [constants](main/constants.py));

```
pip install vosk
pip install soundfile 
pip install aiogram
pip install moviepy
pip install librosa
```
#### 2. Далее вам нужно загрузить модель vosk для вашего языка с [официального сайта](https://alphacephei.com/vosk/models);
* P.S: Лично у меня модели `small` работают лучше

#### 3. После установки распакуйте модель в корневую папку;

#### 4. Далее с помощью https://t.me/BotFather создайте бота и получите его токен;

#### 5. Введите полученный токен и путь к модели vosk в файле [constants](main/constants.py).


## ✅ Вот и все, теперь вы можете запускать бота

Если вы все же хотите прокачать свою модель vosk, попробуйте данный метод - https://habr.com/ru/articles/735480/