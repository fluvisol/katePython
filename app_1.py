from random import randint
General_Table = list ()
Nimfa_Table_1 = list ()
Nimfa_Table_0 = list ()
Adult_Table_0_m = list ()
Adult_Table_0_n = list ()
Adult_Table_1_m = list ()
Adult_Table_1_n = list ()
General_Marry_Table = list ()
Actual_Marry_Table = list ()
Servis = list ()
All_Table = (General_Table, Nimfa_Table_0, Nimfa_Table_1, Adult_Table_0_n, Adult_Table_1_n, Adult_Table_0_m, Adult_Table_1_m, General_Marry_Table, Actual_Marry_Table, Servis)
Name = ("General_Table", "Nimfa_Table_0", "Nimfa_Table_1", "Adult_Table_0_n", "Adult_Table_1_n", "Adult_Table_0_m", "Adult_Table_1_m", "General_Marry_Table", "Actual_Marry_Table", "Servis")
#(["id", "mom_id", "dad_id", "sex", "data_birth", "data_death"])
#(["id", "fem_id", "mal_id", "data_creat", "data_stop"])
general_time = 20
primary_number = 10
min_deaf_age = 10
max_deaf_age = 70
considering_period = 10
min_marry_age = 16 
#чтоб выпадало 0 с вероятностью в 0.6, например
chaild_nomber = randint(0,1)
#надо сделать возможным добавлять любой пол, для этого разобраться со значениями по умолчанию
def creater_new_animals(number, min_deaf_age, max_deaf_age, general_time):
    for i in range(number):
        sex = randint(0, 1)
        #завести в переменную
        data_birth = general_time + randint(0, 25)
        data_death = data_birth + randint(min_deaf_age, max_deaf_age + 1)
        animal = (len(General_Table), None, None, sex, data_birth, data_death)
        print(animal)
        General_Table.append (animal)
        if sex == 0:
            Nimfa_Table_0.append(animal)
        else:
            Nimfa_Table_1.append(animal)
#(["id", "mom_id", "dad_id", "sex", "data_birth", "data_death"])
#(["id", "fem_id", "mal_id", "data_creat", "data_stop"])       
def marry(Adult_Table_0_n = Adult_Table_0_n, Adult_Table_1_n = Adult_Table_1_n, Adult_Table_0_m = Adult_Table_0_m, Adult_Table_1_m = Adult_Table_1_m, General_Marry_Table = General_Marry_Table, Actual_Marry_Table = Actual_Marry_Table):
    #нужно уменьшить количество браков и чтоб были случайными
    for index  in range (min(len(Adult_Table_1_n), len(Adult_Table_0_n))):
        sex = 0
        data_creat = general_time
        data_stop = min(Adult_Table_0_n [index][5], Adult_Table_1_n [index][5], randint(3, 100))
        marry = (len(General_Marry_Table), Adult_Table_0_n [index][0], Adult_Table_1_n [index][0], data_creat, data_stop)
        General_Marry_Table.append (marry)
        Actual_Marry_Table.append (marry)
#можно сделать лучше. Добавить возможность переноса и мат.операций, пока напрямую сделаю
def cleaner(Cunner_Table, const, nomber = 5):
    #global Cunner_Table
    for index  in range (len(Cunner_Table)):
        if Cunner_Table [index][nomber] < const:
            Servis.append(Cunner_Table[index])
    Cunner_Table = Servis
    return Cunner_Table
def all_clenner(Adult_Table_0_m = Adult_Table_0_m, Adult_Table_1_m = Adult_Table_1_m, Adult_Table_0_n = Adult_Table_0_n, Adult_Table_1_n = Adult_Table_1_n, Nimfa_Table_0 = Nimfa_Table_0, Nimfa_Table_1 = Nimfa_Table_1, general_time = general_time, Servis = Servis, Actual_Marry_Table = Actual_Marry_Table):
    #смерти
    cleaner(Adult_Table_0_m, general_time, 5)
    cleaner(Adult_Table_1_m, general_time, 5)
    cleaner(Adult_Table_0_n, general_time, 5)
    cleaner(Adult_Table_1_n, general_time, 5)
    cleaner(Nimfa_Table_0, general_time, 5)
    cleaner(Nimfa_Table_1, general_time, 5)
    #разводы
    cleaner(Actual_Marry_Table, general_time, 4)
    #выписка из малолеток и вписка во взрослых
    for index  in range (len(Nimfa_Table_0)):
        if general_time - Nimfa_Table_0 [index][4] >= min_marry_age:
            Adult_Table_0_n.append(Nimfa_Table_0 [index])   
        else:
            Servis.append(Nimfa_Table_0 [index])
    for index  in range (len(Nimfa_Table_1)):
        print("start work")
        if general_time - Nimfa_Table_1 [index][4] >= min_marry_age:
            Adult_Table_1_n.append(Nimfa_Table_1 [index])   
        else:
            Servis.append(Nimfa_Table_1 [index])
            print(Servis)
    Nimfa_Table_1 = Servis
    Servis.clear()
  
    Nimfa_Table_0 = Servis
    Servis.clear()
    #нужно сделать 
    #return Nimfa_Table_0
#(["id", "mom_id", "dad_id", "sex", "data_birth", "data_death"])
#(["id", "fem_id", "mal_id", "data_creat", "data_stop"])   
def bern_animal ():
    for index in range (len(Actual_Marry_Table)):
        sex = randint(0,2)
        animal = tuple([len(General_Table), Actual_Marry_Table[index][2], Actual_Marry_Table[index][3], sex, general_time, randint (min_deaf_age, max_deaf_age)])
        General_Table.append(animal)
        if animal[3] == 0:
            Nimfa_Table_0.append(animal)
        else:
            Nimfa_Table_1.append(animal)
#Хочу красивую статистику, наверно, надо как-то разделить блоки, чтоб не слишком длинно
#И визуализацию. Куда совать гены?
#0, 5, A, F - для раскраски, пока только полосочки

def show_rezalt(All_Table = All_Table, Name = Name):
    for i in range(len (All_Table)):
        print (Name[i], "-", len(All_Table[i]))
        print (All_Table[i])
        print("****************************")

#с это момента выполнение


creater_new_animals(primary_number, max_deaf_age, max_deaf_age, general_time)
print(General_Table)
print("#######################################")
for index in range (considering_period):
    print(general_time)
    all_clenner()
    marry()
    bern_animal()
    general_time = general_time + 1
show_rezalt(All_Table)



