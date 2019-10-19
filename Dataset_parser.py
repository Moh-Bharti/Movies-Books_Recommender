import pandas as pd
import sklearn as sk
import json
import re
import numpy as np

def parser1(filename):
    arr = pd.read_csv(filename).to_numpy()
    genre = arr[:,3]
    genre_json=(pd.DataFrame(genre).values)
    string_parser(genre_json)
    #genre_dict=json.loads(genre_json)
    id = arr[:,5]
    title = arr[:,8]
    pop = arr[:,10]
    year = arr[:,14]
    rtime = arr[:,16]
    rating = arr[:,22]
    #return genre_json

def string_parser(string):
    #arr = np.zeros()

    for i in range(len(string)):

        text = string[i][0]
        dict = re.split('[{,}]\s',text[1:len(text)-1])
        for j in range(len(dict)//2):
            print(dict[2*j+1])


def parser2(filename):
    arr=0
    return arr
if __name__=='__main__':
    books_tags="book_tags.csv"
    books="books.csv"
    movie="movies_metadata.csv"
    movie_rating="ratings_small.csv"
    book_rating="ratings.csv"
    print(parser1(movie))