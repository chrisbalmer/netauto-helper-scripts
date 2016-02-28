import console, keychain
device = raw_input('Enter device hostname or IP: ')
username = raw_input('Enter username: ')
password = console.secure_input('Enter password: ')

keychain.set_password(device, username, password)

print 'Account saved to keychain.'