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

The roll binds together img-storage, rabbitmq and kvm functionality and requires all those to be installed in the cluster.


## Building

The roll should be built on a devel appliance. THe default httpd server will be replaced with a newer version (2.4) by the bootstrap script.

First run bootstrap on a dev machine:

```shell
% ./bootstrap.sh
```

Then to build the nucleus-roll, execute this on a Rocks development machine

```shell
% make 2>&1 | tee build.log
```

A successful build will create the file `nucleus-*.disk1.iso`. Copy the roll to your Rocks
frontend before continuing with installation.


## Installation

=======================================

<mark>
To make working for development with no proxy node:
</mark>

On service node:
Comment /opt/python/lib/python2.7/site-packages/nucleus_service/nucleus/settings.py   CSRF_COOKIE_SECURE = True line, otherwise requires secure connection

Do chmod 644 /opt/rocks/etc/.nucleus.my.cnf , TODO: make belonging to apache user

=======================================

To install, execute these instructions on a Rocks frontend:

```shell
% rocks add roll *.iso
% rocks enable roll nucleus
% cd /export/rocks/install
% rocks create distro
% rocks run roll nucleus | bash
```

There's a number of manual configuration steps required after the roll's been successfully installed.

The nodes which need to communicate to RabbitMQ server need to be added to RabbitMQ server as users. That's done by the ~root/bin/rabbitmq_config.sh script on the frontend. The nodes will authenticate with its certificates (added on the next step). The only node not added by the script is comet-damn, since it's a service node and we don't want to add proxy node which is also a service node. Either add one by hand to RabbitMQ or add to the script.

(In prod might also want to replace the ```rabbitmq_host=`rocks list host attr` ``` with actual RabbitMQ hostname, since grepping all the params takes forever).

After installing the sec roll, distribute the node certs to nodes:

run ```/usr/share/star69/scripts/S11nucleus <node_ip>``` for every node in the cluster which talks to rabbitmq nucleus exchange.

After that, the public cert from the frontend and ALL compute and CVC goes to /var/secrets/cometvc/pub/ on damn node, and pub cert from damn node goes to the same location on the frontend. That allows Celery decrypt the messges from those hosts. The files should have the .pem extension.

All nodes should be in ssh_known_hosts. Do this with: ```rocks report knownhosts > /etc/ssh/ssh_known_hosts```, then remove &lt;file&gt; &lt;/file&gt; tags,  ```make -C /var/411```

/etc/sdsc/sudoers File should have service and NAS hosts, apache should be able to run /opt/nucleus-scripts/bin/open_tunnel.py on damn node

Set up PAM on damn node for nucleus Yubikey auth to work:
- /etc/pam.d/nucleus
- /etc/nucleus-radius.conf

/etc/img-storage.conf should have "secur_server": true on the frontend and img-storage-vm service running to serve the encryption key to other nodes. All nodes whould have certs defined in /etc/img-storage.conf. Should be done by conf roll, but worth checking.

/opt/rocks/etc/rabbitmq.conf - should have the right RabbitMQ server location

On frontend set /opt/python/lib/python2.7/site-packages/nucleus_service/update_status.py NAS to proper value.

On damn node /opt/python/lib/python2.7/site-packages/nucleus_service/nucleus/settings.py ALLOWED_HOSTS should contain the name of proxy (f.e. comet-nucleus.local)

To add users to nucleus, modify /opt/python/lib/python2.7/site-packages/nucleus_service/nucleus/settings.py on damn node: uncomment the line with django.contrib.auth.backends.ModelBackend and restart the httpd. The passwords will start working and you can login with ~root/.django_admin password. Then comment the line again to only use Yubikeys.

On damn node change to the right hostname in /etc/httpd/conf/httpd.conf, several places:
```
Require host comet-nucleus.local
```