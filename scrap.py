import requests
from bs4 import BeautifulSoup

from flask import Flask
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)

segmentCookie=b; CONSENTMGR=c1:1|c2:1|c3:1|c4:1|c5:1|c6:1|c7:1|c8:1|c9:1|c10:1|c11:1|c12:1|c13:1|c14:1|c15:1|ts:1645827593659|consent:true; marketing_vistor_id=47670323-0abe-403d-981f-1b1ff60297d0; utag_geo_code=BR; _gcl_au=1.1.1780872149.1645827694; sid=QA.CAESEPMaLXfmNE4RpqJ8otnGFX4YusmDkgYiATEqJDZhMjUyMDUwLTNhNTYtNDdhMS04YmMwLWU3YWMzOWUwZTEwMjJApLIohI8SqC7m-FRVXJdxRoZkptrUiOa4XTiTrva6wZCtkGyzgnNli1QWH2z7RQTpfsQWB1tHgHKX6MI8LoLA9joBMUIIdWJlci5jb20.NxHpNK_Y7ESEaoFHyFleeW7Zx0APuuJ6UyIjL6LC5bs; csid=1.1648420026483.CsgxHAoW65MfsF/fS+D41KDwVzvkQrML8b/cpfukVyQ=; _ua={"session_id":"f4d54660-ba68-4efc-8eda-0288f0f4019b","session_time_ms":1645828026683}; udi-id=fqFlyRaSOtlHGjL9QtymXK8ic3pmbTaEkTGJPDYBVppYRnNMKx7zQn43uBpUtZwA324K6kooINioeKrjePcIOzwg1VfBTukmBics1a86FMQ6OnW3fzbtWCvwUPAIHcha+3WzwRTAbefJ0ZZRkK1fD2XUpmQdp2/S0h1P4piLUTgA5dL4hRxDS6jKPzrhCqpj+yMhlIzvP1yT+fCg5cFU1A==tljvHWSElMA95RPBiME5hw==mvk30nD1CBoKRWF/94mjc/ey0QOraN6VHQpOLpAfkWk=; _cc=ARqGNJ8vihGcxbapjBULdRB7; rateLimiterCookieSession={"rateLimitingID":"e98bcaf8-4be0-47a5-8fd9-5da5fa0313db"}; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InNlc3Npb25fdHlwZSI6ImRlc2t0b3Bfc2Vzc2lvbiIsInRlbmFuY3kiOiJ1YmVyL3Byb2R1Y3Rpb24ifSwiaWF0IjoxNjQ1ODI4MDI2LCJleHAiOjE2NDU5MTQ0MjZ9.4XIwFD-GTcQWYq4ssx8iBWcItd7OKEasHtQif3VXy6I; utag_main=v_id:017f32f81544004d246bb7853e6405084004f07c00978$_sn:1$_ss:0$_st:1645832135807$ses_id:1645827593542;exp-session$_pn:8;exp-session$segment:a$optimizely_segment:a; mp_adec770be288b16d9008c964acfba5c2_mixpanel={"distinct_id": "6a252050-3a56-47a1-8bc0-e7ac39e0e102","$device_id": "17f32feb00d20e-05bae066b340b3-4e607a6f-144000-17f32feb00eaa1","$initial_referrer": "https://auth.uber.com/","$initial_referring_domain": "auth.uber.com","$user_id": "6a252050-3a56-47a1-8bc0-e7ac39e0e102"}; udi-fingerprint=9B6ttxLgqXEbdJdE+uzu7YL1FZ4osRuwjgrGz6XwuyKlnziR/2o/4D4eG3w56w7496DF8iN52aMBkPECNf24PA==PvQhIgDAgja88GxePy4r2ubwN3BYF/2076Jr3zGhTCs=

class valor(Resource):
    def get(self):
        html = requests.get("https://m.uber.com/looking?drop%5B0%5D=%7B%22latitude%22%3A-23.528191%2C%22longitude%22%3A-47.4651676%2C%22addressLine1%22%3A%22Mind%20Consulting%20-%20Desenvolvimento%20de%20aplicativos%2C%20desenvolvimento%20web%20%2C%20empresa%20de%20ti%2C%20desenvolvimento%20de%20software%22%2C%22addressLine2%22%3A%22Terceiriza%C3%A7%C3%A3o%20de%20ti%20empresa%20ti%20desenvolvimento%20web%20agencia%20de%20aplicativos%20-%20Avenida%20Ant%C3%B4nio%20Carlos%20Comitre%20-%20Parque%20Campolim%2C%20Sorocaba%20-%20SP%2C%20Brasil%22%2C%22id%22%3A%22ChIJoVHgBOCKxZQRp1yAFrNU65s%22%2C%22provider%22%3A%22google_places%22%2C%22index%22%3A0%7D&pickup=%7B%22latitude%22%3A-23.4677301%2C%22longitude%22%3A-47.4390258%2C%22addressLine1%22%3A%22Rua%20Canan%C3%A9ia%22%2C%22addressLine2%22%3A%22R.%20Canan%C3%A9ia%20-%20Jardim%20Iguatemi%2C%20Sorocaba%20-%20SP%22%2C%22id%22%3A%22EkBSLiBDYW5hbsOpaWEgLSBKYXJkaW0gSWd1YXRlbWksIFNvcm9jYWJhIC0gU1AsIDE4MDg1LTMwNSwgQnJhemlsIi4qLAoUChIJN1IU4u9fz5QR2kGpYg64BsISFAoSCTmcpSLjX8-UEawDui2BWeIC%22%2C%22provider%22%3A%22google_places%22%2C%22index%22%3A0%7D&vehicle=20030105")
        bs = BeautifulSoup(html.text, 'html.parser')
        print(bs)
        input = bs.find_all('div', {'class': '_css-dZTBoz'})
        print(input)
        dol = float(input[0].get("children"))
        return {"bitcoin": dol}


api.add_resource(valor, '/valor')

if __name__ == '__main__':
    app.run()
