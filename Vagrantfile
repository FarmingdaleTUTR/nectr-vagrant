Vagrant.configure(2) do |config|

    # vagrant box
    config.vm.box = "ubuntu/trusty64"

    # ports to access the virtual machine
    config.vm.network "forwarded_port", guest: 8000, host: 8111,
        auto_correct: true

    # shared folder setup
    config.vm.synced_folder ".", "/home/vagrant/nectrvagrant"


    # SSH agent forwarding
    config.ssh.forward_agent = true

    # provisioning script
    config.vm.provision "shell", path: "vagrant/provision.sh",
        privileged: false

end
