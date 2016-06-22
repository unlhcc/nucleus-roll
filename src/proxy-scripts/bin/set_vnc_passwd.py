#!/usr/bin/env python

import argparse
import psutil
import socket
import subprocess
import os, sys


def _setVNCPassword(guest, sleep_time):
	"""Set the VNC connection password for a running guest using the Rocks
	command...

	rocks set host vm vncpasswd <guest> password=random duration=<sleep_time>

	...run via SSH on comet-fe1.

	eg...

	ssh comet-fe1 sudo /opt/rocks/bin/rocks set host vm vncpasswd <guest> password=random duration=<duration>
	"""

	cmd = ['/usr/bin/ssh',
		'-i',
		'/home/nucleus_comet/.ssh/id_rsa_set_vnc_passwd',
		'root@comet-fe1',
		'{host}'.format(host=guest)]

	try:
		retcode = subprocess.call(cmd)
		if retcode < 0:
			print >>sys.stderr, "Child was terminated by signal", -retcode

	except OSError as e:
		print >>sys.stderr, "Execution failed:", e
	
	return retcode


def main():
	parser = argparse.ArgumentParser(description='Set the KVM VNC password for the specified <guest>.')
	parser.add_argument('-G', '--guest', help='KVM guest to tunnel VNC session to (eg. vm-vc3-0 )', required=True)
	parser.add_argument('-s', '--sleep-time', help='sleep time in seconds (default=10)', type=int, default=10)

	args = parser.parse_args()

	# First set a new password on the guest that will be valid for args.sleep_time...
	retcode = _setVNCPassword(args.guest, args.sleep_time)

if __name__ == '__main__':
    main()
