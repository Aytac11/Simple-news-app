from flask import Flask, render_template,request
from data import News,news
app = Flask(__name__)

@app.route("/news")
def xeber():
    return render_template('index.html', data=news)

@app.route("/single/<int:id>")
def SingleNews(id):
     return render_template('single.html', news_id=id, data=news)

# @app.route("/add", methods =["get","post"])
# def add():
#     if request.method=="post":
#         news_title=request.form['title']
#         news_detail=request.form['detail']
#     return render_template('add_news.html',title=news_title,detail=news_detail)
if __name__ == "__main__":
    app.run(debug=True)
