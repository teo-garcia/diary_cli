import inquirer
from inquirer import errors
from app import core


def add_entry():
    questions = [
        inquirer.Text("entry", message="Enter your diary entry")
    ]

    answer = inquirer.prompt(questions)
    entry = answer['entry']
    core.add_entry(entry)
    print("Diary entry added.")


def view_entries():
    print("Previous entries:")
    entries = core.get_entries()
    for entry in entries:
        print(core.format_entry(entry))
    


def main():
    core.init_diary()
    print("Welcome to the Diary App 🤓")
    while True:
        questions = [
            inquirer.List("action", message="Choose an option", choices=[
                ("1. Add a new entry.", add_entry),
                ("2. View past entries.", view_entries),
                ("3. Exit", None)
            ])
        ]

        try:
            answers = inquirer.prompt(questions)
            action = answers["action"]

            if action is None:
                break
            elif callable(action):
                action()
        except errors.EndOfInput as e:
            break


if __name__ == '__main__':
    main()
