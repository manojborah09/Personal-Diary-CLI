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

def delete_entry():
  view_entry()

  num = int(input("Enter entry number to delete :"))
  diary.pop(num-1)


def search_entry():
  keyword = input("Enter the keyword the search the entry : ")

  for entry in diary:
    if keyword.lower() in entry['Title'] or keyword.lower() in entry['Content']:
      
      print("===== MATCH FOUND =====")

      for key , value in entry.items():
        print(key,value)

def main():

  print('''==================== \n PERSONAL DIARY CLI \n ==================== \n''')
    
  print('''1. Add Entry \n 2. View Entries \n 3. Delete \n 4. Search \n 5. Exit \n''')
    
  while True:

    option = int(input("Choose an option : "))

    if option == 1:
      add_entry()

    elif option == 2:
      view_entry()

    elif option == 3:
      delete_entry()

    elif option == 4:
      search_entry()

    elif option == 5:
      exit_program()
      break

  save_entries()

diary = load_entries()
main()






