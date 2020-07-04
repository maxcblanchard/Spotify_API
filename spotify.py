import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import pandas

client_id = 'fdb778fb2ac648489fec11c10f331937'
client_secret = '27acaaaefda14305941ba37cb661cae1'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class Spotify:

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.id_list = []

    def get_track_ids(self):
        self.id_list = []
        results = sp.playlist_tracks(self.playlist_id)
        songs = results['items']
        while results['next']:
            results = sp.next(results)
            songs.extend(results['items'])
        for i in songs:
            song = i['track']
            self.id_list.append(song['id'])
        return self.id_list

    def get_track_features(self, track_list):
        track_info = sp.track(track_list)
        track_feature = sp.audio_features(track_list)

        name = track_info['name']
        length = track_info['duration_ms']
        acousticness = track_feature[0]['acousticness']
        danceability = track_feature[0]['danceability']
        energy = track_feature[0]['energy']
        instrumentalness = track_feature[0]['instrumentalness']
        liveness = track_feature[0]['liveness']
        loudness = track_feature[0]['loudness']
        speechiness = track_feature[0]['speechiness']
        tempo = track_feature[0]['tempo']
        time_signature = track_feature[0]['time_signature']

        info = [name, length, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness,
                tempo,
                time_signature]

        return info

    def acoustincess_calc(self, tracks):
        total_acousticness = 0
        for i in range(len(tracks)):
            total_acousticness += tracks[i][2]
        average_acousticness = total_acousticness / len(tracks)
        return average_acousticness

    def danceability_calc(self, tracks):
        total_danceability = 0
        for i in range(len(tracks)):
            total_danceability += tracks[i][3]
        average_danceability = total_danceability / len(tracks)
        return average_danceability

    def energy_calc(self, tracks):
        total_energy = 0
        for i in range(len(tracks)):
            total_energy += tracks[i][4]
        average_energy = total_energy / len(tracks)
        return average_energy

    def instrumentalness_calc(self, tracks):
        total_instrumentalness = 0
        for i in range(len(tracks)):
            total_instrumentalness += tracks[i][5]
        average_instrumentalness = total_instrumentalness / len(tracks)
        return average_instrumentalness

    def liveness_calc(self, tracks):
        total_liveness = 0
        for i in range(len(tracks)):
            total_liveness += tracks[i][6]
        average_liveness = total_liveness / len(tracks)
        return average_liveness

    def loudness_calc(self, tracks):
        total_loudness = 0
        for i in range(len(tracks)):
            total_loudness += tracks[i][7]
        average_loudness = total_loudness / len(tracks)
        return average_loudness

    def speechiness_calc(self, tracks):
        total_speechiness = 0
        for i in range(len(tracks)):
            total_speechiness += tracks[i][8]
        average_speechiness = total_speechiness / len(tracks)
        return average_speechiness

    def tempo_calc(self, tracks):
        total_tempo = 0
        for i in range(len(tracks)):
            total_tempo += tracks[i][9]
        average_tempo = total_tempo / len(tracks)
        return average_tempo

    def time_signature_calc(self, tracks):
        total_time_signature = 0
        for i in range(len(tracks)):
            total_time_signature += tracks[i][10]
        average_time_signature = total_time_signature / len(tracks)
        return average_time_signature

    def create_list(self):
        tracks = []
        for i in range(len(self.id_list)):
            track = self.get_track_features(self.id_list[i])
            tracks.append(track)
        return self.acoustincess_calc(tracks), self.danceability_calc(tracks), self.energy_calc(tracks), \
            self.instrumentalness_calc(tracks), self.liveness_calc(tracks), self.loudness_calc(tracks), \
            self.speechiness_calc(tracks), self.tempo_calc(tracks), self.time_signature_calc(tracks)




spotify_one = Spotify('spotify:playlist:66mDGk6rWDGMAoRBNIT6J5')
spotify_one.get_track_ids()
print(len(spotify_one.id_list))
spotify_one.create_list()
spotify_two = Spotify('spotify:playlist:1M5bYJb1gP3F94tlF6ZvJ6')
spotify_two.get_track_ids()
print(len(spotify_two.id_list))
spotify_two.create_list()

# df = pandas.DataFrame(tracks, columns=['name', 'duration in ms'])
# df.to_csv("spotify.csv", sep=',')
