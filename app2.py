# 
# class Validations:
#     def idValidations(self,pid):
#         pattern = re.compile("^PDT+[0-9]{4}")
#         while(True):
#             if (pattern.match(pid)):
#                 rowCount = execute_query(f""" SELECT * FROM product WHERE product_id = '{pid}'""")
#                 if(rowCount!=0):
#                     print("ID already exists")
#                     pid = input("Enter the product ID:")
#                     continue
#                 else:
#                     return pid
#             else:
#                 print("invalid product ID")
#                 pid = input("Enter the product ID:")
#                 continue	
    
    
#     def display(self,query):
#         records_list=[]
#         execute_query(query)
#         records = cursor.fetchall()
#         print('List of Products:\n')
#         print("-----------------------------------------")
#         for i in list(map(list,records)):
#             l = (list(filter(lambda x: x != None,i)))
#             records_list.append(l)
#         for i in records_list:
#             print(i)
               
#     def viewProducts(self):
#             execute_query("select count(*) from product")   
#             count = cursor.fetchone()
#             if(count[0]==0):
#                 print("There are no products!")
#                 return 0
#             pdt=int(input("choose the product category:\n1.Mobile\n2.Washing machine\n3.TV\n4.All"))
#             if pdt==1:
#                 self.display("""SELECT  product.product_id,product.product_name,product.product_cost,product.product_color,product.product_currency,mobile.ram,mobile.processor,mobile.screen_size FROM product JOIN mobile ON product.product_id = mobile.product_id WHERE product.product_category='Mobile'""")
#             elif pdt==2:
#                 self.display("""SELECT  product.product_id,product.product_name,product.product_cost,product.product_color,product.product_currency, washingmachine.machinecapacity, washingmachine.rpm, washingmachine.loadtype FROM product JOIN washingmachine ON product.product_id = washingmachine.product_id WHERE product_category='Washing machine'""")
#             elif pdt==3:
#                 self.display("""SELECT  product.product_id,product.product_name,product.product_cost,product.product_color,product.product_currency,isSmart,resolution,screen_size FROM product JOIN television ON product.product_id = television.product_id WHERE product_category='TV'""")
#             elif pdt==4:
#                 self.display("""SELECT  *
#                 FROM product
#                 left JOIN mobile ON product.product_id = mobile.product_id 
#                 left JOIN washingmachine ON product.product_id= washingmachine.product_id 
#                 left join television ON product.product_id = television.product_id;""")
    	
# class Product(Validations):
#     def specifications(self):
#         self.category=int(input("Choose the category:\n1. Mobile\n2. Washing Machine\n3. TV\n"))
#         self.pid = super().idValidations(input("Enter the product ID:"))
#         self.name = input("Enter the product name:")
#         self.cost = int(input("Enter the cost:"))
#         self.currency = input("Enter the currency:")
#         self.color = input("Enter the color:")
        
#         if (self.category==1):
#             self.ram=input("Enter the RAM:")
#             self.processor=input("Enter the processor:")  
#             self.screensize=input("Enter the screen size:")
#             return dict([("ID",self.pid),("Name",self.name),("Product_details",dict([("RAM",self.ram),("Processor",self.processor),("Screensize",self.screensize)])),("Cost",self.cost),("Currency",self.currency),("Category","Mobile"),("Color",self.color)]) 
            
#         elif (self.category==2):
#             self.capacity=input("Enter the machine capacity:")
#             self.rpm=input("Enter the machine rpm:")
#             self.type=input("Enter the machine type:")
#             return dict([("ID",self.pid),("Name",self.name),("Product_details",dict([("MachineCapacity",self.capacity),("RPM",self.rpm),("MachineType",self.type)])),("Cost",self.cost),("Currency",self.currency),("Category","Washing machine"),("Color",self.color)])
                    
#         elif (self.category==3):
#             self.isSmart=input("isSmart:")
#             self.resolution=input("Enter the resolution:")
#             self.screen=input("Enter the screen size:")
#             return dict([("ID",self.pid),("Name",self.name),("Product_details",dict([("isSmart",self.isSmart),("Resolution",self.resolution),("Screensize",self.screen)])),("Cost",self.cost),("Currency",self.currency),("Category","TV"),("Color",self.color)])   
    
# class Admin(Product):
#     def __init__(self):
#         pass
#     def createProduct(self):
#         pdt= super().specifications()
#         execute_query(f"""INSERT INTO product (product_id,product_name,product_cost,product_color,product_category,product_currency) VALUES ('{pdt["ID"]}','{pdt["Name"]}','{pdt["Cost"]}','{pdt["Color"]}','{pdt["Category"]}','{pdt["Currency"]}')""")
#         if pdt['Category']=='Mobile':
#              rowAffected = execute_query(f"""INSERT INTO mobile values ('{pdt["ID"]}','{pdt["Product_details"]["RAM"]}','{pdt["Product_details"]["Processor"]}','{pdt["Product_details"]["Screensize"]}')""")
#         elif pdt['Category']=='Washing machine':
#              rowAffected = execute_query(f"""INSERT INTO washingmachine values ('{pdt["ID"]}','{pdt["Product_details"]["MachineCapacity"]}','{pdt["Product_details"]["RPM"]}','{pdt["Product_details"]["MachineType"]}')""")
#         elif pdt['Category']=='TV':
#              rowAffected = execute_query(f"""INSERT INTO television values ('{pdt["ID"]}','{pdt["Product_details"]["isSmart"]}','{pdt["Product_details"]["Resolution"]}','{pdt["Product_details"]["Screensize"]}')""")
        
#         if rowAffected==1:
#             print("Product has been added!")
#         else:
#             execute_query(f"""DELETE FROM product where product_id='{pdt["ID"]}'""" )
#             print("Product hasnot been added!!!")               
    
#     def deleteProduct(self):   
#         execute_query("select count(*) from product")   
#         count = cursor.fetchone()
#         if(count[0]==0):
#             print("There are no products!")
#         else:
#             delID=input("Enter the ID of the product to be deleted:")
#             rowCount = execute_query(f"""DELETE FROM product where product_id='{delID}'""")
#             if rowCount ==0:
#                 print("ID doesn't exist\n")
#             else:
#                 print("Product has been removed\n")
    
# class ShoppingCart:
#     def cart(self,customer_list):
#         cart={}
#         tcost=0
#         print(customer_list)
#         print("------------\nCart Details\n------------")
#         for i in customer_list:
#             cart[i]=customer_list.count(i)
#         print("ID NAME QTY COST\n")
#         for i in cart:
#             print("{} {} {} {}".format(i[0],i[1],i[2],(i[3]*cart[i])))
#             tcost+=(i[3]*cart[i])
#         print(f"Total Cost: {tcost}")

#     def payment(self):
#         print("Choose the payment method:")
#         pay=int(input("1. Credit/Debit Card\n2. Net Banking\n3. Gpay\n4. PhonePay\n5. Paytm\n6. COD\n"))
#         if(pay==1):
#             print("Credit/Debit card")
#             cardName = input("Enter the name on the card:\n")
#             cardNo = int(input("Enter the card Number:\n"))
#             cvv = int(input("Enter the CVV:\n"))
#             mmyy = input("Enter the mm/yy:")
           
#         elif pay==6:
#             print("Order placed")
#             quit()
#         else:
#             print("Please enter a correct option")

# class Customer(Validations,ShoppingCart):
#         def __init__(self):
#             self.customer_list=[]
            
#         def addProduct(self):
#             while(True):
#                 pdtId=input("Enter the ID of the product you want to add:\n")
#                 execute_query(f"""SELECT * FROM product where product_id = '{pdtId}' """)
#                 product = cursor.fetchone()
#                 self.customer_list.append(product)
#                 print("Product added to the cart!")
#                 print(self.customer_list)
#                 break

#         def delete(self):
#             if(len(self.customer_list)==0):
#                 print("Cart is empty!")
#                 return 0
#             else:
#                 dele=input("Enter the ID of the product you want to delete:\n")
#                 print(self.customer_list)
#                 for i in self.customer_list:
#                         if i[0]==dele:
#                             self.customer_list.remove(i)
#                             print("product removed!\n")
#                             return 1
#                 print("ID doesn't exist")
#                 return 0
                  
#Main function
# if __name__=="__main__": 
#         print( "Welcome to shopping site".center(150,'-'))
#         while(True):
#             try:
#                 user=int(input("Choose one:\n1. Admin\n2. Customer\n"))
#                 break
#             except ValueError as e:
#                 print("Invalid option. please enter a valid option.")
#         #Admin
#         match user:
#             case 1:
#                 admin = Admin()
#                 while(True):
#                     try:
#                         choice=int(input("Enter the option:\n1.ADD\n2.DELETE\n3.DISPLAY\n4.EXIT\n"))
#                     except ValueError:
#                         print("Invalid option. please enter a valid option.")
#                     else:
#                         if choice==4:
#                             break
#                         while(True):
#                             if choice==1:
#                                 admin.createProduct()
#                                 break
#                             elif choice==2:
#                                 admin.deleteProduct()
#                                 break
#                             elif choice==3:
#                                 admin.viewProducts()
#                                 break
#             case 2:
#                 cust = Customer()
#                 while(True):
#                     cust.viewProducts()
#                     action=int(input("1. Add to Cart\n2. Delete Product\n3. Cart\n"))
#                     if action==1:
#                         cust.addProduct()
#                         nav = int(input("1.Go to cart page\n2.Explore\n"))
#                         if(nav==1):
#                             print(cust.customer_list)
#                             cust.cart(cust.customer_list)
#                             value=int(input("Choose option:\n1.Pay\n2.Explore\n"))
#                             if(value==1):
#                                cust.payment()
#                             elif (value==2):
#                                 continue
#                         else: 
#                             continue
#                     elif action==2:
#                         if (cust.delete()==0):
#                             continue
#                     elif action==3:
#                         cust.cart(cust.customer_list)
            
               



import helper
import admin
import customer 
import cart                 
#Main function

if __name__=="__main__": 
    print( "Welcome to shopping site".center(150,'-'))
    user=int(input("Choose one:\n1. Admin\n2. Customer\n"))
    #Admin
    match user:
            case 1:
                admin = admin.Admin()
                while(True):
                    choice=int(input("Enter the option:\n1.ADD\n2.DELETE\n3.DISPLAY\n4.EXIT\n"))
                    if choice==4: 
                        break
                    while(True):
                        if choice==1:
                            admin.createProduct()
                            break
                        elif choice==2:
                            admin.deleteProduct()
                            break
                        elif choice==3:
                            helper.Validations().viewProducts()
                            break                                    
            case 2:
                cust = customer.Customer()
                while(True):
                    helper.Validations().viewProducts()
                    action=int(input("1. Add to Cart\n2. Delete Product\n3. Cart\n"))
                    if action==1:
                        cust.addProduct()
                        nav = int(input("1.Go to cart page\n2.Explore\n"))
                        if(nav==1):
                            print(cust.customer_list)
                            cart.ShoppingCart().cart(cust.customer_list)
                            value=int(input("Choose option:\n1.Pay\n2.Explore\n"))
                            if(value==1):
                                cust.payment()
                            elif (value==2):
                                continue
                        else: 
                            continue
                    elif action==2:
                        if (cust.delete()==0):
                            continue
                        elif action==3:
                            cart.ShoppingCart().cart(cust.customer_list)    
       
               




















































































































# def nameValidation(self,pname):
#         pattern = re.compile("^(?=.{2,20}$)(([a-zA-Z_\s])\\2?(?!\\2))+$")
#         while(True):
#             if (pattern.match(pname)):
#                 return pname
#             else:
#                 print("invalid product name")
#                 pname = input("Enter the product name:")
#                 continue