# Using the vagrant box
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) including the "Oracle VM VirtualBox Extension Pack"
* Install [Vagrant](https://www.vagrantup.com/downloads.html)

In a terminal (Windows users can use powershell)
```
$ vagrant init --minimal lennyt/magma --box-version 0.0.2
$ vagrant up
$ vagrant ssh
vagrant@vagrant-ubuntu-trusty-64:~$ cd magmathon
vagrant@vagrant-ubuntu-trusty-64:~$ git pull && git submodule update
vagrant@vagrant-ubuntu-trusty-64:~$ cd tests
vagrant@vagrant-ubuntu-trusty-64:~$ make clean
vagrant@vagrant-ubuntu-trusty-64:~$ make
```

# Building the vagrant box
This should only be done when changing the Vagrantfile or if you wish to provision a custom vagrant box from scratch. Most users should use the pre-built box using the instructions above.
```
vagrant up
vagrant package
```

### Resources
These resources were helpful in configuring the Vagrant box for USB passthrough.
* http://code-chronicle.blogspot.com/2014/08/connect-usb-device-through-vagrant.html
* https://sonnguyen.ws/connect-usb-from-virtual-machine-using-vagrant-and-virtualbox/
