REDHAT.ROOT = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

build:
	
install::
	/bin/mkdir -p $(ROOT)/$(PKGROOT)/bin
	( \
	  for F in bin/*; do \
	    if test ! -d $${F}; then \
	      install -m0755 $${F} $(ROOT)/$(PKGROOT)/bin; \
	    fi; \
	  done \
	)
clean::
