import streamlit as st
import pickle
import pandas

movie_file = open('movie_dump.pkl','rb')
movie_data = pickle.load(movie_file)
movie_names = movie_data['title']
movie_file.close()

sim_file = open('similarity.pkl','rb')
similarity = pickle.load(sim_file)
sim_file.close()

def recommend_movie(movie_name):
    # find movie in the movie_data
    movie_indx = -1
    for i in range(0,movie_data.shape[0]):
        if movie_names[i] == movie_name:
            movie_indx = i
            break
    if movie_indx == -1:
        print("Movie Not Found in DB!!")
        return []
    
    distances = list(enumerate(similarity[movie_indx]))
    movies_list = sorted(distances,reverse=True,key=lambda x:x[1])[1:-1]
    return movies_list

def show_recommended_movie(movie_name):
    movies_list = recommend_movie(movie_name)
    movies = []
    for i in range(0,5):
        posn = movies_list[i][0]
        id_ = movie_data['id'][posn]
        name_ = movie_names[posn]
        movies.append([id_,name_])
    
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(movies[0][1])
    with col2:
        st.text(movies[1][1])
    with col3:
        st.text(movies[2][1])
    with col4:
        st.text(movies[3][1])
    with col5:
        st.text(movies[4][1])
    return movies_list
    
# print(movie_data['title'].head())

st.title("Movie Recommendation System")

option = st.selectbox("Choose a Movie",movie_data['title'],placeholder='Choose a Movie')
movies_list = []
ptr = 0
if st.button("Recommend"):
    movies_list = show_recommended_movie(option)
    ptr += 5