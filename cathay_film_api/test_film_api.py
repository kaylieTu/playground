import pytest
import film_method
import datetime

@pytest.mark.p1
def test_statuscode_all_films():
    status_code, data = film_method.get_all_films()
    assert status_code == 200 ,"Expected status code is 200"
    

@pytest.mark.p1
def test_statuscode_specific_film():
    status_code, data = film_method.get_specific_film("1")
    assert status_code == 200 ,"Expected status code is 200"


@pytest.mark.p2
def test_statuscode_invliad_film_id():
    status_code, data = film_method.get_specific_film("90")
    assert status_code == 404 ,"Expected status code is 404"
    assert data["detail"] == "Not found" ,"Expected message is Not found"


@pytest.mark.p1
def test_all_films_data_type():
    message="The attribute type for {}"
    status_code, data = film_method.get_all_films()
    assert data['count'] > 0 ,"Verify the count not 0"
    assert isinstance(data['results'],list),"Number of returning results should equal to count"
    assert isinstance(data['results'][0]['title'],str) ,message.format("title")
    assert isinstance(data['results'][0]['episode_id'],int),message.format("episode_id")
    assert isinstance(data['results'][0]['opening_crawl'],str) ,message.format("opening_crawl")
    assert isinstance(data['results'][0]['director'], str) ,message.format("director")
    assert isinstance(data['results'][0]['producer'],str) ,message.format("producer")
    assert film_method.validate_date_iso8601(data['results'][0]['release_date']) ,message.format("release_date")
    assert isinstance(data['results'][0]['characters'][0],str) ,message.format("characters")
    assert isinstance(data['results'][0]['starships'][0], str)  ,message.format("starships")
    assert isinstance(data['results'][0]['species'][0], str) , message.format("species")
    assert film_method.validate_date_time_iso8601(data['results'][0]['created']) , message.format("created date")
    assert film_method.validate_date_time_iso8601(data['results'][0]['edited']) , message.format("edited date")
    assert isinstance(data['results'][0]['url'], str) , message.format("url")
    

@pytest.mark.p1
def test_data_specific_film():
    id='1'
    message="The film {} in id "+id
    status_code, data = film_method.get_specific_film(id)
    assert data['title'] == 'A New Hope' ,message.format("title")
    assert data['episode_id'] == 4 ,message.format("episode_id")
    assert data['opening_crawl'] == "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....", message.format("opening_crawl")
    assert data['director'] == 'George Lucas' ,message.format("director")
    assert data['producer'] == 'Gary Kurtz, Rick McCallum' ,message.format("producer")
    assert data['release_date'] == '1977-05-25' ,message.format("release_date")
    assert len(data['characters']) > 0  ,message.format("characters")
    assert len(data['starships']) > 0  ,message.format("starships")
    assert len(data['species']) > 0 , message.format("species")
    assert data['created'] == '2014-12-10T14:23:31.880000Z' , message.format("created date")
    assert data['edited'] == '2014-12-20T19:49:45.256000Z' , message.format("edited date")
    assert data['url'] == 'https://swapi.dev/api/films/1/' , message.format("url")
 

@pytest.mark.p3
def test_all_films_sorting_by_release_date():
    message="The attribute type for {}"
    status_code, data = film_method.get_all_films()
    count =data['count']
    assert data['results'][0]['release_date'] < data['results'][count-1]['release_date']

@pytest.mark.p3
def test_concurrent_request():
    film_method.run_concurrent_request()

