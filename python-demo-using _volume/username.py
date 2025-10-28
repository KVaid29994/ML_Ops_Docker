import os

FILENAME = "usernames.txt"

def ensure_file_exists():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            pass  # Create empty file

def load_usernames():
    with open(FILENAME, "r") as file:
        return list(set(line.strip() for line in file if line.strip()))

def save_username(username):
    with open(FILENAME, "a") as file:
        file.write(username + "\n")

def main():
    print("👋 Welcome! Let's manage your usernames.")
    ensure_file_exists()

    usernames = load_usernames()

    new_username = input("📝 Enter a new username: ").strip()
    if not new_username:
        print("⚠️ No username entered. Nothing saved.")
        return

    if new_username in usernames:
        print(f"🔁 '{new_username}' already exists in the list.")
    else:
        save_username(new_username)
        print(f"✅ '{new_username}' has been saved.")
        print(f"\n🎉 Welcome, {new_username}!")

    show_list = input("\n📋 Do you want to see the list of all usernames? (yes/no): ").strip().lower()
    if show_list in ["yes", "y"]:
        updated_usernames = sorted(set(load_usernames() + [new_username]))
        print("\n📜 Stored usernames:")
        for name in updated_usernames:
            print(f" - {name}")
    else:
        print("👍 Okay! You can view the list next time.")

if __name__ == "__main__":
    main()