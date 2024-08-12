# Hamza BUYUKSEYMEN PYTHON OPC UA 'SERVER'

#Gereksinimler : 'Python' ve 'pip' bilgisayarda kurulu olmali.
#Gereksinimler : ">>pip install opcua" yani 'opcua' paketi indirilmeli. 

import sys 
import time
from opcua import Server, ua

# 'OPC UA server' degiskeni olusturma
sunucu = Server()

# 'OPC UA baglanti adresini' 'server' olarak tanimlanan degiskene ayarlama
url_adresi = ("opc.tcp://127.168.0.77:12345")
sunucu.set_endpoint(url_adresi)

# 'OPC UA sever'i ile ilgili parametreler icin adres alanı olusturma
adi = ("OPCUA SUNUCUSU")
ad_alani = sunucu.register_namespace(adi)
node_alani = sunucu.get_objects_node()
degisken_alani = node_alani.add_object(ad_alani,"DEGISKENLER")

# 'OPC UA'de donecek degiskenleri tanimlama 
sicaklik = degisken_alani.add_variable(ad_alani,"SICAKLIK",0)
basinc = degisken_alani.add_variable(ad_alani,"BASINÇ",0)

# 'OPC UA'de donecek degiskenleri 'client' tarafindan okunabilir ve yazilabilir olarak ayarlama
sicaklik.set_writable()
basinc.set_writable()
 
# 'OPC UA server'i baslatildi 
sunucu.start()
print("\n{}:\nOPCUA SUNUCUSU BASLATILDI : ".format(url_adresi))

if __name__ == '__main__':
    
    while True:
        
        # 'OPC UA'de donecek degiskenlerin degerlerini atama
        sicaklik_ata = 16
        basinc_ata = 95
        sicaklik.set_value(sicaklik_ata)
        basinc.set_value(basinc_ata)

        print("\n*****************************\n")
        print("\nNode alanım:",node_alani)
        print("\nObjemin NodeID si:",degisken_alani)

        # 'OPC UA'de donecek degiskenlerin NodeID lerini yazdir
        print("\nsıcaklık değikenimin NodeID si : ",sicaklik)
        print("\nbasınç değişkenimin NodeID si : ",basinc)

        # 'OPC UA'de donecek degiskenlerin degerlerini yazdirma
        print("\nsıcaklık değikenimin değeri : ",sicaklik.get_value())
        print("\nbasınç değişkenimin değeri : ",basinc.get_value())

        time.sleep(2)