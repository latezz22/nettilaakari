import openai


openai.api_key = "..."

viestit = [{"role": "system", "content": "Olet suomea puhuva lääkäri ja vain lääkäri. Et tiedä mistään muusta kuin lääkärin toimista. Autat ihmisiä heidän ongelmissaan ja kerrot jos heillä on tarve mennä oikean lääkärin luokse. Muista ettet ole oikea lääkäri vaan apuri, jonka pääasiallinen tarkoitus on huolehtia ihmisistä."}]

def luo_vastaus(viesti):
    viestit.append({"role": "user", "content": viesti})
    vastaus = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = viestit)
    GPT_vastaus = vastaus["choices"][0]["message"]["content"]
    viestit.append({"role": "assistant", "content": GPT_vastaus})
    
    return GPT_vastaus
