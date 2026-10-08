import json
import mysql.connector
from datetime import datetime


def null_if_missing(value):
    return None if value is None else value


con = mysql.connector.connect(
    host="localhost",
    user="devuser",
    passwd="MySecurePassword123!",
    database="CASES"
)

cur = con.cursor()


with open("data/raw/yosar_missing.geojson", "r") as file:
    data = json.load(file)


for i in range(len(data["features"])):

    case = data["features"][i]["properties"]

    # Required fields
    if (
        case["CaseNumber"] is None
        or case["Lat"] is None
        or case["Long"] is None
        or case["SubjectCat"] is None
        or case["EcoRegio_1"] is None
        or case["EcoRegionD"] is None
    ):
        print(f"Skipping case {case.get('CaseNumber')}: missing required data")
        continue

    # Convert Unix timestamp (milliseconds) to Python datetime
    last_seen_time = (
        datetime.fromtimestamp(case["DateTimeLa"] / 1000)
        if case["DateTimeLa"] is not None
        else None
    )

    incident_reported = (
        datetime.fromtimestamp(case["DateTimeIn"] / 1000)
        if case["DateTimeIn"] is not None
        else None
    )

    info = (
        case["CaseNumber"],
        case["Lat"],
        case["Long"],
        null_if_missing(case["IPP_GR_Not"]),
        null_if_missing(case["Intended_D"]),
        last_seen_time,
        incident_reported,
        null_if_missing(case["SubAge"]),
        null_if_missing(case["SubSex"]),
        case["SubjectCat"],
        null_if_missing(case["GroupDynam"]),
        null_if_missing(case["IncidType"]),
        case["EcoRegio_1"],
        case["EcoRegionD"]
    )

    cur.execute(
        """
        INSERT INTO case_info (
            YOSARID,
            initial_latitude,
            initial_longitude,
            last_known_location_description,
            intended_destination,
            last_seen_time,
            incident_reported,
            age,
            sex_group_sex,
            person_type,
            group_dynamics,
            incident_type,
            ecoregion,
            ecoregion_code
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s
        )
        """,
        info
    )


con.commit()

cur.close()
con.close()

print("Import completed successfully.")