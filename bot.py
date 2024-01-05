#Tuodaan openai:n kirjasto.
import openai

#Avain
openai.api_key = "..."

#Alustusviesti
viestit = [{"role": "system", "content": "Olet suomea puhuva lääkäri ja vain lääkäri. Et tiedä mistään muusta kuin lääkärin toimista. Autat ihmisiä heidän ongelmissaan ja kerrot jos heillä on tarve mennä oikean lääkärin luokse. Muista ettet ole oikea lääkäri vaan apuri, jonka pääasiallinen tarkoitus on huolehtia ihmisistä."}]

#Määritellään funktio viestin luonnista
def luo_vastaus(viesti):

    #Generoidaan viesti
    viestit.append({"role": "user", "content": viesti})
    vastaus = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = viestit)
    GPT_vastaus = vastaus["choices"][0]["message"]["content"]
    viestit.append({"role": "assistant", "content": GPT_vastaus})
    #Palautetaan viesti
    return GPT_vastaus
