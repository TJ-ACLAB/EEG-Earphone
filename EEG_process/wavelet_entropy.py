# not enough variance to choose
# wavelet entropy python
import math
import numpy as np
import pywt
from math import log
print(pywt.wavelist(kind='discrete'))

def WE(sig, wavelet = 'db6'):
    n = len(sig)
    
    #sig = y
    
    ap = {}
    coeffs= pywt.wavedec(sig, wavelet,level=5)
    #coeffs= pywt.wavedec(sig, wavelet,mode='smooth',level=5)
    a5,d5,d4,d3,d2,d1=coeffs
   # print(d1)
   # print(d2)
   # print(d3)
   # print(d4)
   # print(d5)
  #  print(a5)

    d1=pywt.threshold(d1, np.mean(d1), mode='soft', substitute=0)
    d2=pywt.threshold(d2, np.mean(d2), mode='soft', substitute=0)
    d3=pywt.threshold(d3, np.mean(d3), mode='soft', substitute=0)
    d4=pywt.threshold(d4, np.mean(d4), mode='soft', substitute=0)
    d5=pywt.threshold(d5, np.mean(d5), mode='soft', substitute=0)

  #  print("-----------------------")
  #  print(d1)
  #  print(d2)
  #  print(d3)
  #  print(d4)
   # print(d5)
  #  A5=pywt.upcoef('a',a5,'db5',take=n)
  #  D5=pywt.upcoef('d',d5,'db5',take=n)
  #  D1=pywt.upcoef('d',d1,'db5',take=n)
  #  D2=pywt.upcoef('d',d2,'db5',take=n)
  #  D3=pywt.upcoef('d',d3,'db5',take=n)
   # D4=pywt.upcoef('d',d4,'db5',take=n)
    #print(D1)
    #print(D2)
    #print(D3)
    #print(D4)
    #print(D5)
    #print(A5)

  #  S5=A5+D5
  #  S4=A5+D5+D4
  #  S3=A5+D5+D4+D3
  #  S2=A5+D5+D4+D3+D2
  #  S1=A5+D5+D4+D3+D2+D1

  #  print(S1)
  #  print(S2)
  #  print(S3)
  #  print(S4)
# print(S5)
    #xn=A+D
   # print(A5)
   # print(len(A5))
   # print(len(sig))
   # print(D5)
    E1 = np.sqrt(np.sum(np.power(d1,2))/len(d1))
    E2 = np.sqrt(np.sum(np.power(d2,2))/len(d2))
    E3 = np.sqrt(np.sum(np.power(d3,2))/len(d3))
    E4 = np.sqrt(np.sum(np.power(d4,2))/len(d4))
    E5 = np.sqrt(np.sum(np.power(d5,2))/len(d5))

    Eto=E1+E2+E3+E4+E5
    
    Pi = np.zeros(5)
    Pi[0]=E1/Eto
    Pi[1]=E2/Eto
    Pi[2]=E3/Eto
    Pi[3]=E4/Eto
    Pi[4]=E5/Eto


   # print(np.sum(Pi))
   # print(Pi)
 




 
        
    # Energy
    
   # Enr = np.zeros(level)
    #for lev in range(0,level):
     #   Enr[lev] = np.sum(np.power(ap[lev],2))/n
        
    #Et = np.sum(Enr)
    
    #Pi = np.zeros(level)
    #for lev in range(0,level):
     #   Pi[lev] = Enr[lev]/Et

   # Shannon entropy     
    SE = - np.sum(np.dot(Pi,np.log(Pi)))
    
    # Renyi entropy

    #2 level
    RE2 = 1/(1-2)*np.log(np.sum(np.power(Pi,2)))

    #3 level
    RE3 = 1/(1-3)*np.log(np.sum(np.power(Pi,3)))

    # Tsallis wavwlet entropy
    TsE= 1/(2-1)*np.sum(Pi-np.power(Pi,2))

    # Generalized Tsallis wavwlet entropy
    GenTsE=1/(2-1)*(1-(np.sum(np.power((np.power(Pi,0.5)),-2))))
    
    return SE,RE2,RE3,TsE,GenTsE


w= pywt.Wavelet('coif2')
print(w)

eeg=[1,0,0.1,0.8,0.1,0,1.9,2.1,2,1.1,3.1,2.1,0.2,1,0.33,0.3,4,0.1,2,0.2]
SE,RE2,RE3,TsE,GenTsE=WE(eeg)
print(pywt.dwt_max_level(2560,"db5"))
#print(SE)
#print(RE2)
#print(RE3)
#print(TsE)
#print(GenTsE)

eeg=[0,0.2,3,0.2,0.2,1.9,3.1,2,1.5,2.1,1.1,1.2,0.4,0.23,1.3,0.14,0.1,1,1.2]
SE2,RE22,RE32,TsE2,GenTsE2=WE(eeg)

#print(SE2)
#print(RE22)
#print(RE32)
#print(TsE2)
#print(GenTsE2)


