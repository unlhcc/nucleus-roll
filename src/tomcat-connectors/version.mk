NAME            = tomcat-connectors
VERSION         = 1.2.41
RELEASE 	= src

SOURCE_DIR	= $(NAME)-$(VERSION)

SRC_SUBDIR         = $(NAME)

SOURCE_NAME        = $(NAME)
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION)-$(RELEASE).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

