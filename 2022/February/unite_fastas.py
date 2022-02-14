import os

os.chdir(r"C:\Users\T-Gamer\Downloads\Soil_Samples\soil\farm_soil")

os.mkdir("Single_Fasta")
os.mkdir("Multiple_Fasta")

dict_vazio = {}

for i in os.listdir():
    file_name_split = i.split("_")[0]
    if file_name_split not in dict_vazio.keys():
        dict_vazio[file_name_split] = 1
    else:
        dict_vazio[file_name_split] += 1

print(dict_vazio)

for i in os.listdir():
    if dict_vazio[i.split("_")[0]] >1:
        os.mv

    else:
        print(i,"Fuck")
