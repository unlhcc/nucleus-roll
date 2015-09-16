# Don't re-import Rules-linux-centos.mk
__RULES_LINUX_CENTOS_MK = yes

REDHAT.ROOT = $(CURDIR)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

ifeq ($(REDHAT.ROOT),)
REDHAT.ROOT     = /usr/src/redhat
endif
ifeq ($(REDHAT.VAR),)
REDHAT.VAR      = /var
endif

REDHAT.SOURCES  = $(REDHAT.ROOT)/SOURCES
REDHAT.SPECS    = $(REDHAT.ROOT)/SPECS
REDHAT.BUILD    = $(REDHAT.ROOT)/BUILD
REDHAT.RPMS     = $(REDHAT.ROOT)/RPMS
REDHAT.SRPMS    = $(REDHAT.ROOT)/SRPMS

ifneq ($(RPM.BUILDROOT),)
BUILDROOT = $(RPM.BUILDROOT)
else
BUILDROOT = $(shell pwd)/$(NAME).buildroot
endif

HOME	= $(CURDIR)

.PHONY: $(HOME)/.rpmmacros
$(HOME)/.rpmmacros:
	rm -f $@
	@echo "%_topdir $(REDHAT.ROOT)" > $@
	@echo "%_buildrootdir $(BUILDROOT)" >> $@
	@echo "%buildroot $(BUILDROOT)" >> $@
	@echo "%_var    $(REDHAT.VAR)" >> $@
	@echo "%debug_package   %{nil}" >> $@

repo_clone: 
	git clone $(GIT_REPO) $(NAME)
	( \
	  cd $(NAME); \
	  git checkout $(RELEASE); \
	)

rpm: $(HOME)/.rpmmacros repo_clone
	mkdir -p $(REDHAT.ROOT)/RPMS/x86_64
	mkdir -p $(REDHAT.SOURCES)
	mkdir -p $(REDHAT.SRPMS)
	( \
	  cd $(NAME); \
	  python setup.py bdist_rpm ; \
	  mv dist/*.x86_64.rpm $(REDHAT.ROOT)/RPMS/x86_64; \
	  mv dist/*.src.rpm $(REDHAT.SRPMS)/; \
	  mv dist/*.tar.gz $(REDHAT.SOURCES)/; \
	)

clean::
	rm -f $(HOME)/.rpmmacros
	rm -rf $(NAME)
