import subprocess
import os
usr = subprocess.check_output('whoami')
os.system("sudo chown {0} /usr/bin/pimarket".format(usr))
