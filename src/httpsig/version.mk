NAME            = opt-httpsig
VERSION         = 1.1.2
RELEASE 	= 0

SOURCE_DIR	= httpsig-$(VERSION)

SRC_SUBDIR         = httpsig

SOURCE_NAME        = httpsig
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

