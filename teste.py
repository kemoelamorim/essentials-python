import requests
import pandas as pd
import xmltodict

resposta = requests.get("https://viacep.com.br/ws/01001000/xml/")

dadosDic = xmltodict.parse(resposta.content)
df = pd.DataFrame.from_dict(dadosDic)
print(df)
