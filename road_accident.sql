
-- -------------------------------------------------------------
-- Road Accident Analysis Database Setup
-- -------------------------------------------------------------

CREATE DATABASE IF NOT EXISTS road_accident_analysis;
USE road_accident_analysis;

-- -------------------------------------------------------------
-- Table Structure
-- -------------------------------------------------------------

CREATE TABLE IF NOT EXISTS road_accident (
    Accident_Index VARCHAR(20),
    Vehicle_Type VARCHAR(50),
    Urban_or_Rural_Area VARCHAR(20),
    Light_Conditions VARCHAR(20),
    Road_Type VARCHAR(50),
    Day_of_Week VARCHAR(20),
    Weather_Conditions VARCHAR(50),
    Casualties INT,
    Severity VARCHAR(20),
    Accident_Year INT
);

-- -------------------------------------------------------------
-- Load Data from CSV
-- -------------------------------------------------------------

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/road_accident.csv'
INTO TABLE road_accident
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Accident_Index, Vehicle_Type, Urban_or_Rural_Area, Light_Conditions, Road_Type,
 Day_of_Week, Weather_Conditions, Casualties, Severity, Accident_Year);

-- -------------------------------------------------------------
-- Sample Data Inserts
-- -------------------------------------------------------------

INSERT INTO road_accident VALUES
('A001', 'Car', 'Urban', 'Day', 'Single Carriageway', 'Friday', 'Fine', 3, 'Slight', 2022),
('A002', 'Bike', 'Rural', 'Night', 'Dual Carriageway', 'Saturday', 'Rain', 1, 'Serious', 2022),
('A003', 'Bus', 'Urban', 'Day', 'Roundabout', 'Monday', 'Fine', 5, 'Slight', 2022),
('A004', 'Van', 'Urban', 'Night', 'One Way Street', 'Wednesday', 'Snow', 2, 'Serious', 2021),
('A005', 'Car', 'Rural', 'Day', 'Single Carriageway', 'Thursday', 'Fine', 4, 'Slight', 2022),
('A006', 'Bike', 'Urban', 'Night', 'Slip Road', 'Sunday', 'Fog', 1, 'Fatal', 2021),
('A007', 'Bus', 'Rural', 'Day', 'Dual Carriageway', 'Tuesday', 'Fine', 3, 'Slight', 2022),
('A008', 'Van', 'Urban', 'Day', 'Single Carriageway', 'Friday', 'Rain', 2, 'Serious', 2022),
('A009', 'Car', 'Urban', 'Night', 'Roundabout', 'Saturday', 'Fine', 1, 'Slight', 2022),
('A010', 'Bike', 'Rural', 'Day', 'Single Carriageway', 'Monday', 'Fine', 2, 'Fatal', 2021);

-- -------------------------------------------------------------
-- Analytical Queries
-- -------------------------------------------------------------

-- 1. Total accidents and casualties (Current Year)
SELECT Accident_Year, COUNT(*) AS Total_Accidents, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Accident_Year;

-- 2. Casualties by Vehicle Type
SELECT Vehicle_Type, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Vehicle_Type
ORDER BY Total_Casualties DESC;

-- 3. Casualties by Area Type
SELECT Urban_or_Rural_Area, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Urban_or_Rural_Area;

-- 4. Casualties by Light Conditions
SELECT Light_Conditions, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Light_Conditions;

-- 5. Casualties by Road Type
SELECT Road_Type, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Road_Type;

-- 6. Casualties by Day of Week
SELECT Day_of_Week, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Day_of_Week;

-- 7. Casualties by Severity
SELECT Severity, COUNT(*) AS Total_Accidents, SUM(Casualties) AS Total_Casualties
FROM road_accident
GROUP BY Severity;

-- -------------------------------------------------------------
-- End of Script
-- -------------------------------------------------------------
