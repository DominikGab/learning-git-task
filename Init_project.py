Lista_zakopow = {
    "piekarnia" : ["bułki", "rogaliki", "chleb"],
    "warzywniak" : ["pomidory", "ogórki","groszek"]
}



for k, v in Lista_zakopow.items():
    print("Idę do", k.capitalize(), "i kupuję tam", v[0].title(),v[1].title(),v[2].title())

print("W sumie kupuję", sum(len(v) for v in Lista_zakopow.values()), "produktów")


# Pozdrowienia
print("Pozdrawiam ze słonecznego Rapallo, we włoskiej Ligurri, gdzie aktualnie przebywam w delegacji!")
  
