from pysnmp.hlapi import *
result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107', 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0)))

g = list(result)

for x in g:
    for y in x[3]:
       print(y)

result2 = nextCmd(SnmpEngine(),
                    CommunityData('public', mpModel=0),
                    UdpTransportTarget(('10.31.70.107', 161)),
                    ContextData(),
                    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')))

b = list(result2)

for a in b:
    for z in a[3]:
       print(z)