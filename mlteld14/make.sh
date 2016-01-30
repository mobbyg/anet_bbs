#/bin/bash

# ddtelnetd make and installation script
#
# By Frank Linhares
#
# version 1.2


if [ -z "$1" ]; then
  echo -e "\nUsage:\n"
  echo -e "make.sh -compile"
  echo -e "to compile and NOT install\n"
  echo -e "OR\n"
  echo -e "make.sh -install"
  echo -e "to compile and INSTALL in /usr/bin/\n"
  exit 1
fi


if [ "$1" = "-compile" ]; then
	g++ -o ddtelnetd ddtelnetd.c -lutil
	echo "done"
	exit 1
fi

if [ "$1" = "-install" ]; then
	if [[ $EUID -ne 0 ]]; then
  		echo "You must be a root user to install ddtelnetd" 2>&1
  		exit 1
	else
  		g++ -o ddtelnetd ddtelnetd.c -lutil
		chmod +x ddtelnetd
		cp ddtelnetd /usr/bin/
		echo "done"
		exit 1
	fi
fi