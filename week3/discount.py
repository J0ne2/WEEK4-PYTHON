def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Test with fixed values instead of input
original_price = 100.0
discount_percentage = 25.0

# Calculate final price
final_price = calculate_discount(original_price, discount_percentage)

# Display result
if discount_percentage >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount applied: {discount_percentage}%")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")