# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:15:17 2019

@author: yldrmemr
"""

import numpy as np
#--------------------------------------------------------------------------
#             -Global Degiskenler Tanımlandı(Sensor Mesafeleri ) -
#--------------------------------------------------------------------------
SagOnMesafe   = np.uint8(250)
SagArkaMesafe = np.uint8(240)
SolOnMesafe   = np.uint8(230)
SolArkaMesafe = np.uint8(220)

#--------------------------------------------------------------------------
#             -Sensor Mesafeleri Birlestirilip Degiskene Atandı   -
#--------------------------------------------------------------------------
SagToplamGonderen =np.uint16(0)
SolToplamGonderen =np.uint16(0)
ToplamDataGonderen= np.uint32(0)

SagToplam = (SagOnMesafe <<8 )  | SagArkaMesafe
SolToplam = (SolOnMesafe <<8 )  | SolArkaMesafe
ToplamData = (SagToplam << 16)  | SolToplam

print("---------------------------------------") 
print("<#####################################>")
print("---------------------------------------")

print("Gonderen SagToplam",SagToplam )
print("Gonderen SolToplam",SolToplam)
print("Gonderen ToplamData",ToplamData)

print("---------------------------------------")

print("SagOnMesafe",SagOnMesafe )
print("SagArkaMesafe",SagArkaMesafe)
print("SolOnMesafe",SolOnMesafe)
print("SolArkaMesafe",SolArkaMesafe)

print("---------------------------------------")
print("<#####################################>")
#--------------------------------------------------------------------------
#             -Sensor Mesafeleri Tekrar Eski Formata Donusturuldu -
#--------------------------------------------------------------------------
SagToplamAlınan =np.uint16(0)
SolToplamAlınan =np.uint16(0)
ToplamDataAlınan= np.uint32(0)

SagOnMesafeOkunan   = np.uint8(0)
SagArkaMesafeOkunan = np.uint8(0)
SolOnMesafeOkunan   = np.uint8(0)
SolArkaMesafeOkunan = np.uint8(0)



ToplamDataAlınan =ToplamData
SolToplamAlınan = (ToplamDataAlınan) & 0xFFFF
SagToplamAlınan = (ToplamDataAlınan >> 16) & 0xFFFF
SagArkaMesafeOkunan = (SagToplamAlınan)& 0xFF
SagOnMesafeOkunan =(SagToplamAlınan >> 8) & 0xFF

SolArkaMesafeOkunan = (SolToplamAlınan)& 0xFF
SolOnMesafeOkunan=(SolToplamAlınan >> 8) & 0xFF

print("---------------------------------------")

print("Alıcı ToplamData",      ToplamDataAlınan)
print("Alıcı SagToplamAlınan", SagToplamAlınan)
print("Alıcı SolToplamAlınan", SolToplamAlınan)

print("---------------------------------------")

print("SagOnMesafeOkunan",   SagOnMesafeOkunan )
print("SagArkaMesafeOkunan", SagArkaMesafeOkunan)
print("SolOnMesafeOkunan",   SolOnMesafeOkunan)
print("SolArkaMesafeOkunan", SolArkaMesafeOkunan)

print("---------------------------------------")
print("<#####################################>")
print("---------------------------------------")


