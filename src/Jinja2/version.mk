NAME            = opt-Jinja2
VERSION         = 2.9.5
RELEASE 	= 0

SOURCE_DIR	= Jinja2-$(VERSION)

SRC_SUBDIR         = Jinja2

SOURCE_NAME        = Jinja2
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

