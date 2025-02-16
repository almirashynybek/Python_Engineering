# Задание 1: Управление пользователями и отправка уведомлений

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username):
        self.users.append(username)

    def remove_user(self, username):
        if username in self.users:
            self.users.remove(username)

        else:
            print("Такого пользователя не существует")


class Notifier:
    def __init__(self, user_manager: UserManager):
        self.user_manager = user_manager  # Store the user manager instance

    def send_notification(self, name: str, text: str):
        if name in self.user_manager.users:
            print(f'Сообщение "{text}" отправлено {name}')
        else:
            print("Такого пользователя не существует")




manager = UserManager()
notifier = Notifier(manager)  # Pass the user manager to Notifier

manager.add_user("Alice")
manager.add_user("Bob")


notifier.send_notification("Alice", "Добро пожаловать!")
notifier.send_notification("Bob", "У вас новое сообщение")
