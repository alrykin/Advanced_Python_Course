from flask import  Flask, render_template, request

app = Flask(__name__)


@app.route("/<string:id>")
def hello_world(id):
    print(request.args)
    print(request.json)
    return "Hello world"

@app.route("/my-new-route")
def my_route():
    my_list = ["1","2","3"]
    users = {
    "John": "New user",
    "Ales": "New user",
    "Janny": "Old user"
    }
    title = "Main page"
    return render_template("index.html",
                            data = "my_data",
                            title = title,
                            users=users,
                            my_list = my_list)

if __name__ == "__main__":
    app.run(debug=True)
