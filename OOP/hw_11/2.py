'''
Миксины:
○ Добавляют специфические функции (например,
  кэширование, логирование).
○ Обычно не содержат основного состояния и структуры
  объекта, а лишь дополняют их.

Ситуация:
У тебя есть два класса: Cat и Dog. Эти классы 
представляют животных и имеют метод make_sound, 
который выводит их уникальный звук: мяуканье или лай.

Теперь ты хочешь добавить к ним функционал логирования
 — чтобы каждый раз, когда животное издает звук, 
 в лог записывалась строка вида:
"Cat: Meowed" или "Dog: Barked".


'''

class LogMixin:
    def log_action(self, message):
        """Log the action by printing or storing the message."""
        print(f"[LOG]: {message}")

class Cat(LogMixin):
    def make_sound(self):
        sound = "meowed"
        self.log_action(f"Cat: {sound}")
        # print(sound)

class Dog(LogMixin):
    def make_sound(self):
        sound = "barked"
        self.log_action(f"Dog: {sound}")
        # print(sound)

cat = Cat()
dog = Dog()

cat.make_sound()
dog.make_sound()