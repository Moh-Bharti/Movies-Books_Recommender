import numpy as np
import scipy as sp
from sklearn import linear_model
import Dataset_parser as dp
import io


#import tensorflow
movie="movies_metadata.csv"
book_rating="book_rating_data.csv"
def user_input():
    arr = 0
    w = 0
    val = input("Enter the name of movie: ")
    a,b,c,d,e,f=dp.info(movie)
    for i in range(len(c)):
        if val==c[i]:
            arr=i
            w = 1
            break
    if val=='#':
        return '#'
    if w==0:
        return "Not Present currently"
    else:
        return arr


"""def logi(arr_rating,arr_year):
    a, b, c, d, e = dp.info(movie)

    p_coeff = np.zeros((len(arr_rating),1))
    for i in  range(len(arr_rating)):




    #return arr_rating


#def naive_bayesian():

    #return 0

"""
def collab(arr_genre,arr_rating,arr_runtime,arr_adult,title,year):
    arr_near=[]

    mr , mg = dp.parser1(movie)
    a,b, c, d, e, f = dp.info(movie)

    for i in range(len(mg)):
        if c[i]!=title:
            p1 = sp.stats.pearsonr(mg[i],arr_genre)
            if np.all(p1)>0:
                r1 = np.sum(p1)

                p2 = abs(mr[i]-arr_rating)
                rtime = abs(f[i]-arr_runtime)
                if r1>0.95 and p2>=0 and p2<1 and rtime<=10 and arr_adult==a[i] and abs(e[i]-year)<5:

                    arr_near.append(c[i])

    return arr_near


def collab_filter(arr_input):
    br = dp.parser2(book_rating)

def find_genre(arr):
    genre = ['Action','Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Horror','Music','Mystery','Romance','Science Fiction','Thriller','War']
    movie_genre=[]
    for i in range(len(arr)):
        if arr[i]!=0:
            movie_genre.append(genre[i])

    return movie_genre




if __name__=='__main__':
    import warnings

    warnings.filterwarnings("ignore")

    a, b, c, d, e, f = dp.info(movie)
    mr, mg = dp.parser1(movie)
    movie_genre=[]
    movies = []
    with open('Movie_sets.txt') as file :
        films=file.readlines()
        films = [x.strip() for x in films]
        with io.open('Movie_info.txt','w',encoding='utf-8') as file1:
            file1.write('Films Seen by Users')
        file1.close()
        for i in range(len(films)):
            inp = list(c).index(films[i])
            with io.open('Movie_info.txt', 'w', encoding='utf-8') as file1:
                file1.write(str(films[i])+'--> Gentre:'+str(find_genre(mg[inp]))[1:-1]+',Year:'+str(e[inp])+',Runtime:'+str(f[inp]))
            file1.close()
            if len(movies) == 0:
                movies.append(collab(mg[inp], mr[inp], f[inp], a[inp], c[inp], e[inp]))
                # movies.append(inp)
            else:
                q = movies.pop()
                p = collab(mg[inp], mr[inp], f[inp], a[inp], c[inp], e[inp])
                # movies.append(inp)
                movies.append(list(set(q + p)))

    file.close()
    with io.open('Recommended_movies.txt', 'w', encoding='utf-8') as file1:
        file1.write('\n')
        file1.write('Recommended movies'+'\n')
        for j in range(len(movies[0])):
            ind = list(c).index(movies[0][j])

            movie_genre.append(find_genre(mg[ind]))
        movie_genre = np.asarray(movie_genre)
        movie_genre = [np.asarray(x) for x in movie_genre]
        movies = np.transpose(movies[0])

        for i in range(len(movies)):

            ind = list(c).index(movies[i])
            file1.write(movies[i]+ '--> Genre:'+str(movie_genre[i])[1:-1]+',Year:'+str(int(e[ind][0]))+',Runtime:'+str(f[ind])+'\n')
    file1.close()

    """while(True):
        inp = user_input()
        if inp=='#':
            break
        elif inp=="Not Present currently":
            print("Not Present currently")
        else:"""
