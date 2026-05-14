from diary import *
from data import diary

def main():
 
  diary.extend(load_entries())

  print("==================\nPERSONAL DIARY CLI\n==================")

  print("1. Add Entry\n2. Show Entries\n3. Delete Entry\n4. Search Entry\n5. Exit")

  while True:

    option = int(input("Enter an option : "))

    if option == 1:
      add_entry()

    elif option == 2:
      show_entries()

    elif option == 3:
      delete_entry()
      
    elif option == 4:
      search_entry()

    elif option == 5:
      print("Goodbye!")

      break

    save_entries()
    
main()
