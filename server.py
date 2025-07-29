import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/mashvisor-team/api/mashvisor'

mcp = FastMCP('mashvisor')

@mcp.tool()
def get_airbnb_rental_rates(state: Annotated[str, Field(description='State short name')],
                            source: Annotated[str, Field(description='Targeting service to fetch estiamtes for. Possible inputs: * airbnb * traditional')],
                            city: Annotated[Union[str, None], Field(description='City name')] = None,
                            neighborhood: Annotated[Union[int, float, None], Field(description="Neighborhood id you're targeting Default: 0")] = None,
                            zip_code: Annotated[Union[str, None], Field(description='Zip code value')] = None) -> dict: 
    '''The endpoint retrieves rental income rates for Airbnb or traditional way for a city, zip code, or a neighborhood, you'll be able to fetch Airbnb rental rates - short term rentals, or long term rentals, calculated based on the location Airbnb occupancy rates'''
    url = 'https://mashvisor-api.p.rapidapi.com/rental-rates'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'source': source,
        'city': city,
        'neighborhood': neighborhood,
        'zip_code': zip_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_traditional_rental_rates(state: Annotated[str, Field(description='State short name')],
                                 source: Annotated[str, Field(description='Targeting service to fetch estiamtes for. Possible inputs: * airbnb * traditional')],
                                 city: Annotated[Union[str, None], Field(description='City name')] = None,
                                 zip_code: Annotated[Union[str, None], Field(description='Zip code value')] = None,
                                 neighborhood: Annotated[Union[int, float, None], Field(description="Neighborhood id you're targeting Default: 0")] = None) -> dict: 
    '''The endpoint retrieves rental income rates for Airbnb or traditional way for a city, zip code, or a neighborhood, you'll be able to fetch Airbnb rental rates - short term rentals, or long term rentals, calculated based on the location Airbnb occupancy rates'''
    url = 'https://mashvisor-api.p.rapidapi.com/rental-rates'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'source': source,
        'city': city,
        'zip_code': zip_code,
        'neighborhood': neighborhood,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_super_hosts(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404')],
                           city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                           page: Annotated[Union[int, float, None], Field(description='Page number. Default: 1')] = None,
                           zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 91342')] = None) -> dict: 
    '''Obtain a list of all Airbnb market super hosts for a zip code or a city.'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/super-hosts'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'page': page,
        'zip_code': zip_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_top_reviewed_homes(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404')],
                                  city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                                  reviews_count: Annotated[Union[int, float, None], Field(description='Any valid integer to fetch listings counts more than the number Default: 30')] = None,
                                  zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 91342')] = None,
                                  page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''List all Airbnb top reviewed homes and most counts of reviews for a specific location: city, or a zip code'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/top-reviewed'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'reviews_count': reviews_count,
        'zip_code': zip_code,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_newly_listed_homes(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                                  city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                                  page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None,
                                  zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 0')] = None) -> dict: 
    '''List all Airbnb homes that are recently listed for a specific location: city, or a zip code.'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/newly-listed'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'page': page,
        'zip_code': zip_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_historical_performance(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404.')]) -> dict: 
    '''This endpoint retrieves the Airbnb listing 12 historical records - nightly price, revenue, occupancy days, unbooked nights, and occupancy rate - for a specific property.'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/23861615/historical'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_listing_info(state: Annotated[str, Field(description='The state of the listing should be provided to the api or api will throw error 404')]) -> dict: 
    '''This endpoint retrieves an Airbnb listing detailed information, reviews, photos, host, estimated rental income, rental rate, night rate , calculated occupancy rate.'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/22518616'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_occupancy_rates(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                               city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                               zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 0')] = None,
                               neighborhood: Annotated[Union[int, float, None], Field(description="Neighborhood id you're targeting Default: 0")] = None) -> dict: 
    '''For each Airbnb listing, we calculate its occupancy rate, month per month, and an annual rate, and we offer our clients a 12-month historical performance for the occupancy rates. Market occupancy rates for a zip code or a neighborhood.'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/occupancy-rates'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'neighborhood': neighborhood,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_airbnb_property_types(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                              zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 0')] = None,
                              city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                              neighborhood: Annotated[Union[int, float, None], Field(description="Neighborhood id you're targeting Default: 0")] = None) -> dict: 
    '''Check all Airbnb market property types for a zip code or a neighborhood and return their counts.'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/property-types'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'zip_code': zip_code,
        'city': city,
        'neighborhood': neighborhood,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_listings(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                 city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                 zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 91342')] = None,
                 page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None,
                 neighborhood: Annotated[Union[int, float, None], Field(description="Neighborhood id you're targeting Default: 0")] = None,
                 items: Annotated[Union[int, float, None], Field(description='Item number per page Default: 4')] = None) -> dict: 
    '''List all active short term rentals - Airbnb listings - for a specific location: city, zip code, or a neighborhood'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/active-listings'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'page': page,
        'neighborhood': neighborhood,
        'items': items,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_market_summary(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                       zip_code: Annotated[Union[int, float, None], Field(description='Any postal zip code. Default: 0')] = None,
                       city: Annotated[Union[str, None], Field(description="A specific city you're looking for.")] = None,
                       neighborhood: Annotated[Union[int, float, None], Field(description="Neighborhood id you're targeting Default: 0")] = None) -> dict: 
    '''Get a summary an overview for a specific Airbnb market location: city, zip code, or a neighborhood'''
    url = 'https://mashvisor-api.p.rapidapi.com/airbnb-property/market-summary'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'zip_code': zip_code,
        'city': city,
        'neighborhood': neighborhood,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_neighborhood_historical_performance(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                                            beds: Annotated[Union[int, float, None], Field(description='0 to 4 bedrooms value Default: 0')] = None,
                                            average_by: Annotated[Union[str, None], Field(description="Neighborhood id you're targeting. Possible Inputs: * occupancy * price * revenue")] = None,
                                            percentile_rate: Annotated[Union[int, float, None], Field(description='Percentile rate Default: 1')] = None,
                                            category: Annotated[Union[str, None], Field(description='AirBnB category type. Possible Inputs: * flat * house * apartment * loft')] = None) -> dict: 
    '''Get an Airbnb submarket (neighborhood) short term historical performance for its listings as an array'''
    url = 'https://mashvisor-api.p.rapidapi.com/neighborhood/268201/historical/airbnb'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'beds': beds,
        'average_by': average_by,
        'percentile_rate': percentile_rate,
        'category': category,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_traditional_neighborhood_historical_performance(state: Annotated[str, Field(description='The state should be provided to the api or api will throw error 404.')],
                                                        beds: Annotated[Union[str, None], Field(description='0 to 4 bedrooms value')] = None,
                                                        year: Annotated[Union[str, None], Field(description='A month to fetch after')] = None,
                                                        month: Annotated[Union[str, None], Field(description='A month to fetch after')] = None) -> dict: 
    '''Get a submarket (neighborhood) short term historical performance for its listings as an array'''
    url = 'https://mashvisor-api.p.rapidapi.com/neighborhood/268201/historical/traditional'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'beds': beds,
        'year': year,
        'month': month,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_traditional_property(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404')],
                             id: Annotated[Union[int, float, None], Field(description='The traditional property Id from the Mashvisor database. Default: 5637233')] = None,
                             mls_id: Annotated[Union[str, None], Field(description='Property MLS id')] = None,
                             address: Annotated[Union[str, None], Field(description='Property street address')] = None,
                             city: Annotated[Union[str, None], Field(description='Property city')] = None,
                             parcel_number: Annotated[Union[str, None], Field(description='Property parcel or APN')] = None,
                             zip_code: Annotated[Union[str, None], Field(description='Property postal code')] = None) -> dict: 
    '''This endpoint retrieves the traditional - long term rental - property's detailed data set stored in Mashvisor database.'''
    url = 'https://mashvisor-api.p.rapidapi.com/traditional-property'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'id': id,
        'mls_id': mls_id,
        'address': address,
        'city': city,
        'parcel_number': parcel_number,
        'zip_code': zip_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_top_airbnb_cities(state: Annotated[str, Field(description='State* name, ex: NV.')],
                          page: Annotated[Union[str, None], Field(description='Page number')] = None,
                          items: Annotated[Union[str, None], Field(description='The items to return the content for. Valid values: 10, ... etc')] = None) -> dict: 
    '''Top Airbnb Cities, this endpoint retrieves the cities has the highest occupancy rates with their total Airbnb active listings in a specific state.'''
    url = 'https://mashvisor-api.p.rapidapi.com/trends/cities'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'page': page,
        'items': items,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_city_summary(state: Annotated[str, Field(description='State name, ex: NV.')],
                     city: Annotated[str, Field(description='City name, ex: Las Vegas.')]) -> dict: 
    '''This endpoint retrieves a summary of airbnb properties, traditional properties, investment properties, and active neighborhoods available on Mashvisor.com for a specific .'''
    url = 'https://mashvisor-api.p.rapidapi.com/trends/summary/NY/Buffalo'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com\n--header', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_location_heatmap(type: Annotated[str, Field(description='AirbnbCoc, or listingPrice, TraditionalCoc, OccupancyRate, AirbnbRental, TraditionalRental')],
                         ne_lat: Annotated[Union[int, float], Field(description='To search to a specific geo area, north east point latitude. e.g: 34.410846062851626 Default: 34.410846062851626')],
                         sw_lng: Annotated[Union[int, float], Field(description='To search to a specific geo area, south west point longitude. e.g: -118.72974734005544 Default: -118.72974734005544')],
                         ne_lng: Annotated[Union[int, float], Field(description='To search to a specific geo area, north east point longitude. e.g: -117.99366335568044 Default: -117.99366335568044')],
                         state: Annotated[str, Field(description='The state to search in. e.g: CA')],
                         sw_lat: Annotated[Union[int, float], Field(description='To search to a specific geo area, south west point latitude. e.g: 33.76436731683163 Default: 33.76436731683163')]) -> dict: 
    '''This endpoint retrieves the investment performance heatmap for a specific geo area.'''
    url = 'https://mashvisor-api.p.rapidapi.com/search/heatmap'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'ne_lat': ne_lat,
        'sw_lng': sw_lng,
        'ne_lng': ne_lng,
        'state': state,
        'sw_lat': sw_lat,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_cities(state: Annotated[str, Field(description='State name, ex: NV. If ignored, it will fetch all available cities')],
                page: Annotated[Union[int, float, None], Field(description='The page to return the content for. Valid values:1, ... etc. Default: 1')] = None,
                items: Annotated[Union[int, float, None], Field(description='The items to return the content for. Valid values: 10, ... etc. Default: 10')] = None) -> dict: 
    '''This endpoint retrieves cities a specific state.'''
    url = 'https://mashvisor-api.p.rapidapi.com/city/list'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'page': page,
        'items': items,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_neighborhoods(state: Annotated[str, Field(description='State name, ex: NV.')],
                       city: Annotated[str, Field(description='City Name, Ex: Los Angeles')]) -> dict: 
    '''This endpoint lists all city available neighborhoods.'''
    url = 'https://mashvisor-api.p.rapidapi.com/city/neighborhoods/FL/Miami'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_top_markets(state: Annotated[str, Field(description='State name, ex: NV.')],
                     items: Annotated[Union[int, float, None], Field(description='The items to return the content for. Valid values: 10, ... etc. Default: 5')] = None) -> dict: 
    '''This endpoint retrieves the top housing cities with their active homes for sale count in a specific state.'''
    url = 'https://mashvisor-api.p.rapidapi.com/city/top-markets'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'items': items,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_investment_performance(state: Annotated[str, Field(description='State name, ex: NV.')],
                                city: Annotated[str, Field(description='City Name, Ex: Los Angeles')]) -> dict: 
    '''This endpoint retrieves the city investment performance, median price, airbnb listings, MLS listings, traditional listings, cap rates, rental rates, and much more'''
    url = 'https://mashvisor-api.p.rapidapi.com/city/investment/NY/Buffalo'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_top_properties(state: Annotated[str, Field(description='State name, ex: NV.')],
                        city: Annotated[str, Field(description='City Name, Ex: Los Angeles')]) -> dict: 
    '''This endpoint retrieves the city's top investment properties performance.'''
    url = 'https://mashvisor-api.p.rapidapi.com/city/properties/GA/Atlanta'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def top_neighborhoods(city: Annotated[str, Field(description='Sity name, ex: Las Vegas.')],
                      state: Annotated[str, Field(description='State name, ex: NV.')],
                      items: Annotated[Union[int, float, None], Field(description='The items to return the content for. Valid values: 10, ... etc. Default: 5')] = None,
                      page: Annotated[Union[int, float, None], Field(description='The page to return the content for. Valid values:1, ... etc Default: 1')] = None) -> dict: 
    '''This endpoint retrieves the neighborhoods has the biggest occupancy in a specific city and state.'''
    url = 'https://mashvisor-api.p.rapidapi.com/trends/neighborhoods'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'city': city,
        'state': state,
        'items': items,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def neighborhood_overview(state: Annotated[str, Field(description="Neighborhood's state")]) -> dict: 
    '''This endpoint retrieves a neighborhood investment analysis and overview.'''
    url = 'https://mashvisor-api.p.rapidapi.com/neighborhood/268201/bar'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_agent(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404')],
              id: Annotated[str, Field(description='The agent Id from the Mashvisor database.')],
              city: Annotated[Union[str, None], Field(description='The agent city from the Mashvisor database.')] = None,
              name: Annotated[Union[str, None], Field(description='The agent full name from the Mashvisor database.')] = None) -> dict: 
    '''This endpoint retrieves a random agent for given non-agent user.'''
    url = 'https://mashvisor-api.p.rapidapi.com/agents/profile/detail'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'id': id,
        'city': city,
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_taxing(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404')]) -> dict: 
    '''This endpoint retrieves the property's detailed data set stored in Mashvisor database.'''
    url = 'https://mashvisor-api.p.rapidapi.com/property/2214791/taxing'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_office(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404.')],
               id: Annotated[Union[int, float], Field(description='The office Id from the Mashvisor database. Default: 6067')]) -> dict: 
    '''This endpoint retrieves the real estate office details for a specific office id.'''
    url = 'https://mashvisor-api.p.rapidapi.com/property/office/details'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def find_property(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404')],
                  zip_code: Annotated[Union[int, float, None], Field(description='Property zip code Default: 0')] = None,
                  id: Annotated[Union[int, float, None], Field(description='The property Id from the Mashvisor database. Default: 2430136')] = None,
                  address: Annotated[Union[str, None], Field(description='Property street address')] = None,
                  parcel_number: Annotated[Union[str, None], Field(description='Property parcel or APN')] = None,
                  city: Annotated[Union[str, None], Field(description='Property city')] = None,
                  mls_id: Annotated[Union[str, None], Field(description='Property MLS id')] = None) -> dict: 
    '''This endpoint retrieves the property's detailed data set stored in Mashvisor database.'''
    url = 'https://mashvisor-api.p.rapidapi.com/property'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'zip_code': zip_code,
        'id': id,
        'address': address,
        'parcel_number': parcel_number,
        'city': city,
        'mls_id': mls_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_investment_performance(state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404.')],
                                    airbnb_rental: Annotated[Union[int, float, None], Field(description='Monthly Airbnb rental income, ex: 2000 Default: 0')] = None,
                                    airbnb_home_owner_insurance: Annotated[Union[int, float, None], Field(description='Sets the airbnb home owner insurance cost, e.g: 83 Default: 0')] = None,
                                    traditional_rental: Annotated[Union[int, float, None], Field(description='Monthly traditional rental income, ex: 1700 Default: 0')] = None,
                                    traditional_home_owner_insurance: Annotated[Union[int, float, None], Field(description='Sets the traditional home owner insurance cost, e.g: 83 Default: 0')] = None,
                                    interest_rate: Annotated[Union[int, float, None], Field(description='Interest rate Default: 0.5')] = None,
                                    startup_cost: Annotated[Union[int, float, None], Field(description='Startup cost Default: 8000')] = None,
                                    traditional_total_expenses: Annotated[Union[int, float, None], Field(description='Sets the traditional total expenses, e.g: 1900 Default: 0')] = None,
                                    traditional_property_tax: Annotated[Union[int, float, None], Field(description='Sets the traditional property tax value, e.g: 1705 Default: 0')] = None,
                                    is_days: Annotated[Union[int, float, None], Field(description='If it\'s set to 0, the "traditional_occupancy" is considered as a percentage, if it\'s 1, it\'s considered as num of days per year Default: 0')] = None,
                                    traditional_management_cost: Annotated[Union[int, float, None], Field(description='Sets the traditional management cost, e.g: 130 Default: 0')] = None,
                                    payment_type: Annotated[Union[str, None], Field(description='loan, cash')] = None,
                                    traditional_occupancy: Annotated[Union[int, float, None], Field(description='num of days per year, or a percentage Based on "is_days" param, eg: 70 as a percentage, or 150 as days Default: 0')] = None,
                                    traditional_maintenance_cost: Annotated[Union[int, float, None], Field(description='Sets the traditional maintenance cost, e.g: 250 Default: 0')] = None,
                                    loan_type: Annotated[Union[int, float, None], Field(description='Loan type Default: 1')] = None,
                                    airbnb_management_cost: Annotated[Union[int, float, None], Field(description='Sets the airbnb management cost, e.g: 120 Default: 0')] = None,
                                    airbnb_maintenance_cost: Annotated[Union[int, float, None], Field(description='Sets the airbnb maintenance cost, e.g: 230 Default: 0')] = None,
                                    max_bid: Annotated[Union[int, float, None], Field(description='Sets the property listing price to its value Default: 0')] = None,
                                    airbnb_total_expenses: Annotated[Union[int, float, None], Field(description='Sets the airbnb total expenses, e.g: 1700 Default: 0')] = None,
                                    airbnb_occupancy: Annotated[Union[int, float, None], Field(description='num of days per year, or a percentage Based on "is_days" param, eg: 70 as a percentage, or 150 as days Default: 0')] = None,
                                    down_payment: Annotated[Union[int, float, None], Field(description='Down payment Default: 10000')] = None,
                                    airbnb_property_tax: Annotated[Union[int, float, None], Field(description='Sets the airbnb property tax value, e.g: 1705 Default: 0')] = None) -> dict: 
    '''This endpoint retrieves the property's investment performance.'''
    url = 'https://mashvisor-api.p.rapidapi.com/property/664367/investment'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'airbnb_rental': airbnb_rental,
        'airbnb_home_owner_insurance': airbnb_home_owner_insurance,
        'traditional_rental': traditional_rental,
        'traditional_home_owner_insurance': traditional_home_owner_insurance,
        'interest_rate': interest_rate,
        'startup_cost': startup_cost,
        'traditional_total_expenses': traditional_total_expenses,
        'traditional_property_tax': traditional_property_tax,
        'is_days': is_days,
        'traditional_management_cost': traditional_management_cost,
        'payment_type': payment_type,
        'traditional_occupancy': traditional_occupancy,
        'traditional_maintenance_cost': traditional_maintenance_cost,
        'loan_type': loan_type,
        'airbnb_management_cost': airbnb_management_cost,
        'airbnb_maintenance_cost': airbnb_maintenance_cost,
        'max_bid': max_bid,
        'airbnb_total_expenses': airbnb_total_expenses,
        'airbnb_occupancy': airbnb_occupancy,
        'down_payment': down_payment,
        'airbnb_property_tax': airbnb_property_tax,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def airbnb_comparable_listings(state: Annotated[str, Field(description='The state of the neighborhood should be provided to the api or api will throw error 404.')],
                               items: Annotated[Union[int, float, None], Field(description='Items number Default: 3')] = None,
                               sort_by: Annotated[Union[str, None], Field(description='Sorting type. Possible input: * name * similarity * distance * address * occupancy * night_price * rental_income * num_of_baths * num_of_rooms * reviews_count')] = None,
                               pid: Annotated[Union[int, float, None], Field(description='Property to fetch comparable listings for. Default: 0')] = None,
                               bedrooms: Annotated[Union[int, float, None], Field(description='Bedrooms number; 0 - 4 Default: 0')] = None,
                               order: Annotated[Union[str, None], Field(description='Order type: desc, or asc')] = None,
                               page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None) -> dict: 
    '''This endpoint retrieves the Airbnb neighborhood's listing data set in Mashvisor database with similarity and distance regarding the target MLS property.'''
    url = 'https://mashvisor-api.p.rapidapi.com/neighborhood/269590/airbnb/details'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'items': items,
        'sort_by': sort_by,
        'pid': pid,
        'bedrooms': bedrooms,
        'order': order,
        'page': page,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def investment_breakdown(recurring_cost: Annotated[Union[int, float], Field(description='Recurring cost of the investment strategy, ex: 1435 Default: 1435')],
                         state: Annotated[str, Field(description='The state of the property should be provided to the api or api will throw error 404.')],
                         startup_cost: Annotated[Union[int, float], Field(description='Startup cost for the investment, e.x: 8000 Default: 8000')],
                         source: Annotated[str, Field(description='Defines the monthly calculations should be calculated for "Airbnb" or "Traditional"')],
                         is_days: Annotated[Union[int, float, None], Field(description='If it\'s set to 0, the "traditional_occupancy" is considered as a percentage, if it\'s 1, it\'s considered as num of days per year Default: 0')] = None,
                         traditional_rental: Annotated[Union[int, float, None], Field(description='Monthly traditional rental income, ex: 1700 Default: 0')] = None,
                         turnover_cost: Annotated[Union[int, float, None], Field(description='Turnover cost Default: 0')] = None,
                         max_bid: Annotated[Union[int, float, None], Field(description='Sets the property listing price to its value Default: 0')] = None,
                         airbnb_rental: Annotated[Union[int, float, None], Field(description='Monthly Airbnb rental income, ex: 2000 Default: 0')] = None,
                         airbnb_occupancy: Annotated[Union[int, float, None], Field(description='num of days per year, or a percentage Based on "is_days" param, eg: 70 as a percentage, or 150 as days Default: 0')] = None,
                         traditional_occupancy: Annotated[Union[int, float, None], Field(description='num of days per year, or a percentage Based on "is_days" param, eg: 70 as a percentage, or 150 as days Default: 0')] = None) -> dict: 
    '''This endpoint retrieves the property's investment breakdown performance for Airbnb or Traditional.'''
    url = 'https://mashvisor-api.p.rapidapi.com/property/664367/investment/breakdown'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recurring_cost': recurring_cost,
        'state': state,
        'startup_cost': startup_cost,
        'source': source,
        'is_days': is_days,
        'traditional_rental': traditional_rental,
        'turnover_cost': turnover_cost,
        'max_bid': max_bid,
        'airbnb_rental': airbnb_rental,
        'airbnb_occupancy': airbnb_occupancy,
        'traditional_occupancy': traditional_occupancy,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_marker(state: Annotated[str, Field(description='The state of the property should be provided to the api or API will throw error 404')],
                    payment: Annotated[str, Field(description='CASH, or LOAN')],
                    pid: Annotated[Union[int, float], Field(description='The property Id from the Mashvisor database. Default: 2207289')],
                    type: Annotated[str, Field(description='Investment, Airbnb, or Traditional')],
                    startupCost: Annotated[Union[int, float, None], Field(description='Default: 8000')] = None,
                    loanType: Annotated[Union[int, float, None], Field(description='The loan type, e.g: 30 Default: 0')] = None,
                    loanTerm: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                    loanInterestOnlyYears: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                    downPayment: Annotated[Union[int, float, None], Field(description='The downpayment for mortgage calculations, e.g: 40000 Default: 0')] = None,
                    loanArmType: Annotated[Union[int, float, None], Field(description='3/1, 5/1, 7/1, 10/1 Default: NaN')] = None,
                    interestRate: Annotated[Union[int, float, None], Field(description='The interest rate for mortgage, e.g: 3.51 Default: 0')] = None,
                    loanArmRate: Annotated[Union[int, float, None], Field(description='Default: 0.25')] = None) -> dict: 
    '''This endpoint retrieves snapshot data about a specific property.'''
    url = 'https://mashvisor-api.p.rapidapi.com/property/marker'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'payment': payment,
        'pid': pid,
        'type': type,
        'startupCost': startupCost,
        'loanType': loanType,
        'loanTerm': loanTerm,
        'loanInterestOnlyYears': loanInterestOnlyYears,
        'downPayment': downPayment,
        'loanArmType': loanArmType,
        'interestRate': interestRate,
        'loanArmRate': loanArmRate,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def traditional_comparable_listings(state: Annotated[str, Field(description='The state of the neighborhood should be provided to the api or api will throw error 404.')],
                                    items: Annotated[Union[int, float, None], Field(description='Items number Default: 5')] = None,
                                    min_price: Annotated[Union[int, float, None], Field(description='min_price of rental value Default: 0')] = None,
                                    sort_by: Annotated[Union[str, None], Field(description='Sorting type. Possible input: * address * similarity * distance * beds * baths * price')] = None,
                                    category: Annotated[Union[int, float, None], Field(description='Bedrooms number Default: 0')] = None,
                                    pid: Annotated[Union[int, float, None], Field(description='Property to fetch comparable listings for. Default: 325215')] = None,
                                    max_price: Annotated[Union[int, float, None], Field(description='max_price of rental value Default: 0')] = None,
                                    page: Annotated[Union[int, float, None], Field(description='Page number Default: 1')] = None,
                                    order: Annotated[Union[str, None], Field(description='Order type: desc, or asc')] = None) -> dict: 
    '''This endpoint retrieves the traditional neighborhood's listing data set in Mashvisor database with similarity and distance regarding the target MLS property.'''
    url = 'https://mashvisor-api.p.rapidapi.com/neighborhood/397651/traditional/listing'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'items': items,
        'min_price': min_price,
        'sort_by': sort_by,
        'category': category,
        'pid': pid,
        'max_price': max_price,
        'page': page,
        'order': order,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def investment_likelihood(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get investment likelihood score for a property, read more about the score in API details section.'''
    url = 'https://mashvisor-api.p.rapidapi.com/ml/investment-likelihood'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def mashmeter(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get neighborhood Mashmeter value, see more about the score in the API details section.'''
    url = 'https://mashvisor-api.p.rapidapi.com/ml/mashmeter'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def property_recommender(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Get recommended properties specs based on Mashvisor AI recommender score, read more about the score in the API details section.'''
    url = 'https://mashvisor-api.p.rapidapi.com/ml/recommended_property'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def baths(state: Annotated[str, Field(description='')],
          city: Annotated[Union[str, None], Field(description='')] = None,
          zip_code: Annotated[Union[str, None], Field(description='')] = None,
          address: Annotated[Union[str, None], Field(description='')] = None,
          lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
          lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
          beds: Annotated[Union[int, float, None], Field(description='Default: 2')] = None,
          baths: Annotated[Union[int, float, None], Field(description='Default: 3')] = None,
          home_type: Annotated[Union[str, None], Field(description='')] = None,
          resource: Annotated[Union[str, None], Field(description='')] = None,
          neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the location (city, zip code, neighborhood, or a street address) bathrooms revenue and occupancy breakdown.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/baths'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def rental_activity_data(state: Annotated[str, Field(description='')],
                         city: Annotated[Union[str, None], Field(description='')] = None,
                         zip_code: Annotated[Union[str, None], Field(description='')] = None,
                         address: Annotated[Union[str, None], Field(description='')] = None,
                         lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                         lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                         beds: Annotated[Union[int, float, None], Field(description='Default: 3')] = None,
                         baths: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
                         home_type: Annotated[Union[str, None], Field(description='')] = None,
                         resource: Annotated[Union[str, None], Field(description='')] = None,
                         neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the Airbnb location rental activity performance and group for booked and unbooked nights.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/rental-activity-data'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_types(state: Annotated[str, Field(description='')],
                   city: Annotated[Union[str, None], Field(description='')] = None,
                   zip_code: Annotated[Union[str, None], Field(description='')] = None,
                   address: Annotated[Union[str, None], Field(description='')] = None,
                   lat: Annotated[Union[int, float, None], Field(description='Default: 37.351423')] = None,
                   lng: Annotated[Union[int, float, None], Field(description='Default: -122.0357769')] = None,
                   beds: Annotated[Union[int, float, None], Field(description='Default: 2')] = None,
                   baths: Annotated[Union[int, float, None], Field(description='Default: 2')] = None,
                   home_type: Annotated[Union[str, None], Field(description='')] = None,
                   resource: Annotated[Union[str, None], Field(description='')] = None,
                   neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the Search for property types in a location (city, zip code, neighborhood, or street address) and gets their stats.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/property-types'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def insights(state: Annotated[str, Field(description='')],
             city: Annotated[Union[str, None], Field(description='')] = None,
             zip_code: Annotated[Union[str, None], Field(description='')] = None,
             address: Annotated[Union[str, None], Field(description='')] = None,
             home_type: Annotated[Union[str, None], Field(description='')] = None,
             resource: Annotated[Union[str, None], Field(description='')] = None,
             neighborhood_id: Annotated[Union[str, None], Field(description='')] = None,
             lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
             lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
             beds: Annotated[Union[int, float, None], Field(description='Default: 3')] = None,
             baths: Annotated[Union[int, float, None], Field(description='Default: 2')] = None) -> dict: 
    '''This endpoint retrieves the Lookup location (city, zip code, neighborhood, or street address) and gets its insights.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/lookup'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def export_comps(state: Annotated[str, Field(description='')],
                 city: Annotated[Union[str, None], Field(description='')] = None,
                 zip_code: Annotated[Union[str, None], Field(description='')] = None,
                 address: Annotated[Union[str, None], Field(description='')] = None,
                 lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                 lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                 beds: Annotated[Union[int, float, None], Field(description='Default: 2')] = None,
                 baths: Annotated[Union[int, float, None], Field(description='Default: 1')] = None,
                 home_type: Annotated[Union[str, None], Field(description='')] = None,
                 resource: Annotated[Union[str, None], Field(description='')] = None,
                 neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the export of all location (city, zip code, neighborhood, or street address) comparables used in the analysis.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/export-comps'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def nearby_listings(state: Annotated[str, Field(description='')],
                    city: Annotated[Union[str, None], Field(description='')] = None,
                    zip_code: Annotated[Union[str, None], Field(description='')] = None,
                    address: Annotated[Union[str, None], Field(description='')] = None,
                    lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                    lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                    beds: Annotated[Union[int, float, None], Field(description='Default: 2')] = None,
                    baths: Annotated[Union[int, float, None], Field(description='Default: 2')] = None,
                    home_type: Annotated[Union[str, None], Field(description='')] = None,
                    resource: Annotated[Union[str, None], Field(description='')] = None,
                    neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the top5 location (city, zip code, neighborhood, or street address) MLS listings in the area.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/nearby-listings'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_comps(state: Annotated[str, Field(description='')],
               city: Annotated[Union[str, None], Field(description='')] = None,
               zip_code: Annotated[Union[str, None], Field(description='')] = None,
               address: Annotated[Union[str, None], Field(description='')] = None,
               lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
               lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
               beds: Annotated[Union[int, float, None], Field(description='Default: 3')] = None,
               baths: Annotated[Union[int, float, None], Field(description='Default: 3')] = None,
               home_type: Annotated[Union[str, None], Field(description='')] = None,
               resource: Annotated[Union[str, None], Field(description='')] = None,
               neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the list of all locations (city, zip code, neighborhood, or street address) comparables used in the analysis.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/list-comps'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def beds(state: Annotated[str, Field(description='')],
         city: Annotated[Union[str, None], Field(description='')] = None,
         zip_code: Annotated[Union[str, None], Field(description='')] = None,
         address: Annotated[Union[str, None], Field(description='')] = None,
         lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
         lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
         beds: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
         baths: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
         home_type: Annotated[Union[str, None], Field(description='')] = None,
         resource: Annotated[Union[str, None], Field(description='')] = None,
         neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the location (city, zip code, neighborhood, or a street address) bedrooms revenue and occupancy breakdown'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/beds'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def historical_performance(state: Annotated[str, Field(description='')],
                           city: Annotated[Union[str, None], Field(description='')] = None,
                           zip_code: Annotated[Union[str, None], Field(description='')] = None,
                           address: Annotated[Union[str, None], Field(description='')] = None,
                           lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                           lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                           beds: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                           baths: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                           home_type: Annotated[Union[str, None], Field(description='')] = None,
                           resource: Annotated[Union[str, None], Field(description='')] = None,
                           neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the location (city, zip code, neighborhood, or street address) historical performance.'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/historical-performance'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def revenue_stats(state: Annotated[str, Field(description='')],
                  city: Annotated[Union[str, None], Field(description='')] = None,
                  zip_code: Annotated[Union[str, None], Field(description='')] = None,
                  address: Annotated[Union[str, None], Field(description='')] = None,
                  lat: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                  lng: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                  beds: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                  baths: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                  home_type: Annotated[Union[str, None], Field(description='')] = None,
                  resource: Annotated[Union[str, None], Field(description='')] = None,
                  neighborhood_id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint retrieves the revenue and occupancy statistics in a location (city, zip code, neighborhood, or street address).'''
    url = 'https://mashvisor-api.p.rapidapi.com/rento-calculator/revenue-stats'
    headers = {'x-rapidapi-host': 'mashvisor-api.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'state': state,
        'city': city,
        'zip_code': zip_code,
        'address': address,
        'lat': lat,
        'lng': lng,
        'beds': beds,
        'baths': baths,
        'home_type': home_type,
        'resource': resource,
        'neighborhood_id': neighborhood_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
