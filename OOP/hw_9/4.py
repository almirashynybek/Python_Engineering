# Задание 1: Проверка времени суток

class TimeUtils:
    # def __init__(self, hour):
    #         self.hour = hour
    
    @staticmethod     
    def is_morning(hour):
        if hour in range(6,13):
            return True
        
        return False
    
time = TimeUtils()
print(time.is_morning(12))
