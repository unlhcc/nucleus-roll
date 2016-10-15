NAME            = opt-cffi
VERSION         = 1.7.0
RELEASE 	= 0

SOURCE_DIR	= cffi-$(VERSION)

SRC_SUBDIR         = cffi

SOURCE_NAME        = cffi
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

