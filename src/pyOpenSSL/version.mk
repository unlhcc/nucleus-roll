NAME            = opt-pyOpenSSL
VERSION         = 16.0.0
RELEASE 	= 0

SOURCE_DIR	= pyOpenSSL-$(VERSION)

SRC_SUBDIR         = pyOpenSSL

SOURCE_NAME        = pyOpenSSL
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

