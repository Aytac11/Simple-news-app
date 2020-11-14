from flask import Flask, render_template
from data import News,news
app = Flask(__name__)

@app.route("/news")
def xeber():
    return render_template('index.html', data=news)

@app.route("/single/<int:id>")
def SingleNews(id):
     return render_template('single.html', news_id=id, data=news)

if __name__ == "__main__":
    app.run(debug=True)
