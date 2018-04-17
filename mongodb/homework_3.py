import pprint
from pymongo import MongoClient

# part A
client = MongoClient()
db = client.test
movies = db.movies
for movie in movies.find({"genres":"Drama"}, {"rated":"NOT RATED"}):
    movies.update({"_id": movie["_id"]},{'$set':{"rated": "Pending rating"}})

# part B
movies.insert_one({'title':'A Quiet Place', 'year':2018, 'countries':['USA'], 'genres':['Drama','Horror','Sci-Fi'], 'directors': ['John Krasinski'], 'imdb':{'id':6644220, 'rating':8.1, 'votes':52876}})

# part C
numGenres = movies.aggregate([{'$match': {"genres": "Drama"}}, {'$group':{'_id':'Drama', 'count':{'$sum':1}}}])

# part D
numCountries = movies.aggregate([{'$match':{"countries": "China", 'rated':'Pending rating'}},{'$group':{'_id':{"country":"China", "rating":"Pending rating"}, 'count':{'$sum':1}}}])

# part E
test2 = db.test2
test3 = db.test3
test2.insert({'id': '001', 'word': 'Apple'}) 
test3.insert({'id': '001', 'word': 'Apple'})

test2.insert({'id': '002', 'word': 'Banana'})
test3.insert({'id': '002', 'word': 'Banana'})

result = test2.aggregate([{'$lookup':{'from':'test3','localField':'id','foreignField':'id','as':'result'}}])
print(list(result))
