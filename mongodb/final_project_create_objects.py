# user has "publish", and photo has "publisher". That's ther relationships.

from pymongo import MongoClient
import datetime

db = MongoClient().final
user = db.User
photo = db.Photo

user.insert({
    "Email": "a@gmail.com",
    "Name": "a",
    "Password": "a",
    "Follower":
    [
        {"Email": "b@gmail.com"},
        {"Email": "c@gmail.com"}
    ],
    "Following":
    [
        {"Email": "b@gmail.com"},
        {"Email": "c@gmail.com"}
    ],
    "Info":
    [
        {"Address": "Earth"},
        {"Gender": "Male"},
        {"Age": "18"}
    ],
    "Publish":
    ["a1", "a2", "a3", "a4", "a5"]
})

user.insert({
    "Email": "b@gmail.com",
    "Name": "b",
    "Password": "b",
    "Follower":
    [
        {"Email": "a@gmail.com"},
        {"Email": "c@gmail.com"}
    ],
    "Following":
    [
        {"Email": "a@gmail.com"},
        {"Email": "c@gmail.com"}
    ],
    "Info":
    [
        {"Address": "Earth"},
        {"Gender": "Male"},
        {"Age": "18"}
    ],
    "Publish":
    ["b1", "b2", "b3", "b4", "b5"]
})

user.insert({
    "Email": "c@gmail.com",
    "Name": "c",
    "Password": "c",
    "Follower":
    [
        {"Email": "b@gmail.com"},
        {"Email": "a@gmail.com"}
    ],
    "Following":
    [
        {"Email": "b@gmail.com"},
        {"Email": "a@gmail.com"}
    ],
    "Info":
    [
        {"Address": "Earth"},
        {"Gender": "Male"},
        {"Age": "18"}
    ],
    "Publish":
    ["c1", "c2", "c3", "c4", "c5"]
})




photo.insert({
    "Name": "a1",
    "Publisher": "a@gmail.com",
    "Upvote":
    [
        {"Email": "a@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "a@gmail.com", "Comment": "Good"},
        {"Email": "b@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "a2",
    "Publisher": "a@gmail.com",
    "Upvote":
    [
        {"Email": "a@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "a@gmail.com", "Comment": "Good"},
        {"Email": "b@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "a3",
    "Publisher": "a@gmail.com",
    "Upvote":
    [
        {"Email": "a@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "a@gmail.com", "Comment": "Good"},
        {"Email": "b@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "a4",
    "Publisher": "a@gmail.com",
    "Upvote":
    [
        {"Email": "a@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "a@gmail.com", "Comment": "Good"},
        {"Email": "b@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "a5",
    "Publisher": "a@gmail.com",
    "Upvote":
    [
        {"Email": "a@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "a@gmail.com", "Comment": "Good"},
        {"Email": "b@gmail.com", "Comment": "Bad"}
    ]
})

photo.insert({
    "Name": "b1",
    "Publisher": "b@gmail.com",
    "Upvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "b@gmail.com", "Comment": "Good"},
        {"Email": "c@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "b2",
    "Publisher": "b@gmail.com",
    "Upvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "b@gmail.com", "Comment": "Good"},
        {"Email": "c@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "b3",
    "Publisher": "b@gmail.com",
    "Upvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "b@gmail.com", "Comment": "Good"},
        {"Email": "c@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "b4",
    "Publisher": "b@gmail.com",
    "Upvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "b@gmail.com", "Comment": "Good"},
        {"Email": "c@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "b5",
    "Publisher": "b@gmail.com",
    "Upvote":
    [
        {"Email": "b@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "b@gmail.com", "Comment": "Good"},
        {"Email": "c@gmail.com", "Comment": "Bad"}
    ]
})

photo.insert({
    "Name": "c1",
    "Publisher": "c@gmail.com",
    "Upvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "c@gmail.com", "Comment": "Good"},
        {"Email": "a@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "c2",
    "Publisher": "c@gmail.com",
    "Upvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "c@gmail.com", "Comment": "Good"},
        {"Email": "a@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "c3",
    "Publisher": "c@gmail.com",
    "Upvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "c@gmail.com", "Comment": "Good"},
        {"Email": "a@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "c4",
    "Publisher": "c@gmail.com",
    "Upvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "c@gmail.com", "Comment": "Good"},
        {"Email": "a@gmail.com", "Comment": "Bad"}
    ]
})
photo.insert({
    "Name": "c5",
    "Publisher": "c@gmail.com",
    "Upvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Downvote":
    [
        {"Email": "c@gmail.com"}
    ],
    "Comment":
    [
        {"Email": "c@gmail.com", "Comment": "Good"},
        {"Email": "a@gmail.com", "Comment": "Bad"}
    ]
})

