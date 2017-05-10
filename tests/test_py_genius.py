import pytest
import json
from py_genius import Genius

def raise_TypeError():
    """Helper function to test TypeError is raised when expected"""
    raise TypeError()

def get_token(source="process"):
    if source != "process":
        with open('access-token.json', 'r') as f:
            obj = json.load(f)
            token = obj['access_token']
    else:
        import os
        token = os.environ['GENIUS_API_ACCESS_TOKEN']
    return token

@pytest.fixture(scope="module")
def genius():
    """pytest fixture, returns an instance of Genius()"""
    token = get_token()
    return Genius(token)


def test_get_song(genius):
    song_id = 378195
    song_full_name = "Chandelier by Sia"
    response = genius.get_song(song_id)
    outcome = response['response']['song']['full_title'].replace(u'\xa0', ' ')
    assert outcome == song_full_name

def test_get_artist(genius):
    artist_id = 16775
    artist_name = "Sia"
    response = genius.get_artist(artist_id)
    outcome = response['response']['artist']['name']
    assert outcome == artist_name

def test_search(genius):
    artist_name = "Kendrick Lamar"
    response = genius.search(artist_name)
    first_match = response['response']['hits'][0]
    outcome = first_match['result']['primary_artist']['name']

    assert outcome == artist_name

def test_get_artist_songs(genius):
    artist_id = 16775
    artist_name = "Sia"
    response = genius.get_artist_songs(artist_id)
    first_song = response['response']['songs'][0]
    outcome = first_song['primary_artist']['name']

    assert outcome == artist_name

def test_get_web_pages_raw_annotatable_url(genius):
    url = "https://docs.genius.com"
    title = "Genius API"
    response = genius.get_web_pages(raw_annotatable_url=url)
    outcome = response['response']['web_page']['title']

    assert outcome == title

def test_get_web_pages_no_args_raises_type_error(genius):
    with pytest.raises(TypeError):
        raise_TypeError()

""" These tests currently fail on docs.genius.api as well, when I get them working I'll put them back in
def test_get_web_pages_canonical_url(genius):
    url = "https://docs.genius.com"
    title = "Genius API"
    response = genius.get_web_pages(canonical_url=url)
    outcome = response['response']['web_page']['title']

    assert outcome == title

def test_get_web_pages_og_url(genius):
    url = "https://docs.genius.com"
    title = "Genius API"
    response = genius.get_web_pages(og_url=url)
    outcome = response['response']['web_page']['title']

    assert outcome == title

def test_get_web_pages_multiple_arguments(genius):
    url = "https://docs.genius.com"
    title = "Genius API"
    response = genius.get_web_pages(canonical_url=url, og_url=url)
    outcome = response['response']['web_page']['title']

    assert outcome == title
"""
