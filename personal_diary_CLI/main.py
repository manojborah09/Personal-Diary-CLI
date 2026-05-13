diary = []

def add_entry():

  entry = {
    'Title' : input("Enter title : "),
    'Content' : input("Enter content : ")
  }
  
  diary.append(entry)


def view_entry():
  print("===== ALL ENTRIES =====")

  for i in diary:
    for key,value in i.items():
      print(key,value)

def exit_program():
  return "Goodbye"

def main():

  print('''====================
  PERSONAL DIARY CLI
    ====================''')
    
  print('''1. Add Entry
  2. View Entries
  3. Exit''')
    

  while True:

    option = int(input("Choose an option : "))

    if option == 1:
      add_entry()

    elif option == 2:
      view_entry()

    elif option == 3:
      exit_program()
      break

main()






