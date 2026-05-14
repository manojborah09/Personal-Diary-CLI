import json
from data import diary

def save_entries():
  # funtion to convert entries input by the user in the diary list into json file

  with open('personal_diary_CLI/diary.json' , 'w') as f:
    json.dump(diary,f,indent = 4)

def load_entries():
  # function to use the data inside the json file and convert to pyhton object whenwver needed

  with open('personal_diary_CLI/diary.json' , 'r') as f:
    content_of_json = json.load(f)

  return content_of_json