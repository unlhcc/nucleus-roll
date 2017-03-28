NAME            = opt-vine
VERSION         = 1.1.3
RELEASE 	= 0

SOURCE_DIR	= vine-$(VERSION)

SRC_SUBDIR         = vine

SOURCE_NAME        = vine
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

