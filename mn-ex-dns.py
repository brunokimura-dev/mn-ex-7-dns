Last login: Wed Apr 30 08:48:05 on console

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
kimura@Brunos-MacBook-Pro (~) $ !ssh
ssh kimura@200.133.202.157 -p18084
kimura@200.133.202.157's password: 
Permission denied, please try again.
kimura@200.133.202.157's password: 
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-213-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

  System information as of Wed Apr 30 13:58:36 UTC 2025

  System load:  0.69                Users logged in:        0
  Usage of /:   70.6% of 915.81GB   IP address for ens20f3: 172.20.22.13
  Memory usage: 5%                  IP address for lxcbr0:  10.0.3.1
  Swap usage:   0%                  IP address for virbr0:  192.168.122.1
  Processes:    562

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Infrastructure is not enabled.

0 updates can be applied immediately.

344 additional security updates can be applied with ESM Infra.
Learn more about enabling ESM Infra service for Ubuntu 18.04 at
https://ubuntu.com/18-04


Last login: Fri Apr 25 21:45:22 2025 from 200.144.94.3
kimura@baldurdia:~$ 















kimura@baldurdia:~$ cd 25-
25-mltcp/         25-topicos/       25-topicos-aulas/ 
kimura@baldurdia:~$ cd 25-topicos
kimura@baldurdia:~/25-topicos$ 



















































kimura@baldurdia:~/25-topicos$ ls -la
total 12
drwxrwxr-x  3 kimura kimura 4096 Apr  1 19:05 .
drwxr-xr-x 40 kimura kimura 4096 Apr  8 15:17 ..
drwxrwxr-x  4 kimura kimura 4096 Apr  1 19:23 1-vagrant
kimura@baldurdia:~/25-topicos$ cd 1-vagrant/
Vbox/        workstation/ 
kimura@baldurdia:~/25-topicos$ cd 1-vagrant/workstation/
kimura@baldurdia:~/25-topicos/1-vagrant/workstation$ 














































kimura@baldurdia:~/25-topicos/1-vagrant/workstation$ ls -la
total 24
drwxrwxr-x 6 kimura kimura 4096 Apr 25 13:21 .
drwxrwxr-x 4 kimura kimura 4096 Apr  1 19:23 ..
drwxrwxr-x 2 kimura kimura 4096 Apr 23 17:50 bgp
drwxrwxr-x 3 kimura kimura 4096 Apr 23 17:51 mn-ex-5-bgp
drwxrwxr-x 2 kimura kimura 4096 Apr 16 11:56 ospf-1
-rw-rw-rw- 1 kimura kimura    0 Apr 23 17:21 r1.bgp.log
-rw-rw-rw- 1 kimura kimura    0 Apr 23 17:21 r1.zebra.log
-rw-rw-rw- 1 kimura kimura    0 Apr 23 17:21 r2.bgp.log
-rw-rw-rw- 1 kimura kimura    0 Apr 23 17:21 r2.zebra.log
drwxrwxr-x 2 kimura kimura 4096 Apr 16 14:33 rip1
kimura@baldurdia:~/25-topicos/1-vagrant/workstation$ mkdir dns
kimura@baldurdia:~/25-topicos/1-vagrant/workstation$ cd dns/
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ 








































kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ ls -la
total 8
drwxrwxr-x 2 kimura kimura 4096 Apr 30 13:59 .
drwxrwxr-x 7 kimura kimura 4096 Apr 30 13:59 ..
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ cp ../
bgp/          dns/          mn-ex-5-bgp/  ospf-1/       r1.bgp.log    r1.zebra.log  r2.bgp.log    r2.zebra.log  rip1/         
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ cp ../ospf-1/* .
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ ls -la
total 344
drwxrwxr-x 2 kimura kimura   4096 Apr 30 13:59 .
drwxrwxr-x 7 kimura kimura   4096 Apr 30 13:59 ..
-rw-rw-r-- 1 kimura kimura     79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 kimura kimura   5239 Apr 30 13:59 mn-ex-1.py
-rw-rw-r-- 1 kimura kimura   3136 Apr 30 13:59 mn-ex-2.py
-rw-rw-r-- 1 kimura kimura   3901 Apr 30 13:59 mn-ex-2.py.backup
-rw-rw-r-- 1 kimura kimura   2118 Apr 30 13:59 mn-ex-base-1.py
-rw-rw-r-- 1 kimura kimura    249 Apr 30 13:59 r1.ospf.conf
-rw-rw-r-- 1 kimura kimura 121949 Apr 30 13:59 r1.ospf.log
-rw-rw-r-- 1 kimura kimura    189 Apr 30 13:59 r1.zebra.conf
-rw-rw-r-- 1 kimura kimura    679 Apr 30 13:59 r1.zebra.log
-rw-rw-r-- 1 kimura kimura    279 Apr 30 13:59 r2.ospf.conf
-rw-rw-r-- 1 kimura kimura 166102 Apr 30 13:59 r2.ospf.log
-rw-rw-r-- 1 kimura kimura     72 Apr 30 13:59 r2.zebra.conf
-rw-rw-r-- 1 kimura kimura    627 Apr 30 13:59 r2.zebra.log
-rw-rw-r-- 1 kimura kimura    368 Apr 30 13:59 zebra.conf
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ cp mn-ex-1.py mn-ex-dns.py
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ nano mn-ex-dns.py 
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ ls -la
total 352
drwxrwxr-x 2 kimura kimura   4096 Apr 30 14:09 .
drwxrwxr-x 7 kimura kimura   4096 Apr 30 13:59 ..
-rw-rw-r-- 1 kimura kimura     79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 kimura kimura   5239 Apr 30 13:59 mn-ex-1.py
-rw-rw-r-- 1 kimura kimura   3136 Apr 30 13:59 mn-ex-2.py
-rw-rw-r-- 1 kimura kimura   3901 Apr 30 13:59 mn-ex-2.py.backup
-rw-rw-r-- 1 kimura kimura   2118 Apr 30 13:59 mn-ex-base-1.py
-rw-rw-r-- 1 kimura kimura   1919 Apr 30 14:09 mn-ex-dns.py
-rw-rw-r-- 1 kimura kimura   1919 Apr 30 14:09 mn-ex-dns.py~
-rw-rw-r-- 1 kimura kimura    249 Apr 30 13:59 r1.ospf.conf
-rw-rw-r-- 1 kimura kimura 121949 Apr 30 13:59 r1.ospf.log
-rw-rw-r-- 1 kimura kimura    189 Apr 30 13:59 r1.zebra.conf
-rw-rw-r-- 1 kimura kimura    679 Apr 30 13:59 r1.zebra.log
-rw-rw-r-- 1 kimura kimura    279 Apr 30 13:59 r2.ospf.conf
-rw-rw-r-- 1 kimura kimura 166102 Apr 30 13:59 r2.ospf.log
-rw-rw-r-- 1 kimura kimura     72 Apr 30 13:59 r2.zebra.conf
-rw-rw-r-- 1 kimura kimura    627 Apr 30 13:59 r2.zebra.log
-rw-rw-r-- 1 kimura kimura    368 Apr 30 13:59 zebra.conf
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ rm mn-ex-1.py 
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ rm mn-ex-2.py 
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ rm mn-ex-base-1.py* 
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ 




kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ ls -la
total 336
drwxrwxr-x 2 kimura kimura   4096 Apr 30 14:09 .
drwxrwxr-x 7 kimura kimura   4096 Apr 30 13:59 ..
-rw-rw-r-- 1 kimura kimura     79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 kimura kimura   3901 Apr 30 13:59 mn-ex-2.py.backup
-rw-rw-r-- 1 kimura kimura   1919 Apr 30 14:09 mn-ex-dns.py
-rw-rw-r-- 1 kimura kimura   1919 Apr 30 14:09 mn-ex-dns.py~
-rw-rw-r-- 1 kimura kimura    249 Apr 30 13:59 r1.ospf.conf
-rw-rw-r-- 1 kimura kimura 121949 Apr 30 13:59 r1.ospf.log
-rw-rw-r-- 1 kimura kimura    189 Apr 30 13:59 r1.zebra.conf
-rw-rw-r-- 1 kimura kimura    679 Apr 30 13:59 r1.zebra.log
-rw-rw-r-- 1 kimura kimura    279 Apr 30 13:59 r2.ospf.conf
-rw-rw-r-- 1 kimura kimura 166102 Apr 30 13:59 r2.ospf.log
-rw-rw-r-- 1 kimura kimura     72 Apr 30 13:59 r2.zebra.conf
-rw-rw-r-- 1 kimura kimura    627 Apr 30 13:59 r2.zebra.log
-rw-rw-r-- 1 kimura kimura    368 Apr 30 13:59 zebra.conf
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ rm mn-ex-2.py.backup 
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ rm r*
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ 



































kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ ls -la
total 24
drwxrwxr-x 2 kimura kimura 4096 Apr 30 14:10 .
drwxrwxr-x 7 kimura kimura 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 kimura kimura   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 kimura kimura 1919 Apr 30 14:09 mn-ex-dns.py
-rw-rw-r-- 1 kimura kimura 1919 Apr 30 14:09 mn-ex-dns.py~
-rw-rw-r-- 1 kimura kimura  368 Apr 30 13:59 zebra.conf
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ rm zebra.conf 
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ 













































kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ ls -la
total 20
drwxrwxr-x 2 kimura kimura 4096 Apr 30 14:10 .
drwxrwxr-x 7 kimura kimura 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 kimura kimura   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 kimura kimura 1919 Apr 30 14:09 mn-ex-dns.py
-rw-rw-r-- 1 kimura kimura 1919 Apr 30 14:09 mn-ex-dns.py~
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ nano mn-ex-dns.py
kimura@baldurdia:~/25-topicos/1-vagrant/workstation/dns$ cd ..
kimura@baldurdia:~/25-topicos/1-vagrant/workstation$ cd ..
kimura@baldurdia:~/25-topicos/1-vagrant$ 












































kimura@baldurdia:~/25-topicos/1-vagrant$ ls -la
total 16
drwxrwxr-x 4 kimura kimura 4096 Apr  1 19:23 .
drwxrwxr-x 3 kimura kimura 4096 Apr  1 19:05 ..
drwxrwxr-x 3 kimura kimura 4096 Apr  2 15:16 Vbox
drwxrwxr-x 7 kimura kimura 4096 Apr 30 13:59 workstation
kimura@baldurdia:~/25-topicos/1-vagrant$ cd Vbox/
kimura@baldurdia:~/25-topicos/1-vagrant/Vbox$ 















































kimura@baldurdia:~/25-topicos/1-vagrant/Vbox$ ls -la
total 68
drwxrwxr-x 3 kimura kimura  4096 Apr  2 15:16 .
drwxrwxr-x 4 kimura kimura  4096 Apr  1 19:23 ..
-rw-rw-r-- 1 kimura kimura   319 Apr  2 15:12 install.sh
-rw-rw-r-- 1 kimura kimura   804 Apr  1 21:55 install.sh.old
-rw------- 1 kimura kimura 41699 Apr 16 11:51 ubuntu-bionic-18.04-cloudimg-console.log
drwxrwxr-x 3 kimura kimura  4096 Apr  1 23:35 .vagrant
-rw-rw-r-- 1 kimura kimura   431 Apr  1 23:56 Vagrantfile
kimura@baldurdia:~/25-topicos/1-vagrant/Vbox$ vagrant reload
==> default: Checking if box 'ubuntu/bionic64' is up to date...
==> default: A newer version of the box 'ubuntu/bionic64' for provider 'virtualbox' is
==> default: available! You currently have version '20230607.0.0'. The latest is version
==> default: '20230607.0.5'. Run `vagrant box update` to update.
==> default: Clearing any previously set forwarded ports...
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 22 (guest) => 2200 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /vagrant => /home/kimura/25-topicos/1-vagrant/Vbox
    default: /workstation => /home/kimura/25-topicos/1-vagrant/workstation
==> default: Machine already provisioned. Run `vagrant provision` or use the `--provision`
==> default: flag to force provisioning. Provisioners marked to run always will still run.
kimura@baldurdia:~/25-topicos/1-vagrant/Vbox$ vagrant ssh
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 4.15.0-213-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Apr 30 14:13:46 UTC 2025

  System load:  0.28              Processes:             102
  Usage of /:   6.9% of 38.70GB   Users logged in:       0
  Memory usage: 3%                IP address for enp0s3: 10.0.2.15
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Infrastructure is not enabled.

3 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

186 additional security updates can be applied with ESM Infra.
Learn more about enabling ESM Infra service for Ubuntu 18.04 at
https://ubuntu.com/18-04

New release '20.04.6 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Fri Apr 25 13:12:19 2025 from 10.0.2.2
vagrant@ubuntu-bionic:~$ cd /workstation/
vagrant@ubuntu-bionic:/workstation$ 
vagrant@ubuntu-bionic:/workstation$ ls -la
total 28
drwxrwxr-x  1 vagrant vagrant 4096 Apr 30 13:59 .
drwxr-xr-x 25 root    root    4096 Apr 30 14:11 ..
drwxrwxr-x  1 vagrant vagrant 4096 Apr 23 17:50 bgp
drwxrwxr-x  1 vagrant vagrant 4096 Apr 30 14:10 dns
drwxrwxr-x  1 vagrant vagrant 4096 Apr 23 17:51 mn-ex-5-bgp
drwxrwxr-x  1 vagrant vagrant 4096 Apr 16 11:56 ospf-1
-rw-rw-rw-  1 vagrant vagrant    0 Apr 23 17:21 r1.bgp.log
-rw-rw-rw-  1 vagrant vagrant    0 Apr 23 17:21 r1.zebra.log
-rw-rw-rw-  1 vagrant vagrant    0 Apr 23 17:21 r2.bgp.log
-rw-rw-rw-  1 vagrant vagrant    0 Apr 23 17:21 r2.zebra.log
drwxrwxr-x  1 vagrant vagrant 4096 Apr 16 14:33 rip1
vagrant@ubuntu-bionic:/workstation$ cd mn-ex-5-bgp/
vagrant@ubuntu-bionic:/workstation/mn-ex-5-bgp$ cd ..
vagrant@ubuntu-bionic:/workstation$ cd dns/
vagrant@ubuntu-bionic:/workstation/dns$ 






































vagrant@ubuntu-bionic:/workstation/dns$ ls -la
total 20
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 14:10 .
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 vagrant vagrant   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:10 mn-ex-dns.py
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:09 mn-ex-dns.py~
vagrant@ubuntu-bionic:/workstation/dns$ cp ../
bgp/          dns/          mn-ex-5-bgp/  ospf-1/       r1.bgp.log    r1.zebra.log  r2.bgp.log    r2.zebra.log  rip1/         
vagrant@ubuntu-bionic:/workstation/dns$ cp ../ospf-1/
mininet_run.sh     mn-ex-2.py         mn-ex-base-1.py    r1.ospf.log        r1.zebra.log       r2.ospf.log        r2.zebra.log       
mn-ex-1.py         mn-ex-2.py.backup  r1.ospf.conf       r1.zebra.conf      r2.ospf.conf       r2.zebra.conf      zebra.conf         
vagrant@ubuntu-bionic:/workstation/dns$ cp ../ospf-1/^C
vagrant@ubuntu-bionic:/workstation/dns$ 









































vagrant@ubuntu-bionic:/workstation/dns$ ls -la
total 20
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 14:10 .
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 vagrant vagrant   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:10 mn-ex-dns.py
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:09 mn-ex-dns.py~
vagrant@ubuntu-bionic:/workstation/dns$ sh mininet_run.sh  mn-ex-dns.py
*** Removing excess controllers/ofprotocols/ofdatapaths/pings/noxes
killall controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
killall -9 controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
pkill -9 -f "sudo mnexec"
*** Removing junk from /tmp
rm -f /tmp/vconn* /tmp/vlogs* /tmp/*.out /tmp/*.log
*** Removing old X11 tunnels
*** Removing excess kernel datapaths
ps ax | egrep -o 'dp[0-9]+' | sed 's/dp/nl:/'
***  Removing OVS datapaths
ovs-vsctl --timeout=1 list-br
ovs-vsctl --timeout=1 list-br
*** Removing all links of the pattern foo-ethX
ip link show | egrep -o '([-_.[:alnum:]]+-eth[[:digit:]]+)'
ip link show
*** Killing stale mininet node processes
pkill -9 -f mininet:
*** Shutting down stale tunnels
pkill -9 -f Tunnel=Ethernet
pkill -9 -f .ssh/mn
rm -f ~/.ssh/mn/*
*** Cleanup complete.
*** Creating network
*** Adding hosts:
dnsabc dnsorg dnsroot dnsxyz www1 www2 
*** Adding switches:
Traceback (most recent call last):
  File "mn-ex-dns.py", line 73, in <module>
    run()
  File "mn-ex-dns.py", line 57, in run
    net = Mininet(topo=topo, link=TCLink, switch=OVSBridge, controller=None) #, host=CPULimitedHost)
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 174, in __init__
    self.build()
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 502, in build
    self.buildFromTopo( self.topo )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 483, in buildFromTopo
    self.addSwitch( switchName, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 260, in addSwitch
    sw = cls( name, **defaults )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1295, in __init__
    OVSSwitch.__init__( self, *args, **kwargs )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1070, in __init__
    Switch.__init__( self, name, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 893, in __init__
    self.dpid = self.defaultDpid( dpid )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 912, in defaultDpid
    raise Exception( 'Unable to derive default datapath ID - '
Exception: Unable to derive default datapath ID - please either specify a dpid or use a canonical switch name such as s23.
vagrant@ubuntu-bionic:/workstation/dns$ !nano
nano ../bgp/mn-ex-bgp.py 
vagrant@ubuntu-bionic:/workstation/dns$ ls
mininet_run.sh  mn-ex-dns.py  mn-ex-dns.py~
vagrant@ubuntu-bionic:/workstation/dns$ nano mn-ex-dns.py
vagrant@ubuntu-bionic:/workstation/dns$ 
vagrant@ubuntu-bionic:/workstation/dns$ sh mininet_run.sh  mn-ex-dns.py
*** Removing excess controllers/ofprotocols/ofdatapaths/pings/noxes
killall controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
killall -9 controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
pkill -9 -f "sudo mnexec"
*** Removing junk from /tmp
rm -f /tmp/vconn* /tmp/vlogs* /tmp/*.out /tmp/*.log
*** Removing old X11 tunnels
*** Removing excess kernel datapaths
ps ax | egrep -o 'dp[0-9]+' | sed 's/dp/nl:/'
***  Removing OVS datapaths
ovs-vsctl --timeout=1 list-br
ovs-vsctl --timeout=1 list-br
*** Removing all links of the pattern foo-ethX
ip link show | egrep -o '([-_.[:alnum:]]+-eth[[:digit:]]+)'
ip link show
*** Killing stale mininet node processes
pkill -9 -f mininet:
*** Shutting down stale tunnels
pkill -9 -f Tunnel=Ethernet
pkill -9 -f .ssh/mn
rm -f ~/.ssh/mn/*
*** Cleanup complete.
*** Creating network
*** Adding hosts:
dnsabc dnsorg dnsroot dnsxyz www1 www2 
*** Adding switches:
Traceback (most recent call last):
  File "mn-ex-dns.py", line 73, in <module>
    run()
  File "mn-ex-dns.py", line 57, in run
    net = Mininet(topo=topo, link=TCLink, switch=OVSBridge, controller=None) #, host=CPULimitedHost)
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 174, in __init__
    self.build()
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 502, in build
    self.buildFromTopo( self.topo )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 483, in buildFromTopo
    self.addSwitch( switchName, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 260, in addSwitch
    sw = cls( name, **defaults )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1295, in __init__
    OVSSwitch.__init__( self, *args, **kwargs )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1070, in __init__
    Switch.__init__( self, name, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 893, in __init__
    self.dpid = self.defaultDpid( dpid )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 912, in defaultDpid
    raise Exception( 'Unable to derive default datapath ID - '
Exception: Unable to derive default datapath ID - please either specify a dpid or use a canonical switch name such as s23.
vagrant@ubuntu-bionic:/workstation/dns$ nano mn-ex-dns.py
vagrant@ubuntu-bionic:/workstation/dns$ 




vagrant@ubuntu-bionic:/workstation/dns$ sh mininet_run.sh  mn-ex-dns.py
*** Removing excess controllers/ofprotocols/ofdatapaths/pings/noxes
killall controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
killall -9 controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
pkill -9 -f "sudo mnexec"
*** Removing junk from /tmp
rm -f /tmp/vconn* /tmp/vlogs* /tmp/*.out /tmp/*.log
*** Removing old X11 tunnels
*** Removing excess kernel datapaths
ps ax | egrep -o 'dp[0-9]+' | sed 's/dp/nl:/'
***  Removing OVS datapaths
ovs-vsctl --timeout=1 list-br
ovs-vsctl --timeout=1 list-br
*** Removing all links of the pattern foo-ethX
ip link show | egrep -o '([-_.[:alnum:]]+-eth[[:digit:]]+)'
ip link show
*** Killing stale mininet node processes
pkill -9 -f mininet:
*** Shutting down stale tunnels
pkill -9 -f Tunnel=Ethernet
pkill -9 -f .ssh/mn
rm -f ~/.ssh/mn/*
*** Cleanup complete.
*** Creating network
*** Adding hosts:
dnsabc dnsorg dnsroot dnsxyz www1 www2 
*** Adding switches:
Traceback (most recent call last):
  File "mn-ex-dns.py", line 74, in <module>
    run()
  File "mn-ex-dns.py", line 58, in run
    net = Mininet(topo=topo, link=TCLink, switch=OVSSwitch, controller=None) #, host=CPULimitedHost)
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 174, in __init__
    self.build()
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 502, in build
    self.buildFromTopo( self.topo )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 483, in buildFromTopo
    self.addSwitch( switchName, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 260, in addSwitch
    sw = cls( name, **defaults )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1070, in __init__
    Switch.__init__( self, name, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 893, in __init__
    self.dpid = self.defaultDpid( dpid )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 912, in defaultDpid
    raise Exception( 'Unable to derive default datapath ID - '
Exception: Unable to derive default datapath ID - please either specify a dpid or use a canonical switch name such as s23.
vagrant@ubuntu-bionic:/workstation/dns$ nano mn-ex-dns.py
vagrant@ubuntu-bionic:/workstation/dns$ nano mn-ex-dns.py
vagrant@ubuntu-bionic:/workstation/dns$ nano mn-ex-dns.py
vagrant@ubuntu-bionic:/workstation/dns$ 




vagrant@ubuntu-bionic:/workstation/dns$ sh mininet_run.sh  mn-ex-dns.py
*** Removing excess controllers/ofprotocols/ofdatapaths/pings/noxes
killall controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
killall -9 controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
pkill -9 -f "sudo mnexec"
*** Removing junk from /tmp
rm -f /tmp/vconn* /tmp/vlogs* /tmp/*.out /tmp/*.log
*** Removing old X11 tunnels
*** Removing excess kernel datapaths
ps ax | egrep -o 'dp[0-9]+' | sed 's/dp/nl:/'
***  Removing OVS datapaths
ovs-vsctl --timeout=1 list-br
ovs-vsctl --timeout=1 list-br
*** Removing all links of the pattern foo-ethX
ip link show | egrep -o '([-_.[:alnum:]]+-eth[[:digit:]]+)'
ip link show
*** Killing stale mininet node processes
pkill -9 -f mininet:
*** Shutting down stale tunnels
pkill -9 -f Tunnel=Ethernet
pkill -9 -f .ssh/mn
rm -f ~/.ssh/mn/*
*** Cleanup complete.
*** Creating network
*** Adding controller
*** Adding hosts:
dnsabc dnsorg dnsroot dnsxyz www1 www2 
*** Adding switches:
Traceback (most recent call last):
  File "mn-ex-dns.py", line 74, in <module>
    run()
  File "mn-ex-dns.py", line 58, in run
    net = Mininet(topo=topo, link=TCLink, switch=OVSSwitch, controller=Controller) #, host=CPULimitedHost)
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 174, in __init__
    self.build()
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 502, in build
    self.buildFromTopo( self.topo )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 483, in buildFromTopo
    self.addSwitch( switchName, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 260, in addSwitch
    sw = cls( name, **defaults )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1070, in __init__
    Switch.__init__( self, name, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 893, in __init__
    self.dpid = self.defaultDpid( dpid )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 912, in defaultDpid
    raise Exception( 'Unable to derive default datapath ID - '
Exception: Unable to derive default datapath ID - please either specify a dpid or use a canonical switch name such as s23.
vagrant@ubuntu-bionic:/workstation/dns$ 






vagrant@ubuntu-bionic:/workstation/dns$ !nano
nano mn-ex-dns.py
vagrant@ubuntu-bionic:/workstation/dns$ sh mininet_run.sh  mn-ex-dns.py
*** Removing excess controllers/ofprotocols/ofdatapaths/pings/noxes
killall controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
killall -9 controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
pkill -9 -f "sudo mnexec"
*** Removing junk from /tmp
rm -f /tmp/vconn* /tmp/vlogs* /tmp/*.out /tmp/*.log
*** Removing old X11 tunnels
*** Removing excess kernel datapaths
ps ax | egrep -o 'dp[0-9]+' | sed 's/dp/nl:/'
***  Removing OVS datapaths
ovs-vsctl --timeout=1 list-br
ovs-vsctl --timeout=1 list-br
*** Removing all links of the pattern foo-ethX
ip link show | egrep -o '([-_.[:alnum:]]+-eth[[:digit:]]+)'
ip link show
*** Killing stale mininet node processes
pkill -9 -f mininet:
*** Shutting down stale tunnels
pkill -9 -f Tunnel=Ethernet
pkill -9 -f .ssh/mn
rm -f ~/.ssh/mn/*
*** Cleanup complete.
*** Creating network
*** Adding controller
*** Adding hosts:
dnsabc dnsorg dnsroot dnsxyz www1 www2 
*** Adding switches:
Traceback (most recent call last):
  File "mn-ex-dns.py", line 74, in <module>
    run()
  File "mn-ex-dns.py", line 58, in run
    net = Mininet(topo=topo, link=TCLink, switch=OVSSwitch, controller=Controller) #, host=CPULimitedHost)
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 174, in __init__
    self.build()
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 502, in build
    self.buildFromTopo( self.topo )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 483, in buildFromTopo
    self.addSwitch( switchName, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/net.py", line 260, in addSwitch
    sw = cls( name, **defaults )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 1070, in __init__
    Switch.__init__( self, name, **params )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 893, in __init__
    self.dpid = self.defaultDpid( dpid )
  File "/home/vagrant/.local/lib/python2.7/site-packages/mininet/node.py", line 912, in defaultDpid
    raise Exception( 'Unable to derive default datapath ID - '
Exception: Unable to derive default datapath ID - please either specify a dpid or use a canonical switch name such as s23.
vagrant@ubuntu-bionic:/workstation/dns$ 




vagrant@ubuntu-bionic:/workstation/dns$ ls -la
total 20
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 14:19 .
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 vagrant vagrant   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 vagrant vagrant 1973 Apr 30 14:18 mn-ex-dns.py
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:09 mn-ex-dns.py~
vagrant@ubuntu-bionic:/workstation/dns$ cp mn.py^C
vagrant@ubuntu-bionic:/workstation/dns$ nano mn.py
vagrant@ubuntu-bionic:/workstation/dns$ ls -la
total 24
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 14:20 .
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 vagrant vagrant   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 vagrant vagrant 1973 Apr 30 14:18 mn-ex-dns.py
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:09 mn-ex-dns.py~
-rw-rw-r-- 1 vagrant vagrant 1480 Apr 30 14:20 mn.py
vagrant@ubuntu-bionic:/workstation/dns$ 





































vagrant@ubuntu-bionic:/workstation/dns$ ls -la
total 24
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 14:20 .
drwxrwxr-x 1 vagrant vagrant 4096 Apr 30 13:59 ..
-rw-rw-r-- 1 vagrant vagrant   79 Apr 30 13:59 mininet_run.sh
-rw-rw-r-- 1 vagrant vagrant 1973 Apr 30 14:18 mn-ex-dns.py
-rw-rw-r-- 1 vagrant vagrant 1919 Apr 30 14:09 mn-ex-dns.py~
-rw-rw-r-- 1 vagrant vagrant 1480 Apr 30 14:20 mn.py
vagrant@ubuntu-bionic:/workstation/dns$ sh mininet_run.sh mn.py 
*** Removing excess controllers/ofprotocols/ofdatapaths/pings/noxes
killall controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
killall -9 controller ofprotocol ofdatapath ping nox_corelt-nox_core ovs-openflowd ovs-controllerovs-testcontroller udpbwtest mnexec ivs ryu-manager 2> /dev/null
pkill -9 -f "sudo mnexec"
*** Removing junk from /tmp
rm -f /tmp/vconn* /tmp/vlogs* /tmp/*.out /tmp/*.log
*** Removing old X11 tunnels
*** Removing excess kernel datapaths
ps ax | egrep -o 'dp[0-9]+' | sed 's/dp/nl:/'
***  Removing OVS datapaths
ovs-vsctl --timeout=1 list-br
ovs-vsctl --timeout=1 list-br
*** Removing all links of the pattern foo-ethX
ip link show | egrep -o '([-_.[:alnum:]]+-eth[[:digit:]]+)'
ip link show
*** Killing stale mininet node processes
pkill -9 -f mininet:
*** Shutting down stale tunnels
pkill -9 -f Tunnel=Ethernet
pkill -9 -f .ssh/mn
rm -f ~/.ssh/mn/*
#!/usr/bin/python

import os

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class NetTopo(Topo):
        def build(self, **_opts):
                switch = self.addSwitch('s1')
                dnsroot = self.addHost('dnsroot')
                dnsorg = self.addHost('dnsorg')
                dnsabc = self.addHost('dnsabc')
                dnsxyz = self.addHost('dnsxyz')
                www1 = self.addHost('www1')
                www2 = self.addHost('www2')

                self.addLink(dnsroot, switch)
                self.addLink(dnsorg, switch)
                self.addLink(dnsabc, switch)
                self.addLink(dnsxyz, switch)
                self.addLink(www1, switch)
                self.addLink(www2, switch)


def create_ip_net(net):
        print "create_ip_net"
        net['dnsroot'].cmdPrint("ifconfig dnsroot-eth0 195.0.0.10/24")
        net['dnsorg'].cmdPrint("ifconfig dnsorg-eth0 195.0.0.21/24")
        net['dnsabc'].cmdPrint("ifconfig dnsabc-eth0 195.0.0.31/24")
        net['dnsxyz'].cmdPrint("ifconfig dnsxyz-eth0 195.0.0.32/24")
        net['www1'].cmdPrint("ifconfig www1-eth0 195.0.0.41/24")
        net['www2'].cmdPrint("ifconfig www2-eth0 195.0.0.42/24")

def net_test(net):
        print "Network connectivity"
        net['www1'].cmdPrint('ping -c 3 195.0.0.10')
        net['www1'].cmdPrint('ping -c 3 195.0.0.21')
        net['www1'].cmdPrint('ping -c 3 195.0.0.31')
        net['www1'].cmdPrint('ping -c 3 195.0.0.32')
        net['www1'].cmdPrint('ping -c 3 195.0.0.42')

def os_system(cmd):
        print(cmd)
        os.system(cmd)

def cleanup_bind():
        os_system('rm -rdf /home/mininet/*')
        os_system('rm -rdf /mnt/dns*')
        os_system('pkill named')
        os_system('pkill bind')

def set_start_named(net, node):
        net[node].cmdPrint("aa-exec -p unconfined -- named -u root -c {}/named.conf -g & ".format(node))

def set_host_nameserver(net, node, name_server):
        net[node].cmdPrint("echo 'nameserver {}' > /etc/resolv.conf".format(name_server))
        net[node].cmdPrint("cat /etc/resolv.conf")

def run():
        cleanup_bind()
        topo = NetTopo()
        net = Mininet(topo=topo, link=TCLink, controller=Controller)
        net.start()
        print "Host connections"
        dumpNodeConnections(net.hosts)

        create_ip_net(net)
        #net_test(net)
        set_start_named(net, 'dnsroot')
        set_start_named(net, 'dnsorg')
        set_start_named(net, 'dnsabc')
        set_start_named(net, 'dnsxyz')

        set_host_nameserver(net, 'www1', '195.0.0.31')
        net['www1'].cmdPrint('ping -c 3 www2.xyz.org')

        set_host_nameserver(net, 'www2', '195.0.0.32')
        net['www2'].cmdPrint('ping -c 3 www1.abc.org')

        CLI(net)
        net.stop()
        cleanup()

if __name__ == '__main__':
        setLogLevel( 'info' )
        run()

