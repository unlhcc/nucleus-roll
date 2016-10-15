NAME            = opt-pycparser
VERSION         = 2.14
RELEASE 	= 0

SOURCE_DIR	= pycparser-$(VERSION)

SRC_SUBDIR         = pycparser

SOURCE_NAME        = pycparser
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

