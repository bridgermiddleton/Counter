from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "this is the secretest of secret keys"
@app.route('/')
def counter():
    if 'views' in session:
        session['views'] += 1
    else:
        session['views'] = 1
    return render_template("index.html")

@app.route("/destroy_session", methods=["POST"])
def destroy():
    session.clear()
    return redirect("/")
    


if __name__=="__main__":
    app.run(debug=True)