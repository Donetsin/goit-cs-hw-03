import mdb_context as mdb

db = mdb.get_db()

def create_records():
    result_one = db.cats.insert_one(
        {
            "name": "barsik",
            "age": 3,
            "features": ["ходить в капці", "дає себе гладити", "рудий"],
        }
    )

    print(result_one.inserted_id)

    result_many = db.cats.insert_many(
        [
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
        ]
    )
    print(result_many.inserted_ids)

def read_all_records():
    records = db.cats.find()
    for record in records:
        print(record)

def read_record_by_name(name):
    record = db.cats.find_one({"name": name})
    if record:
        print(record)
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")


def update_age_by_name(name, new_age):
    result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print(f"Вік кота з ім'ям {name} оновлено на {new_age}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

def add_feature_by_name(name, new_feature):
    result = db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print(f"Характеристика '{new_feature}' додана до кота з ім'ям {name}.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

def delete_record_by_name(name):
    result = db.cats.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кіт з ім'ям {name} видалений.")
    else:
        print(f"Кіт з ім'ям {name} не знайдений.")

def delete_all_records():
    result = db.cats.delete_many({})
    print(f"Видалено {result.deleted_count} записів.")


if __name__ == "__main__":
    create_records()
    read_all_records()
    read_record_by_name("barsik")
    update_age_by_name("barsik", 4)
    add_feature_by_name("barsik", "любить спати")
    delete_record_by_name("barsik")
    delete_all_records()
