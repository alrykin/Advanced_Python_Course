import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import *
from app import STORE_TITLE#Импортируем глобальную переменную название магазина

# Texts(**{"title": "Greetings", "body": f"Вас приветствует {STORE_TITLE}"}).save()
# Texts(**{"title": "About", "body": f"Телеграм-бот-магазин {STORE_TITLE} был создан для того чтобы вы могли приобрести качественные алкогольные напитки не выходя из своего смартфона)))"}).save()
# Texts(**{"title": "Last news", "body": f"Внимение Акция! Магазин {STORE_TITLE} предлагает супер акцию, закажи 10 бутылок водки и получи еще одну в подарок !"}).save()

# g_vine_obj = Category(**{"title": "Грузинские вина", "description": "Вина из родины этого благородного напитка солнечной Грузии"}).save()
# ua_vine_obj = Category(**{"title": "Украинские вина", "description": "Отечественные вина"}).save()
#
# i_vodka_obj = Category(**{"title": "Импортная водка", "description": "Водка заграничного производства"}).save()
# ua_vodka_obj = Category(**{"title": "Украинская водка", "description": "Водка отечественного производства"}).save()
#
# stout_beer_obj = Category(**{"title": "СТАУТ (STOUT)", "description": "Плотный темный эль с густой кремовой пеной"}).save()
# ale_beer_obj = Category(**{"title": "ЭЛЬ (ALE)", "description": "Темный, горько-сладкий алкогольный напиток, приготавливаемый аналогично пиву"}).save()
#
#
# vodka_obj = Category(**{
#     "title": "Водка",
#     "description": "Крепкий алкогольный напиток, бесцветный водно-спиртовой раствор с характерным вкусом и спиртовым запахом."
#         }
#     ).save()
# vodka_obj.add_subcategory(i_vodka_obj)
# vodka_obj.add_subcategory(ua_vodka_obj)
# vodka_obj.save()
#
#
# vine_obj = Category(**{
#     "title": "Вино",
#     "description": "Алкогольный напиток получаемый полным или частичным спиртовым брожением виноградного сока (иногда с добавлением спирта и других веществ — так называемое «креплёное вино»)"
#         }
#     ).save()
#
# vine_obj.add_subcategory(g_vine_obj)
# vine_obj.add_subcategory(ua_vine_obj)
# vine_obj.save()
#
# beer_obj = Category(**{
#     "title": "Пиво", "description": "Слабоалкогольный напиток, получаемый спиртовым брожением солодового сусла"
#         }
#     ).save()
#
# beer_obj.add_subcategory(stout_beer_obj)
# beer_obj.add_subcategory(ale_beer_obj)
# beer_obj.save()
#
#
# strong_alco_obj = Category(**{"title": "Крепкие алкогольные напитки", "description": "содержание спирта от 30 до 65 %об."}).save()
# strong_alco_obj.add_subcategory(vodka_obj)
# strong_alco_obj.save()
#
# semi_alco_obj = Category(**{"title": "Среднеалкогольные напитки", "description": "содержание спирта от 9 до 30 %об."}).save()
# semi_alco_obj.add_subcategory(vine_obj)
# semi_alco_obj.save()
#
# low_alco_obj = Category(**{"title": "Слабоалкогольные напитки", "description": "содержание спирта от 1,5 до 8 %об."}).save()
# low_alco_obj.add_subcategory(beer_obj)
# low_alco_obj.save()
#
#
# Product(**{
#     "title": "Водка Finlandia",
#     "description": "vodka from Finland",
#     "price": 18900,
#     "new_price": 16900,
#     "is_discount": True,
#     "properties": Properties(**{"weight": 0.5}),
#     "category": i_vodka_obj,
#
#     }
# ).save()
#
# priduct_obj = Product(**{
#     "title": "Водка Nemiroff Premium De Luxe",
#     "description": "Премиум водка от именитого Украинского производителя",
#     "price": 17900,
#     "new_price": 0,
#     "is_discount": False,
#     "properties": Properties(**{"weight": 0.7}),
#     "category": ua_vodka_obj,
#     }
# ).save()
#
#
# priduct_obj = Product(**{
#     "title": "Вино Saperavi",
#     "description": "Красное полусладкое; Производитель: Ichkitidze Gocha's Estate Wines; Крепость: 13%; Сахар: 3г/л",
#     "price": 33500,
#     "new_price": 0,
#     "is_discount": False,
#     "properties": Properties(**{"weight": 0.75}),
#     "category": g_vine_obj,
#     }
# ).save()
#
#
# priduct_obj = Product(**{
#     "title": "Вино Шардоне",
#     "description": "Белое Сухое; Производитель: Колонiст; Крепость: 13%",
#     "price": 19400,
#     "new_price": 0,
#     "is_discount": False,
#     "properties": Properties(**{"weight": 0.75}),
#     "category": ua_vine_obj,
#     }
# ).save()
#
# priduct_obj = Product(**{
#     "title": "Пиво BrewDog Cocoa Psycho",
#     "description": "Имперский стаут; Производитель: Brew Dog,; Крепость: 10%",
#     "price": 19900,
#     "new_price": 0,
#     "is_discount": False,
#     "properties": Properties(**{"weight": 0.33}),
#     "category": stout_beer_obj,
#     }
# ).save()
#
# priduct_obj = Product(**{
#     "title": "Пиво Easy IPA",
#     "description": "Эль с пряными нотками; Производитель: Flying Dog; Крепость: 4.7%",
#     "price": 9500,
#     "new_price": 0,
#     "is_discount": False,
#     "properties": Properties(**{"weight": 0.33}),
#     "category": ale_beer_obj,
#     }
# ).save()
