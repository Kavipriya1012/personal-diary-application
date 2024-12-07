import os
import json
from datetime import datetime

# File to store the diary entries
DIARY_FILE = "diary.json"

# Function to load diary entries from file
def load_diary():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, "r") as file:
            return json.load(file)
    return {}

# Function to save diary entries to file
def save_diary(diary_entries):
    with open(DIARY_FILE, "w") as file:
        json.dump(diary_entries, file, indent=4)

# Function to add a new diary entry
def add_entry(diary_entries):
    date = input("Enter the date for the diary entry (YYYY-MM-DD): ")
    if date in diary_entries:
        print(f"Diary entry for {date} already exists. You can edit it.")
    else:
        entry = input(f"Write your diary entry for {date}: ")
        diary_entries[date] = entry
        save_diary(diary_entries)
        print(f"Diary entry for {date} has been saved.")

# Function to view diary entries
def view_entries(diary_entries):
    if not diary_entries:
        print("No diary entries available.")
        return

    print("\nDiary Entries:")
    for date, entry in sorted(diary_entries.items()):
        print(f"Date: {date} - Entry: {entry}")

# Function to delete a diary entry
def delete_entry(diary_entries):
    date = input("Enter the date of the diary entry to delete (YYYY-MM-DD): ")
    if date in diary_entries:
        del diary_entries[date]
        save_diary(diary_entries)
        print(f"Diary entry for {date} has been deleted.")
    else:
        print("No entry found for this date.")

# Function to search for an entry by date
def search_entry(diary_entries):
    date = input("Enter the date to search for (YYYY-MM-DD): ")
    if date in diary_entries:
        print(f"Diary entry for {date}: {diary_entries[date]}")
    else:
        print("No entry found for this date.")

# Function to display the menu
def display_menu():
    print("\nPersonal Diary Application")
    print("1. Add Diary Entry")
    print("2. View Diary Entries")
    print("3. Delete Diary Entry")
    print("4. Search Diary Entry by Date")
    print("5. Exit")

# Main program logic
def main():
    diary_entries = load_diary()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_entry(diary_entries)
        elif choice == "2":
            view_entries(diary_entries)
        elif choice == "3":
            delete_entry(diary_entries)
        elif choice == "4":
            search_entry(diary_entries)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
