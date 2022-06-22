# Surfs_Up 

## Overview


The purpose is to analysis the provided metrological data, which had been stored in a SQLite database(.sqlte), to prove to investors that opening a Surf n’ Shake shop in Hawaii would be a wise investment opportunity. The store would sell/rent surf boards accompanied by a cold sweet delightful ice cream, year-round. The issue at hand is the investors fear the lack of success, as they have invested in similar business, which failed due to weather. In order to convince the investors, the data needs to prove the weather won’t have a detrimental impact on the business. 


The provided data (hawaii.sqlite) was stored in a SQLite database and in order to create queries from the data, for our purposes we used, SQLAlchemy. After importing the SQLAlchemy dependencies in Jupyter notebook and pulling the data from the database Flask was used to depict the results. When flask was run in the terminal a web address was provided http://127.0.0.1:5000 . 

(image web_link)


## Results 

There are two months that will be extrapolated on, June and December, as those months would give the most information for summer and winter. 

Images ( June temp and precipitation descriptions )
Images (December temp and precipitation descriptions)


* The data between the 2 months are fairly similar in that they have an average temperature around 75˚F (June) and 71˚F (December). Since the temperature   
  has a slight difference, it shows consistency throughout the year (across seasons).  The weather doesn’t show massive fluctuation throughout the year 
  like NYC, where its 88˚F during June and 44˚F in December. 
  
     * While the temperatures show slight variance in degree, December has a higher average precipitation of 0.217 inches compared to that of June which 
       is on average 0.136 inches. 

* The minimum temperature shows the largest gap between December (56˚F) and June (64˚F). These lower temperatures aren’t ideal for ice cream and/or surfing. When thinking of the lower temperatures their clientele needs to be taken into account. Will most of the clientele be guests or avid surfers? Guest may not feel comfortable surfing in colder weather or may not have the appropriate wet suit to accommodate the difference in water temperature. 
  
   * The same applies to the maximum precipitation, if it’s raining up to 6 inches in December and 4 inches in June, will people feel comfortable to surf    
     in those conditions. While the precipitation isn’t normal for neither month, the odd day of immense rainfall may prove to hurt the business 
     on those days. 
          
*	The frequency of the temperatures in June remains constant between 70-80˚F, which is weather many people would deem “beach weather”.  The frequency of 
  December temperatures seems to be around 67- 76˚F, which is not radically different that June. During December 71˚F seems to be the most frequent 
  temperature, which is only 4˚F different from the average temperature of June.  
  
*	An additional query provided, via scatterplot, shows the correlation between the temperature and precipitation. As the temperature increases the amount 
  of precipitation decreases, in both graphs. In both the graphs the odds of the precipitation being more than 3 inches is incredibly uncommon, but 
  possible. The scatterplot proves the precipitation and temperature, throughout the year,  wouldn’t have a detrimental impact on the success of the shop, 
  as many people would continue to flutter in! 


## Summary 


Since the initial concern with the investors had been from previous investments and their failure to thrive due to the weather, that isn’t the case with this shop in Hawaii. The temperatures are consistent year- round along with the amount of precipitation. The difference between the 2 months (and seasons) are miniscule: their occasional low temperatures and high precipitation amount will negatively impact the business, but not on a large scale. Opening a Surf n’ Shake in Hawaii year-round would be a great investment!
