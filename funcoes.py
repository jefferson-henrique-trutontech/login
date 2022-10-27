def verif_login(username, passw, users):
    for user in users:
        if username.lower() == user[0].lower() and passw == user[1]:
            return True
    return False

def verif_cadastro(username, passw, verifPass, users):
    for user in users:
        if username.lower() == user[0].lower() or username == '':
            return False
    if passw != verifPass or passw == '':
        return False
    return True
