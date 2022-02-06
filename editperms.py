import subprocess
import os
usr = subprocess.check_output('whoami').decode('utf-8')
usr_2 = usr.replace('\n', "")
os.system("sudo chown {0} /usr/bin/pimarket".format(usr_2))
