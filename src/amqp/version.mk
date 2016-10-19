NAME            = opt-amqp
VERSION         = 1.4.9
RELEASE 	= 0

SOURCE_DIR	= amqp-$(VERSION)

SRC_SUBDIR         = amqp

SOURCE_NAME        = amqp
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

