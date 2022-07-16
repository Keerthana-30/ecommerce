from copy import error
import mysql.connector
import re

connection = mysql.connector.connect(host='localhost',database='applications',user='root',password='123456789',buffered=True)
cursor = connection.cursor()
def execute_query(query):
    try:
        cursor.execute(query)
        connection.commit()
        return cursor.rowcount
    except error:
        print(f"Error: '{error}'")

class Validations:
    def idValidations(self,pid):
        pattern = re.compile("^PDT+[0-9]{4}")
        while(True):
            if (pattern.match(pid)):
                rowCount = execute_query(f""" SELECT * FROM product WHERE product_id = '{pid}'""")
                if(rowCount!=0):
                    print("ID already exists")
                    pid = input("Enter the product ID:")
                    continue
                else:
                    return pid
            else:
                print("invalid product ID")
                pid = input("Enter the product ID:")
                continue

    def nameValidation(self,pname,text):
        pattern = re.compile("^[A-Za-z]{20}")
        while(True):
            if (pattern.match(pname)):
                return pname
            else:
                print("invalid Name.No special characters are allowed.")
                pname = input(text)
                continue	
    
    def display(self,query):
        records_list=[]
        execute_query(query)
        records = cursor.fetchall()
        print('List of Products:\n')
        print("-----------------------------------------")
        for i in list(map(list,records)):
            l = (list(filter(lambda x: x != None,i)))
            records_list.append(l)
        for i in records_list:
            print(i)
               
    def viewProducts(self):
            execute_query("select count(*) from product")   
            count = cursor.fetchone()
            if(count[0]==0):
                print("There are no products!")
                return 0
            pdt=int(input("choose the product category:\n1.Mobile\n2.Washing machine\n3.TV\n4.All"))
            if pdt==1:
                self.display("""SELECT  product.product_id,product.product_name,product.product_cost,product.product_color,product.product_currency,mobile.ram,mobile.processor,mobile.screen_size FROM product JOIN mobile ON product.product_id = mobile.Mob_pdt_id WHERE product.product_category='Mobile'""")
            elif pdt==2:
                self.display("""SELECT  product.product_id,product.product_name,product.product_cost,product.product_color,product.product_currency, washingmachine.machinecapacity, washingmachine.rpm, washingmachine.loadtype FROM product JOIN washingmachine ON product.product_id = washingmachine.was_pdt_id WHERE product_category='Washing machine'""")
            elif pdt==3:
                self.display("""SELECT  product.product_id,product.product_name,product.product_cost,product.product_color,product.product_currency,isSmart,resolution,screen_size FROM product JOIN television ON product.product_id = television.tel_pdt_id WHERE product_category='TV'""")
            elif pdt==4:
                self.display("""SELECT  *
                FROM product
                left JOIN mobile ON product.product_id = mobile.Mob_pdt_id 
                left JOIN washingmachine ON product.product_id= washingmachine.was_pdt_id 
                left join television ON product.product_id = television.tel_pdt_id;""")


