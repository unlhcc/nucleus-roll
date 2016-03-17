# SDSC "nucleus" roll

## Overview

This roll bundles the Nucleus virtual cluster management software for Comet.

## Requirements

To build/install this roll you must have root access to a Rocks development
machine (e.g., a frontend or development appliance).

If your Rocks development machine does *not* have Internet access you must
download the appropriate nucleus source file(s) using a machine that does
have Internet access and copy them into the `src/<package>` directories on your
Rocks development machine.


## Dependencies

The sdsc-roll must be installed on the build machine, since the build process
depends on make include files provided by that roll.


## Building

To build the nucleus-roll, execute this on a Rocks development
machine (e.g., a frontend or development appliance):

```shell
% make 2>&1 | tee build.log
```

A successful build will create the file `nucleus-*.disk1.iso`.  If you built
the roll on a Rocks frontend, proceed to the installation step. If you built the
roll on a Rocks development appliance, you need to copy the roll to your Rocks
frontend before continuing with installation.


## Installation

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To make working for development:

On service node:
Comment /opt/python/lib/python2.7/site-packages/nucleus_service/nucleus/settings.py   CSRF_COOKIE_SECURE = True line, otherwise requires secure connection

Do chmod 644 /opt/rocks/etc/.nucleus.my.cnf , TODO: make belonging to apache user

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To install, execute these instructions on a Rocks frontend:

```shell
% rocks add roll *.iso
% rocks enable roll nucleus
% cd /export/rocks/install
% rocks create distro
% rocks run roll nucleus | bash
```

In addition to the software itself, the roll installs nucleus environment
module files in:

```shell
/opt/modulefiles/applications/nucleus
```


## Testing

The nucleus-roll includes a test script which can be run to verify proper
installation of the roll documentation, binaries and module files. To
run the test scripts execute the following command(s):

```shell
% /root/rolltests/nucleus.t 
```

