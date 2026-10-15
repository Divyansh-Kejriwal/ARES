USE CASES;
CREATE TABLE Case_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    YOSARID VARCHAR(10) NOT NULL,
    initial_latitude DECIMAL(10, 8) NOT NULL,
    initial_longitude DECIMAL(11, 8) NOT NULL,
    last_known_location_description TEXT,
    intended_destination VARCHAR(255),
    last_seen_time DATETIME,
    incident_reported DATETIME,
    age INT,
    sex_group_sex VARCHAR(50),
    person_type VARCHAR(100) NOT NULL,
    group_dynamic VARCHAR(255),
    incident_type VARCHAR(100),
    ecoregion VARCHAR(255) NOT NULL,
    ecoregion_code VARCHAR(50) NOT NULL
);