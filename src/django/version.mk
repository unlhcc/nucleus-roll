NAME            = opt-Django
VERSION         = 1.9.4
RELEASE 	= 0

SOURCE_DIR	= Django-$(VERSION)

SRC_SUBDIR         = Django

SOURCE_NAME        = Django
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

