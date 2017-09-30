File_Size_List = []
File_Hash_List = []
File_Name_List = []

DB_PATH = ".\Foxdb\main.hdb" # maleware DB
memory = 1024 * 100 # 102400

def DB_Pattern():
    with open(DB_PATH, "rb") as fdb:
        for hdb in fdb.readlines(memory):
            hdb = hdb.split("\n")[0]
            print(hdb)
            File_Hash_List.append(str(hdb.split(':')[0]))
            File_Size_List.append(int(hdb.split(':')[1]))
            File_Name_List.append(str(hdb.split(':')[2]))
        #hdb=hdb.split("\n")[0]

