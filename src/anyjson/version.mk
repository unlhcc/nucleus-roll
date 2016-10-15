NAME            = opt-anyjson
VERSION         = 0.3.3
RELEASE 	= 0

SOURCE_DIR	= anyjson-$(VERSION)

SRC_SUBDIR         = anyjson

SOURCE_NAME        = anyjson
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

