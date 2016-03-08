rpm:: build
	-cp *.x86_64.rpm $(REDHAT.RPMS)/$(ARCH)/
	-cp *64.rpm $(REDHAT.RPMS)/$(ARCH)/
