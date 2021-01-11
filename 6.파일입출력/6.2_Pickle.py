users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f = open('users.txt', 'wb')
import pickle
pickle.dump(users, f)
f.close()