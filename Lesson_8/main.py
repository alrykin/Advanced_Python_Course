# 1) Создать базу данных товаров, у товара есть: Категория (связанная таблица),
# название, есть ли товар в продаже или на складе, цена, кол-во единиц.Создать html страницу.
# На первой странице выводить ссылки на все категории, при переходе на категорию получать
# список всех товаров в наличии ссылками, при клике на товар выводить его цену, полное описание и кол-во единиц в наличии.
# 2) Создать страницу для администратора, через которую он может добавлять новые товары и категории.
from flask import  Flask, render_template, request
import sqlite3

class DBContextManager:

    def __init__(self, db):
        self._db = db

    def __enter__(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.commit()
        self._conn.close()


app = Flask(__name__)
db = "estore.db"
store_title = "eStore"

@app.route("/")
def home():
    with DBContextManager(db) as db_obj:
        request = db_obj.execute("select category_name, id from categories")
        result = request.fetchall()
    categories_dict = {key: value for (key, value) in result}
    return render_template("index.html", store_title=store_title, categories_dict=categories_dict)

@app.route("/goods/<category>/<id>/")
def goods_by_id(id, category):
    with DBContextManager(db) as db_obj:
        sql = "select name, id from goods where category = ? and  (for_sale_count or on_stock_count) > 0"
        request = db_obj.execute(sql, [id])
        result = request.fetchall()
    goods = {key: value for (key, value) in result}
    return render_template("goods.html", category = category, store_title=store_title, goods=goods)

@app.route("/item_detail/<id>")
def item_detail(id):
    with DBContextManager(db) as db_obj:
        sql = "select * from goods where id = ?"
        request = db_obj.execute(sql, [id])
        item = request.fetchall()[0]
    specification = item[6].replace('\n', '<br>')
    return render_template("item_detail.html", item=item, store_title=store_title, specification=specification)

@app.route("/admin")
def admin_home():
    with DBContextManager(db) as db_obj:
        request = db_obj.execute("select category_name, id from categories")
        result = request.fetchall()
    categories_dict = {key: value for (key, value) in result}
    return render_template("admin.html", store_title=store_title, categories_dict=categories_dict)

@app.route("/add_category", methods = ['POST'])
def add_category():
    return 'Done'
@app.route("/add_item", methods = ['POST'])
def add_item():
    return 'Done'


if __name__ == "__main__":
    app.run(debug=True)
