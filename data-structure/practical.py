#create a todo list
todo_list = ["buy a milk", "buy a bread", "buy a water", "pay the bills"]


# adding the task
# def add_task():
#     task= input("Enter the task: ")
#     todo_list.append(task)
#     print("Task added successfully")
#     print(todo_list)

# add_task()

# def remove_task():
#     task= input("Enter the task: ")
#     if task.lower() not in todo_list:
#         print("Task not found")
#         return
#     else:
#         todo_list.remove(task)
#         print("Task removed successfully")
#         print(todo_list)

# remove_task()

# create a list to store and calculate the frequency of grades
grades = [50, 60, 70, 80, 90, 100]

grades.append(95)
print(grades)

avg_grades = sum(grades) / len(grades)
print(avg_grades)

# fing the highest and lowest grade
highest_grade= max(grades)
lower_grade= min(grades)
print(highest_grade)
print(lower_grade)

inventory=["apples", "bananas", "oranges", "grapes", "kiwi"]

inventory.append("mango")
print(inventory)
# inventory.remove("oranges")
# print(inventory)

#check if its in the stock
item = "oranges"

if item in inventory:
    print(f"{item} is in the stock")
else:
    print(f"{item} is not in the stock")


feedback= ['Great Service!', 'Good Service', 'Average Service', 'Bad Service', 'Terrible Service']
feedback.append('Excellent Service')
print(feedback)

# counting specific service
positive_feedback= sum(1 for comment in feedback if "great" in comment.lower() or "excellent" in comment.lower() or "good" in comment.lower())
print(positive_feedback)

for comment in feedback:
    print(f"{comment}")

