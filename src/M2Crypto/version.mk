NAME            = opt-M2Crypto
VERSION         = 0.23.0
RELEASE 	= 0

SOURCE_DIR	= M2Crypto-$(VERSION)

SRC_SUBDIR         = M2Crypto

SOURCE_NAME        = M2Crypto
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

