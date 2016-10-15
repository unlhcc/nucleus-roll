NAME            = opt-cryptography
VERSION         = 1.4
RELEASE 	= 0

SOURCE_DIR	= cryptography-$(VERSION)

SRC_SUBDIR         = cryptography

SOURCE_NAME        = cryptography
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

