
REDHAT.ROOT = $(CURDIR)/../../

ROLLPY = python

ifndef PYPATH
  PYPATH = python
endif
PYVERSION = $(shell $(PYPATH) -c "from __future__ import print_function;import sys;print(sys.version[:3])")

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
include $(SDSCDEVEL)/Pull.mk
include $(SDSCDEVEL)/Rules.mk

build:: $(SRC_DIRS)
	@echo "::: Package $(NAME) build complete :::"

install::
	( \
	    cd $(SOURCE_DIR)/native; \
	    ./configure --with-apxs=/usr/bin/apxs; \
	    make; \
	    mkdir -p $(ROOT)/usr/lib64/httpd/modules/; \
	    cp apache-2.0/mod_jk.so $(ROOT)/usr/lib64/httpd/modules/; \
        )
	@echo "::: Package $(NAME) install complete :::"

clean::
	rm -rf $(SOURCE_DIR)

