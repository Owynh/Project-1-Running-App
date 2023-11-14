import datetime as dt
import math

objDistance = int(input("Quel est votre objectif de distance : "))
distanceAct = int(input("Combien de km avez-vous parcouru jusqu'à présent ?"))
dateAjd = dt.date.today()
dateLimite = input("Entrez la date limite (YYYY-MM-DD): ")
dateLimite = dt.datetime.strptime(dateLimite, "%Y-%m-%d").date()
deltaDate = (dateLimite - dateAjd).days
deltaDistance = objDistance - distanceAct

moyenneQuotidienne = deltaDistance / deltaDate
moyenneQuotidienneArrondie = math.ceil(deltaDistance / deltaDate)

print("Vous devez courir en moyenne", moyenneQuotidienneArrondie,"(", moyenneQuotidienne, ") km par jour pendant", deltaDate, 
      "jours pour atteindre votre objectif.")

