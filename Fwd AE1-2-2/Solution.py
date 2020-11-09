#!/usr/bin/env python
# coding: utf-8

# In[43]:


import csv
def programmenu():
    print('{:*^100}'.format(" * "))
    column1 = ["1 LIST ALL","2 LIST ID","3 LIST NAME","7  EXIT"]
    column2 = ["4 DELETE ID","5 UPDATE ID ", "6 ADD"," "]
    for c1, c2 in zip(column1, column2):
        print ("%-15s  %s" % (c1, c2))
    print('{:*^100}'.format(" * "))
    choic=int((input("Enter your choice")))
    return choic


# In[44]:


def updateprogrammenu():
    #idchoic=serachid_record() 
    print('{:*^100}'.format(" * "))
    column1 = ["1 NAME","2 PRICE"]
    column2 = ["3 IN STOCK","4 EXIT"]
    for c1, c2 in zip(column1, column2):
        print ("%-15s  %s" % (c1, c2))
    print('{:*^100}'.format(" * "))
    choic=int((input("Enter your choice  ")))
    return choic


# In[45]:





def create_csvfile():
    records=[ 
        {'Name':'Soap', 'ID':'12367345', 'Price':'1.99', 'In Stock':'100'},
        {'Name':'chocolate', 'ID':'1998700374', 'Price':'.99', 'In Stock':'40'},
        {'Name':'Batteries', 'ID':'6476398475', 'Price':'2.55', 'In Stock':'60'},
        {'Name':'Deodrant', 'ID':'1998700524', 'Price':'5.69', 'In Stock':'240'},
        
    ]
    csv_writer = csv.writer(open('Filecreation.csv','w'),delimiter=',', lineterminator='\n')
    csv_writer.writerow(['Name', 'ID ', 'Price', 'In Stock'])
    for rec in records:
        csv_writer.writerow([rec['Name'],rec['ID'],rec['Price'],rec['In Stock']])


def listall_csv():
    for row in csv.reader(open('Filecreation.csv', 'r'), delimiter = ','):
        print(row)   


# In[46]:


def serachid_record():
    with open('Filecreation.csv','r') as prodfile:
        filereadr = csv.reader(prodfile)
        found = False
        serid = input("Enter the ID to search \t ")
        for row in filereadr:
            if row[1] == serid:
                found = True
                print(row)
    if not found:
        print("No Record Found.")
                
        


# In[ ]:





# In[47]:


def serchname_record():
    with open('Filecreation.csv','r') as prodfile:
        filereadr = csv.reader(prodfile)
        found = False
        serid = input("Enter the Name to search \t ")
        for row in filereadr:
            if row[0] == serid:
                found = True
                print(row)
    if not found:
        print("No Record Found.")


# In[ ]:





# In[48]:


import csv
def delete_record():
    with open("Filecreation.csv", "r") as f:
        data = list(csv.reader(f))
    with open("Filecreation.csv", "w") as f:
        serid = input("Enter the Name to search \t ")
        writer = csv.writer(f,lineterminator = '\n')
        for row in data:
            if row[1] != serid:
                writer.writerow(row)
    


# In[ ]:





# In[ ]:





# In[49]:


def add_row():
    name=input('NAME? ')
    ID=input('ID? ')
    Price=input('PRICE? ')
    InStock=input('ADD STOCK ')
    info=[name,ID,Price,InStock]
    with open('Filecreation.csv','a') as file:
        writer=csv.writer(file,lineterminator = '\n')
        #writer.writerow('\n')
        writer.writerow(info)
    file.close()


# In[50]:


def updaterecord():
    loop = 1
    choice = 0
    serachid_record()
    while loop == 1:
        choice = updateprogrammenu()
        if choice == 1:
            name=input('NAME? ')
            with open("Filecreation.csv", "r") as f:
                data = list(csv.reader(f))
            with open("Filecreation.csv", "w") as f:
                #serid = input("Enter the Name to search \t ")
                 writer = csv.writer(f,lineterminator = '\n')
                 for row in data:
                    if row[1] == serid:
                        writer.writerow(row)
            
            #pass
            #listall_csv()
        elif choice == 2:
            name=input('PRICE? ')
            with open("Filecreation.csv", "r") as f:
                data = list(csv.reader(f))
            with open("Filecreation.csv", "w") as f:
                #serid = input("Enter the Name to search \t ")
                 writer = csv.writer(f,lineterminator = '\n')
                 for row in data:
                    if row[2] == serid:
                        writer.writerow(row)
            #pass
        elif choice == 3:
            #pass
            name=input('INSTOCK? ')
            with open("Filecreation.csv", "r") as f:
                data = list(csv.reader(f))
            with open("Filecreation.csv", "w") as f:
                #serid = input("Enter the Name to search \t ")
                 writer = csv.writer(f,lineterminator = '\n')
                 for row in data:
                    if row[1] == serid:
                        writer.writerow(row)
        elif choice == 4:
            loop = 0
    


# In[ ]:





# In[ ]:





# In[51]:



        
if __name__ == "__main__":
create_csvfile()

loop = 1
choice = 0
while loop == 1:
    choice = programmenu()
    if choice == 1:
        #pass
        listall_csv()
    elif choice == 2:
        serachid_record()
        #pass
    elif choice == 3:
        serchname_record()
        #pass
    elif choice == 4:
        #pass
        delete_record()
    elif choice == 5:
        updaterecord()
        #pass
    elif choice == 6:
        add_row()
    elif choice == 7:
        print("Exiting!!! Bye")
        loop = 0
   # read_csv();


# In[ ]:




