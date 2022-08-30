#importações 
from os import getcwd
import os
import sys
import datetime
import time
import html

#códigos
estou_aqui = getcwd()
plataforma = sys.platform
versao = sys.version
environ = os.environ
casa = os.getenv('HOME')
hoje = datetime.date.today()
dia_hoje = datetime.date.today().day
mes_hoje = datetime.date.today().month
ano_hoje = datetime.date.today().year
data_formatada = datetime.date.isoformat(datetime.date.today())
hora_atual = time.strftime("%H:%M")
dia_semana = time.strftime("%A, %p")
html_codificado = html.escape("This HTML fragment contains a <script>script</script> tag")
html_descodificado = html.unescape("I &hearts; Python's &lt;standard library&gt;.")

# prints
print (estou_aqui)
print (plataforma)
print (versao)
print (environ)
print (casa)
print (hoje)
print (dia_hoje)
print (mes_hoje)
print (ano_hoje)
print (data_formatada)
print (hora_atual)
print (dia_semana)
print (html_codificado)
print (html_descodificado)
