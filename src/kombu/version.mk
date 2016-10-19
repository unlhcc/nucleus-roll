NAME            = opt-kombu
VERSION         = 3.0.34
RELEASE 	= 0

SOURCE_DIR	= kombu-$(VERSION)

SRC_SUBDIR         = kombu

SOURCE_NAME        = kombu
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

