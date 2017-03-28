NAME            = opt-coreapi
VERSION         = 2.3.0
RELEASE 	= 0

SOURCE_DIR	= coreapi-$(VERSION)

SRC_SUBDIR         = coreapi

SOURCE_NAME        = coreapi
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

