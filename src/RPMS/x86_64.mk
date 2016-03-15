rpm:: build
	tar xvf *.tar
	-cp *.x86_64*.rpm $(REDHAT.RPMS)/$(ARCH)/
	-cp *64.rpm $(REDHAT.RPMS)/$(ARCH)/
