def mass_pwd():
    with open("Master_Password.txt", "r") as f:
        master_password=f.read()
    return master_password
