import json
import os

DIARY_FILE = "app/data/diary.json"

def init_diary():
  if not os.path.exists(DIARY_FILE):
    with open(DIARY_FILE, 'w') as file:
      json.dump([], file)

def add_entry(entry):
  if not entry.strip():
    print("Error: The diary entry cannot be empty.")
    return
  
  with open(DIARY_FILE, 'r') as file:
    entries = json.load(file)

  next_id = 1

  if entries:
    next_id = max(entry["id"] for entry in entries) + 1

  new_entry = {
    "id": next_id,
    "description": entry
  }

  entries.append(new_entry)


  with open(DIARY_FILE, 'w') as file:
    json.dump(entries, file, indent=2)

def get_entries():
  with open(DIARY_FILE, 'r') as file:
    entries = json.load(file)
  return entries

def format_entry(entry):
  return f"{entry['id']}. {entry['description']}"

def delete_entry(entry_id):
  with open(DIARY_FILE, 'r') as file:
    entries = json.load(file)
  
  entries = [entry for entry in entries if entry['id'] != entry_id]

  with open(DIARY_FILE, 'w') as file:
    json.dump(entries, file, indent=2)