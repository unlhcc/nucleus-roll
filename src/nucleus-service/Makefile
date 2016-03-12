
REDHAT.ROOT = $(CURDIR)/../../

ifndef PYPATH
  PYPATH = python
endif
PYVERSION = $(shell $(PYPATH) -c "from __future__ import print_function;import sys;print(sys.version[:3])")


-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
include pull.mk

build: $(SRC_DIRS)
	@echo "::: Package $(NAME) build complete :::"

repo_clone: 
	git clone $(GIT_REPO) $(NAME)
	( \
	  cd $(NAME); \
	  git checkout $(RELEASE); \
	)

install:: repo_clone
	( \
	    cd $(NAME); \
	    $(PY.PATH) setup.py install --root=$(ROOT) \
        )
	@echo "::: Package $(NAME) install complete :::"

clean::
	rm -rf $(SOURCE_DIR)

#rpm:: repo_clone
#	( \
#		cd $(NAME); \
#		python setup.py bdist_rpm; \
#		mkdir -p $(REDHAT.RPMS)/noarch; \
#		mv dist/nucleus_service-0.0.1-1.noarch.rpm $(REDHAT.RPMS)/noarch/; \
#	)
