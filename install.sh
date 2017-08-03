
#!/usr/bin/env bash

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     machine=Linux;;
    Darwin*)    machine=Mac;;
    CYGWIN*)    machine=Cygwin;;
    MINGW*)     machine=MinGw;;
    *)          machine="UNKNOWN:${unameOut}"
esac

echo "Your system: ${machine}"
echo ""

if [ ${machine} = Linux ] ; then
	echo "--install ansible for debian system--"
	apt-get install software-properties-common -y 
	apt-add-repository ppa:ansible/ansible -y
	apt-get update
	apt get install ansible -y 
	echo "Successful"
	ansible --version

elif [ ${machine} = Cygwin ] ; then
	apt-cyg install git python-{jinja2,six,yaml}
	git clone --depth 1 git://github.com/ansible/ansible
	cd ansible
	PATH+=:~+/bin
	export PYTHONPATH=~+/lib
	ansible --version
fi

