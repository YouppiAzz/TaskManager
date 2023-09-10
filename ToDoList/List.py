from flask import Flask,render_template,request

app = Flask(__name__)

Tasks = []
DoneTasks = []

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if 'task' in request.form:
            newTask = request.form['task']
            Tasks.append(newTask)
        if "action" in request.form:
            action = request.form['action']
            if action == 'done':
                index = int(request.form['index'])
                DoneTasks.append(Tasks[index])
                del Tasks[index]
            elif action == 'delete':
                index = int(request.form['index'])
                del Tasks[index]
        


    return render_template("main.html", Tasks=enumerate(Tasks),DoneTasks=DoneTasks)

if __name__ == "__main__":
    app.run(debug=True, port="8000")