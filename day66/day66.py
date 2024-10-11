# საშუალო არითმეტიკის გამოთვლისთვის
def average_grade(grades):
    if len(grades) != 5:
        raise ValueError("გთხოვთ, გადააჭარბოთ 5 საგნის ნიშნებს.")
    return sum(grades) / len(grades)

# ფუნქცია, რომელიც ითვლის, რამდენ წელში გახდებით 18 წლის
def years_until_18(current_age):
    if current_age >= 18:
        return 0
    return 18 - current_age

# მაგალითი: 
# 1. საშუალო არითმეტიკა
grades = [7, 8, 9, 6, 10]
average = average_grade(grades)
print(f"საშუალო არითმეტიკული: {average}")

# 2. ასაკი
current_age = 15
years_left = years_until_18(current_age)
print(f"{years_left} წელი დარჩა, რომ 18 წლის გახდეთ.")