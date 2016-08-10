
REDHAT.ROOT = $(CURDIR)/../../

	    #CFLAGS="-Wl,-rpath=/opt/python/lib:/opt/gnu/gmp/lib" 
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
	    $(MODULE_LOAD_GMP); \
	    cd $(SOURCE_DIR); \
	    patch -p0 < $(CURDIR)/gmp_module.diff; \
	    python setup.py install --root=$(ROOT); \
        )
	@echo "::: Package $(NAME) install complete :::"

clean::
	rm -rf $(SOURCE_DIR)

