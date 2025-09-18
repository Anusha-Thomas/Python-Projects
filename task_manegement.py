def task():
    tasks = []

    print("----WELCOME TO THE TASK MANEGEMENT APP-----")

    total_task = int(input("Enter how many task you want to add: "))
    for i in range(1, total_task+1):
        task_name = input(f"Ener task {i} ")
        tasks.append(task_name)

    print(f"Todays task are \n {tasks}")

    while True:
        operation = int(input("Enter\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n")) 
       
        if operation == 1:
            add = input("Enter the task you want to Add = ") 
            tasks.append(add)  
            print(f"task {add} has been sucessfully added....")

        elif operation == 2:
            update_val = input("Enter the task number you want to update = ") 
            if update_val in tasks:
                up = input("Enter a new task = ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"updated task {up}")

        elif operation == 3:
            del_val = input("Enter the task you want to Delete = ") 
            if update_val in tasks:
                up = input("Enter a new task = ")
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has been deleted... ")

        elif operation == 4:
            print(f"Total task = {tasks} ")

        elif operation == 5:
            print("closing the program....")  
            break
        else:
            print("invalid input")  
 

task()