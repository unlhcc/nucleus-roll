NAME            = opt-django-rest-swagger
VERSION         = 2.1.2
RELEASE 	= 0

SOURCE_DIR	= django-rest-swagger-$(VERSION)

SRC_SUBDIR         = django-rest-swagger

SOURCE_NAME        = django-rest-swagger
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

