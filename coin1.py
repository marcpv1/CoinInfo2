from coinbase.wallet.client import Client
from coinbase.wallet.model import Transaction
#from forex_python.converter import CurrencyRates
import sys
import json
import httplib
import urllib

sys.path.insert(0,'/home/pi/coinbase_git')
import config_coin_mpv
import config_coin_arg

if (len(sys.argv)>0):
   user = sys.argv[1]

if (user=='mpv'):
    api_key = config_coin_mpv.api_key
    api_secret = config_coin_mpv.api_secret
   
if (user=='arg'):
    api_key = config_coin_arg.api_key
    api_secret = config_coin_arg.api_secret


client = Client(api_key, api_secret)
currency_EUR = 'BTC-EUR'
currency_USD = 'BTC-USD'
currencyEURUSD='EUR-USD'
currency_LINK='LINK-EUR'
currency_LINK_USD='LINK-USD'
currency_ETH='ETH-EUR'
currency_ETH_USD='ETH-USD'
currency_ADA='ADA-EUR'
currency_ADA_USD='ADA-USD'
currency_SOL='SOL-EUR'
currency_SOL_USD='SOL-USD'

total = 0
message = []

preu = client.get_spot_price(currency_pair=currency_EUR)
preuEUR = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_USD)
preuUSD = str(preu.amount)
preu0 = client.get_spot_price(currency_pair=currencyEURUSD)
preuEUR0 = str(preu0.amount)
preu = client.get_spot_price(currency_pair=currency_LINK)
preuLINK = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_LINK_USD)
preuLINK_USD = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_ETH)
preuETH = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_ETH_USD)
preuETH_USD = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_ADA)
preuADA = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_ADA_USD)
preuADA_USD = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_SOL)
preuSOL = str(preu.amount)
preu = client.get_spot_price(currency_pair=currency_SOL_USD)
preuSOL_USD = str(preu.amount)


accounts = client.get_accounts()

print("<br>1 &euro; = " + str(preuEUR0) + " $")
fvalortotal=0

llista = []
llista_id = []
llista_nomcompte = []
llista_saldo = []

for wallet in accounts.data:

    #print(wallet)
    valor = str( wallet['native_balance'])
    balanc = str(wallet['balance'])
    fvalor = float(valor.replace("EUR ",""))

    if round(fvalor)!=0:

      if str(wallet['currency'])=='BTC':
         cadena = '<br/><br/>'
         cadena = cadena + '<a href="https://coinmarketcap.com/es/currencies/bitcoin/" target="_blank">'
         cadena = cadena + '<img src=\"https://assets.bitstamp.net/widgets/s/widgets/widgets/img/btc.5e2d1332.svg\" width=\"40\" height=\"40\"></a>'
         cadena = cadena + '<b> Bitcoin </b><br><font size=\"5\">(' + preuEUR + ' &euro;/' + preuUSD + ' $)</font>'
         cadena += '<br>Saldo ' + balanc
         cadena += '<br>Saldo ' + valor.replace("EUR ","") + ' &euro;'
         llista.insert(0,cadena)
         llista_id.insert(0,str(wallet['id']))
         llista_nomcompte.insert(0,str(wallet['name']))
         llista_saldo.insert(0,round(fvalor,2))

      if str(wallet['currency'])=='LINK':
         cadena2 = '<br/><br/>'
         cadena2 = cadena2 + '<a href="https://coinmarketcap.com/es/currencies/chainlink/" target="_blank">'
         cadena2 = cadena2 + '<img src=\"https://assets.bitstamp.net/dashboard/s/widgets/dashboard/98015f33f9e7bcb0acc781f022646f8f.svg\" width=\"40\" height=\"40\"></a>'
         cadena2 = cadena2 + '<b> Chainlink </b><br><font size=\"5\">('+ preuLINK + ' &euro;/' + preuLINK_USD + ' $)</font>'
         cadena2 += '<br>Saldo ' + balanc
         cadena2 += '<br>Saldo ' + valor.replace("EUR ","") + ' &euro;'
         llista.append(cadena2)
         llista_id.append(str(wallet['id']))
         llista_nomcompte.append(str(wallet['name']))
         llista_saldo.append(round(fvalor,2))

      if str(wallet['currency'])=='ETH':
         cadena3 = '<br/><br/>'
         cadena3 = cadena3 + '<a href="https://coinmarketcap.com/es/currencies/ethereum/" target="_blank">'
         cadena3 = cadena3 + '<img src=\"https://assets.bitstamp.net/dashboard/s/widgets/dashboard/44cfa606c6c2ace5de7d6a29ff2bb998.svg\" width=\"40\" height=\"40\"></a>'
         cadena3 = cadena3 + '<b> Ethereum</b><br><font size=\"5\">('+ preuETH + ' &euro;/' + preuETH_USD + ' $)</font>'
         cadena3 += '<br>Saldo ' + balanc
         cadena3 += '<br>Saldo ' + valor.replace("EUR ","") + ' &euro;'
         llista.append(cadena3)
         llista_id.append(str(wallet['id']))
         llista_nomcompte.append(str(wallet['name']))
         llista_saldo.append(round(fvalor,2))

      if str(wallet['currency'])=='ADA':
         cadena3 = '<br/><br/>'
         cadena3 = cadena3 + '<a href="https://coinmarketcap.com/es/currencies/cardano/" target="_blank">'
         cadena3 = cadena3 + '<img src=\"https://s2.coinmarketcap.com/static/img/coins/64x64/2010.png\" width=\"40\" height=\"40\"></a>'
         cadena3 = cadena3 + '<b> Cardano</b><br><font size=\"5\">('+ preuADA + ' &euro;/' + preuADA_USD + ' $)</font>'
         cadena3 += '<br>Saldo ' + balanc
         cadena3 += '<br>Saldo ' + valor.replace("EUR ","") + ' &euro;'
         llista.append(cadena3)
         llista_id.append(str(wallet['id']))
         llista_nomcompte.append(str(wallet['name']))
         llista_saldo.append(round(fvalor,2))

      if str(wallet['currency'])=='SOL':
         cadena3 = '<br/><br/>'
         cadena3 = cadena3 + '<a href="https://coinmarketcap.com/es/currencies/solana/" target="_blank">'
         cadena3 = cadena3 + '<img src=\"https://dynamic-assets.coinbase.com/d2ba1ad058b9b0eb4de5f0ccbf0e4aecb8d73d3a183dbaeabbec2b6fd77b0a636598e08467a05da7e69f39c65693f627edf7414145ee6c61e01efc831652ca0f/asset_icons/8733712db93f857c04b7c58fb35eafb3be360a183966a1e57a6e22ee5f78c96d.png\" width=\"40\" height=\"40\"></a>'
         cadena3 = cadena3 + '<b> Solana</b><br><font size=\"5\">('+ preuSOL + ' &euro;/' + preuSOL_USD + ' $)</font>'
         cadena3 += '<br>Saldo ' + balanc
         cadena3 += '<br>Saldo ' + valor.replace("EUR ","") + ' &euro;'
         llista.append(cadena3)
         llista_id.append(str(wallet['id']))
         llista_nomcompte.append(str(wallet['name']))
         llista_saldo.append(round(fvalor,2))

      fvalortotal+=fvalor

for i in range(len(llista)) :
          #print(llista[i])
          i+=1

    
print("<br><br><b>Saldo Total</b>")
print("<br>" + str(fvalortotal) + " &euro;")

print("<br><br><b>CARTERA</b>")

i=0
llista_valor_transacc = []
ftransaccionstotal=0

for id in llista_id:

 print(llista[i])
 #print("<br><b>" + llista_nomcompte[i] + " </b>")
 transactions = client.get_transactions(id)
 ftransaccionswallet=0
 str_transacc="<i>Transaccions </i>"
 str_transacc+="<button type=\"button\" class=\"btn btn-info\" data-toggle=\"collapse\" data-target=\"#transacc" + str(i) + "\">+</button>"
 str_transacc+="<div id=\"transacc" + str(i) + "\" class=\"collapse\">"
 str_transacc+="<font size=\"5\">"
 for t in transactions.data:

        #print("<p>" + t.details.header[:-3] + "</p>")
        fvalor=float(t.native_amount.amount)
        
        str_transacc+="<p>" + t.native_amount.amount + " &euro;"
        str_transacc+=" " + t.created_at[:10] + "</p>"
        #print("<p>" + str(t.amount) + "</p>")        

        ftransaccionswallet+=fvalor
       
        ftransaccionstotal+=fvalor
 str_transacc+="<p>Total: " + str(ftransaccionswallet) + " &euro;</p>"
 str_transacc+="</font></div>"
 llista_valor_transacc.append(ftransaccionswallet)
 print("<p>Benefici: " + str(llista_saldo[i]-ftransaccionswallet) + " &euro;")
 
 fperc_benefici=0
 if (ftransaccionswallet>0):
     fperc_benefici=((llista_saldo[i]*100)/ftransaccionswallet)-100
 
 if (fperc_benefici>=0):
     print(" <font size=\"5\"><span style=\"color:rgb(0,180,0);\">+" + str(round(fperc_benefici,2)) + "%</span></font></p>")
 else:
     print(" <font size=\"5\"><span style=\"color:red;\">" + str(round(fperc_benefici,2)) + "%</span></font></p>")
 print(str_transacc)
 i=i+1

print("<br>")
print("<br><b>Valor actual:</b> " + str(fvalortotal) + " &euro;")
print("<br><b>Total transaccions:</b> " + str(ftransaccionstotal) + " &euro;")

fperc_benefici=round(((fvalortotal*100)/ftransaccionstotal)-100,2)

if (fperc_benefici>=0):
    spercbenefici="<font size=\"5\"><span style=\"color:rgb(0,180,0);\">+" + str(fperc_benefici) + "%</span></font>"
else:
    spercbenefici="<font size=\"5\"><span style=\"color:red;\">" + str(fperc_benefici) + "%</span></font>"

if ((fvalortotal-ftransaccionstotal)>=0):
 print("<br><b>Benefici: </b>" + str(fvalortotal-ftransaccionstotal) + " &euro;</span> " + spercbenefici)
else:
 print("<br><b>Benefici: </b>" + str(fvalortotal-ftransaccionstotal) + " &euro;</span> " + spercbenefici)
