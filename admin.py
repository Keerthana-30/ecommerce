import helper  

class Product():
    def specifications(self):
        self.category=int(input("Choose the category:\n1. Mobile\n2. Washing Machine\n3. TV\n"))
        self.pid =helper.Validations().idValidations(input("Enter the product ID:"))
        self.name = helper.Validations.nameValidation(input("Enter the product name:"),"Enter the product Name:")
        self.cost = int(input("Enter the cost:"))
        self.currency = input("Enter the currency:")
        self.color = input("Enter the color:")
        
        if (self.category==1):
            self.ram=input("Enter the RAM:")
            self.processor=input("Enter the processor:")  
            self.screensize=input("Enter the screen size:")
            return dict([("ID",self.pid),("Name",self.name),("Product_details",dict([("RAM",self.ram),("Processor",self.processor),("Screensize",self.screensize)])),("Cost",self.cost),("Currency",self.currency),("Category","Mobile"),("Color",self.color)]) 
            
        elif (self.category==2):
            self.capacity=input("Enter the machine capacity:")
            self.rpm=input("Enter the machine rpm:")
            self.type=input("Enter the machine type:")
            return dict([("ID",self.pid),("Name",self.name),("Product_details",dict([("MachineCapacity",self.capacity),("RPM",self.rpm),("MachineType",self.type)])),("Cost",self.cost),("Currency",self.currency),("Category","Washing machine"),("Color",self.color)])
                    
        elif (self.category==3):
            self.isSmart=input("isSmart:")
            self.resolution=input("Enter the resolution:")
            self.screen=input("Enter the screen size:")
            return dict([("ID",self.pid),("Name",self.name),("Product_details",dict([("isSmart",self.isSmart),("Resolution",self.resolution),("Screensize",self.screen)])),("Cost",self.cost),("Currency",self.currency),("Category","TV"),("Color",self.color)])   
    

class Admin(Product):
    
    def createProduct(self):
        pdt= super().specifications()
        helper.execute_query(f"""INSERT INTO product (product_id,product_name,product_cost,product_color,product_category,product_currency) VALUES ('{pdt["ID"]}','{pdt["Name"]}','{pdt["Cost"]}','{pdt["Color"]}','{pdt["Category"]}','{pdt["Currency"]}')""")
        if pdt['Category']=='Mobile':
             rowAffected = helper.execute_query(f"""INSERT INTO mobile values ('{pdt["ID"]}','{pdt["Product_details"]["RAM"]}','{pdt["Product_details"]["Processor"]}','{pdt["Product_details"]["Screensize"]}')""")
        elif pdt['Category']=='Washing machine':
             rowAffected = helper.execute_query(f"""INSERT INTO washingmachine values ('{pdt["ID"]}','{pdt["Product_details"]["MachineCapacity"]}','{pdt["Product_details"]["RPM"]}','{pdt["Product_details"]["MachineType"]}')""")
        elif pdt['Category']=='TV':
             rowAffected = helper.execute_query(f"""INSERT INTO television values ('{pdt["ID"]}','{pdt["Product_details"]["isSmart"]}','{pdt["Product_details"]["Resolution"]}','{pdt["Product_details"]["Screensize"]}')""")
        
        if rowAffected==1:
            print("Product has been added!")
        else:
            helper.execute_query(f"""DELETE FROM product where product_id='{pdt["ID"]}'""" )
            print("Product hasnot been added!!!")               
    
    def deleteProduct(self):   
        helper.execute_query("select count(*) from product")   
        count =  helper.cursor.fetchone()
        if(count[0]==0):
            print("There are no products!")
        else:
            delID=input("Enter the ID of the product to be deleted:")
            rowCount = helper.execute_query(f"""DELETE FROM product where product_id='{delID}'""")
            if rowCount ==0:
                print("ID doesn't exist\n")
            else:
                print("Product has been removed\n")
                