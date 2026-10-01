# ARES - A System for finding people who went missing

This is a python  project the collects data of missing people from open source websites and with the help of mathematical models tries to find the optimal location that is best for finding the person. It optimizes for the best results as to minimizing the searching cost and by terrain.

---

## Structure of the Program

The program is majorly divided into 5 core steps. It is given below

1. Extracting data from the websites.
2. Storing data in a build in database.
3. Calculating the probability of finding a person based on the provided information.
4. Optimizing the engine to save on costing, manual labour, time and probability.
5. Displaying the output into a understandable visual output making it easier for experts as well as non-experts for understand the data.

---

## Structure of the modules with useage

### 1. DATABASE - CASES

It would contain all the nessary information for the cases of different people. It is divided majorly into 3 tables.

1. **TableInformation** - It contains all the fields categorized into essestial for the case and non-essential for the case. It also contains a third category named model features which has other data that can pe used for making even finer prediction about a persons information.

2. **CaseInformation** - It contains all the basic information regarding a specific case such as case_id, name, image, status, last_known_location, missing_from, inital_destination.
3. **Observations** - This table helps the core models for making predictions it is the list of all the observations for a case making it escpically usefull it contains fields like observation_id, case_id, timestamps, location, observation_type, value, reliability and source.
