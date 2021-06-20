from meta import cls, ask_yes_no
from db import condb, info_ssh_by_id
from subprocess import call


def showallssh():
    db = condb()
    cursor = db.cursor()
    cls()
    print("All your ssh connection :")
    req = cursor.execute("SELECT * FROM ssh_info")
    for line in req.fetchall():
        id_ssh = line[0]
        name = line[1]
        ip = line[2]
        user = line[3]
        print("")
        print(f"Connection n°{id_ssh} '{name}' : ")
        print("IP : ", ip)
        print("User: ", user)
    db.close()


def addssh():
    db = condb()
    cursor = db.cursor()
    cls()
    print("ADDING A SSH USER :")
    print("\n")
    print("We need information about your new user !")
    ssh_name = input("The name of your connection (leave blank for using ip as name) : ")
    ssh_add_ip = input("Host IP : ")
    if not ssh_name:
        ssh_name = ssh_add_ip
    ssh_add_user = input("Username : ")
    ask_yes_no("Do you use a password for auth [y/n] ? ")
    new_ssh = (cursor.lastrowid, ssh_name, ssh_add_ip, ssh_add_user)
    print("\n")
    print(f"Information about your new SSH connection '{ssh_name}' :")
    print(f"IP Address : {ssh_add_ip}")
    print(f"User : {ssh_add_user}")
    add_conf = ask_yes_no("Do you want to add this ssh connection [y/n] ? ")
    if add_conf == "n":
        return
    cursor.execute("INSERT INTO ssh_info (id, name, ip, user) VALUES(?, ?, ?, ?)", new_ssh)
    db.commit()
    print(f"Connection n°{cursor.lastrowid} : {ssh_name} added with sucess")
    db.close()


def sshcon():
    id_to_con = int(input("Enter the number of the SSH connection you want to connect to : "))
    ssh_info = info_ssh_by_id(id_to_con)
    ip = ssh_info[1]
    user = ssh_info[2]
    cls()
    call(["ssh", f"{user}@{ip}"])
