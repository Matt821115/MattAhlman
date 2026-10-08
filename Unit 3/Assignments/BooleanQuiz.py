#   5 comparison operators
less_than_four = float(input("Give me a number that is less than 4.\n>> "))
print(less_than_four < 4)
is_twelve = float(input("Give me the number twelve.\n>> "))
print(is_twelve == 12)
greater_than_six = float(input("Give me a number greater than six.\n>> "))
print(greater_than_six > 6)
gt_or_e_sixty_nine = float(input("Give me a number greater than or equal to sixty-nine.\n>> "))
print(gt_or_e_sixty_nine >= 69)
lt_or_e_four_twenty = float(input("Give me a number less than or equal to four hundred twenty.\n>> "))
print(lt_or_e_four_twenty <= 420)

#   3 logical operators
best_robot = input("what is the best 2025-2026 FRC team?\n>> ")
print(best_robot == ("4414" or "HighTide" or "4414 HighTide" or "HighTide 4414"))
best_videogame = input("What is the best video game?\n>> ")
print(best_videogame == ("tetris" or "Tetris" or "pong" or "Pong"))
password = input("Type in your password:\n>> ")
print(password == "your password")
