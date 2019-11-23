import pandas as pd
import sklearn as sk
import json
import re
import numpy as np
import csv
import matplotlib.pyplot as plt

def info(filename):
    arr = pd.read_csv(filename).to_numpy()
    id = arr[:, 5]
    title = arr[:, 8]
    pop = arr[:, 10]
    year = arr[:, 14]
    year1 = np.zeros((len(year),1))
    for i in range(len(year)):

        year1[i] = int(year[i][-4:])
    rtime = arr[:, 16]
    ad = arr[:,0]

    return ad,id,title,pop,year1,rtime

def parser1(filename):
    arr = pd.read_csv(filename).to_numpy()
    genre = arr[:,3]
    genre_json=(pd.DataFrame(genre).values)
    genre_movie=genre_parser(genre_json)

    #genre_dict=json.loads(genre_json)

    rating = arr[:,22]
    array = rating_calc(rating)
    return array,genre_movie
def rating_calc(arr):
    array = np.empty(np.shape(arr))
    rat = np.zeros((11,1))
    for i in range(len(arr)):
        array[i]=arr[i]/2
        if array[i]>=0 and array[i]<0.5:
            array[i]=0
            rat[0]+=1
        elif array[i]>=0.5 and array[i]<1:
            array[i]=0.5
            rat[1]+=1
        elif array[i]>=1 and array[i]<1.5:
            array[i]=1
            rat[2]+=1
        elif array[i]>=1.5 and array[i]<2:
            array[i]=1.5
            rat[3]+=1
        elif array[i]>=2 and array[i]<2.5:
            array[i]=2
            rat[4]+=1
        elif array[i]>=2.5 and array[i]<3:
            array[i]=2.5
            rat[5]+=1
        elif array[i]>=3 and array[i]<3.5:
            array[i]=3
            rat[6]+=1
        elif array[i]>=3.5 and array[i]<4:
            array[i]=3.5
            rat[7]+=1
        elif array[i]>=4 and array[i]<4.5:
            array[i]=4
            rat[8]+=1
        elif array[i]>=4.5 and array[i]<5:
            array[i]=4.5
            rat[9]+=1
        else:
            rat[10]+=1
            array[i]=5

    return array
def genre_parser(string):
    n = len(string)
    arr = np.zeros((n,17))

    for i in range(len(string)):
        text = string[i][0]
        dict = re.split('[{,}]\s',text[1:len(text)-1])
        for j in range(len(dict)//2):
            a = dict[2*j+1]
            a = a[9:len(a)-2]
            if a=='Action':
                arr[i,0]=1
            elif a=='Adventure':
                arr[i,1]=1
            elif a=='Animation':
                arr[i,2]=1
            elif a=='Comedy':
                arr[i,3]=1
            elif a=='Crime':
                arr[i,4]=1
            elif a=='Documentary':
                arr[i,5]=1
            elif a=='Drama':
                arr[i,6]=1
            elif a=='Family':
                arr[i,7]=1
            elif a=='Fantasy':
                arr[i,8]=1
            elif a=='History':
                arr[i,9]=1

            elif a=='Horror':
                arr[i,10]=1
            elif a=='Music':
                arr[i,11]=1
            elif a=='Mystery':
                arr[i,12]=1
            elif a=='Romance':
                arr[i,13]=1
            elif a=='Science Fiction':
                arr[i,14]=1
            elif a=='Thriller':
                arr[i,15]=1
            elif a=='War':
                arr[i,16]=1
    #print(np.shape(arr))
    return arr
def parser2(filename):
    arr = []
    with open(filename)as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            rating = (row[2])
            arr.append(rating)
            isbn = (row[0])
    rate = np.zeros((11,1))
    for i in range(1,len(arr)):

        a = arr[i]
        if a!='':
            rate[int(a),:]+=1
    return rate
if __name__=='__main__':
    books_tags="book_tags.csv"
    books="books.csv"
    movie="movies_metadata.csv"
    movie_rating="movie_ratings.csv"
    book_rating="book_rating_data.csv"
    book_rating= parser2(book_rating)
    plt.plot(book_rating)
    plt.xlabel("ratings in the range of 0-10")
    plt.ylabel("Frequency of the movies in the given range")
    plt.text(8.5, 600000, "No. of books are 120K", style='oblique', color='green')
    plt.show()
    #print(book_rating)
    '''''rat,gen = parser1(movie)
    gen1 = np.zeros((len(gen[0]),1))
    for i in range(len(gen[0])):
        gen1[i]=np.sum(gen[:,i])
    x =np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
    plt.figure(1)

    plt.xticks(x,['Action','Adven.','Anim.','Comedy','Crime','Docu.','Drama','Family','Fantasy','Hist.','Horror','Music','Mystery','Romance','SciFi','Thriller','War'])
    plt.plot(gen1)
    plt.xlabel("genre",fontdict={'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 12,
        })
    plt.ylabel("no. of movies",fontdict={'family': 'serif',
        'color':  'red',
        'weight': 'normal',
        'size': 12,
        })
    plt.text(14, 18900, "No. of movies are 45K", style='oblique', color='green')

    plt.plot(rat)
    plt.xlabel("ratings in the range of 1-10")
    plt.ylabel("Frequency of the movies in the given range")
    plt.text(8.5,13900,"No. of movies are 45K",style='oblique',color='green')
    plt.show()'''''