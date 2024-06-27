def month_to_season(a):
     if a in (12,1,2):
         return ("Зима")
     elif a == 3 or a == 4 or a == 5:
         return("Весна")
     elif a == 6 or a == 7 or a == 8:
         return("Лето")
     elif a == 9 or a == 10 or a == 11:
         return("Осень")
     else: return("укажите правильный номер месяца")
print(month_to_season(int(input('введите номер месяца '))))