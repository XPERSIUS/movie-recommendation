import pickle
import pandas as pd
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    recommend_movies_posters=[]
    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append((i[0]))
    return recommend_movies,recommend_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)
st.title('movie recommender')


similarity=pickle.load(open('similarity.pkl', 'rb'))
selected_movie_name=st.selectbox('How would u',movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    for i in names:
        st.text(i)

    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(names[0])
    #     st.image(posters[0])
    # with col2:
    #     st.text(names[1])
    #     st.image(posters[1])
    #
    # with col3:
    #     st.text(names[2])
    #     st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])





