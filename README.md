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

## /recommendations/food-for-restaurant/<restaurant_id>

### GET

Recommends for <customer_id> dishes from <restuarant_id>.

**URL parameter**:

The ID of the restaurant should be specified in the URL:  
`.../recommendations/food-for-restaurant/5e9494aadd757435187a6dbd`  
The <restaurant_id> should be the 24-character hex-strings corresponding to the `providerId`.

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/food-for-restaurant/5ebcf11126e32517c46effff`
 
**Returned data example**:

```JSON
{
    "success": "true",
    "data": [
        [
            {
                "_id": "5ebcf37226e32517c46f0058",
                "name": "Barbecue Ribs",
                "category": [],
                "price": 17,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/04/Palak-Paneer-PTR.jpg",
                "ingredients": [
                    "Avocado Spread",
                    "Cornichons",
                    "File Powder",
                    "Pork",
                    "Longan"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f0054",
                "name": "Pasta Carbonara",
                "category": [],
                "price": 21,
                "image": "http://picturetherecipe.com/wp-content/uploads/2018/06/Bombay-Green-Chutney-Sandwich-PictureTheRecipe.jpg",
                "ingredients": [
                    "Potatoes",
                    "Buckwheat",
                    "Artichoke",
                    "Radish"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f0056",
                "name": "Bruschette with Tomato",
                "category": [],
                "price": 34,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Firecracker-Shrimp-small1.jpg",
                "ingredients": [
                    "Hummus",
                    "Currants",
                    "Chives"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f0055",
                "name": "Seafood Paella",
                "category": [],
                "price": 34,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Shepherds-Pie-Final-small.jpg",
                "ingredients": [
                    "Mastic",
                    "Warehou",
                    "Annatto Seed",
                    "Asian Noodles"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f003a",
                "name": "Philadelphia Maki",
                "category": [],
                "price": 32,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/04/Palak-Paneer-PTR.jpg",
                "ingredients": [
                    "Enoki Mushrooms",
                    "Anchovies",
                    "Honey",
                    "Green Tea Noodles"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f0039",
                "name": "Kebab",
                "category": [],
                "price": 27,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Shepherds-Pie-Final-small.jpg",
                "ingredients": [
                    "Peaches",
                    "Lamb",
                    "Butternut Pumpkin"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f0059",
                "name": "Meatballs with Sauce",
                "category": [],
                "price": 16,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/01/Rogan-Josh-by-PictureTheRecipe.jpg",
                "ingredients": [
                    "Fish Stock",
                    "Green Tea",
                    "Asian Noodles"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f003c",
                "name": "Cauliflower Penne",
                "category": [],
                "price": 31,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Firecracker-Shrimp-small1.jpg",
                "ingredients": [
                    "Nashi Pear",
                    "Malt Vinegar",
                    "Butternut Pumpkin",
                    "Cinnamon",
                    "Rye"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f0052",
                "name": "Pork Sausage Roll",
                "category": [],
                "price": 28,
                "image": "http://picturetherecipe.com/wp-content/uploads/2017/09/Hay-Js-Bistro-Review-Rack-of-Lamb-by-PictureTheRecipe.jpg",
                "ingredients": [
                    "Rice Syrup",
                    "Oat Flour",
                    "Guava"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36e26e32517c46f0037",
                "name": "Philadelphia Maki",
                "category": [],
                "price": 23,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/04/Palak-Paneer-PTR.jpg",
                "ingredients": [
                    "Enoki Mushrooms",
                    "Anchovies",
                    "Honey",
                    "Green Tea Noodles"
                ],
                "allergenes": []
            }
        ]
    ]
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
 `http://127.0.0.1:5000/recommendations/food/5ebcf11126e32517c46effff`

**Returned data example**:

```JSON
{
    "success": "true",
    "data": [
        [
            {
                "_id": "5ebcf36f26e32517c46f0039",
                "name": "Kebab",
                "category": [],
                "price": 27,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Shepherds-Pie-Final-small.jpg",
                "ingredients": [
                    "Peaches",
                    "Lamb",
                    "Butternut Pumpkin"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f003a",
                "name": "Philadelphia Maki",
                "category": [],
                "price": 32,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/04/Palak-Paneer-PTR.jpg",
                "ingredients": [
                    "Enoki Mushrooms",
                    "Anchovies",
                    "Honey",
                    "Green Tea Noodles"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f003c",
                "name": "Cauliflower Penne",
                "category": [],
                "price": 31,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Firecracker-Shrimp-small1.jpg",
                "ingredients": [
                    "Nashi Pear",
                    "Malt Vinegar",
                    "Butternut Pumpkin",
                    "Cinnamon",
                    "Rye"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f005d",
                "name": "Pappardelle alla Bolognese",
                "category": [],
                "price": 22,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Firecracker-Shrimp-small1.jpg",
                "ingredients": [
                    "Limes",
                    "Cucumber",
                    "Hot Smoked Salmon",
                    "Hummus",
                    "Kenchur"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f005b",
                "name": "Kebab",
                "category": [],
                "price": 23,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Shepherds-Pie-Final-small.jpg",
                "ingredients": [
                    "Peaches",
                    "Lamb",
                    "Butternut Pumpkin"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf37226e32517c46f005c",
                "name": "Chicken Fajitas",
                "category": [],
                "price": 15,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/01/Football-Pizza-Pockets-Final-2-small-.jpg",
                "ingredients": [
                    "Potatoes",
                    "Peaches",
                    "Radish"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f003d",
                "name": "Tacos",
                "category": [],
                "price": 19,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/01/Chicken-65-Wings-Indian-Masala-Wings-PictureTheRecipe.jpg",
                "ingredients": [
                    "Kokam",
                    "Shark",
                    "Polenta",
                    "Corn Syrup",
                    "Rice Syrup"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36e26e32517c46f0037",
                "name": "Philadelphia Maki",
                "category": [],
                "price": 23,
                "image": "http://picturetherecipe.com/wp-content/uploads/2020/04/Palak-Paneer-PTR.jpg",
                "ingredients": [
                    "Enoki Mushrooms",
                    "Anchovies",
                    "Honey",
                    "Green Tea Noodles"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36f26e32517c46f003b",
                "name": "Seafood Paella",
                "category": [],
                "price": 18,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Shepherds-Pie-Final-small.jpg",
                "ingredients": [
                    "Mastic",
                    "Warehou",
                    "Annatto Seed",
                    "Asian Noodles"
                ],
                "allergenes": []
            }
        ],
        [
            {
                "_id": "5ebcf36e26e32517c46f0033",
                "name": "Kebab",
                "category": [],
                "price": 24,
                "image": "http://picturetherecipe.com/wp-content/uploads/2012/07/Shepherds-Pie-Final-small.jpg",
                "ingredients": [
                    "Peaches",
                    "Lamb",
                    "Butternut Pumpkin"
                ],
                "allergenes": []
            }
        ]
    ]
}
```

## /recommendations/restaurant-by-food

### GET

Recommends for <customer_id> a list of <=10 restaurants that have at least one speciality in common with one of the restaurants preferred by <customer_id>(id est, one that has received a score>6).

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
`http://127.0.0.1:5000/recommendations/restaurant-by-food`

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


## /recommendations/stats/food-per-restaurant/<restaurant_id>

### GET

Returns a svg with the number of orders for every dish from <restaurant_id>.

**URL parameter**:

The ID of the restaurant should be specified in the URL:  
`.../recommendations/stats/food-per-restaurant/5eb16d673a637d28884dc226?...`  
The <restaurant_id> should be the 24-character hex-string corresponding to the `providerId`.

**Query parameters**:

-   order - asc/desc(after which the orders count for each dish is displayed)
-   show_count - int(how many dishes are shown)
-   token 

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  

`http://127.0.0.1:5000/recommendations/stats/food-per-restaurant/5ebcf11126e32517c46effff?order=asc&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/f1.svg?raw=true)

## /recommendations/stats/food-all-restaurants

### GET

Returns a svg with the number of orders for every dish from all the restaurants.

**Query parameters**:

-   order - asc/desc(after which the orders count for each dish is displayed)
-   show_count - int(how many dishes are shown)
-   token

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/stats/food-all-restaurants?order=asc&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/f2.svg?raw=true)

## /recommendations/stats/orders-per-hour

### GET

Returns a svg with the number of orders per hour for all restaurants.

**Query parameter**:

-   token

**Return codes**:

-   200 - OK
-   400 - There was a problem fetching data

**Usage example**:  
 `http://127.0.0.1:5000/recommendations/stats/orders-per-hour?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI1ZWFhOTQ2ODMwYThmMTI5OGQ0ZmMyZjgiLCJpYXQiOjE1ODgyMzc0NTZ9.Ll2HDuN79KKWr5OoQTiZVWBemyDqdo3kDz74Bvi6lOA`

**Returned data example**:

![alt text](https://github.com/killagann/ran/blob/master/o1.svg?raw=true)

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
`http://127.0.0.1:5000/search/restaurant/R`

**Returned data example**:

```JSON
{
  "success": "true",
  "data": {
    "name_recommended_restaurant": "Ramonita"
  }
}
```
