from collections import Counter
import helper
class ShoppingCart:
    def cart(self,customer_list):
        cart={}
        tcost=0
        print(customer_list)
        print("------------\nCart Details\n------------")
        for i in customer_list:
            cart[i]=customer_list.count(i)
        print("ID NAME QTY COST\n")
        for i in cart:
            print("{} {} {} {}".format(i[0],i[1],i[2],(i[3]*cart[i])))
            tcost+=(i[3]*cart[i])
        print(f"Total Cost: {tcost}")

    def payment(self):
        print("Choose the payment method:")
        pay=int(input("1. Credit/Debit Card\n2. Net Banking\n3. Gpay\n4. PhonePay\n5. Paytm\n6. COD\n"))
        if(pay==1):
            self.creditCard()           
        elif pay==6:
            print("Order placed")
            quit()
        else:
            print("Please enter a correct option")
    
    def creditCard(self):
        print("Credit/Debit")
        self.cardName = helper.Validations.nameValidation(input("Enter the name on the card:\n"),"Enter the name on the card:\n")

        self.cardNo = int(input("Enter the card Number:\n"))
        
        self.cvv = int(input("Enter the CVV:\n"))
        self.mmyy = input("Enter the mm/yy:")   

        
        
    #     digits = digits_of(card_number)
    #     odd_digits = digits[-1::-2]
    #     even_digits = digits[-2::-2]
    #     checksum = 0
    #     checksum += sum(odd_digits)
    #     for d in even_digits:
    #         checksum += sum(digits_of(d*2))
    #     return checksum % 10

    # print('Valid') if luhn_checksum("4532015112830366")==0 else print('Invalid') 

            

            
            