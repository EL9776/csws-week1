Usernames = []

while len(Usernames):
    username = Usernames.pop()
    if username == 'Admin':
        print( 'Hello 1 ' + username)
    elif len(Usernames) == 0: 
        print("We need to find some users ")
    else:
        print("hello " + username)
    