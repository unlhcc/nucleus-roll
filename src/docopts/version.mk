NAME            = opt-docopts
VERSION         = 0.6.1
RELEASE         = fix2

SOURCE_DIR	= docopts-$(VERSION)

SRC_SUBDIR         = docopts

SOURCE_NAME        = docopts
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION)-$(RELEASE).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

