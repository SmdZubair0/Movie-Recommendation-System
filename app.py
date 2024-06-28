from flask import Flask,request,render_template
import requests as rs
import pickle as pkl
import pandas as pd
import json

with open("config.json") as f:
    API_KEY = json.load(f)['api_key']

def fetch_poster(i,ps):
    response = rs.get(f"https://api.themoviedb.org/3/movie/{i}?api_key="+API_KEY)
    data = response.json()
    try:
        return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    except:
        return "https://image.tmdb.org/t/p/w500/"+ps

df = pd.read_csv('files/Title_ids.csv')
similarities = json.load(open('files/similarities.json','rb'))

movieslist = list(df['title'].values)


app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def home():
    movies = []
    movieimgs = []

    if request.method == 'POST':
        name = request.form.get("moviename")
        id = df[df['title'].str.lower() == name.lower()].id.values[0]

        d = similarities[str(id)]
        for i in d:
            movieid = i
            movie = df[df.id==movieid].title.values[0]
            ps = df[df.id==movieid].poster_path.values[0]
            movies.append(movie)
            movieimgs.append(fetch_poster(movieid,ps))
        
        print(movies)
        return render_template("index.html",predicted=zip(movies,movieimgs),movielist=movieslist)
    return render_template("index.html",predicted=[],movielist=movieslist)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)