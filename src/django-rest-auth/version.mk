NAME            = opt-django-rest-auth
VERSION         = 0.9.1
RELEASE 	= 0

SOURCE_DIR	= django-rest-auth-$(VERSION)

SRC_SUBDIR         = django-rest-auth

SOURCE_NAME        = django-rest-auth
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

