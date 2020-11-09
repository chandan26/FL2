#!/usr/bin/env python
# coding: utf-8

# In[39]:


import csv
def programmenu():
    print('{:*^100}'.format(" * "))
    column1 = ["1 LIST ALL","2 LIST ID","3 LIST NAME","7  EXIT"]
    column2 = ["4 DELETE ID","5 UPDATE ID ", "6 ADD"," "]
    for c1, c2 in zip(column1, column2):
        print ("%-15s  %s" % (c1, c2))
    print('{:*^100}'.format(" * "))
    choic=int((input("Enter your choice \t")))
    return choic


# In[40]:


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


# In[41]:





def create_csvfile():
    records=[ 
        {'Name':'Soap', 'ID':'12367345', 'Price':'1.99', 'In Stock':'100'},
        {'Name':'chocolate', 'ID':'1998700374', 'Price':'.99', 'In Stock':'40'},
        {'Name':'Batteries', 'ID':'6476398475', 'Price':'2.55', 'In Stock':'60'},
        {'Name':'Deodrant', 'ID':'1998700524', 'Price':'5.69', 'In Stock':'240'},
        
    ]
    csv_writer = csv.writer(open('ProductFile.csv','w'),delimiter=',', lineterminator='\n')
    csv_writer.writerow(['Name', 'ID ', 'Price', 'In Stock'])
    for rec in records:
        csv_writer.writerow([rec['Name'],rec['ID'],rec['Price'],rec['In Stock']])


def listall_csv():
    for row in csv.reader(open('ProductFile.csv', 'r'), delimiter = ','):
        print(row)   


# In[42]:


def serachid_record():
    with open('ProductFile.csv','r') as prodfile:
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





# In[43]:


def serchname_record():
    with open('ProductFile.csv','r') as prodfile:
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





# In[44]:


import csv
def delete_record():
    found=False
    with open("ProductFile.csv", "r") as f:
        data = list(csv.reader(f))
    with open("ProductFile.csv", "w") as f:
        serid = input("Enter the Name to delete \t ")
        writer = csv.writer(f,lineterminator = '\n')
        for row in data:
            if row[1] != serid:
                writer.writerow(row)
    if not found:
         print("No Record Found.")
    


# In[ ]:














def add_row():
    name=input('NAME? ')
    ID=input('ID? ')
    Price=input('PRICE? ')
    InStock=input('ADD STOCK ')
    info=[name,ID,Price,InStock]
    with open('ProductFile.csv','a') as file:
        writer=csv.writer(file,lineterminator = '\n')
        #writer.writerow('\n')
        writer.writerow(info)
    file.close()


# In[46]:


def updaterecord():
    loop = 1
    choice = 0
    #serachid_record()
    stid=validationupdate()
    
    while loop == 1:
        choice = updateprogrammenu()
        if choice == 1:
            updateNamefunc(stid)
            #pass
            #listall_csv()
        elif choice == 2:
            updatePricefunc(stid)
            #pass
        elif choice == 3:
            #pass
            updateStockfunc(stid)
        elif choice == 4:
            loop = 0
    


# In[47]:


import csv
def validationupdate():
    stid=input('Enter an ID')
    with open('ProductFile.csv','r') as prodfile:
        filereadr = csv.reader(prodfile)
        found = False
        #serid = input("Enter the ID to search \t ")
        for row in filereadr:
            if row[1] == stid:
                found = True
                print(row)
                return stid
    if not found:
        print("No Record Found.")
        #exit(0)
    


# In[ ]:





# In[48]:


#Name,ID ,Price,In Stock
def updateNamefunc(stid):
    #stid= input("Enter a ID : ")
    new_rows = []
    found = False
    fieldnames = ['Name', 'ID ', 'Price', 'In Stock']
    with open('ProductFile.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if stid == row['ID ']:
                row['Name'] = input("enter new Name  {} \t".format('Name'))
            new_rows.append({'Name': row['Name'], 'ID ': row['ID '], 'Price': row['Price'],'In Stock': row['In Stock']})
        

    # Write the amended data out to the file.
    with open('ProductFile.csv', 'w') as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames,lineterminator = '\n')
        writer.writerows(new_rows)


# In[49]:


def updatePricefunc(stid):
    new_rows = []
    #stid= input("Enter a ID : ")
    fieldnames = ['Name', 'ID ', 'Price', 'In Stock']
    with open('ProductFile.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if stid == row['ID ']:
                row['Price'] = input("enter new Price  {} \t".format('Price'))
            new_rows.append({'Name': row['Name'], 'ID ': row['ID '], 'Price': row['Price'],'In Stock': row['In Stock']})

    # Write the amended data out to the file.
    with open('ProductFile.csv', 'w') as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames,lineterminator = '\n')
        writer.writerows(new_rows)


# In[50]:


def updateStockfunc(stid):
    new_rows = []
    #stid= input("Enter a ID : ")
    fieldnames = ['Name', 'ID ', 'Price', 'In Stock']
    with open('ProductFile.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if stid == row['ID ']:
                row['In Stock'] = input("enter new Stock  {} \t".format('In Stock'))
            new_rows.append({'Name': row['Name'], 'ID ': row['ID '], 'Price': row['Price'],'In Stock': row['In Stock']})

    # Write the amended data out to the file.
    with open('ProductFile.csv', 'w') as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames,lineterminator = '\n')
        writer.writerows(new_rows)


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





# In[ ]:




