NAME            = opt-itypes
VERSION         = 1.1.0
RELEASE 	= 0

SOURCE_DIR	= itypes-$(VERSION)

SRC_SUBDIR         = itypes

SOURCE_NAME        = itypes
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

