# Macro CMF

# Project as a part of my Center of Mathematical Finance program.

The goal is to determine macro factors that affect the price of the US Crude Oil. 
Research tests several hypotheses including the one that there is no such dependence.  

Data used is from the International Monetary Fund.


![alt text](https://acyhk.com/images/products/products-commodities-banner-image.jpg)



### Code:
- Part 1.0 presents a way to modify parsed data and adjust it to special project conditions and structure. As well as choosing key features that affect our target.

- Part 1.1 improves previous one and uses LassoChoosingTeam.py.

- Part 2.0 leverages the features with lightgbm, regression tests (such as F-test, T-test), includes Linear Regression, Boosting.

- Part 2.1 Seasonality and trends of data, as well as lagging. Also include previously used predictive models.

- LassoChoosingTeam.py is an individual file that implements Lasso Linear Model, which helps defining most relevant features.


### Data:
- PCPS_12-10-2022 20-33-48-66_timeSeries.csv - Orignal IMF data.
- commodities.csv - converted IMF data.
- commodities_with_date.csv - slightly different version of the privious one.


:shipit:
