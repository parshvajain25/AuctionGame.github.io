import requests
from bs4 import BeautifulSoup
import yaml
import json

# data = {
#         "allRounders" : { "Andre Russell":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/177/andre-russell"},       
#         }

data = {"wicketkeepers":{"KL Rahul":"https://www.iplt20.com/teams/kings-xi-punjab/squad/1125/kl-rahul",
"Quinton de Kock":"https://www.iplt20.com/teams/mumbai-indians/squad/834/quinton-de-kock",
"Rishabh Pant":"https://www.iplt20.com/teams/delhi-capitals/squad/2972/rishabh-pant",
"MS Dhoni":"https://www.iplt20.com/teams/chennai-super-kings/squad/1/ms-dhoni",
"Parthiv Patel":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/44/parthiv-patel",
"Jos Buttler":"https://www.iplt20.com/teams/rajasthan-royals/squad/509/jos-buttler",
"Dinesh Karthik":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/102/dinesh-karthik",
"Wridhiman Saha":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/16/wriddhiman-saha"},
  
  "bowlers": {"Imran Tahir":"https://www.iplt20.com/teams/chennai-super-kings/squad/898/imran-tahir",
"Kagiso Rabada":"https://www.iplt20.com/teams/delhi-capitals/squad/1664/kagiso-rabada",
"Deepak Chahar":"https://www.iplt20.com/teams/chennai-super-kings/squad/140/deepak-chahar",
"Jasprit Bumrah":"https://www.iplt20.com/teams/mumbai-indians/squad/1124/jasprit-bumrah",
"Khaleel Ahmed":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/2964/khaleel-ahmed",
"Mohammad Shami":"https://www.iplt20.com/teams/kings-xi-punjab/squad/94/mohammad-shami",
"Yuzvendra Chahal":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/111/yuzvendra-chahal",
"Rashid Khan":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/2885/rashid-khan",
"Harbhajan Singh":"https://www.iplt20.com/teams/chennai-super-kings/squad/103/harbhajan-singh",
"Lasith Malinga":"https://www.iplt20.com/teams/mumbai-indians/squad/211/lasith-malinga",
"Ravi Ashwin":"https://www.iplt20.com/teams/delhi-capitals/squad/8/ravichandran-ashwin",
"Rahul Chahar":"https://www.iplt20.com/teams/mumbai-indians/squad/3763/rahul-chahar",
"Ishant Sharma":"https://www.iplt20.com/teams/delhi-capitals/squad/38/ishant-sharma",
"Bhuvaneshwar Kumar":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/116/bhuvneshwar-kumar",
"Chris Morris":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/836/chris-morris",
"Sandeep Sharma":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/1112/sandeep-sharma",
"Amit Mishra":"https://www.iplt20.com/teams/delhi-capitals/squad/30/amit-mishra",
"Jofra Archer":"https://www.iplt20.com/teams/rajasthan-royals/squad/3502/jofra-archer",
"Navdeep Saini":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/3824/navdeep-saini",
"Piyush Chawla":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/76/piyush-chawla"},

   "batsmen":{ "David Warner":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/170/david-warner",
"Shikhar Dhawan":"https://www.iplt20.com/teams/delhi-capitals/squad/41/shikhar-dhawan",
"Chris Gayle":"https://www.iplt20.com/teams/kings-xi-punjab/squad/236/chris-gayle",
"Virat Kohli":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/164/virat-kohli",
"Shreyas Iyer":"https://www.iplt20.com/teams/delhi-capitals/squad/1563/shreyas-iyer",
"AB de Villiers":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/233/ab-de-villiers",
"Suryakumar Yadav":"https://www.iplt20.com/teams/mumbai-indians/squad/108/suryakumar-yadav",
"Chris Lynn":"https://www.iplt20.com/teams/mumbai-indians/squad/179/chris-lynn",
"Rohit Sharma":"https://www.iplt20.com/teams/mumbai-indians/squad/107/rohit-sharma",
"Faf du Plessis":"https://www.iplt20.com/teams/chennai-super-kings/squad/24/faf-du-plessis",
"Ajinkya Rahane":"https://www.iplt20.com/teams/delhi-capitals/squad/135/ajinkya-rahane",
"Suresh Raina":"https://www.iplt20.com/teams/chennai-super-kings/squad/14/suresh-raina",
"Prithvi Shaw":"https://www.iplt20.com/teams/delhi-capitals/squad/3764/prithvi-shaw",
"Manish Pandey":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/123/manish-pandey",
"Nitish Rana":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/2738/nitish-rana",
"Sanju Samson":"https://www.iplt20.com/teams/rajasthan-royals/squad/258/sanju-samson",
"Mayank Agrawal":"https://www.iplt20.com/teams/kings-xi-punjab/squad/158/mayank-agarwal",
"Steve Smith":"https://www.iplt20.com/teams/rajasthan-royals/squad/271/steve-smith",
"Shubhman Gill":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/3761/shubman-gill",
"Ambati Rayudu":"https://www.iplt20.com/teams/chennai-super-kings/squad/100/ambati-rayudu",
"Kane Williamson":"https://www.iplt20.com/teams/sunrisers-hyderabad/squad/440/kane-williamson"},

 "allRounders" : { "Andre Russell":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/177/andre-russell",
"Hardik Pandya":"https://www.iplt20.com/teams/mumbai-indians/squad/2740/hardik-pandya",
"Shane Watson":"https://www.iplt20.com/teams/chennai-super-kings/squad/227/shane-watson",
"Moenn Alli":"https://www.iplt20.com/teams/royal-challengers-bangalore/squad/1735/moeen-ali",
"Keiron Pollard":"https://www.iplt20.com/teams/mumbai-indians/squad/210/kieron-pollard",
"Krunal Pandya":"https://www.iplt20.com/teams/mumbai-indians/squad/3183/krunal-pandya",
"Sunil Narine":"https://www.iplt20.com/teams/kolkata-knight-riders/squad/203/sunil-narine",
"Ben Stokes":"https://www.iplt20.com/teams/rajasthan-royals/squad/1154/ben-stokes",
"Ravindra Jadeja":"https://www.iplt20.com/teams/chennai-super-kings/squad/9/ravindra-jadeja",
"Dwayne Bravo":"https://www.iplt20.com/teams/chennai-super-kings/squad/25/dwayne-bravo",
"Axar Patel":"https://www.iplt20.com/teams/delhi-capitals/squad/1113/axar-patel"}
}

finaldata = dict()

for category in data:
    print()
    print(category)
    finaldata[category] = dict()
        
    for name in data[category]:
        print(name)
        finaldata[category][name] = dict()
        url = data[category][name]

        r = requests.get(url)
        soup = BeautifulSoup(r.content , 'lxml')
        tables = soup.find_all('table' , attrs={'class':'player-stats-table'})
        avlyears = ['2019' , '2018' , '2017']

        if category == "bowlers" or category == "allRounders":
            for tr in tables[1].find_all('tr')[2:5]:
                i = 1
                for td in tr.find_all('td'):
                    if i == 1:
                        year = td.text
                        if year not in avlyears:
                            break
                        else:
                            finaldata[category][name][year] = dict()

                    if i == 2:
                        finaldata[category][name][year]['matches'] = td.text
                    elif i == 5:
                        finaldata[category][name][year]['wickets'] = td.text
                    elif i == 8:
                        finaldata[category][name][year]['economy'] = td.text
                    
                    if i == 6:
                        if category == "allRounders":
                            finaldata[category][name][year]['bowlingAverage'] = td.text
                        else:
                            finaldata[category][name][year]['average'] = td.text

                    i += 1
    
        for tr in tables[0].find_all('tr')[2:5]:
            i = 1
            for td in tr.find_all('td'):
                if category == "bowlers":
                    if i == 1:
                        year = td.text
                        if year not in avlyears:
                            break

                    if i == 13:
                        finaldata[category][name][year]['catches'] = td.text
                else:
                    if i == 1:
                        year = td.text
                        if year not in avlyears:
                            break
                        else:
                            if category != "allRounders":
                                finaldata[category][name][year] = dict()
                    
                    if i == 2:
                        finaldata[category][name][year]['matches'] = td.text
                    elif i == 4:
                        finaldata[category][name][year]['runs'] = td.text
                    elif i == 8:
                        finaldata[category][name][year]['sr'] = td.text
                    elif i == 13:
                        finaldata[category][name][year]['catches'] = td.text

                    if category == "wicketkeepers" and i == 14:
                        finaldata[category][name][year]['stumpings'] = td.text

                    if i == 6:
                        if category == "allRounders":
                            finaldata[category][name][year]['battingAverage'] = td.text
                        else:
                            finaldata[category][name][year]['average'] = td.text

                i += 1

file = open("playerdata.yaml" , 'w')
yaml.dump(finaldata , file)
jsonfile = open("playerdata.json" , 'w')
json.dump(finaldata , jsonfile , indent = 4)
print(finaldata)