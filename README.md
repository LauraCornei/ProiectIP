# Recommendations API

## Response structure

The structure of the API responses' body is as follows:

-   for successful responses, a JSON object containing the properties:
    -   `success`: `true`
    -   `data`: An object, structure detailed for each route below.
-   for unsuccessful responses, a JSON object containing the
    properties:
    -   `success`: `false`
    -   `error`: An object containing a `message` property, and sometimes additional helpful properties.

All the routes below are protected by a token. This is required in order to obtain <customer_id>, the id of a customer which should be the 24-character hex-string corresponding to the `clientId`.
	
## /recommendations/restaurant

### GET

Recommends for <customer_id> a restaurant based on the reviews made by the other customers. 

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
`http://127.0.0.1:5000/recommendations/restaurant`
`token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWIxNmZkZjRhZmJmNjU0OTY2Y2I2OGQiLCJpYXQiOjE1ODgyMzc0NTZ9.OG3o5XPIDDGlyFusinKVN11w27b5JYCSwLMl9XhYHeI`
 
**Returned data example**:

```JSON
[
    {
        "role": "Provider",
        "confirmed": true,
        "_id": "5eb175094afbf654966cb690",
        "name": "Gimmy Restaurant",
        "email": "gimmy_restaurant@gmail.com",
        "__v": 1,
        "emailToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWIxNzUwOTRhZmJmNjU0OTY2Y2I2OTAiLCJpYXQiOjE1ODg2ODgxMzd9.Pea0iTISyAny4IEluMMcvZxrbODpTRheIjhy88yK4tg",
        "details": {
            "location": {
                "latitude": 53.5,
                "longitude": 43.2
            },
            "images": [
                "https://d2fdt3nym3n14p.cloudfront.net/venue/1360/gallery/3022/conversions/sole8-big.jpg",
                "https://d2fdt3nym3n14p.cloudfront.net/venue/1360/gallery/3023/conversions/sole3-big.jpg"
            ],
            "specials": [
                "pizza",
                "pasta"
            ],
            "commandsQueue": [
                "",
                "cccccccccccc",
                "5ead3934340c241a2014b4b8",
                "5ead4f803f29fe06b727b88a"
            ],
            "reservationsQueue": [
                "",
                "bbbbbbbbbbbb",
                "5ead38cf340c241a2014b4b7"
            ],
            "_id": "5eb17a5b251c5187bd97251a",
            "userId": "5eb175094afbf654966cb690",
            "CUI": "ER563KIDO34",
            "__v": 0,
            "description": "A place with good food and nice vibes.",
            "priceCategory": "Medium",
            "rating": 4.5,
            "capacity": 57,
            "type": "Canteen",
            "menu": {
                "_id": "5eb17a5c251c5187bd97253d",
                "providerId": "5eb17a5b251c5187bd97251a",
                "__v": 0,
                "courses": [
                    {
                        "category": [
                            "pizza"
                        ],
                        "ingredients": [
                            "onion",
                            "salami",
                            "mushrooms",
                            "eggs",
                            "cheese"
                        ],
                        "allergenes": [
                            "eggs",
                            "milk"
                        ],
                        "_id": "5eb17a5c6f436666294bc420",
                        "name": "house pizza",
                        "price": 30,
                        "image": "https://img.favpng.com/7/18/21/shashlik-pizza-dish-main-course-restaurant-png-favpng-6qHVKG4NM94QxrdHUWzwj75y5.jpg"
                    },
                    {
                        "category": [
                            "pasta"
                        ],
                        "ingredients": [
                            "onion",
                            "salami",
                            "tomatoes",
                            "eggs",
                            "cheese"
                        ],
                        "allergenes": [
                            "eggs",
                            "milk"
                        ],
                        "_id": "5eb17a5c6f436666294bc421",
                        "name": "house pasta",
                        "price": 25,
                        "image": "https://img.favpng.com/7/18/21/shashlik-pizza-dish-main-course-restaurant-png-favpng-6qHVKG4NM94QxrdHUWzwj75y5.jpg"
                    }
                ]
            },
            "schedule": {
                "_id": "5eb17a5c251c5187bd972551",
                "providerId": "5eb17a5b251c5187bd97251a",
                "__v": 0,
                "schedule": [
                    {
                        "_id": "5eb17a5c6f436666294bc422"
                    }
                ]
            },
            "id": "5eb17a5b251c5187bd97251a"
        },
        "id": "5eb175094afbf654966cb690"
    }
]
```

## /recommendations/asd/<restaurant_id>


### GET

Recommends for <customer_id> a dish from <restuarant_id>.

**URL parameter**:

The ID of the restaurant should be specified in the URL:  
`.../recommendations/asd/5e9494aadd757435187a6dbd`  
The <restaurant_id> should be the 24-character hex-strings corresponding to the `providerId`.

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/asd/5e9494aadd757435187a6dbd`
 `token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZThjNGYzNTE4NDJiYTMyMmM1YzEzZWMiLCJpYXQiOjE1ODgyMzc0NTZ9.pMNWm-7sQNgGM7EDQPdaSFX8a7eZSRWkzEJlD0BYMms`
 
**Returned data example**:

```JSON
{
    "success": true,
    "data": {
    []
    }
}
```

## /recommendations/food/<restaurant_id>

### GET

Recommends for <restaurant_id> new dishes to offer to its customers.

**URL parameter**:

The ID of the restaurant should be specified in the URL:  
`.../recommendations/food/5eb16d673a637d28884dc226`  
The <restaurant_id> should be the 24-character hex-string corresponding to the `providerId`.

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/food/5eb16d673a637d28884dc226`

**Returned data example**:

```JSON
{
    "success": true,
    "data": {
        []
    }
}
```

## /recommendations/restaurant_by_food

### GET

Recommends for <customer_id> a list of <=10 restaurants that have at least one speciality in common with one of the restaurants preferred by <customer_id>(id est, one that has received a score>5).

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
`http://127.0.0.1:5000/recommendations/restaurant_by_food`
`token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWIxNmZkZjRhZmJmNjU0OTY2Y2I2OGQiLCJpYXQiOjE1ODgyMzc0NTZ9.OG3o5XPIDDGlyFusinKVN11w27b5JYCSwLMl9XhYHeI`


**Returned data example**:

```JSON
{
  "success": "true",
  "data": [
    {
      "role": "Provider",
      "confirmed": true,
      "_id": "5eb175094afbf654966cb690",
      "name": "Gimmy Restaurant",
      "email": "gimmy_restaurant@gmail.com",
      "__v": 1,
      "emailToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWIxNzUwOTRhZmJmNjU0OTY2Y2I2OTAiLCJpYXQiOjE1ODg2ODgxMzd9.Pea0iTISyAny4IEluMMcvZxrbODpTRheIjhy88yK4tg",
      "details": {
        "location": {
          "latitude": 53.5,
          "longitude": 43.2
        },
        "images": [
          "https://d2fdt3nym3n14p.cloudfront.net/venue/1360/gallery/3022/conversions/sole8-big.jpg",
          "https://d2fdt3nym3n14p.cloudfront.net/venue/1360/gallery/3023/conversions/sole3-big.jpg"
        ],
        "specials": [
          "pizza",
          "pasta"
        ],
        "commandsQueue": [
          "",
          "cccccccccccc",
          "5ead3934340c241a2014b4b8",
          "5ead4f803f29fe06b727b88a"
        ],
        "reservationsQueue": [
          "",
          "bbbbbbbbbbbb",
          "5ead38cf340c241a2014b4b7"
        ],
        "_id": "5eb17a5b251c5187bd97251a",
        "userId": "5eb175094afbf654966cb690",
        "CUI": "ER563KIDO34",
        "__v": 0,
        "description": "A place with good food and nice vibes.",
        "priceCategory": "Medium",
        "rating": 4.5,
        "capacity": 57,
        "type": "Canteen",
        "menu": {
          "_id": "5eb17a5c251c5187bd97253d",
          "providerId": "5eb17a5b251c5187bd97251a",
          "__v": 0,
          "courses": [
            {
              "category": [
                "pizza"
              ],
              "ingredients": [
                "onion",
                "salami",
                "mushrooms",
                "eggs",
                "cheese"
              ],
              "allergenes": [
                "eggs",
                "milk"
              ],
              "_id": "5eb17a5c6f436666294bc420",
              "name": "house pizza",
              "price": 30,
              "image": "https://img.favpng.com/7/18/21/shashlik-pizza-dish-main-course-restaurant-png-favpng-6qHVKG4NM94QxrdHUWzwj75y5.jpg"
            },
            {
              "category": [
                "pasta"
              ],
              "ingredients": [
                "onion",
                "salami",
                "tomatoes",
                "eggs",
                "cheese"
              ],
              "allergenes": [
                "eggs",
                "milk"
              ],
              "_id": "5eb17a5c6f436666294bc421",
              "name": "house pasta",
              "price": 25,
              "image": "https://img.favpng.com/7/18/21/shashlik-pizza-dish-main-course-restaurant-png-favpng-6qHVKG4NM94QxrdHUWzwj75y5.jpg"
            }
          ]
        },
        "schedule": {
          "_id": "5eb17a5c251c5187bd972551",
          "providerId": "5eb17a5b251c5187bd97251a",
          "__v": 0,
          "schedule": [
            {
              "_id": "5eb17a5c6f436666294bc422"
            }
          ]
        },
        "id": "5eb17a5b251c5187bd97251a"
      },
      "id": "5eb175094afbf654966cb690"
    }
  ]
}
```


## /recommendations/stats/food_per_restaurant/<restaurant_id>

### GET

Returns a svg with the number of orders for every dish from <restaurant_id>.

**URL parameter**:

The ID of the restaurant should be specified in the URL:  
`.../recommendations/stats/food_per_restaurant/5eb16d673a637d28884dc226?...`  
The <restaurant_id> should be the 24-character hex-string corresponding to the `providerId`.

**Query parameters**:

-   order - asc/desc(after which the orders count for each dish is displayed)
-   show_count - int(how many dishes are shown)
-   token 

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  

`http://127.0.0.1:5000/recommendations/stats/food_per_restaurant/5eb16d673a637d28884dc226?order=asc&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/f1.svg?raw=true)

## /recommendations/stats/food_all_restaurants

### GET

Returns a svg with the number of orders for every dish from all the restaurants.

**Query parameters**:

-   order - asc/desc(after which the orders count for each dish is displayed)
-   show_count - int(how many dishes are shown)

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/stats/food_all_restaurants?order=asc&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/f2.svg?raw=true)

## /recommendations/stats/orders_per_hour

### GET

Returns a svg with the number of orders per hour for all restaurants.

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/stats/orders_per_hour?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/o1.svg?raw=true)

## /recommendations/stats/orders_per_hour/<restaurant_id>

### GET

Returns a svg with the number of orders per hour for <restaurant_id>.

**URL parameter**:

The ID of the restaurant should be specified in the URL:  
`.../recommendations/stats/orders_per_hour/5eb16d673a637d28884dc226?...`  
The <restaurant_id> should be the 24-character hex-string corresponding to the `providerId`.

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/stats/orders_per_hour/5eb16d673a637d28884dc226?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/o2.svg?raw=true)

## search/restaurant/<restaurant_prefix>

### GET

Returns for <customer_id> the name of the restaurant that matches <restaurant_prefix> based on different criteria such as the number of reviews/orders that have been received.

**URL parameters**:

The restaurant prefix should be specified in the URL:  
`.../search/restaurant/Rest`  
The <restaurant_prefix> should be a valid prefix of the string corresponding to the `name` associated to a `providerId`.

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
`http://127.0.0.1:5000/search/restaurant/Rest`
`token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZThjNGYzNTE4NDJiYTMyMmM1YzEzZWMiLCJpYXQiOjE1ODgyMzc0NTZ9.pMNWm-7sQNgGM7EDQPdaSFX8a7eZSRWkzEJlD0BYMms`

 
**Returned data example**:

```JSON
{
  "name_recommended_restaurant": "Recommendation starting with given prefix not found"
}
```
