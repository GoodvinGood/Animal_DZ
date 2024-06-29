import pickle

# Базовый класс Animal, который содержит общие атрибуты и методы для всех животных
class Animal:
    def __init__(self, name, age):
        self.name = name  # Имя животного
        self.age = age  # Возраст животного

    def make_sound(self):
        pass  # Метод, который будет переопределен в подклассах

    def eat(self):
        print(f"{self.name} ест.")  # Метод, который выводит сообщение о том, что животное ест

# Подкласс Bird, который наследует от Animal
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Размах крыльев

    def make_sound(self):
        print(f"{self.name} чирикает.")  # Переопределенный метод make_sound для птиц

# Подкласс Mammal, который наследует от Animal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Цвет шерсти

    def make_sound(self):
        print(f"{self.name} рычит.")  # Переопределенный метод make_sound для млекопитающих

# Подкласс Reptile, который наследует от Animal
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Тип чешуи

    def make_sound(self):
        print(f"{self.name} шипит.")  # Переопределенный метод make_sound для рептилий

# Функция, демонстрирующая полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()  # Вызывает метод make_sound для каждого животного в списке

# Класс Zoo, который использует композицию для хранения информации о животных и сотрудниках
class Zoo:
    def __init__(self):
        self.animals = []  # Список животных в зоопарке
        self.staff = []  # Список сотрудников зоопарка

    def add_animal(self, animal):
        self.animals.append(animal)  # Добавляет животное в зоопарк

    def add_staff(self, staff_member):
        self.staff.append(staff_member)  # Добавляет сотрудника в зоопарк

    def show_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} лет")  # Выводит информацию о каждом животном

    def show_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, {staff.role}")  # Выводит информацию о каждом сотруднике

# Базовый класс Staff для сотрудников зоопарка
class Staff:
    def __init__(self, name, role):
        self.name = name  # Имя сотрудника
        self.role = role  # Роль сотрудника

# Подкласс ZooKeeper, который наследует от Staff
class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")  # Метод для кормления животного

# Подкласс Veterinarian, который наследует от Staff
class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")  # Метод для лечения животного

# Функции для сохранения и загрузки информации о зоопарке
def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)  # Сохраняет объект зоопарка в файл

def load_zoo(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)  # Загружает объект зоопарка из файла

# Пример использования программы

# Создаем животных
bird = Bird("Попугай", 2, "Средний")
mammal = Mammal("Лев", 5, "Золотистый")
reptile = Reptile("Змея", 3, "Гладкая")

# Создаем сотрудников
zookeeper = ZooKeeper("Иван", "Смотритель")
vet = Veterinarian("Доктор Смит", "Ветеринар")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_staff(zookeeper)
zoo.add_staff(vet)

# Демонстрируем полиморфизм
animal_sound(zoo.animals)

# Сохраняем зоопарк в файл
save_zoo(zoo, "zoo.pkl")

# Загружаем зоопарк из файла
loaded_zoo = load_zoo("zoo.pkl")
loaded_zoo.show_animals()
loaded_zoo.show_staff()