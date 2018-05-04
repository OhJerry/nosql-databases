# Put the use case you chose here. Then justify your database choice:
# Use case: Instagram-like app. Database: MongoDB.
# MongoDB is document oriented, and is dynamic and flexible. So for each user or photo, we do not need to assign rigid schema. For app like instagram, such feature would be very helpful.
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# MongoDB stores data in a distributed system. So when one of the servers went down, others would ensure the performance.
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# Password. We could have several different layers of backups. One stores info one month ago, one stores info one week ago. So we could always have backup to retrieve data.
#

from pymongo import MongoClient
import datetime

db = MongoClient().final
user = db.User
photo = db.Photo

# Action 1: <A User signs up for an account>
user.insert({
    "Email": "d@gmail.com",
    "Name": "d",
    "Password": "d",
    "Follower": [],
    "Following": [],
    "Info": [],
    "Publish": []
})


# Action 2: <User publishes a photo>
photo.insert({
    "Name": "d1",
    "Publisher": "d@gmail.com",
    "Upvote": [],
    "Downvote": [],
    "Comment": []
})

# Action 3: <User follows someone>
user.update({"Email": "a@gmail.com"},{"$push":{"Following": {"Email": "b@gmail.com"}}})
user.update({"Email": "b@gmail.com"},{"$push":{"Follower": {"Email": "a@gmail.com"}}})

# Action 4: <A user sees all the photos of one particular person they follow>
list(photo.find({"Publisher": "a@gmail.com"}))

# Action 5: <A user comments on another's photo>
photo.update({"Name": "a1"}, {"$push":{"Comment": "Not bad"}})

# Action 6: <A user upvotes a photo>
photo.update({"Name": "a1"}, {"$push":{"Upvote": {"Email": "d@gmail.com"}}})

# Action 7: <A user downvotes a photo>
photo.update({"Name": "a1"}, {"$push":{"Downvote": {"Email": "d@gmail.com"}}})

# Action 8: <A user adds his info>
user.update({"Email": "d@gmail.com"},{"$push":{"Info": {"Gender": "Female"}}})



