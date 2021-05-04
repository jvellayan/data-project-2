# commands to run in docker
# create database 
create database project2;

# switch to specific database
use project2;


# create table
CREATE TABLE final ( 
	factor INT, 
	pi DECIMAL (50,25), 
	time DATETIME, 
PRIMARY KEY (factor)  );

# after uploading everything to the table, view entire 
SELECT * FROM final;

# Analysis

# pi only commands
SELECT AVG(pi) FROM final;
SELECT MIN(pi) FROM final;
SELECT MAX(pi) FROM final;
SELECT DISTINCT pi from final;
SELECT STD(pi) FROM final;
SELECT VARIANCE(pi) FROM final;
SELECT POWER(pi,(1/3)) FROM final;

# factor only commands
SELECT AVG(factor) FROM final;
SELECT MIN(factor) FROM final;
SELECT MAX(factor) FROM final;
SELECT DISTINCT factor from final;
SELECT STD(factor) FROM final;
SELECT VARIANCE(factor) FROM final;
SELECT POWER(factor,(1/3)) FROM final;

#joint commands
SELECT factor,pi FROM final ORDER BY pi DESC;
SELECT factor/pi FROM final; 
SELECT pi/factor FROM final;
SELECT pi*factor FROM final;
SELECT power(factor, (1/pi)) FROM final;
