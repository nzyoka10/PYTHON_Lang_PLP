"""
    # * Week 3 Assignment
    # 
    #~ Function to calculate the final price after applying a discount.

        #!           Parameters:
        #*              - price: The original price of the item.
        #*               - discount_percent: The discount percentage.

    #*              Returns:
    #*               - The final price after applying the discount, or the original price if no discount is applied.
"""

# create function calculate_discount
def calculate_discount(price, discount_percent):
    
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        
        #* calculate  discount amount
        discount_amount = price * (discount_percent / 100)
        
        #* apply discount to the original price
        final_price = price - discount_amount
        
        #* return the final price after applying the discount
        return final_price
    
    else:
        # If the discount is less than 20%, return the original price
        return price

#^ Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

#* Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

#* Check if a discount was applied
if final_price != original_price:
    
    #* If a discount was applied, print the final price after applying the discount
    print("Final price after applying the discount: Kes:.", final_price)
    
else:
    #* If no discount was applied, print the original price
    print("No discount applied. \n Original price: Kes:.", original_price)
