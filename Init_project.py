Lista_zakopow = {
    "piekarnia" : ["bułki", "rogaliki"],
    "warzywniak" : ["pomidory", "ogórki"]
}



for k, v in Lista_zakopow.items():
    print("Idę do", k.capitalize(), "i kupuję tam", v[0].title(),v[1].title())

print("W sumie kupuję", sum(len(v) for v in Lista_zakopow.values()), "produktów")


  