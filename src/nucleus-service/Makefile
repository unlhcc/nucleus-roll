
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

repo_clone: 
	git clone $(GIT_REPO) $(NAME)
	( \
	  cd $(NAME); \
	  git checkout $(RELEASE); \
	)

install:: repo_clone
	( \
	    $(MODULE_LOAD_PYTHON); \
	    cd $(NAME); \
	    python setup.py install --root=$(ROOT) \
        )
	@echo "::: Package $(NAME) install complete :::"

clean::
	rm -rf $(SOURCE_DIR)

#rpm:: repo_clone
#	    python setup.py install --prefix=$(ROOT)/opt/python --root=/opt/python \
#	( \
#		cd $(NAME); \
#		python setup.py bdist_rpm; \
#		mkdir -p $(REDHAT.RPMS)/noarch; \
#		mv dist/nucleus_service-0.0.1-1.noarch.rpm $(REDHAT.RPMS)/noarch/; \
#	)
