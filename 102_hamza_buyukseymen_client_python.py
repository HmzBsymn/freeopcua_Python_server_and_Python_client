# Hamza BUYUKSEYMEN PYTHON OPC UA 'CLIENT'

#Gereksinimler : 'Python' ve 'pip' bilgisayarda kurulu olmali.
#Gereksinimler : ">>pip install opcua" yani 'opcua' paketi indirilmeli. 
#Onceden OPC UA 'server'i baslatildi.
#Bu projede OPC UA 'server'i 'python'dir.

import sys
from opcua import Client , ua
import time

# 'Endpoint' tanitimi: OPC UA 'server'in 'url'si.
url = "opc.tcp://127.168.0.77:12345"

try:
        # 'Python'da bir OPC UA 'client'i tanimla OPC UA 'server'a bagla.
        istemci = Client(url)
        istemci.connect()
        print("\nOPC UA sunucusuna baglanildi!!!:")

except Exception as err:
        # Baglanti hatasi oldugu zaman islet:
        print("\nOPC UA sunucusuna baglanilamadi !!! :",err)
        sys.exit(1)

if __name__ =='__main__' :

        #'OPC UA'de donecek degiskenleri 'client' tarafinda tanimlama :
        #Degiskenler , 'server'daki degiskenlerin 'NodeId'leri ile cagirilir.
        #'Python Server'da {NodeId : ns=xx , i=xx}
        sicaklik_node = istemci.get_node("ns=2;i=2")
        basinc_node   = istemci.get_node("ns=2;i=3")
        
        while True:

            # 'OPC UA'de donecek degiskenlerin degerini 'client' tarafinda okuma:
            # 'Node'larin guncel degerlerini oku degiskene ata ve bastir.

            sicaklik_degeri = sicaklik_node.get_value()
            print("\n Anlik sicaklik degeri : ", sicaklik_degeri)

            basinc_degeri = basinc_node.get_value()
            print("\n Anlik basinc degeri : ",basinc_degeri)

            #'OPC UA'de donecek degiskenlerin degerini 'client' tarafindan yazma:

            sicaklik_yeni = 30.25
            basinc_yeni = 230.84

            istemci.set_values([sicaklik_node],[sicaklik_yeni])
            istemci.set_values([basinc_node],[basinc_yeni])

            # Gelecek iterasyon için 2 saniye bekle.
            time.sleep(2)


