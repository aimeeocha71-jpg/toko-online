def login(username, password):
    if username == "aimeeocha71" and password == "12345":
        return "Login berhasil!"
    else:
        return "Username atau password salah!"


print("=== LOGIN TOKO ONLINE ===")

username = input("Username: ")
password = input("Password: ")

print(login(username, password))