from aiogram.types import Update

data = {
    "update_id": 128526,
    "message": {
        "message_id": 11223,
        "from": {
            "id": 12345678,
            "is_bot": False,
            "first_name": "FirstName",
            "last_name": "LastName",
            "username": "username",
            "language_code": "ru",
        },
        "chat": {
            "id": 12345678,
            "first_name": "FirstName",
            "last_name": "LastName",
            "username": "username",
            "type": "private",
        },
        "date": 1508709711,
        "text": "Hi, world!",
    },
}

update = Update(**data)
print(update)
print(update.message)
print(update.message.from_user)
print(update.message.from_user.id)
print(update.json(indent=3))
