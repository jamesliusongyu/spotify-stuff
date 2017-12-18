import spotipy
import spotipy.oauth2 as oauth2
import sys
import billboard as bb
import pandas as pd
import numpy as np
import json
import speech_recognition as sr
import webbrowser as wb
import csv
googlechrome=wb.get('chrome')


def get_songidd(song):
    results = spotify.search(q=song, type='track')
    items = results['tracks']['items'][0]['preview_url']
    
    googlechrome.open_new_tab(items)


r = sr.Recognizer()
with sr.Microphone() as source:
    #print("Please wait. Calibrating microphone...")
    #r.adjust_for_ambient_noise(source,duration=5)
    print("What song would u like to hear?")
    audio = r.listen(source)
    print (r.recognize_google(audio))
    get_songidd(r.recognize_google(audio))



    





credentials = oauth2.SpotifyClientCredentials(
    client_id='3ff93e9255ed4dcbb736e431634665a6',
    client_secret='8b335b5782b146a18e6f897ce02dd63d')
token = credentials.get_access_token()

spotify = spotipy.Spotify(auth=token)


chart = bb.ChartData('hot-100')
ddf = pd.DataFrame(index= range(1,100), columns=('Song Name','Artist','Hit or Not','Danceability','Energy','Key','Loudness','Mode','Speechiness','Acousticness','Instrumentalness','Liveness','Valence','Tempo','Duration_Ms','Time_Signature'))

def create_dataframe(chart):
    i=1
    for x in chart:
        
        song_id = get_songid(str(x.title))
        y = get_audio_features(song_id)
        danceability=y[0]['danceability']
        energy=y[0]['energy']
        liveness=y[0]['liveness']
        tempo=y[0]['tempo']
        speechiness=y[0]['speechiness']
        acousticness=y[0]['acousticness']
        instrumentalness=y[0]['instrumentalness']
        time_signature=y[0]['time_signature']
        key=y[0]['key']
        duration_ms=y[0]['duration_ms']
        loudness=y[0]['loudness']
        valence=y[0]['valence']
        mode=y[0]['mode']
        if x.peakPos<50:
            hit_or_not=1
        else:
            hit_or_not=0
        
        ddf.loc[i]=pd.Series({'Song Name': str(x.title),'Artist':str(x.artist),'Hit or Not':hit_or_not,'Danceability':danceability,'Energy':energy,'Liveness':liveness,'Tempo':tempo,'Speechiness':speechiness,'Acousticness':acousticness,'Instrumentalness':instrumentalness,'Time_Signature':time_signature,'Key':key,'Duration_Ms':duration_ms,'Loudness':loudness,'Valence':valence, 'Mode':mode})
        i+=1
        
#create_dataframe(chart)


def get_artist(name):
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        return items[0]
    else:
        return None
    
def get_artist_id(name):
    results = spotify.search(q='artist:' + name, type='artist')
    items = results['artists']['items'][0]
    return items['id']

def get_songid(song):
    results = spotify.search(q=song, type='track')
    items = results['tracks']['items'][0]['id']
    return items
(get_songid('rockstar'))

def get_audio_features(songid):
    tid='spotify:track:'+str(songid)
    y=spotify.audio_features(tid)
    
    return y
    
#print (get_audio_features(get_songid('gucci gang')))

def show_artist_albums(artist):
    albums = []
    results = spotify.artist_albums(artist, album_type='album')
    albums.extend(results['items'])
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
    seen = set() # to avoid dups
    albums.sort(key=lambda album:album['name'].lower())
    for album in albums:
        name = album['name']
        if name not in seen:
            print((' ' + name))
            seen.add(name)
##
##def show_recommendations_for_artist(artist):
##    #print get_artist(artist)['id']
##    albums = []
##    results = spotify.recommendations(seed_artists = ('6mfK6Q2tzLMEchAr0e9Uzu')
##    print get_artist(artist)['id']
##    for track in results['tracks']:
##        print track['name'], '-', track['artists'][0]['name']
#print get_artist('bruno mars')
#print spotify.artist(get_artist_id('bruno mars'))
#print spotify.artist_related_artists(get_artist_id('bruno mars'))
def get_related_artists(artist):
    data=spotify.artist_related_artists(get_artist_id(artist))
    related_artists=[]
    artists=data['artists']
    for x in artists:
        related_artists.append(x['name'])
    print related_artists
#get_related_artists('bruno mars')




