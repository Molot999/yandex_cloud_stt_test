from config import bot, BOT_TOKEN
from telebot.types import Message, Voice
from yandex_cloud import get_text_from_speech

# Используем декоратор из объекта класса TeleBot, в который передаем параметр commands - список команд, при вызове которых будет вызываться данная функция
@bot.message_handler(commands=['start']) 
def start(message:Message): # Определяем функцию для обработки команды /start, она принимает объект класса Message - сообщение
    bot.send_message(message.chat.id, "Йоу! Отправь мне аудиосообщение") # Отправляем новое сообщение, указав ID чата с пользователем и сам текст сообщения

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    voice:Voice = message.voice
    file_id = voice.file_id
    voice_file = bot.get_file(file_id)
    voice_path = voice_file.file_path
    file_base_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{voice_path}"
    speech_text = get_text_from_speech(file_base_url)
    bot.send_message(message.chat.id, speech_text)

if __name__ == "__main__":
    bot.polling(non_stop=True)
