# Asks the user how many students will register (loop length)
# Creates a new text file and opens it for writing
num_students = int(input("How many students will register? "))
print("Student ID registration form: \n")
with open('reg_form.txt', 'w') as output_file:
    output_file.write("ID List: \n\n")
    for i in range(num_students):
        ID = input(f"Student {i+1}, enter your ID number: ")
        output_file.write(f"\tStudent {i+1}:\t{ID} sign here: _____________________\n")# Asks each student for their ID and writes it into the text file with the Sign line
print("Success! All IDs have been saved in reg_form.txt")



