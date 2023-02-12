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
general_time = 0
primary_number = 10
longevity = randint (15, 80)
considering_period = 10
min_marry_age = 16 

def creater_new_animals(number, longevity, general_time=0):
    for index  in range(general_time, number, 1):
        sex = 1
        #завести в переменную
        data_birth = general_time + randint(0, 25)
        data_death = data_birth + longevity
        animal = (len(General_Table), None, None, sex, data_birth, data_death)
        General_Table.append (animal)
        Nimfa_Table_1.append(animal)

creater_new_animals (20, 30)
def show_rezalt(All_Table = All_Table, Name = Name):
    for i in range(9):
        print (Name[i], "-", len(All_Table[i]))
        print (All_Table[i])
        print("****************************")

print ("#############################################")
show_rezalt(All_Table)


