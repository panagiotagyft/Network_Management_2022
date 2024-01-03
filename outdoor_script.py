#!/usr/bin/python

from mininet.node import OVSKernelSwitch, Host
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
    info( '*** Add switches/APs\n')
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid',
                             channel='1', mode='g', position='144.0,411.0,0')
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid',
                             channel='1', mode='g', position='273.0,140.0,0')
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid',
                             channel='1', mode='g', position='397.0,617.0,0')
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid',
                             channel='1', mode='g', position='504.0,404.0,0')
    ap5 = net.addAccessPoint('ap5', cls=OVSKernelAP, ssid='ap5-ssid',
                             channel='1', mode='g', position='725.0,210.0,0')
    ap6 = net.addAccessPoint('ap6', cls=OVSKernelAP, ssid='ap6-ssid',
                             channel='1', mode='g', position='819.0,508.0,0')
    ap7 = net.addAccessPoint('ap7', cls=OVSKernelAP, ssid='ap7-ssid',
                             channel='1', mode='g', position='961.0,258.0,0')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts/stations\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    sta1 = net.addStation('sta1', ip='10.0.0.1',
                           position='147.0,800.0,0', range=116)
    sta2 = net.addStation('sta2', ip='10.0.0.2',
                           position='210.0,800.0,0', range=116)
    sta3 = net.addStation('sta3', ip='10.0.0.3',
                           position='180.0,800.0,0', range=116)
    sta4 = net.addStation('sta4', ip='10.0.0.4',
                           position='260.0,800.0,0', range=116)
    sta5 = net.addStation('sta5', ip='10.0.0.5',
                           position='292.0,800.0,0', range=116)
    sta6 = net.addStation('sta6', ip='10.0.0.6',
                           position='369.0,800.0,0', range=116)
    sta7 = net.addStation('sta7', ip='10.0.0.7',
                           position='427.0,800.0,0', range=116)
    sta8 = net.addStation('sta8', ip='10.0.0.8',
                           position='482.0,800.0,0', range=116)
    sta9 = net.addStation('sta9', ip='10.0.0.9',
                           position='542.0,800.0,0', range=116)
    sta10 = net.addStation('sta10', ip='10.0.0.10',
                           position='605.0,800.0,0', range=116)
    sta11 = net.addStation('sta11', ip='10.0.0.11',
                           position='48.0,379.0,0', range=116)
    sta12 = net.addStation('sta12', ip='10.0.0.12',
                           position='47.0,300.0,0', range=116)
    sta13 = net.addStation('sta13', ip='10.0.0.13',
                           position='134.0,311.0,0', range=116)
    sta14 = net.addStation('sta14', ip='10.0.0.14',
                           position='577.0,365.0,0', range=116)
    sta15 = net.addStation('sta15', ip='10.0.0.15',
                           position='578.0,426.0,0', range=116)
    sta16 = net.addStation('sta16', ip='10.0.0.16',
                           position='524.0,484.0,0', range=116)
    sta17 = net.addStation('sta17', ip='10.0.0.17',
                           position='901.0,482.0,0', range=116)
    sta18 = net.addStation('sta18', ip='10.0.0.18',
                           position='919.0,586.0,0', range=116)
    sta19 = net.addStation('sta19', ip='10.0.0.19',
                           position='862.0,285.0,0', range=116)
    sta20 = net.addStation('sta20', ip='10.0.0.20',
                           position='936.0,325.0,0', range=116)
    sta21 = net.addStation('sta21', ip='10.0.0.21',
                           position='754.0,297.0,0', range=116)
    sta22 = net.addStation('sta22', ip='10.0.0.22',
                           position='168.0,185.0,0', range=116)

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info( '*** Add links\n')
    net.addLink(h1, s1)

    net.plotGraph(max_x=1000, max_y=1000)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches/APs\n')
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])
    net.get('ap4').start([])
    net.get('ap5').start([])
    net.get('ap6').start([])
    net.get('ap7').start([])
    net.get('s1').start([])

    info( '*** Post configure nodes\n')

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

