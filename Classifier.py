import numpy as np
import scipy as sp
from sklearn import linear_model
import Dataset_parser as dp
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
                if r1>0.9 and p2>=0 and p2<1 and rtime<=10 and arr_adult==a[i] and abs(e[i]-year)<5:

                    arr_near.append(c[i])

    return arr_near


def collab_filter(arr_input):
    br = dp.parser2(book_rating)



if __name__=='__main__':
    import warnings

    warnings.filterwarnings("ignore")

    """a, b, c, d, e, f = dp.info(movie)
    mr, mg = dp.parser1(movie)
    movies = []
    while(True):
        inp = user_input()
        if inp=='#':
            break
        elif inp=="Not Present currently":
            print("Not Present currently")
        else:
            if len(movies)==0:
                movies.append(collab(mg[inp], mr[inp], f[inp], a[inp],c[inp],e[inp]))
                #movies.append(inp)
            else:
                q = movies.pop()
                p = collab(mg[inp], mr[inp], f[inp], a[inp],c[inp],e[inp])
                #movies.append(inp)
                movies.append(list(set(q+p)))

    print(movies)
    print(np.shape(movies))"""
