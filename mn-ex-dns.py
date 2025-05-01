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

