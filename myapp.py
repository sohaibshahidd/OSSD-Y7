import tkinter as tk

def read_file():
    try:
        with open("users.txt", "r") as f:
            return [line.strip().split(",") for line in f.readlines()]
    except:
        return []

def write_file(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")

def login():
    users = read_file()
    u = entry_user.get()
    p = entry_pass.get()

    for user, pwd in users:
        if user == u and pwd == p:
            result.config(text="Login Successful")
            return

    result.config(text="Invalid Credentials")

def signup():
    u = entry_user.get()
    p = entry_pass.get()

    users = read_file()

    for user, _ in users:
        if user == u:
            result.config(text="User already exists")
            return

    write_file(u, p)
    result.config(text="Signup Successful")

def main():
    global entry_user, entry_pass, result

    tk.Label(root, text="Username").pack()
    entry_user = tk.Entry(root)
    entry_user.pack()

    tk.Label(root, text="Password").pack()
    entry_pass = tk.Entry(root, show="*")
    entry_pass.pack()

    tk.Button(root, text="Login", command=login).pack()
    tk.Button(root, text="Signup", command=signup).pack()

    result = tk.Label(root, text="")
    result.pack()

root = tk.Tk()
root.title("Login System")

main()

root.mainloop()
