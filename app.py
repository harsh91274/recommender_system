import streamlit as st
import pickle 
import requests

movies=pickle.load(open("movies_list.pkl", 'rb'))
movies_list=movies['title'].values

similarity=pickle.load(open("similarity.pkl", 'rb'))

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=4fee081e814556a22cd6f0b1d0f77802&language=en-US".format(movie_id)
#     data=requests.get(url)
#     data=data.json()
#     poster_path=data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
#     return full_path

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=4fee081e814556a22cd6f0b1d0f77802&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path



def recommend(movie):
    index=movies[movies['title']==movie].index[0] #get index of input movie
    distance=sorted(list(enumerate(similarity[index])), reverse=True, key= lambda vector:vector[1])

    recommend_movies=[]
    recommend_posters=[]
    for i in distance[0:5]:
        #print(new_data.iloc[i[0]].title)
        movies_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movies_id))
    
    return recommend_movies


###STREAMLIT APP###
st.header("Movie Recommender System")
select_value=st.selectbox("Select movie from dropdown", movies_list)


if st.button("Show Recommendations"):
    movie_name, movie_posters=recommend(select_value)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(movie_names[0])
        st.image(movies_posters[0])

    with col2:
        st.text(movie_names[1])
        st.image(movies_posters[1])

    with col3:
        st.text(movie_names[2])
        st.image(movies_posters[2])

    with col4:
        st.text(movie_names[3])
        st.image(movies_posters[3])

    with col5:
        st.text(movie_names[4])
        st.image(movies_posters[4])
