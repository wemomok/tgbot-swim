from peewee import *

db = SqliteDatabase("databases/database.sqlite3", pragmas={'foreign_keys': 1})


class BaseModel(Model):
    id = PrimaryKeyField(unique=1)

    class Meta:
        database = db
        order_by = "id"


class User(BaseModel):
    username = CharField(null=True, unique=True)
    password = CharField(null=True)

    class Meta:
        db_table = "users"


class Chat(BaseModel):
    chatID = IntegerField()
    is_reged = BooleanField()
    user = ForeignKeyField(User)

    class Meta:
        db_table = "chats"
