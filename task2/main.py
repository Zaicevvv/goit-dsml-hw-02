from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://zaicevvv1991:mysecretpassword@mymongodb.mby1agw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    server_api=ServerApi("1"),
)

db = client.book

# result_one = db.cats.insert_one(
#     {
#         "name": "barsik",
#         "age": 3,
#         "features": ["ходить в капці", "дає себе гладити", "рудий"],
#     }
# )

# print(result_one.inserted_id)

# result_many = db.cats.insert_many(
#     [
#         {
#             "name": "Lama",
#             "age": 2,
#             "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
#         },
#         {
#             "name": "Liza",
#             "age": 4,
#             "features": ["ходить в лоток", "дає себе гладити", "білий"],
#         },
#     ]
# )
# print(result_many.inserted_ids)


def find_all():
    cats = db.cats.find({})
    for cat in cats:
        print(cat)


# find_all()


def find_cat():
    to_find = input("Cats name to find: ")
    cat = {"name": to_find}
    cat_by_name = db.cats.find_one(cat)
    if cat_by_name is None:
        return "[Error]: Cat not found"
    else:
        return cat_by_name


# print(type(find_cat()))


def update_cats_age_by_name():
    name = find_cat()
    if type(name) == str:
        return name
    age = int(input("Enter new age of the cat: "))
    db.cats.update_one({"name": name["name"]}, {"$set": {"age": age}})
    return f'Cats "{name["name"]}" age updated successfully!'


# print(update_cats_age_by_name())


def add_cats_feature_by_name():
    name = find_cat()
    if type(name) == str:
        return name
    feature = input("Enter new feature of the cat: ")
    db.cats.update_one({"name": name["name"]}, {"$push": {"features": feature}})
    return f'Cats "{name["name"]}" features updated successfully!'


# print(add_cats_feature_by_name())


def delete_cat_by_name():
    name = find_cat()
    if type(name) == str:
        return name
    db.cats.delete_one({"name": name["name"]})
    return f'Cat "{name["name"]}" was successfully deleted!'


# print(delete_cat_by_name())


def truncate_db():
    db.cats.delete_many({})
    return "Database truncated successfully!"


# print(truncate_db())
