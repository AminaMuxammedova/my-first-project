#1-masala
student_grades = {"Matematika": 90, "Fizika": 85, "Informatika": 95}
#1-vazifa
student_grades["Kimyo"] = 88
result1 = student_grades
print("1-vazifa natijasi:", result1)
#2-vazifa
student_grades["Fizika"] = 87
result2 = student_grades
print("2-vazifa natijasi:", result2)
#3-vazifa
del student_grades["Informatika"]
result3 = student_grades
print("3-vazifa natijasi:", result3)
#4-vazifa
result4 = sum(student_grades.values())
print("4-vazifa natijasi:", result4)
#5-vazifa
result5 = sum(student_grades.values()) / len(student_grades)
print("5-vazifa natijasi:", result5)
#6-vazifa
result6 = max(student_grades.values())
print("6-vazifa natijasi:", result6)
#7-vazifa
result7 = min(student_grades.values())
print("7-vazifa natijasi:", result7)
#8-vazifa
result8 = list(student_grades.keys())
print("8-vazifa natijasi:", result8)
#9-vazifa
result9 = list(student_grades.values())
print("9-vazifa natijasi:", result9)
#10-vazifa
result10 = len(student_grades) == 0
print("10-vazifa natijasi:", result10)

#2-masala
fruits = {"olma": 5000, "banan": 12000, "uzum": 8000}
#1-vazifa
fruits["anor"] = 10000
result1 = fruits
print("1-vazifa natijasi:", result1)
#2-vazifa
fruits["banan"] = 15000
result2 = fruits
print("2-vazifa natijasi:", result2)
#3-vazifa
del fruits["uzum"]
result3 = fruits
print("3-vazifa natijasi:", result3)
#4-vazifa
result4 = sum(fruits.values())
print("4-vazifa natijasi:", result4)
#5-vazifa
result5 = max(fruits, key=fruits.get)
print("5-vazifa natijasi:", result5)
#6-vazifa
result6 = min(fruits, key=fruits.get)
print("6-vazifa natijasi:", result6)
#7-vazifa
result7 = sorted(fruits.values())
print("7-vazifa natijasi:", result7)
#8-vazifa
result8 = len(fruits)
print("8-vazifa natijasi:", result8)
#9-vazifa
result9 = fruits.get("olma")
print("9-vazifa natijasi:", result9)
#10-vazifa
result10 = sorted(fruits.keys())
print("10-vazifa natijasi:", result10)

#3-masala
cities = {"Toshkent": 2500000, "Samarqand": 550000, "Buxoro": 280000}
#1-vazifa
cities["andijon"] = 600000
result1 = cities
print("1-vazifa natijasi:",result1)
#2-vazifa
cities["toshkent"] = 2600000
result2 = cities
print("2-vazifa natijasi:", result2)
#3-vazifa
del cities["buxoro"]
result3 = cities
print("3-vazifa natijasi:", result3)
#4-vazifa
result4 = sum(cities.values())
print("4-vazifa natijasi:", result4)
#5-vazifa
result5 = sum()































