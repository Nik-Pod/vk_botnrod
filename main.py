import vk_api, random, sqliter, random

token = "5261c9df5a17fb9107054f94c530880a41e12ec0352bd6b6a27b76534bd1f081a3c8f02092f56ed298035"

vk = vk_api.VkApi(token=token)
vk._auth_token()

nation = ['Ительмены', 'Карелы', 'Казахи', 'Грузины', 'Эвенки', 'Чукчи','Абхазы', 'Ненцы', 'Евреи', 'Цыгане', 'Ингуши', 'Чуваши', 'Чеченцы', 'Армяне', 'Аварцы', 'Азербайджанцы', 'Башкиры', 'Буряты', 'Якуты', 'Мордва', 'Удмурты', 'Осетинцы', 'Алтайцы', 'Кабардинцы', 'Ханты', 'Черкесы', 'Молдоване', 'Калмыки']

while True:
    messages = vk.method("messages.getConversations", {"offset": 0, "count":  20, "filter": "unanswered"})
    if messages["count"] > 0:
        text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        if text == 'Начать':
            msg = 'Для прохождения жеребьевки используйте команду:\n/get_nation ваш_класс\nПример: /get_nation 5-5'
            vk.method("messages.send", {"user_id": user_id, "message": msg, "random_id": random.randint(1, 1000)})
        elif '/get_nation' in text:
            msg = text.split('/get_nation ')[-1]
            if len(msg) != '':
                n = random.choice(nation)
                nation.remove(n)
                sqliter.add_class(msg, n)
                vk.method("messages.send", {"user_id": user_id, "message": n, "random_id": random.randint(1, 1000)})
