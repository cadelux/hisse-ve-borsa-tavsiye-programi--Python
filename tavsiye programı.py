#########################################Piyasa İzleme ve Tavsiye Programı V1.01##############################
import time
import requests
from bs4 import BeautifulSoup


def aselsan_anlık():
    url="https://www.msn.com/en-us/money/stockdetails/ist-asels/fi-bk8sa2"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_='precurrentvalue'):
        return stock.get_text()
        
    
def aselsan_degisim():
    
    url="https://www.msn.com/en-us/money/stockdetails/ist-asels/fi-bk8sa2"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_=['chngeamount increase',
                                           'chngeamount decrease'],attrs={'data-role':'percentchange'}):
        return stock.get_text() 
    
    ########################################################
    
def microsoft_anlik():
    url="https://www.msn.com/en-us/money/stockdetails/nas-msft/fi-a1xzim"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_='precurrentvalue'):
        return stock.get_text()

def microsoft_degisim():
    url="https://www.msn.com/en-us/money/stockdetails/nas-msft/fi-a1xzim"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_=['chngeamount increase',
                                           'chngeamount decrease'],attrs={'data-role':'percentchange'}):
        return stock.get_text() 

        ########################################################

def apple_anlik():
    url="https://www.msn.com/en-us/money/stockdetails/nas-aapl/fi-a1mou2"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_='precurrentvalue'):
        return stock.get_text()

def apple_degisim():
    url="https://www.msn.com/en-us/money/stockdetails/nas-aapl/fi-a1mou2"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_=['chngeamount increase',
                                           'chngeamount decrease'],attrs={'data-role':'percentchange'}):
        return stock.get_text()

      ########################################################

def amazon_anlik():
    url="https://www.msn.com/en-us/money/stockdetails/nas-amzn/fi-a1nhlh?symbol=AMZN&form=PRMFPS"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_='precurrentvalue'):
        return stock.get_text()
         
def amazon_degisim():
    url="https://www.msn.com/en-us/money/stockdetails/nas-amzn/fi-a1nhlh?symbol=AMZN&form=PRMFPS"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_=['chngeamount increase',
                                           'chngeamount decrease'],attrs={'data-role':'percentchange'}):
        return stock.get_text()
  
    
  
        ########################################################

def tesla_anlik():
    url="https://www.msn.com/en-us/money/stockdetails/nas-tsla/fi-a24kar?symbol=TSLA&form=PRMFPS"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_='precurrentvalue'):
        return stock.get_text()
        
def tesla_degisim():
    url="https://www.msn.com/en-us/money/stockdetails/nas-tsla/fi-a24kar?symbol=TSLA&form=PRMFPS"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_=['chngeamount increase',
                                           'chngeamount decrease'],attrs={'data-role':'percentchange'}):
        return stock.get_text()
         
        ########################################################    


def netflix_anlik():

    url="https://www.msn.com/en-us/money/stockdetails/nas-nflx/fi-a1ygoc"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_='precurrentvalue'):
        return stock.get_text()
        
def netflix_degisim():
    url="https://www.msn.com/en-us/money/stockdetails/nas-nflx/fi-a1ygoc"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('div', class_=['chngeamount increase',
                                           'chngeamount decrease'],attrs={'data-role':'percentchange'}):
        return stock.get_text()
         ########################################################


##############  KRİPTO PARA #################

def  bitcoin_anlik():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s)',attrs={'data-reactid':'92'}):
        return stock.get_text()
    
def bitcoin_degisim():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(600) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(600) C($negativeColor)'],attrs={'data-reactid':'96'}):
        return stock.get_text()
    
    
###########################################    
 
def  etherium_anlik():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s)',attrs={'data-reactid':'124'}):
        return stock.get_text()
    
def etherium_degisim():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(600) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(600) C($negativeColor)'],attrs={'data-reactid':'128'}):
        return stock.get_text()
    
###########################################
def  tether_anlik():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s)',attrs={'data-reactid':'156'}):
        return stock.get_text()
    ""
    
def tether_degisim():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(600) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(600) C($negativeColor)'],attrs={'data-reactid':'160'}):
        return stock.get_text()
 ###########################################         
 

###########################################
def  xrp_anlik():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s)',attrs={'data-reactid':'188'}):
        return stock.get_text()
    
def xrp_degisim():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(600) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(600) C($negativeColor)'],attrs={'data-reactid':'192'}):
        return stock.get_text()
 ###########################################          
   
###########################################
def  cardano_anlik():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s)',attrs={'data-reactid':'252'}):
        return stock.get_text()
    
def cardano_degisim():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(600) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(600) C($negativeColor)'],attrs={'data-reactid':'256'}):
        return stock.get_text()
 ###########################################                    
    
 ###########################################
def  xlm_anlik():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s)',attrs={'data-reactid':'444'}):
        return stock.get_text()
    
def xlm_degisim():
    url="https://finance.yahoo.com/cryptocurrencies"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('td', class_='Va(m) Ta(end) Pstart(20px) Fw(600) Fz(s)',attrs={'data-reactid':'447'}):
        return stock.get_text()
 ###########################################   
 

 ########################### DÖVİZ ALTIN ##########################
 
def dolar_anlik():
    url="https://finance.yahoo.com/quote/USDTRY=X/"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',attrs={'data-reactid':'32'}):
        return stock.get_text()


def dolar_degisim():
    url="https://finance.yahoo.com/quote/USDTRY=X/"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'],attrs={'data-reactid':'33'}):
        return stock.get_text()
    
############################
    
def euro_anlik():
    url="https://finance.yahoo.com/quote/eurtry=x?ltr=1"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',attrs={'data-reactid':'32'}):
        return stock.get_text()


def euro_degisim():
    url="https://finance.yahoo.com/quote/eurtry=x?ltr=1"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'],attrs={'data-reactid':'33'}):
        return stock.get_text()
        
##################################

def sterlin_anlik():
    url="https://finance.yahoo.com/quote/gbptry=x/"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',attrs={'data-reactid':'32'}):
        return stock.get_text()


def sterlin_degisim():
    url="https://finance.yahoo.com/quote/gbptry=x/"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'],attrs={'data-reactid':'33'}):
        return stock.get_text()
##################################

def altin_anlik():

    url="https://finance.yahoo.com/quote/GC=F?p=GC=F"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',attrs={'data-reactid':'32'}):
       return(stock.get_text())
       


def altin_degisim():
    url="https://finance.yahoo.com/quote/GC=F?p=GC=F"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'],attrs={'data-reactid':'33'}):
        return stock.get_text()  

##################################

def gümüs_anlik():
    url="https://finance.yahoo.com/quote/SI=F?p=SI=F"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',attrs={'data-reactid':'32'}):
        return stock.get_text()


def gümüs_degisim():
    url="https://finance.yahoo.com/quote/SI=F?p=SI=F"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'],attrs={'data-reactid':'33'}):
        return stock.get_text()     

##################################

def hamyag_anlik():
    url="https://finance.yahoo.com/quote/CL=F?p=CL=F"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)',attrs={'data-reactid':'32'}):
         return stock.get_text()


def hamyag_degisim():
    url="https://finance.yahoo.com/quote/CL=F?p=CL=F"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"lxml")
    for stock in soup.find_all('span', class_=['Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)',
                                           'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'],attrs={'data-reactid':'33'}):
        return stock.get_text()          
  




a=gümüs_degisim().split()
b=a[1].split("%")
c=b[0].split("(")
gümüsdegisim=float(c[1])


a=hamyag_degisim().split()
b=a[1].split("%")
c=b[0].split("(")
hamyagdegisim=float(c[1])


a=altin_degisim().split()
b=a[1].split("%")
c=b[0].split("(")
altindegisim=float(c[1])



a=sterlin_degisim().split()
b=a[1].split("%")
c=b[0].split("(")
sterlindegisim=float(c[1])


a=euro_degisim().split()
b=a[1].split("%")
c=b[0].split("(")
eurodegisim=float(c[1])


a=dolar_degisim().split()
b=a[1].split("%")
c=b[0].split("(")
dolardegisim=float(c[1])





a=xlm_degisim().split("%")
xlmdegisim=float(a[0])


a=cardano_degisim().split("%")
cardanodegisim=float(a[0])


a=xrp_degisim().split("%")
xrpdegisim=float(a[0])


a=tether_degisim().split("%")
tetherdegisim=float(a[0])


a=etherium_degisim().split("%")
etheriumdegisim=float(a[0])


a=bitcoin_degisim().split("%")
bitcoindegisim=float(a[0])



      
aselsan=aselsan_degisim().split("%")
xaselsan=float(aselsan[0])


tesla=tesla_degisim().split("%")
xtesla=float(tesla[0])
   
    
    
netflix=netflix_degisim().split("%")
xnetflix=float(netflix[0])

    
amazon=amazon_degisim().split("%")
xamazon=float(amazon[0])


apple=apple_degisim().split("%")
xapple=float(apple[0])


microsoft=microsoft_degisim().split("%")
xmicrosoft=float(microsoft[0])




def sirkettavsiye():
    if(-9<xaselsan<-6):
        print("Aselsan %",xaselsan," kuvvetli alım!")
    if(3<xaselsan<6):
        print("Aselsan %",xaselsan," alım!")    
    if(-6<xaselsan<-3):
        print("Aselsan %",xaselsan," riskli alım!")       
    if(6<xaselsan<9):
        print("Aselsan %",xaselsan," yüksek riskli alım!")            
    if(xaselsan<-9):
        print("Aselsan %",xaselsan," kuvvetli satış!")         
    if(-3<xaselsan<0):
        print("Aselsan %",xaselsan," satış!")      
    if(0<xaselsan<=3):
        print("Aselsan %",xaselsan," riskli satış!") 
    
        
    if(-9<xmicrosoft<-6):
        print("Microsoft %",xmicrosoft," kuvvetli alım!")  
    if(3<xmicrosoft<6):
        print("Microsoft %",xmicrosoft," alım!")    
    if(-6<xmicrosoft<-3):
        print("Microsoft %",xmicrosoft," riskli alım!")  
    if(6<xmicrosoft<9):
        print("Microsoft %",xmicrosoft," yüksek riskli alım!")       
    if(xmicrosoft<-9):
        print("Microsoft %",xmicrosoft," kuvvetli satış!")         
    if(-3<xmicrosoft<0):
        print("Microsoft %",xmicrosoft," satış!")      
    if(0<xmicrosoft<=3):
        print("Microsoft %",xmicrosoft," riskli satış!") 
         
         
    if(-9<xapple<-6):
        print("Apple %",xapple," kuvvetli alım!")  
    if(3<xapple<6):
        print("Apple %",xapple," alım!")    
    if(-6<xapple<-3):
        print("Apple %",xapple," riskli alım!")  
    if(6<xapple<9):
        print("Apple %",xapple," yüksek riskli alım!")       
    if(xapple<-9):
        print("Apple %",xapple," kuvvetli satış!")         
    if(-3<xapple<0):
        print("Apple %",xapple," satış!")      
    if(0<xapple<=3):
        print("Apple %",xapple," riskli satış!")                 
   
        
    if(-9<xamazon<-6):
        print("Amazon %",xamazon," kuvvetli alım!")  
    if(3<xamazon<6):
        print("Amazon %",xamazon," alım!")    
    if(-6<xamazon<-3):
        print("Amazon %",xamazon," riskli alım!")  
    if(6<xamazon<9):
        print("Amazon %",xamazon," yüksek riskli alım!")       
    if(xamazon<-9):
        print("Amazon %",xamazon," kuvvetli satış!")         
    if(-3<xamazon<0):
        print("Amazon %",xamazon," satış!")      
    if(0<xamazon<=3):
        print("Amazon %",xamazon," riskli satış!")          
        
    
   
    if(-9<xtesla<-6):
        print("Tesla %",xtesla," kuvvetli alım!")  
    if(3<xtesla<6):
        print("Tesla %",xtesla," alım!")    
    if(-6<xtesla<-3):
        print("Tesla %",xtesla," riskli alım!")  
    if(6<xtesla<9):
        print("Tesla %",xtesla," yüksek riskli alım!")       
    if(xtesla<-9):
        print("Tesla %",xtesla," kuvvetli satış!")         
    if(-3<xtesla<0):
        print("Tesla %",xtesla," satış!")      
    if(0<xtesla<=3):
        print("Tesla %",xtesla," riskli satış!")    
           
        
        
    if(-9<xnetflix<-6):
        print("Netflix %",xnetflix," kuvvetli alım!")     
    if(3<xnetflix<6):
        print("Netflix %",xnetflix," alım!")    
    if(-6<xnetflix<-3):
        print("Netflix %",xnetflix," riskli alım!")  
    if(6<xnetflix<9):
        print("Netflix %",xnetflix," yüksek riskli alım!")      
    if(xnetflix<-9):
        print("Netflix %",xnetflix," kuvvetli satış!")         
    if(-3<xnetflix<0):
        print("Netflix %",xnetflix," satış!")      
    if(0<xnetflix<=3):
        print("Netflix %",xnetflix," riskli satış!")    
        
    else:
        print("Başka Alış ve satış tavsiyesi şu anlık bulunmuyor.")
        
    while True:
        secim2=int(input("Ekranı yenilemek için 1 e basıınız\ngeri gelmek için 0 a :"))
        if(secim2==0): 
            baslangic()
        print(sirkettavsiye())    

def kriptotavsiye():
    if(-9<bitcoindegisim<-6):
        print("Bitcoin %",bitcoindegisim," kuvvetli alım!")
    if(3<bitcoindegisim<6):
        print("Bitcoin %",bitcoindegisim," alım!")    
    if(-6<bitcoindegisim<-3):
        print("Bitcoin %",bitcoindegisim," riskli alım!")       
    if(6<bitcoindegisim<9):
        print("Bitcoin %",bitcoindegisim," yüksek riskli alım!")            
    if(bitcoindegisim<-9):
        print("Bitcoin %",bitcoindegisim," kuvvetli satış!")         
    if(-3<bitcoindegisim<0):
        print("Bitcoin %",bitcoindegisim," satış!")      
    if(0<bitcoindegisim<=3):
        print("Bitcoin %",bitcoindegisim," riskli satış!")
    
        
    if(-9<etheriumdegisim<-6):
        print("Etherium %",etheriumdegisim," kuvvetli alım!")  
    if(3<etheriumdegisim<6):
        print("Etherium %",etheriumdegisim," alım!")    
    if(-6<etheriumdegisim<-3):
        print("Etherium %",etheriumdegisim," riskli alım!")  
    if(6<etheriumdegisim<9):
        print("Etherium %",etheriumdegisim," yüksek riskli alım!")       
    if(etheriumdegisim<-9):
        print("Etherium %",etheriumdegisim," kuvvetli satış!")         
    if(-3<etheriumdegisim<0):
        print("Etherium %",etheriumdegisim," satış!")      
    if(0<etheriumdegisim<=3):
        print("Etherium %",etheriumdegisim," riskli satış!")
         
         
    if(-9<tetherdegisim<-6):
        print("Tether %",tetherdegisim," kuvvetli alım!")  
    if(3<tetherdegisim<6):
        print("Tether %",tetherdegisim," alım!")    
    if(-6<tetherdegisim<-3):
        print("Tether %",tetherdegisim," riskli alım!")  
    if(6<tetherdegisim<9):
        print("Tether %",tetherdegisim," yüksek riskli alım!")       
    if(tetherdegisim<-9):
        print("Tether %",tetherdegisim," kuvvetli satış!")         
    if(-3<tetherdegisim<0):
        print("Tether %",tetherdegisim," satış!")      
    if(0<tetherdegisim<=3):
        print("Tether %",tetherdegisim," riskli satış!")
        
   
        
    if(-9<xrpdegisim<-6):
        print("XRP %",xrpdegisim," kuvvetli alım!")  
    if(3<xrpdegisim<6):
        print("XRP %",xrpdegisim," alım!")    
    if(-6<xrpdegisim<-3):
        print("XRP %",xrpdegisim," riskli alım!")  
    if(6<xrpdegisim<9):
        print("XRP %",xrpdegisim," yüksek riskli alım!")       
    if(xrpdegisim<-9):
        print("XRP %",xrpdegisim," kuvvetli satış!")         
    if(-3<xrpdegisim<0):
        print("XRP %",xrpdegisim," satış!")      
    if(0<xrpdegisim<=3):
        print("XRP %",xrpdegisim," riskli satış!")      
        
    
   
    if(-9<cardanodegisim<-6):
        print("Cardano %",cardanodegisim," kuvvetli alım!")  
    if(3<cardanodegisim<6):
        print("Cardano %",cardanodegisim," alım!")    
    if(-6<cardanodegisim<-3):
        print("Cardano %",cardanodegisim," riskli alım!")  
    if(6<cardanodegisim<9):
        print("Cardano %",cardanodegisim," yüksek riskli alım!")       
    if(cardanodegisim<-9):
        print("Cardano %",cardanodegisim," kuvvetli satış!")         
    if(-3<cardanodegisim<0):
        print("Cardano %",cardanodegisim," satış!")      
    if(0<cardanodegisim<=3):
        print("Cardano %",cardanodegisim," riskli satış!")    
        
        
    if(-9<xlmdegisim<-6):
        print("XLM %",xlmdegisim," kuvvetli alım!")     
    if(3<xlmdegisim<6):
        print("XLM %",xlmdegisim," alım!")    
    if(-6<xlmdegisim<-3):
        print("XLM %",xlmdegisim," riskli alım!")  
    if(6<xlmdegisim<9):
        print("XLM %",xlmdegisim," yüksek riskli alım!")      
    if(xlmdegisim<-9):
        print("XLM %",xlmdegisim," kuvvetli satış!")         
    if(-3<xlmdegisim<0):
        print("XLM %",xlmdegisim," satış!")      
    if(0<xlmdegisim<=3):
        print("XLM %",xlmdegisim," riskli satış!")    
        
    else:
        print("Başka Alış ve satış tavsiyesi şu anlık bulunmuyor.")
        
    while True:
        secim2=int(input("Ekranı yenilemek için 1 e basıınız\ngeri gelmek için 0 a :"))
        if(secim2==0): 
            baslangic()
        print(kriptotavsiye())    
 
def doviztavsiye():
    if(-9<altindegisim<-6):
        print("Altın %",altindegisim," kuvvetli alım!")    
    if(3<altindegisim<6):
        print("Altın %",altindegisim," alım!")    
    if(-6<altindegisim<-3):
        print("Altın %",altindegisim," riskli alım!")       
    if(6<altindegisim<9):
        print("Altın %",altindegisim," yüksek riskli alım!")            
    if(altindegisim<-9):
        print("Altın %",altindegisim," kuvvetli satış!")         
    if(-3<altindegisim<0):
        print("Altın %",altindegisim," satış!")      
    if(0<altindegisim<=3):
        print("Altın %",altindegisim," riskli satış!") 
    
        
    if(-9<dolardegisim<-6):
        print("Dolar %",dolardegisim," kuvvetli alım!")  
    if(3<dolardegisim<6):
        print("Dolar %",dolardegisim," alım!")    
    if(-6<dolardegisim<-3):
        print("Dolar %",dolardegisim," riskli alım!")  
    if(6<dolardegisim<9):
        print("Dolar %",dolardegisim," yüksek riskli alım!")       
    if(dolardegisim<-9):
        print("Dolar %",dolardegisim," kuvvetli satış!")         
    if(-3<dolardegisim<0):
        print("Dolar %",dolardegisim," satış!")      
    if(0<dolardegisim<=3):
        print("Dolar %",dolardegisim," riskli satış!")  
         
         
    if(-9<eurodegisim<-6):
        print("Euro %",eurodegisim," kuvvetli alım!")  
    if(3<eurodegisim<6):
        print("Euro %",eurodegisim," alım!")    
    if(-6<eurodegisim<-3):
        print("Euro %",eurodegisim," riskli alım!")  
    if(6<eurodegisim<9):
        print("Euro %",eurodegisim," yüksek riskli alım!")       
    if(eurodegisim<-9):
        print("Euro %",eurodegisim," kuvvetli satış!")         
    if(-3<eurodegisim<0):
        print("Euro %",eurodegisim," satış!")      
    if(0<eurodegisim<=3):
        print("Euro %",eurodegisim," riskli satış!")        
   
        
    if(-9<sterlindegisim<-6):
        print("Sterlin %",sterlindegisim," kuvvetli alım!")  
    if(3<sterlindegisim<6):
        print("Sterlin %",sterlindegisim," alım!")    
    if(-6<sterlindegisim<-3):
        print("Sterlin %",sterlindegisim," riskli alım!")  
    if(6<sterlindegisim<9):
        print("Sterlin %",sterlindegisim," yüksek riskli alım!")       
    if(sterlindegisim<-9):
        print("Sterlin %",sterlindegisim," kuvvetli satış!")         
    if(-3<sterlindegisim<0):
        print("Sterlin %",sterlindegisim," satış!")      
    if(0<sterlindegisim<=3):
        print("Sterlin %",sterlindegisim," riskli satış!")        
        
    
   
    if(-9<hamyagdegisim<-6):
        print("Hamyağ %",hamyagdegisim," kuvvetli alım!")  
    if(3<hamyagdegisim<6):
        print("Hamyağ %",hamyagdegisim," alım!")    
    if(-6<hamyagdegisim<-3):
        print("Hamyağ %",hamyagdegisim," riskli alım!")  
    if(6<hamyagdegisim<9):
        print("Hamyağ %",hamyagdegisim," yüksek riskli alım!")       
    if(hamyagdegisim<-9):
        print("Hamyağ %",hamyagdegisim," kuvvetli satış!")         
    if(-3<hamyagdegisim<0):
        print("Hamyağ %",hamyagdegisim," satış!")      
    if(0<hamyagdegisim<=3):
        print("Hamyağ %",hamyagdegisim," riskli satış!") 
        
        
    if(-9<gümüsdegisim<-6):
        print("Gümüş %",gümüsdegisim," kuvvetli alım!")     
    if(3<gümüsdegisim<6):
        print("Gümüş %",gümüsdegisim," alım!")    
    if(-6<gümüsdegisim<-3):
        print("Gümüş %",gümüsdegisim," riskli alım!")  
    if(6<gümüsdegisim<9):
        print("Gümüş %",gümüsdegisim," yüksek riskli alım!")      
    if(gümüsdegisim<-9):
        print("Gümüş %",gümüsdegisim," kuvvetli satış!")         
    if(-3<gümüsdegisim<0):
        print("Gümüş %",gümüsdegisim," satış!")      
    if(0<gümüsdegisim<=3):
        print("Gümüş %",gümüsdegisim," riskli satış!")     
        
    else:
        print("Başka Alış ve satış tavsiyesi şu anlık bulunmuyor.")
        
    while True:
        secim2=int(input("Ekranı yenilemek için 1 e basıınız\ngeri gelmek için 0 a :"))
        if(secim2==0): 
            baslangic()
        print(doviztavsiye())
           


 
    
print("                    ####### Hoşgeldiniz #######")


def baslangic():
       
    
    print("1-Şirket Piyasaları 2-Kripto Para Piyasaları 3-Döviz Piyasaları 4-Çıkış Yap")
    secim=int(input("Lütfen Bir Seçim Yapınız:"))
                         ##### ŞİRKET PİYASALARI  
    
    if(secim==1):
        
        ############ şirket piyasaları #########
        
        print("ŞİRKET PİYASALARI seçildi")
        print("1-Aselsan\n2-Microsoft\n3-Apple\n4-Amazon\n5-Tesla\n6-Netflix\n7-Yatırım tavsiyesi al!")
        secim1=int(input("Seçim yapınız: "))
    
        if(secim1==1): ######Aselsan###
            while True:
                print('Aselsan piyasa değeri: '+aselsan_anlık())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #ASELSAN
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Aselsan % değişim değeri değeri "+aselsan_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();
           
                          
        if(secim1==2):###########Microsoft########
            while True:
                print('Microsoft piyasa değeri: '+microsoft_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Microsoft
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Microsoft % değişim değeri değeri "+microsoft_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();         
                
        if(secim1==3):#######APPLE#######
            while True:
                print('Apple piyasa değeri: '+apple_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #APPLE
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Apple % değişim değeri değeri "+apple_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();  
        if(secim1==4):#######Amazon#######
            while True:
                print('\nAmazon piyasa değeri: ',amazon_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Amazon
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Amazon % değişim değeri değeri "+amazon_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();
        if(secim1==5):#######Tesla#######
            while True:
                print('Tesla piyasa değeri: '+tesla_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Tesla
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Tesla % değişim değeri değeri "+tesla_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();    
                          
        if(secim1==6):#######Netflix#######
            while True:
                print('Netflix piyasa değeri: '+netflix_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Netflix
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Netflix % değişim değeri değeri "+netflix_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();                
        if(secim1==7):
            sirkettavsiye()
            

                     ##### KRİPTO PARA PİYASALARI  
                     
    if(secim==2):
        print("Kripto Para PİYASALARI seçildi")
        print("1-Bitcoin 2-Etherium 3-Tether 4-XRP 5-Cardano 6-XLM 7-Yatırım Tavsiyesi Al! ")
        secim1=int(input("Seçim yapınız: ")) 
        if(secim1==1):###########Bitcoin########
            while True:
                print('Bitcoin piyasa değeri: '+bitcoin_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Bitcoin
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Bitcoin % değişim değeri değeri "+bitcoin_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();      
                    
        if(secim1==2):###########Etherium########
            while True:
                print('Etherium piyasa değeri: '+etherium_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Etherium
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Etherium % değişim değeri değeri "+etherium_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();               
                
        if(secim1==3):###########Tether########
            while True:
                print('Tether piyasa değeri: '+tether_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Tether
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Tether % değişim değeri değeri "+tether_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();      
        if(secim1==4):###########XRP########
            while True:
                print('XRP piyasa değeri: '+xrp_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #XRP
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("XRP % değişim değeri değeri "+xrp_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();                  
        if(secim1==5):###########Cardano########
            while True:
                print('Cardano piyasa değeri: '+cardano_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Cardano
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Cardano % değişim değeri değeri "+cardano_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();                  
        if(secim1==6):###########XLM########
            while True:
                print('XLM piyasa değeri: '+xlm_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #XLM
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("XLM % değişim değeri değeri "+xlm_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();                
        if(secim1==7):
            kriptotavsiye()          
            
        
            
                
                    
                    
        
                       ##### DÖVİZ PİYASALARI  
    if(secim==3):
        
        ############ DÖVİZ PİYASALARI #########
        
        print("ŞDÖVİZ PİYASALARI seçildi")
        print("1-Altın\n2-Dolar\n3-Euro\n4-Sterlin\n5-Hamyağ\n6-Gümüş\n7-Yatırım tavsiyesi al!")
        secim1=int(input("Seçim yapınız: "))
    
        if(secim1==1): ######Altın###
            while True:
                print('Altın piyasa değeri: '+altin_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Altın
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Altın % değişim değeri değeri "+altin_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();
           
                          
        if(secim1==2):###########Dolar########
            while True:
                print('Dolar piyasa değeri: '+dolar_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Dolar
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Dolar % değişim değeri değeri "+dolar_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();         
                
        if(secim1==3):#######Euro#######
            while True:
                print('Euro piyasa değeri: '+euro_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Euro
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Euro % değişim değeri değeri "+euro_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();  
        if(secim1==4):#######Sterlin#######
            while True:
                print('\Sterlin piyasa değeri: ',sterlin_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                 
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Sterlin % değişim değeri değeri "+sterlin_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();
        if(secim1==5):#######Hamyağ#######
            while True:
                print('Hamyağ piyasa değeri: '+hamyag_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Hamyağ
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Hamyağ % değişim değeri değeri "+hamyag_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();    
                          
        if(secim1==6):#######Gümüş#######
            while True:
                print('Gümüş piyasa değeri: '+gümüs_anlik())
                secim2=int(input("değeri yenilemek için 1 e basıınız\ngeri gelmek için 0 a\n % değişim değeri için 2e :"))
                  #Gümüş
                if(secim2==0):
                    baslangic();
                if(secim2==2):
                    while True:
                      print("Gümüş % değişim değeri değeri "+gümüs_degisim())
                      secim2=int(input("değeri yenilemek için 1 e basıınız geri gelmek için 0a :"))
                      if(secim2==0):
                          baslangic();                
        if(secim1==7):
            doviztavsiye()
         
                    
                    ##### ÇIKIŞ YAP ######
        
    if(secim==4):
        print("Çıkış yapılıyor...")
        time.sleep(3)
            
      
     
baslangic()  
 

#aselsan_anlık()
#aselsan_degisim()

#microsoft_anlik()
#microsoft_degisim()    
     
#apple_anlik()
#apple_degisim()

#amazon_anlik()           
#amazon_degisim() 
          
#tesla_anlik()
#tesla_degisim()

#netflix_anlik() 
#netflix_degisim()   

#bitcoin_anlik()         
#bitcoin_degisim()      

#etherium_anlik()
#etherium_degisim()   

#tether_anlik()
#tether_degisim()    

#xrp_anlik()
#xrp_degisim()    

#cardano_anlik()
#cardano_degisim()             

#xlm_anlik()
#xlm_degisim() 
          
#dolar_anlik()
#dolar_degisim()     
      
#euro_anlik()
#euro_degisim()     
      
#sterlin_anlik()
#sterlin_degisim()

#altin_anlik()
#altin_degisim()  
          
#gümüs_anlik()
#gümüs_degisim()

#hamyag_anlik()
#hamyag_degisim()    
            
            
            
        
       
        
       
        
        
          
          
          
          
             
             
          
          
          
          
       
              
          

          
        


    