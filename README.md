# Alphavantage_Stock_Daata
To extract Intra day Data from alphavantage

Variables
1.year - Year you want to start scrapping the data from
2.month - Month you want to ingest data from
3.api_key - API Key generated from  'https://www.alphavantage.co/'
4.symbol - NASDAQ/NYSE trading Symbol


The script will scrape data data from the year and month passed in the inital variables and will scrape till current year and month
If a Free API is used there will be a pause of 1.30 mins and to job will stop after 100 api calls due to free api limit
If premium API is used no halts in middle

Data will be stored in a CSV file and that CSV file can be used for excel analysis or used for ML usinf spark or pandas 
