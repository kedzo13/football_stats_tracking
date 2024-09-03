import requests
from datetime import datetime, timedelta
import csv 

# Postavi API ključ i URL
API_KEY = '9d14315aa5534bda83ca294fd290d3c7'  # Zamijeni s pravim API ključem
URL = 'https://api.football-data.org/v4/matches'

# Postavi datume u filterima na prošle i buduće datume
today = datetime.today().date()
date_from = today - timedelta(days=1)  
date_to = today + timedelta(days=3)    

filters = {
    'dateFrom': str(date_from),
    'dateTo': str(date_to),
    'permission': 'TIER_ONE'
}

headers = {
    'X-Auth-Token': API_KEY
}

# Napravi GET zahtjev za dohvaćanje utakmica
response = requests.get(URL, headers=headers, params=filters)

# Ispis statusnog koda, zaglavlja i sadržaja odgovora za dijagnostiku
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Text:", response.text)

# Provjeri je li zahtjev uspješan
if response.status_code == 200:
    data = response.json()

    # Otvori CSV datoteku za pisanje
    with open('football_matches.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(['Home team', 'Away team', 'Half time score', 'Full time score'])

        #zapiši podatke o utakmicama 
        if 'matches' in data and data['matches']:
            for match in data['matches']:
                home_team = match['homeTeam']['shortName']
                away_team = match['awayTeam']['shortName']
                half_time_score = f"{match['score']['halfTime']['home']}-{match['score']['halfTime']['away']}"
                full_time_score = f"{match['score']['fullTime']['home']}-{match['score']['fullTime']['away']}"

                writer.writerow([home_team, away_team, half_time_score, full_time_score])

    # Prikaz podataka
    print("Data:", data)
else:
    print("Error while data gathering.")
