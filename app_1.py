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
#(["id", "mom_id", "dad_id", "sex", "data_birth", "data_death"])
#(["id", "fem_id", "mal_id", "data_creat", "data_stop"])
general_time = 0
primary_number = 10
longevity = randint (15, 80)
considering_period = 30
min_marry_age = 16 
#чтоб выпадало 0 с вероятностью в 0.6, например
chaild_nomber = randint(0,3)
#надо сделать возможным добавлять любой пол, для этого разобраться со значениями по умолчанию
def creater_new_animals(number, longevity, general_time):
    for index  in range(general_time, number, 1):
        sex = randint(0, 1)
        #завести в переменную
        data_birth = general_time + randint(0, 25)
        data_death = data_birth + longevity
        animal = (len(General_Table), None, None, sex, data_birth, data_death)
        General_Table.append (animal)
        if sex == 0:
            Nimfa_Table_0.append(animal)
        else:
            Nimfa_Table_1.append(animal)
#(["id", "mom_id", "dad_id", "sex", "data_birth", "data_death"])
#(["id", "fem_id", "mal_id", "data_creat", "data_stop"])       
def marry():
    #это очень медленное и работает c одним полом
    #нужно уменьшить количество браков
    #как бы их перемешать.... а то рандом замедлять будет 
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
def all_clenner():
    global Nimfa_Table_0
    global Nimfa_Table_1
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
    for index  in range (len(Nimfa_Table_1)):
        if general_time - Nimfa_Table_1 [index][4] >= min_marry_age:
            Adult_Table_1_n.append(Nimfa_Table_1 [index])   
        else:
            Servis.append(Nimfa_Table_1 [index])
    Nimfa_Table_1 = Servis
    for index  in range (len(Nimfa_Table_0)):
        if general_time - Nimfa_Table_0 [index][4] >= min_marry_age:
            Adult_Table_0_n.append(Nimfa_Table_0 [index])   
        else:
            Servis.append(Nimfa_Table_0 [index])
    Nimfa_Table_0 = Servis
#(["id", "mom_id", "dad_id", "sex", "data_birth", "data_death"])
#(["id", "fem_id", "mal_id", "data_creat", "data_stop"])   
def bern_animal ():
    for index in range (len(Actual_Marry_Table)):
        sex = randint(0,2)
        animal = tuple(len(General_Table), Actual_Marry_Table[index][2], Actual_Marry_Table[index][3], sex, general_time, longevity)
        General_Table.append(animal)
        if animal[3] == 0:
            Nimfa_Table_0.append(animal)
        else:
            Nimfa_Table_1.append(animal)
#Хочу красивую статистику, наверно, надо как-то разделить блоки, чтоб не слишком длинно
#И визуализацию. Куда совать гены?
#0, 5, A, F - для раскраски, пока только полосочки

creater_new_animals(primary_number, longevity, general_time)

for index in range (considering_period):
    all_clenner()
    marry()
    bern_animal()
    general_time = general_time + 1

def show_rezalt:
    print ("General_Table ", len(General_Table))
    print (General_Table)
    print("****************************")
    print ("Nimfa_Table_0 ", len (Nimfa_Table_0))
    print (Nimfa_Table_0)
    print("****************************")
    print ("Nimfa_Table_1 ", len (Nimfa_Table_1))
    print (Nimfa_Table_1)
    print("****************************")
    print ("Adult", len(Adult_Table_0_m) + len(Adult_Table_0_n) + len(Adult_Table_1_m) + len(Adult_Table_1_n))
    print(Adult_Table_1_n)
    print(Adult_Table_0_m)
    print (Adult_Table_1_n)
    print (Adult_Table_1_m)

