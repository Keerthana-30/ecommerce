import helper
class Customer():
        def __init__(self):
            self.customer_list=[]
            
        def addProduct(self):
            while(True):
                pdtId=input("Enter the ID of the product you want to add:\n")
                helper.execute_query(f"""SELECT * FROM product where product_id = '{pdtId}' """)
                product =helper.cursor.fetchone()
                self.customer_list.append(product)
                print("Product added to the cart!")
                print(self.customer_list)
                break

        def delete(self):
            if(len(self.customer_list)==0):
                print("Cart is empty!")
                return 0
            else:
                dele=input("Enter the ID of the product you want to delete:\n")
                helper.Validations().idValidations(dele)
                for i in self.customer_list:
                        if i[0]==dele:
                            self.customer_list.remove(i)
                            print("product removed!\n")
                            return 1
                print("ID doesn't exist")
                return 0
                
                
                