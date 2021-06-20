import sqlite3

argdb = ('"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, "name"	TEXT, "value" TEXT',
         '"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, "name" TEXT, "ip"	TEXT NOT NULL, "user"	TEXT NOT NULL')


def initdb(connection):
    print("Starting the database verification...")  # Verify if table exist
    cursordb = connection.cursor()
    listdb_create = ("metadata", "ssh_info")
    for i in range(0, len(listdb_create)):
        command = f"CREATE TABLE IF NOT EXISTS {listdb_create[i]} ({argdb[i]})"
        cursordb.execute(command)
    print("Database verification ended !")


def condb():
    try:
        conn = sqlite3.connect("ssh.db")
    except Exception as e:
        print(f"ERROR WHEN CONNECTING TO DB: {e}")
    return conn


def info_ssh_by_id(id_ssh):
    db = condb()
    cursor = db.cursor()
    id_db = (id_ssh, )
    req = cursor.execute("SELECT * FROM ssh_info WHERE id = ?", id_db)
    for line in req.fetchone():
        name = line[1]
        ip = line[2]
        user = line[3]
        db.close()
        return [name, ip, user]


def fetch_last_ip():
    db = condb()
    cursor = db.cursor()
    metadata_name = ("lastcon", )
    req = cursor.execute("SELECT value FROM metadata WHERE name = ?;", metadata_name)
    try:
        result = req.fetchone()[0]
    except TypeError:
        result = None
    db.close()
    return result
