PKGROOT            = /opt/guacamole
NAME               = guacamole-server
VERSION            = 0.9.9
RELEASE            = 0
TARBALL_POSTFIX    = tar.gz

SRC_SUBDIR         = $(NAME)

SOURCE_NAME        = $(NAME)
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = $(TARBALL_POSTFIX)
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS        = $(SOURCE_PKG)

