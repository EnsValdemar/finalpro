import config
import requests

# Функция для создания заказа
# Используем метод POST из библиотеки requests и указываем полный путь и тело запроса
def post_new_order(order_body):
    # Отправляем запрос на создание заказа, передаём тело запроса
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=order_body)

# Функция для получения заказа по его трек номеру
# Используем метод GET из библиотеки requests и указываем полный путь
# В конце пути добавляем трек номер (тип данных - строка)
def get_order_by_track_number(track_number):
    # Отправляем запрос на получение заказа по треку заказа.
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH + str(track_number))




