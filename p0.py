import csv
from flask import Flask, request, render_template
import random

app = Flask(__name__)

def read_movies_from_csv():
    movies = []
    with open('movies.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movies.append({
                'title': row['title'],
                'genre': row['genre'],
                'year': int(row['year']),
                'rating': float(row['rating'])
            })
    return movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    genre = request.form['genre']
    start_year = int(request.form['start_year'])
    end_year = int(request.form['end_year'])
    start_rating = float(request.form['start_rating'])
    end_rating = float(request.form['end_rating'])

    # Read movies data from CSV
    movies = read_movies_from_csv()

    # Filter movies based on user inputs (you can modify the criteria based on your needs)
    recommended_movies = [
        movie for movie in movies
        if movie['genre'] == genre
        and start_year <= movie['year'] <= end_year
        and start_rating <= movie['rating'] <= end_rating
    ]

    # Shuffle the list of recommended movies and choose the top 5
    random.shuffle(recommended_movies)
    top_5_recommendations = recommended_movies[:5]

    return render_template('recommendations.html', movies=top_5_recommendations)

if __name__ == '__main__':
    app.run(debug=True)

