
# Вальдемар Энс, 10-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_requests

    # Автотест для создания заказа и проверки, что по треку заказа можно получить данные о заказе
def test_auto_test():

    # Сохраняем в переменную track_number значение ключа 'track' в формате json (из ответа на POST-запрос)
    # Передаём в функцию для создания заказа параметр order_body из файла data
    track_number = sender_stand_requests.post_new_order(data.order_body).json()['track']

    # Сохраняем в переменную response результат вызова функции для получения заказа по его трек номеру
    # Передаём в функцию для получения заказа по его трек номеру параметр track_number (объявленную выше переменную)
    response = sender_stand_requests.get_order_by_track_number(track_number)

    # Проверяем, что код ответа равен 200
    assert response.status_code == 200


