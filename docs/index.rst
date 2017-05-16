.. py_genius documentation master file, created by
   sphinx-quickstart on Thu May 11 21:36:04 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to py_genius's documentation!
=====================================

#########
py_genius
#########

Installation
------------
::

   pip install py_genius

Get started
-----------

#. pip install py_genius
#. Create an account on genius.com
#. Register an application at https://genius.com/api-clients and Generate an Access Token


Usage
-----
.. code-block:: python
   
   import os
   from py_genius import Genius

   g = Genius(os.environ['GENIUS_API_ACCESS_TOKEN'])
   search_results = g.search('Sia')
   sia_id = search_results['response']['hits'][0]['result']['primary_artist']['id']
   
   sia = g.get_artist(sia_id)
   
   sia_songs = g.get_artist_songs(sia_id)

   chandelier_id = [
       song['response']['song']['id']
       for song 
       in sia_songs 
       if song['response']['song']['full_title'] == 'Chandelier by Sia'
   ][0]

   chandelier = g.get_song(chandelier_id)

