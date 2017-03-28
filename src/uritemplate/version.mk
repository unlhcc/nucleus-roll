NAME            = opt-uritemplate
VERSION         = 3.0.0
RELEASE 	= 0

SOURCE_DIR	= uritemplate-$(VERSION)

SRC_SUBDIR         = uritemplate

SOURCE_NAME        = uritemplate
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

