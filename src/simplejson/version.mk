NAME            = opt-simplejson
VERSION         = 3.10.0
RELEASE 	= 0

SOURCE_DIR	= simplejson-$(VERSION)

SRC_SUBDIR         = simplejson

SOURCE_NAME        = simplejson
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

