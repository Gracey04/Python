def to_do_list():
    tasks= []

    while True:
        print("1- Add task")
        print("2- remove task")
        print("3- view tasks")
        print("4- Exit")

        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            print("Task added succesfully")
        
        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:  
                tasks.remove(task)
                print("Task removed")
            else:
                print("Task not found")

        elif choice == "3":
            if len(task) == "0":
                print("Your to do list is empty")
            else:
                print("Your to do list")
                for task in tasks:
                    print(task)

        elif choice == "4":
            print("Your tasks are saved")
            break

        else:
            print("Invalid option, try again")
        
to_do_list()
            


    
    

      

    

