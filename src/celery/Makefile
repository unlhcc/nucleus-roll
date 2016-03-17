
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
	tar -xvzf $(SOURCE_PKG)
	@echo "::: Package $(NAME) build complete :::"

install::
	( \
	    $(MODULE_LOAD_PYTHON); \
	    cd $(SOURCE_DIR); \
	    python setup.py install --root=$(ROOT); \
        )

	mkdir -p $(ROOT)/etc/init.d
	mkdir -p $(ROOT)/etc/default
	( \
	    $(INSTALL) -m755 initd/* $(ROOT)/etc/init.d; \
	    $(INSTALL) -m755 default/* $(ROOT)/etc/default \
	)

	@echo "::: Package $(NAME) install complete :::"

clean::
	rm -rf $(SOURCE_DIR)

