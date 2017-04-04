NAME            = opt-celery
VERSION         = 4.0.2
RELEASE 	= 0

SOURCE_DIR	= celery-$(VERSION)

SRC_SUBDIR         = celery

SOURCE_NAME        = celery
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

