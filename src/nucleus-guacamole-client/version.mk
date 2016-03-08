NAME               = nucleus-guacamole-client
VERSION            = 0.9.8
RELEASE            = 0
TARBALL_POSTFIX    = tgz

SRC_SUBDIR         = $(NAME)

SOURCE_NAME        = $(NAME)
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tgz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TGZ_PKGS           = $(SOURCE_PKG)

