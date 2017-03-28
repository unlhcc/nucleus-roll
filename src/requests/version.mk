NAME            = opt-requests
VERSION         = 2.13.0
RELEASE 	= 0

SOURCE_DIR	= requests-$(VERSION)

SRC_SUBDIR         = requests

SOURCE_NAME        = requests
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

