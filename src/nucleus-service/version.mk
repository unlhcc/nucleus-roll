NAME            = nucleus-service
VERSION         = 1.0
BUILD_HASH 	= 1a8ad0c
RELEASE        :=$(shell bash ../../version.sh -r).g$(BUILD_HASH)

SOURCE_DIR	= $(NAME)

GIT_REPO	= ssh://git@forge.sdsc.edu:7999/xsd/$(NAME).git
