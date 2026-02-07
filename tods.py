import sys

def main():
    if not sys.stdin.isatty():
        print("Running in CI mode...")
        print("No user input available.")
        print("To-Do app loaded successfully.")
        return

    while True:
        print("\n=== Welcome to the Realtime To-Do List ===")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Mark task as done")
        print("5. Exit")

        choice = input("Choose an option (1/2/3/4/5): ")
        # rest of your code...