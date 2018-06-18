# Using the vagrant box
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) including download the "Oracle VM VirtualBox Extension Pack"
* Install [Vagrant](https://www.vagrantup.com/downloads.html)

In a terminal (Windows users can use powershell)
```
vagrant init lennyt/magma \
  --box-version 0.0.1
vagrant up
vagrant ssh
```

# Building the vagrant box

```
vagrant up
vagrant package
```

## Resources
* http://code-chronicle.blogspot.com/2014/08/connect-usb-device-through-vagrant.html
* https://sonnguyen.ws/connect-usb-from-virtual-machine-using-vagrant-and-virtualbox/
