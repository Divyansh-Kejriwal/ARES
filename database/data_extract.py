import json
import mysql.connector

con = mysql.connector.connect(host="localhost", user="devuser", passwd="MySecurePassword123!", database="CASES")
cur = con.cursor()

with open("data/raw/yosar_missing.geojson", "r") as file:
    data = json.load(file)


for i in range(1,213):
    case = data["features"][i]["properties"]
    # 8, 5, 6, 14, 15, 16, 17, 19, 20,21, 22, 23
    info = (str(case["SARNumber"]),case["Lat"], case["Long"], str(case["ContactMet"]), str(case["EcoRegionD"]), str(case["EcoRegio_1"]), str(case["IncidType"]), str(case["GroupDynam"]), str(case["SubjectCat"]), str(case["SubSex"]), case["SubAge"])
    cur.execute("INSERT INTO Case_info (YOSARID, Latitude, Longitude, ContactMethod, EnvRegion, EnvRegionCode, IncidentType, GroupDynamics, SubjectCategory, Subsex, SubAge) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)",(info))
    con.commit()
con.close()
