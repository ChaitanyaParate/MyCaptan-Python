import csv
def write_into_csv(info_list):
    with open("Student_info.csv" , mode="a" , newline='' ) as csv_file:
        writer = csv.writer(csv_file)
        
        
        if csv_file.tell() == 0:
            writer.writerow(["Name" , "Age" , "Contact" , "E-mail"])

        
        writer.writerow(info_list)




condition = True

student_num = 1

while(condition):
    student_info = input("\nEnter the information of the student for student #{} in the following format - \n(Name Age Contact E-mail ID): ".format(student_num))
    
    
    splited_student_info = student_info.split(" ")
    
    
    print("\nThe entered information is - \nName: {} \nAge: {} \nContact: {} \nE-mail ID: {}"
          .format(splited_student_info[0], splited_student_info[1], splited_student_info[2], splited_student_info[3]))
    
    conformation = input("Is the entered information correct? (yes/no): ")
    
    if conformation == "yes":
        
        write_into_csv(splited_student_info)
        student_num = student_num + 1
        
        
        admin_choice = input("Input (yes/no) if you want to enter the information of another student: ")
        
        if admin_choice == "yes":
            condition = True
        
        elif admin_choice == "no": 
            
            condition = False

    elif conformation == "no":
        print("\nPlease re-enter the information!")
    
    
    
        