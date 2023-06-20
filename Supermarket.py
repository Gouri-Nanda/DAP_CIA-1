import mysql.connector
import pandas as pd
def add_product():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    ICode=input("Enter Item Code:")
    Icmp=input("Enter Company Name:")
    IName = input("Enter the name of the product: ")
    IName=IName.upper()
    IPrice = int(input("Enter the price of the product: "))
    IStock = int(input("Enter the stock of the product: "))
    DoP=input("Enter Date of purchase:")
    cursor.execute('Insert into Items values("%s","%s","%s",%s,%s,"%s")'%(ICode,IName,Icmp,IPrice,IStock,DoP))
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Product inserted.")
def display_product():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    query=("SELECT*FROM Items")
    cursor.execute(query)
    item_no=[]
    item_name=[]
    item_cmp=[]
    item_price=[]
    item_stock=[]
    item_dd=[]
    for(Ino,Iname,Icmp,price,stock,dd)in cursor:
        item_no.append(Ino)
        item_name.append(Iname)
        item_cmp.append(Icmp)
        item_price.append(price)
        item_stock.append(stock)
        item_dd.append(dd)
    cnx.commit()
    cursor.close()
    cnx.close()
    data={"Item Code":item_no,"Item Name":item_name,"Item Company":item_cmp,"Price":item_price,"Stock(s) available":item_stock,"Date of Purchase":item_dd}
    df=pd.DataFrame(data)
    if df.empty:
        return "NO RECORDS AVAILABLE"
    else:
        return df
def delete_product():
    name = input("Enter the name of the product to delete: ")
    name=name.upper()
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    qry=("DELETE FROM Items where IName= %s")
    del_rec=(name,)
    cursor.execute(qry,del_rec)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Record deleted successfully.")
def update_product():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    name = input("Enter the name of the product to update: ")
    name=name.upper()
    print("Enter New data.")
    Ino=input("Enter Item code:")
    Iname=input("Enter Item Name:")
    Iname=Iname.upper()
    Icmp=input("Enter Company Name:")
    price=int(input("Enter Item Price:"))
    qty=int(input("Enter Available stock:"))
    print("Enter Date of purchase(date/month/year):")
    dd=input("Enter date:")
    qry=('update Items set ICode=%s,IName=%s,ICmp=%s,IPrice=%s,IQty=%s,DoP=%s where IName=%s')
    data=(Ino,Iname,Icmp,price,qty,dd,name)
    cursor.execute(qry,data)
    cnx.commit()
    cursor.close()
    cnx.close()
def search_product():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    Ino=input("Enter item no to be searched:")
    qry=("select*from Items where Icode=%s")
    rec_srch=(Ino,)
    cursor.execute(qry,rec_srch)
    rec_count=0
    for(Ino,Iname,Icmp,price,qty,dd)in cursor:
        rec_count+=1
        print("====================================")
        print("Item Code:",Ino)
        print("Item Name:",Iname)
        print("Item Company:",Icmp)
        print("Item Price:",price)
        print("Total Stock:",qty)
        print("Date of Purchase:",dd)
        print("====================================")
        print(rec_count,"Record(s) found")
    cnx.commit()
    cursor.close()
    cnx.close()
def customer_add():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()   
    Name=input("Enter Customer Name:")
    Name=Name.upper()
    Score=int(input("Enter Customer Score:"))
    cursor.execute('Insert into customerscore values("%s",%s)'%(Name,Score))
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Record inserted.")
def customer_display():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    query=("SELECT*FROM customerscore")
    cursor.execute(query)
    cust_score=[]
    cust_name=[]
    for(name,score)in cursor:
        cust_name.append(name)
        cust_score.append(score)
    cnx.commit()
    cursor.close()
    cnx.close()
    data={"Customer Name":cust_name,"Customer Score":cust_score}
    df=pd.DataFrame(data)
    if df.empty:
        return "NO RECORDS AVAILABLE"
    else:
        return df
def customer_delete():
    cname = input("Enter Customer Name to delete: ")
    cname=cname.upper()
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    qry=("DELETE FROM customerscore where Cname= %s")
    del_rec=(cname,)
    cursor.execute(qry,del_rec)
    cnx.commit()
    cursor.close()
    cnx.close()
    print("Record deleted successfully.")
def customer_update():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    cname = input("Enter the customer name: ")
    cname=cname.upper()
    print("Enter New data.")
    name=input("Enter Customer Name: ")
    name=name.upper()
    score=int(input("Enter Customer Score"))
    qry=("update customerscore set Cname=%s,Cscore=%s where Cname=%s")
    data=(name,score,cname)
    cursor.execute(qry,data)
    cnx.commit()
    cursor.close()
    cnx.close()
def customer_search():
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    cname=input("Enter customer name to be searched:")
    cname=cname.upper()
    qry=("select*from customerscore where Cname=%s")
    rec_srch=(cname,)
    cursor.execute(qry,rec_srch)
    rec_count=0
    for(cname,cscore)in cursor:
        rec_count+=1
        print("====================================")
        print("Customer Name:",cname)
        print("Customer Score:",cscore)
        print("====================================")
        print(rec_count,"Record(s) found")
    cnx.commit()
    cursor.close()
    cnx.close()
def calculate_bill():
    name_prod=[]
    price_prod=[]
    qty_prod=[]
    total_prod=[]
    total=0
    begin=True
    cnx=mysql.connector.connect(user='root',passwd='root@2004',host='localhost',database='Supermarket')
    cursor=cnx.cursor()
    print("\n***********************************************************************\n")
    print("                                 BILLING                                 ")
    print("\n***********************************************************************")
    while begin==True:
        name = input("Enter the name of the product (or 'Done' to finish): ")
        name=name.upper()
        if name == 'DONE':
            print("YOU ARE NOW EXITING FROM BILLING MENU")
            begin=False    
        else:
            quantity = int(input("Enter the quantity: "))
            qry=("select IPrice from Items where IName=%s")
            rec_srch=(name,)
            cursor.execute(qry,rec_srch)
            for price in cursor:
                if price==None:
                    print(f"{name} is not in the list of products.")
                else:
                    price=price[0]
                    name_prod.append(name)
                    price_prod.append(price)
                    qty_prod.append(quantity)
                    total_prod.append(price*quantity)
                    a=price*quantity
                    total=total+a
    data={"PRODUCT NAME":name_prod,"PRICE":price_prod,"Quantity":qty_prod,"Amount":total_prod}
    df=pd.DataFrame(data)
    print(df)
    print("Total Amount ",total)
    cnx.commit()
    cursor.close()
    cnx.close()
start=True
start_1=True
start_2=True
while start:
    print("\n***********************************************************************")
    print("==================== Supermarket Management System ====================")
    print("====================        ABC SUPERMARKET        ====================")
    print("====================           MAIN MENU           ====================")
    print("***********************************************************************")
    print("\n1. Items Menu")
    print("\n2. Customer Menu")
    print("\n3. Billing")
    print("\n0. Exit")
    ch=int(input("\nEnter your choice: "))
    if ch==1:
        print("\nYOU ARE IN ITEMS MENU")
        while start_1:
            print("\n1. Add product")
            print("\n2. Delete product")
            print("\n3. Update product")
            print("\n4. Search Product")
            print("\n5. Display products")
            print("\n0. Exit")
            ch = int(input("Enter your choice: "))
            if ch == 1:
                add_product()
            elif ch == 2:
                delete_product()
            elif ch == 3:
                update_product()
            elif ch == 4:
                search_product()
            elif ch == 5:
                print(display_product())
            elif ch == 0:
                print("YOU ARE NOW EXITING FROM ITEMS MENU.")
                start_1=False
            else:
                print("Invalid choice")
    elif ch==2:
        print("\nYOU ARE IN CUSTOMER MENU")
        while start_2:
            print("\n1. Add customer details")
            print("\n2. Delete customer details")
            print("\n3. Update customer details")
            print("\n4. Search customer details")
            print("\n5. Display customer details")
            print("\n0. Exit")
            ch = int(input("\nEnter your choice: "))
            if ch == 1:
                customer_add()
            elif ch == 2:
                customer_delete()
            elif ch == 3:
                customer_update()
            elif ch == 4:
                customer_search()
            elif ch == 5:
                print(customer_display())
            elif ch == 0:
                print("YOU ARE NOW EXITING FROM ITEMS MENU")
                start_2=False
            else:
                print("Invalid choice.")
    elif ch==3:
        calculate_bill()
        print("\n***** THANK YOU, VISIT AGAIN :) *****")
    elif ch==0:
        print("ARE YOU SURE YOU WANT TO EXIT?\nYES  NO")
        ch=input()
        ch=ch.lower()
        if ch=='yes':
            print("YOU ARE EXITING FROM THE PROGRAM. HAVE A GOOD DAY <3")
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            start=False
    else:
        print("Invalid choice :( \nTry again with another choice.")
        
