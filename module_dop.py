#Дополнительное практическое задание по модулю: "Базовые структуры данных."
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list (students) #переводим массив в список
students_az = (sorted(students_list)) #сортируем список по алфавиту
#print( students_az ) - проверка
len_of_grades = (len(grades)) #длина списка оценок
#print(len_of_grades, type(len_of_grades))
grades_new =[None]*(len_of_grades) #создаем пустой список той же длины, что и список оценок

for i in range(len_of_grades):  #заполняем новый список средними баллами в цикле
  #  print(i, grades[i]) - проверка
    grades_new[i] = (sum(grades[i])/len(grades[i]))
   # print (grades_new[i]) - проверка
#print(grades_new) - проверка
table_students =dict(zip (students_az,grades_new )) #сшиваем 2 списка с помощью zip в словарь dict
print (table_students)

#grades_new_too = int(map(sum(grades)/len(grades)),grades) какой синтаксис у map? вместо цикла применить map
#print(grades_new_too)
