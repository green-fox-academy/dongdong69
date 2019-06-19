# Real-estate Project
---
Requement:

- build a simple engine that helps home owners assess the value of their property. The engine will use a machine learning algorithm to determine the final figure.

- To be more specific, you want to build this pilot phase for homeowners in the county of *Somerset, United Kingdom*.
## Plan
---
1. Get the dataset(day01).
2. Understanding the data(day01).
3. Clean the data(data preporcessing, day02).
4. Train and test your data(day03).
5. Interface(day04).
6. What else I can do(day05):
- Data visualization?
- nlp?
- computer version?

## Dataset
---
- [gov.uk](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads)
Do not have enhough information.
<br />
- [Zoopla](https://developer.zoopla.co.uk/)
<br />
It is a good api for our project.
<br />

Which contaions:
<br />
- country : The country of the house
- county : The county(somerset)
- street
- post_town
- out_code : With the street name, post town and out_code we can find the house.
- dersription : Dersrip how is the house looks like.
- details of rooms : How many bedroom, floors, recepts, bathroom
- latitude
- longitude : With the latitude and longitude we can findout the spercific loc of the house.
- new_home : Is it new?
- price : The price of the house.

<br />
- url = http://api.zoopla.co.uk/api/v1/property_listings.js?zed_index=?&include_sold=1&page_number=1&listing_status=sale&page_size=10&order_by=age&area=somerset&api_key=jwttfkz79asz2d9h8sms7tuu



## Data Preporcessing
---
- Pick out the useful information
- one-hot encode
Using one-hot encode function to encode 'out_code', 'post_town' and 'street'

## Data Visualization
---
- map
Using map shows the price of different area.

## Data Modeling
---
- Regression
- neural network
- decision tree
- nlp --> description

## Data Analysis
---


## Thanks
---
![image](powered-by-zoopla.png)
