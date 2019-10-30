# from my_course_notes.Lesson_10_notes.models.workers import Person, Location
# print(sys.path)
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from models.blog import Author, Post


author_obj = Author(first_name="Aleksandr", last_name="Yaremenko").save()
post_text = """
(ООП) — методология программирования, основанная на представлении
программы в виде совокупности объектов, каждый из которых является экземпляром
определённого класса, а классы образуют иерархию наследования.
"""
post_dict = {
    "title" : "Основы ООП",
     "post" : post_text,
     "view_count": 0,
     "author" : author_obj,
     "tag" : "программирование",
}
Post(**post_dict).save()

#
# sub_cat_obj = SubCategory(name="tequila", description="drink for real amigos")
# cat_obj = ItemCategory(**{"name": "strong alcohol", "subcategory": sub_cat_obj})
# item_dict = {
#     "name" : "Espolon 0.7",
#     "intems_count" : 39,
#     "category" : cat_obj,
#     "price" : 459,
#     "view_count" : 0
# }
# Item(**item_dict).save()
#
#
# sub_cat_obj = SubCategory(name="beer", description="alcoholic drink obtained by fermentation")
# cat_obj = ItemCategory(**{"name": "low alcohol", "subcategory": sub_cat_obj})
# item_dict = {
#     "name" : "obolon svetloe 0.5",
#     "intems_count" : 1000,
#     "category" : cat_obj,
#     "price" : 20,
#     "view_count" : 0
# }
# Item(**item_dict).save()
