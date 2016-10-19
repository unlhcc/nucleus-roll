NAME            = opt-billiard
VERSION         = 3.3.0.23
RELEASE 	= 0

SOURCE_DIR	= billiard-$(VERSION)

SRC_SUBDIR         = billiard

SOURCE_NAME        = billiard
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

