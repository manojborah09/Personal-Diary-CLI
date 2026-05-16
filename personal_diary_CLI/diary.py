from data import *
from storage import *
import datetime

def add_entry():
  # function to input data or entry

  entry = { 
    'title' : input('Enter Title : '),
    'content' : input('Enter Content : '),
    'time' : datetime.datetime.today().isoformat()
  }

  diary.append(entry)

def show_entries():
  # function to view all the entries in the list 

  print("===== All Entries =====")

  for i in load_entries():
    for key,value in i.items():
      print(f"{key.upper()} : {value}")
     
    print("========================")
 

def delete_entry():
  # function to delete entry according to the indices

  show_entries()

  index_to_delete = int(input("Enter the index to delete : "))
  diary.pop(index_to_delete-1)

def search_entry():
  # function to search entry using keyword
  
  keyword_entry = input("Enter a keyword to search entry : ")

  for entry in diary:
    if keyword_entry.lower() in entry['title'] or keyword_entry.lower() in entry['content'] :

      print("====== Match Found ======")

      for key,value in entry.items():
        print(key,value)

