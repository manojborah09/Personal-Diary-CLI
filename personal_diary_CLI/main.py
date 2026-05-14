import json

def add_entry():

  entry = {
    'Title' : input("Enter title : "),
    'Content' : input("Enter content : ")
  }
  
  diary.append(entry)


def view_entry():
  print("===== ALL ENTRIES =====")

  for i in load_entries():
    for key,value in i.items():
      print(key,value)

def exit_program():
  return "Goodbye"

def save_entries():
  with open('diary.json' , 'w') as f:
    json.dump(diary,f,indent=4)

def load_entries():
  with open('diary.json' , 'r') as f:
    content_of_json = json.load(f)

  return content_of_json

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

  save_entries()

diary = load_entries()
main()






