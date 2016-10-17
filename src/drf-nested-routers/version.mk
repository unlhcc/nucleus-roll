NAME            = opt-drf-nested-routers
VERSION         = 0.11.1
RELEASE 	= 0

SOURCE_DIR	= drf-nested-routers-$(VERSION)

SRC_SUBDIR         = drf-nested-routers

SOURCE_NAME        = drf-nested-routers
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

