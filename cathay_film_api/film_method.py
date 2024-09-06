import requests
import re
import asyncio
import time

base_url='https://swapi.dev/api/films'

'''
This method is to get all films by and it will return status code and json data
'''
def get_all_films():
    try:
        response = requests.get(base_url)
        statusCode=response.status_code
        data=response.json()
        return statusCode, data
    except requests.exceptions.RequestException as e:
        print("Request fail", str(e))
'''
This method is to get specific film by given id and it will return status code and json data
'''
def get_specific_film(id):
    try:
        response = requests.get(base_url+"/"+id)
        statusCode=response.status_code
        data=response.json()
        return statusCode, data
    except requests.exceptions.RequestException as e:
        print("Request fail", str(e)) 


def validate_date_time_iso8601(datetime_val):
    date_time_regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    match_iso8601 = re.compile(date_time_regex).match
    try:            
        if match_iso8601( datetime_val ) is not None:
            return True
    except:
        pass
    return False

def validate_date_iso8601(date_val):
    date_regex =r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$'
    match_iso8601 = re.compile(date_regex).match
    try:            
        if match_iso8601( date_val ) is not None:
            return True
    except:
        pass
    return False


async def counter(until: int) -> None:
     now= time.perf_counter()
     print ("start counter")
     for i in range(0, until):
          last = now
          await asyncio.sleep(0)
          now = time.perf_counter()
          print(f"{i}: was asleep for {now - last}s")


def send_request(url: str) -> int:
        response = requests.get(url)
        
        return response.status_code

async def send_async_request(url: str) -> int:
        return await asyncio.to_thread(send_request,url)

async def run_concurrent_request() -> None:
     task=asyncio.create_task(counter(100))
     status_code = await send_async_request(base_url)
     assert status_code == 200
     print(f"Got http response with status {status_code}")           