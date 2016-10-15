NAME            = opt-python-pam
VERSION         = 1.8.2
RELEASE 	= 0

SOURCE_DIR	= python-pam-$(VERSION)

SRC_SUBDIR         = python-pam

SOURCE_NAME        = python-pam
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

