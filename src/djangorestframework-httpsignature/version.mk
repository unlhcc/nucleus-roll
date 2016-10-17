NAME            = opt-djangorestframework-httpsignature
VERSION         = 1.0.0
RELEASE 	= 0

SOURCE_DIR	= djangorestframework-httpsignature-$(VERSION)

SRC_SUBDIR         = djangorestframework-httpsignature

SOURCE_NAME        = djangorestframework-httpsignature
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = tar.gz
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

TAR_GZ_PKGS           = $(SOURCE_PKG)

