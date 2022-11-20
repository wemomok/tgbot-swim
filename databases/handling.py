if __name__ == '__main__':
    from models import *
    # for user in User.select():
    #     print(user.id, user.username)
    # user = User(username="test").save()
    # Chat(chatID=0, is_reged=False, user=user).save()
    chats = Chat.select(Chat, User).join(User).where(Chat.user.id == 1)
    for chat in chats:
        print(chat.user.username)
else:
    from databases.models import *
from peewee import *


def new_user():
    with db:
        User().save()

        
def check_if_user_exist(username):
    with db:
        try:
            User.select().where(User.username == username).get()
            return True
        except User.DoesNotExist:
            return False


def check_if_chat_exist(chatID):
    with db:
        try:
            Chat.select().where(Chat.chatID == chatID).get()
            return True
        except Chat.DoesNotExist:
            return False


with db:
    db.create_tables([User, Chat])
