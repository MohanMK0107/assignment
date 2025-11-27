def calculate_compound_interest(principal, interest, period):
    r = interest / 100
    total_amount = principal * (1 + r) ** period
    ci = total_amount - principal
    print(f"Your Annual Compound Interest for Rs.{principal} over {period} years at {interest}% interest is: Rs {ci:.2f}")
    return ci, total_amount

calculate_compound_interest(10000, 10, 5)
