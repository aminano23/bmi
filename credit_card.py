
def mask_credit_card(card_number):
   
    if len(card_number) != 16 or not card_number.isdigit():
        print("Invalid card number")
        return
    

    masked_card = '*' * 12 + card_number[-4:]
    
    print(f"Masked Card: {masked_card}")

card_number = input("Enter a credit card number: ")
12
mask_credit_card(card_number)


