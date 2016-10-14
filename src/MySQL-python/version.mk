NAME            = sdsc-MySQL-python
VERSION         = 1.2.5
RELEASE 	= 0

SOURCE_DIR	= MySQL-python-$(VERSION)

SRC_SUBDIR         = MySQL-python

SOURCE_NAME        = MySQL-python
SOURCE_VERSION     = $(VERSION)
SOURCE_SUFFIX      = zip
SOURCE_PKG         = $(SOURCE_NAME)-$(SOURCE_VERSION).$(SOURCE_SUFFIX)
SOURCE_DIR         = $(SOURCE_PKG:%.$(SOURCE_SUFFIX)=%)

ZIP_PKGS           = $(SOURCE_PKG)

