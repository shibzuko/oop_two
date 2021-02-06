
class Animal:
    def __init__(self, eat, weight, voice, name):
        self.eat = eat  
        self.weight = weight 
        self.voice = voice
        self.name = name

    def eating(self, time):
        return self.eat * time   

    def weighing(self, new_weight):
        self.weight = new_weight   


class Poultry(Animal):
    egg = 1

    def collect_eggs(self, quantity):
        return self.egg * quantity


class Cattle(Animal):
    milk = 0  

    def milking(self, time):
        return self.milk * time


class goose(Poultry, Animal):
    voice = 'Quack'


class Cow(Cattle, Animal):
    voice = 'Muu'
    milk = 15


class Sheep(Animal):
    voice = 'Bee'
    wool = 15  

    def hair_shearing(self, quantity):
        return self.wool * quantity


class Chicken(Poultry, Animal):
    voice = 'Co-co'

    def collecting_eggs(self, quantity):
        self.egg += quantity


class Goat(Cattle, Animal):
    voice = 'Mee'
    milk = 10


class Duck(Poultry, Animal):
    voice = 'Quack'


goose_1 = goose(1, 2, 'Кря', 'Серый')
goose_2 = goose(1, 2, 'Кря', 'Белый')

cow = Cow(10, 400, 'Мууу', 'Манька')

sheep_1 = Sheep(7, 55, 'Бее', 'Барашек')
sheep_2 = Sheep(6, 61, 'Бее', 'Кудрявый')

chicken_1 = Chicken(2, 1, 'Кудах', 'Ко-Ко')
chicken_2 = Chicken(2, 1, 'Кудах', 'Кукареку')

goat_1 = Goat(3, 80, 'Мее', 'Рога')
goat_2 = Goat(3, 90, 'Мее', 'Копыта')

duck = Duck(2, 3, 'Кря', 'Кряква')

animals_dict = {goose_1.name: goose_1.weight, goose_2.name: goose_2.weight, cow.name: cow.weight,
                sheep_1.name: sheep_1.weight, sheep_2.name: sheep_2.weight,
                chicken_1.name: chicken_1.weight, chicken_2.name: chicken_2.weight,
                goat_1.name: goat_1.weight, goat_2.name: goat_2.weight, duck.name: duck.weight}

count = 0
for weight_animal in animals_dict.values():
    count += weight_animal
print('Общий вес животных', count,  'килораммов')

max_count = 0
animal_id = 0
for i, y in animals_dict.items():
    if max_count < y:
        max_count = y
        animal_id = i
print(animal_id, 'самое тяжелое животное')