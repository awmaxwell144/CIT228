currentUsers = ["John","Bob","Emily","Isabel","Charlie","Admin"]
newUsers = ['Emerson','BOB','Lily','george','Ben']

currentLower = [user.lower() for user in currentUsers]

for new in newUsers:
    if new.lower() in currentLower:
        print(f'Sorry {new}, that name is taken')
    else:
        print(f'Great, {new} is still available')
