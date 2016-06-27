#!/usr/bin/env python

import argparse
import socket
import subprocess
import os, sys


def _getUnusedPort():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', 0))
	addr,port = s.getsockname()
	s.close()
	return port

def _createTunnel(port, vnc_params, command):
	if port is 0:
		port = _getUnusedPort();

	cmd = ['/usr/bin/ssh',
		'-f',
		'-o',
		'BatchMode=yes',
		'-o',
		'ExitOnForwardFailure=yes',
		'-L',
		'{local_port}:localhost:{host_port}'.format(local_port=port, host_port=vnc_params['hostport']),
		'{remote_host}'.format(remote_host=vnc_params['hostname']),
		'{remote_cmd}'.format(remote_cmd=command)]

	try:
		p = subprocess.Popen(cmd)
		p.communicate()
		if p.returncode < 0:
			print >>sys.stderr, "Child was terminated by signal %d" % (-p.returncode)
			port = -p.returncode
		else:
			if p.returncode > 0:
				print "Child returned %d" % p.returncode
				port = -p.returncode

	except OSError as e:
		print >>sys.stderr, "Execution failed:", e

	return port;

def main():
	parser = argparse.ArgumentParser(description='Create SSH port-forward from <port> on localhost to KVM VNC server <hostport> on <hostname>.')
	parser.add_argument('-P', '--port', help='Port on localhost to tunnel VNC session to (default = 0)', required=False, default=0)
	parser.add_argument('-H', '--hostname', help='Physical host to tunnel VNC session to (eg. comet-01-01 )', required=True)
	parser.add_argument('-p', '--hostport', help='KVM VNC service listening port (eg. 5900)', required=True)
	parser.add_argument('-s', '--sleep-time', help='sleep time in seconds (default=10)', type=int, default=10)

	args = parser.parse_args()

	vnc_params = {'hostname': args.hostname, 'hostport': args.hostport}
	remote_cmd = 'sleep {sleep_time}'.format(sleep_time=args.sleep_time)

	# Create a tunnel that will stay open for args.sleep_time...
	port = _createTunnel(args.port, vnc_params, remote_cmd);

	if port < 0:
		sys.exit(os.EX_OSERR)
	else:
		#print "https://comet-nucleus.sdsc.edu/nucleus-guacamole/index.html?hostname=localhost&port=%d" % (port)
		print >>sys.stdout, "%d" % (port)

	sys.exit(os.EX_OK)

if __name__ == '__main__':
    main()
