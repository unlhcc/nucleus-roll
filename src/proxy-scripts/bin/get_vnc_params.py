#!/usr/bin/env python

import argparse
import json
import subprocess
import os, sys


def _getVNCParamsForGuest(guest):
	"""Get the configured VNC connection parameters for a running guest
	using the Rocks command...

	rocks list host vm vnc <guest> showpassword=true

	eg..

	ssh comet-fe1 sudo /opt/rocks/bin/rocks list host vm vnc <guest> showpassword=true
	"""
	cmd = ['/usr/bin/ssh',
		'-i',
		'/home/nucleus_comet/.ssh/id_rsa_get_vnc_params',
		'root@comet-fe1',
		'{host}'.format(host=guest)]

	try:
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

	except OSError as e:
		print >>sys.stderr, "Execution failed:", e

	params = ''
	for line in iter(proc.stdout.readline,''):
		import re
		params += line.rstrip().strip()
		# If you care about NOT getting a JSON array with only one element uncomment
		# the following two lines...
		#params = re.sub(r'^\[','',params,1)
		#params = re.sub(r'\]$','',params,1)
	
	return params

def main():
	parser = argparse.ArgumentParser(description='Get the VNC connection parameters for <guest>.')
	parser.add_argument('-G', '--guest', help='KVM guest to obtain VNC connection parameters for (eg. vm-vc3-0 )', required=True)

	args = parser.parse_args()

	# Second obtain phys-host of <guest>...
	params = _getVNCParamsForGuest(args.guest)

	if params is None:
		sys.exit(os.EX_OSERR)
	else:
		print >>sys.stdout, params

	sys.exit(os.EX_OK)

if __name__ == '__main__':
    main()
