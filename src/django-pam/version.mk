NAME            = opt-django-pam
VERSION         = 1.1.2
RELEASE 	= 0

SOURCE_DIR	= django-pam-$(VERSION)

SRC_SUBDIR         = django-pam

SOURCE_NAME        = django-pam
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

