NAME            = opt-enum
VERSION         = 0.4.6
RELEASE 	= 0

SOURCE_DIR	= enum-$(VERSION)

SRC_SUBDIR         = enum

SOURCE_NAME        = enum
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

