NAME            = opt-openapi-codec
VERSION         = 1.3.1
RELEASE 	= 0

SOURCE_DIR	= openapi-codec-$(VERSION)

SRC_SUBDIR         = openapi-codec

SOURCE_NAME        = openapi-codec
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

