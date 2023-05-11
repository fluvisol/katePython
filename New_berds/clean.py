
import random

#TODO если возможно, сделать более нормальным хранение, например, не хранить в большом списке статус
animals = list()
live_animals = list ()
marry = list()
live_marry = list ()
servis = list()

marry_age = 3
age = 15
data = 0
add_to_mary = 100
#количество детей/челочисленное, как часто, не забыть вписать ноль!
#distribution_children = (0, 1, 2, 3, 60, 20, 3, 1)
distribution_children = (0, 1, 60, 20)
accidental_deaths = 0.0005
#old_deaths = 0.3
#infant_deaths = -0.1* animal_age ^(2)+30

# простые функции
def create_animals(nomber, data_creating_1 = 0):
    for i in range(nomber):
        animals.append([len(animals), random.choice (["M", "W"]), data_creating_1, data_creating_1 + age, 0, 0, "N"])
        live_animals.append(animals[-1])
# TODO добавить чтоб они с какой-то вероятностью встречались, а не 100%
def marry_creater(id_animal):
    if live_animals[id_animal][6] == "N" and general_time - live_animals[id_animal][2] >= marry_age:
        for partner in live_animals:
            if partner[1] != live_animals[id_animal][1] and partner [6] == "N" and general_time - partner[2] >= marry_age:
                marry.append([len(marry), id_animal, partner[0], general_time, general_time + add_to_mary])
                live_marry.append(marry[-1])
                live_animals[id_animal][6] = "H"
                partner[6] = "H"
                break

#эта функция ужасна, её надо исправить и аакуратно засунуть в следующую, а ту переименовать            
def death (animal):
    animal[3] = general_time
def all_deaths(live_animals = live_animals):
    for animal in live_animals:
        random.choices([death(animal), None], weights= [accidental_deaths *100, (1-accidental_deaths) * 100])
        #сделать детскую смртность и старческую, для этого подключить параболу, матобработка

#разобраться с глобальными переменными
def birth_animal(marry_id):
    animals.append([len(animals), random.choice (["M", "W"]), general_time, general_time + age, marry [marry_id][1], marry [marry_id][2], "N"])
    live_animals.append(animals[-1])

def delate_die_animals():
    servis =[live for live in live_animals if live[3] >= general_time]
    live_animals.clear()
    live_animals.extend(servis)

def delate_die_marry():
    servis =[live for live in live_marry if live_animals [live[1]] [3] and live_animals [live[2]] [3] >= general_time]
    live_marry.clear()
    live_marry.extend(servis)

# сложные функции
def temporarily_marriage(live_animals = live_animals):
    for animals in live_animals:
        random.choices ([marry_creater(animals[0]), None], weights= [1, 10])

def normal_fertility(marry_id, distribution_children):
    nomber_baby = random.choices(tuple(distribution_children[0:(len(distribution_children)//2)]), weights=tuple(distribution_children[(len(distribution_children)//2):]))
    for __ in range(len(nomber_baby)):
        birth_animal(marry_id)

def all_normal_fertility(distribution_children = distribution_children):
    for marry_nomber in range (len(live_marry)):
        normal_fertility(marry_nomber, distribution_children)


# редкие функции
# def beby_boom():
#     new_fertility = [new for new in (distribution_children[(len(distribution_children)//2):])]
#     #new_fertility =  
#     normal_fertility (new_fertility)

# def merry_boom(nomber): 
#     for i in range(nomber):
#         marry_creater(i)

#функция простого года



print ("new"*20)
general_time = 1
create_animals (10, 0)
general_time = 4


for i in range (18):
    print(general_time)
    all_deaths()
    delate_die_animals()
    delate_die_marry()
    temporarily_marriage()
    all_normal_fertility()
    general_time = general_time +1

# print ("animals")
# for i in animals:
#     print (i)

# print ("marry")    
# for i in marry:
#     print (i)

print ("live_animals")    
for i in live_animals:
    print (i)

print ("live_marry")    
for i in live_marry:
    print (i)


