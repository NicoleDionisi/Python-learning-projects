import os
List=[]
if os.path.exists("todo.txt"):
  with open("todo.txt", "r") as file:
    List=[line.strip() for line in file.readlines()]
    print("List imported succesfully.")
else:
  print("List not found. Creating a new list.")
while True:
 main=input("this is your to do list, what would you like to do?" \
            " 1.Add  2.See list  3.Delete   4.Exit  5.Reset ") 
 while True:
   if main.isdigit():
    main=int(main)
    if main==1:
     Task=input("What would you like to add on your list? ")
     List.append(Task)
     print("Task added succesfully")
     with open("todo.txt", "w") as file:
       for task in List:
         file.write(task+"\n")
     break
    if main==2:
      if not List:
       print("Your list is empty")
       break
      else:
       print("Your To do list is ")
       for n, Task in enumerate(List):
        print(f"{n+1} {Task}")
      break
    if main==3: 
      if not List:
        print("Your list is empty.")
        break
      else:
        deleted=input("What would you like to delete from your list? ")
        if deleted.isdigit():
          deleted=int(deleted)
          if 1<=deleted<=len(List):
            List.pop(deleted-1)
            print("Task deleted succesfully.")
            with open("todo.txt", "w") as file:
              for task in List:
                file.write(task+"\n")
            break
          else:
           print("You must say the number of a task in your list")
          break
        else:
         print("You must say the number of a task in your list")
         break
    if main==4:
      print("Ok, bye.")
      exit()
    if main==5:
      conf=input("Are you sure you want to delete EVERYTHING? (yes/no): ")
      if conf.lower()=="yes":
        List.clear()
        with open("todo.txt", "w") as file:
          file.write("")
        print("List reset successfully. ")
        break
      if conf.lower()=="no":
        print("Reset cancelled.")
        break

    else:
        print("Please select a valid option.   ")
   else: 
    print("please select a number.  ")
   break
