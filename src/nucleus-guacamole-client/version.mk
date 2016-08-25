NAME            = nucleus-guacamole-client
VERSION         = 0.9.8
BUILD_HASH      = 34eddef
RELEASE        :=$(shell bash ../../version.sh -r).g$(BUILD_HASH)

SOURCE_DIR      = $(NAME)

GIT_REPO        = ssh://git@forge.sdsc.edu:7999/xsd/$(NAME).git
