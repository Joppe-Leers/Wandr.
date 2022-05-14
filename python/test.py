from tokenize import String
import populartimes
import csv

count = 0
db = populartimes.get("AIzaSyBFB_MsLRj07vAoNqD92rqKEt-k5s2hbDg",["point_of_interest"],(50.868614, 4.669696),(50.898708, 4.730951))
print(db)
with open('day_snapshot.txt', 'w', encoding="utf-8") as f:
    for x in db:
        #name = db[count]["name"]
        lat = db[count]["coordinates"]["lat"]
        lng = db[count]["coordinates"]["lng"]
        busylvl = db[count]['populartimes'][2]['data']
        f.write(str(lat) + " " + str(lng) + " ")
        count2 = 0
        for h in busylvl:
            f.write(str(busylvl[count2]) + " ")
            count2 = count2 + 1
        count = count + 1
        f.write("\n")


