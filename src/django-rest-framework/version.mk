NAME            = opt-djangorestframework
VERSION         = 3.6.2
RELEASE 	= 0

SOURCE_DIR	= djangorestframework-$(VERSION)

SRC_SUBDIR         = djangorestframework

SOURCE_NAME        = djangorestframework
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

