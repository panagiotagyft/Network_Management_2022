#!/usr/bin/python

from mininet.node import Controller, OVSKernelSwitch, Host
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call


def myNetwork():

    net = Mininet_wifi(topo=None,
                       build=False,
                       link=wmediumd,
                       wmediumd_mode=interference,
                       ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6653)

    info( '*** Add switches/APs\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid', channel='1', mode='g', position='149.0,679.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid', channel='1', mode='g', position='497.0,533.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid', channel='1', mode='g', position='807.0,207.0,0')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid', channel='1', mode='g', position='1193.0,417.0,0')

    info( '*** Add hosts/stations\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    sta1 = net.addStation('sta1', ip='10.0.0.1', position='29.0,495.0,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2', position='33.0,623.0,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3', position='61.0,729.0,0')
    sta4 = net.addStation('sta4', ip='10.0.0.4', position='315.0,609.0,0')
    sta5 = net.addStation('sta5', ip='10.0.0.5', position='145.0,487.0,0')
    sta6 = net.addStation('sta6', ip='10.0.0.6', position='543.0,649.0,0')
    sta7 = net.addStation('sta7', ip='10.0.0.7', position='361.0,447.0,0')
    sta8 = net.addStation('sta8', ip='10.0.0.8', position='677.0,547.0,0')
    sta9 = net.addStation('sta9', ip='10.0.0.9', position='555.0,395.0,0')
    sta10 = net.addStation('sta10', ip='10.0.0.10', position='1187.0,239.0,0')
    sta11 = net.addStation('sta11', ip='10.0.0.11', position='1219.0,641.0,0')
    sta12 = net.addStation('sta12', ip='10.0.0.12', position='1059.0,581.0,0')
    sta13 = net.addStation('sta13', ip='10.0.0.13', position='1089.0,483.0,0')
    sta14 = net.addStation('sta14', ip='10.0.0.14', position='1055.0,301.0,0')
    sta15 = net.addStation('sta15', ip='10.0.0.15', position='953.0,89.0,0')
    sta16 = net.addStation('sta16', ip='10.0.0.16', position='787.0,53.0,0')
    sta17 = net.addStation('sta17', ip='10.0.0.17', position='617.0,121.0,0')
    sta18 = net.addStation('sta18', ip='10.0.0.18', position='703.0,301.0,0')
    sta19 = net.addStation('sta19', ip='10.0.0.19', position='855.0,381.0,0')
    sta20 = net.addStation('sta20', ip='10.0.0.20', position='1255.0,517.0,0')

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(h1, s1)
    
    net.plotGraph(max_x=1500, max_y=1200)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('s1').start([c0])
    net.get('ap1').start([c0])
    net.get('ap2').start([c0])
    net.get('ap3').start([c0])
    net.get('ap4').start([c0])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

