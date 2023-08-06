import requests
from config import YC_STT_API_KEY

# URL для отправки аудиофайла на распознавание
STT_URL = 'https://stt.api.cloud.yandex.net/speech/v1/stt:recognize'

def get_text_from_speech(file_url):
    # Выполняем GET-запрос по ссылке на аудиофайл
    response = requests.get(file_url)

    # Если запрос к серверу Telegram не удался...
    if response.status_code != 200:
        return None

    # Получаем из ответа запроса наш аудиофайл
    audio_data = response.content
    
    # Создам заголовок с API-ключом для Яндекс.Облака, который пошлем в запросе
    headers = {
        'Authorization': f'Api-Key {YC_STT_API_KEY}'
    }
    
    # Отправляем POST-запрос на сервер Яндекс, который занимается расшифровкой аудио,
    # передав его URL, заголовок и сам файл аудиосообщения
    response = requests.post(STT_URL, headers=headers, data=audio_data)

    # Если запрос к Яндекс.Облаку не удался...
    if not response.ok:
        return None

    # Преобразуем JSON-ответ сервера в объект Python
    result = response.json()
    # Возвращаем текст аудиосообщения
    return result.get('result')
