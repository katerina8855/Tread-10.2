import threading
import time
class warrior(threading.Thread):
    def __init__(self, name, skill):
        super(warrior, self).__init__()
        self.name = name
        self.skill = skill
    def run(self):
        enemy = 100
        days_to_defend = enemy // self.skill
        print(f"{self.name} имеет {days_to_defend} дней на защиту")
        for day in range(1, days_to_defend + 1):
            remaining_enemy = enemy - (day * self.skill)
            if remaining_enemy < 0:
                remaining_enemy = 0
            print(f"{self.name} ослабил вражеское войско на {self.skill} человек и осталось врагов: {remaining_enemy}")
            time.sleep(1)
        print(f"{self.name} успешно защитил королевство")


knight_1 = warrior("Король Артур", 20)
knight_2 = warrior("Сэр Тристан", 30)
knight_1.start()
knight_2.start()
knight_1.join()
knight_2.join()