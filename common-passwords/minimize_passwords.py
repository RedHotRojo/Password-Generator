write = open("common_passwords.txt.min.txt", 'w')
write.write('\n'.join([pswd for pswd in open("common_passwords.txt", 'r').read().split('\n') if len(pswd) >= 8]))
write.close()