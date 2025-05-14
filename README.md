# 🎬 Movie Recommendation System

A simple content-based movie recommender that suggests movies similar to the one provided by the user, based on metadata like genres, cast, crew, and overview.

## 🚀 Features
- Takes a movie name as input and returns similar movies
- Uses textual metadata (cast, crew, genre, etc.) and NLP to calculate similarity
- Lightweight and easy to understand
- Clean and responsive web UI built using HTML & CSS
- Enter a movie name and get 6 similar movies as recommendations


## 🛠️ How It Works
1. Combine metadata fields (genres, cast, crew, overview)
2. Convert combined text into vectors and generate word embeddings using "word2vec"
3. Compute similarity between movie vectors using `NearestNeighbors`
4. Return top 5 similar movies

## 📦 Tech Stack
- Python
- pandas, numpy
- scikit-learn
- gensim

## 📂 Folder Structure
<pre> 📦 movie-recommendation/ 
    ├── files/ 
    │ ├── Title_ids.csv 
    │ ├── cast.json 
    │ ├── directors.json 
    │ ├── genres.json  
    │ └── similarities.json 
    ├── static/ 
    │ ├── aboutstyle.css 
    │ ├── homestyle.css 
    │ ├── layoutstyle.css 
    │ ├── i1.jpg 
    │ ├── i2.jpg 
    │ ├── link.png 
    │ ├── logo.png 
    │ └── unnamed.png 
    ├── templates/ 
    │ ├── about.html 
    │ ├── contact.html 
    │ ├── index.html 
    │ └── layout.html 
    ├── .gitignore 
    ├── Recommender.ipynb 
    ├── app.py 
    ├── config.json 
    ├── data.txt 
    ├── recomendation_system.txt 
    ├── requirements.txt 
    └── README.md </pre>

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommendation.git
cd movie-recommendation

pip install -r requirements.txt

python app.py
```

Open browser and navigate to <br>
http://127.0.0.1:5000/
