import unittest, sys, datetime
sys.path.insert(0, './models/')
from base import Base
sys.path.insert(0, '..')
from queries import *

exec(open("./run.py").read())

class TestConcertTracker(unittest.TestCase):
    users = session.query(User).all()
    shows = session.query(Show).all()
    cornell_1977 = session.query(Show).filter_by(date=datetime.date(1977, 5, 8)).one()
    bands = session.query(Band).all()
    dead = bands[0]
    cities = session.query(City).all()
    venues = session.query(Venue).all()
    msg = session.query(Venue).filter_by(name="Madison Square Garden").one()
    songs = session.query(Song).all()
    cornell_scarlet_begonias = session.query(ShowSong).filter_by(id=4).one()

    def test_users(self):
        self.assertEqual(len(self.users), 3)

    def test_user_has_name(self):
        self.assertEqual(self.users[0].name, 'John Doe')
        self.assertEqual(self.users[1].name, 'Frank Stallone')

    def test_user_has_many_shows(self):
        self.assertEqual(len(self.users[0].shows), 3)
        self.assertEqual(len(self.users[1].shows), 2)

    def test_shows(self):
        self.assertEqual(len(self.shows), 5)

    def test_show_has_date(self):
        self.assertEqual(self.shows[0].date, datetime.date(1977, 5, 8))

    def test_show_has_many_users(self):
        self.assertEqual(len(self.cornell_1977.users), 2)

    def test_show_belongs_to_band(self):
        self.assertEqual(self.cornell_1977.band.name, 'Grateful Dead')

    def test_show_belongs_to_venue(self):
        self.assertEqual(self.cornell_1977.venue.name, 'Barton Hall')

    def test_bands(self):
        self.assertEqual(len(self.bands), 3)

    def test_band_has_name(self):
        self.assertEqual(self.dead.name, 'Grateful Dead')

    def test_band_has_many_shows(self):
        self.assertEqual(len(self.dead.shows), 3)

    def test_cities(self):
        self.assertEqual(len(self.cities), 4)

    def test_city_has_name(self):
        self.assertEqual(self.cities[0].name, 'Uniondale, NY')

    def test_city_has_many_venues(self):
        nyc = session.query(City).filter_by(name='New York, NY').one()
        self.assertEqual(len(nyc.venues), 2)

    def test_venues(self):
        self.assertEqual(len(self.venues), 5)

    def test_venue_belongs_to_venue(self):
        self.assertEqual(self.venues[0].city.name, 'Uniondale, NY')

    def test_venue_has_many_shows(self):
        self.assertEqual(len(self.msg.shows), 2)

    def test_venue_has_name_and_capacity(self):
        self.assertEqual(self.msg.name, 'Madison Square Garden')
        self.assertEqual(self.msg.capacity, 20789)

    def test_songs(self):
        self.assertEqual(len(self.songs), 4)

    def test_song_has_name(self):
        self.assertEqual(self.songs[0].name, 'Mike\'s Song')

    def test_show_songs_has_length(self):
        self.assertEqual(self.cornell_scarlet_begonias.length, 675)

    def test_show_songs_has_notes(self):
        self.assertEqual(self.cornell_scarlet_begonias.notes, 'famous Cornell Scarlet->Fire')

    def test_count_user_ids(self):
        result = count_user_ids(session)[0]
        self.assertEqual(result, 3)

    def test_return_band_name_and_total_shows_histogram(self):
        result = return_band_name_and_total_shows_histogram(session)
        self.assertEqual(result, {'Grateful Dead': 3, 'Phish': 2, 'My Band From High School': 0})

    def test_user_total_shows(self):
        jd_total_shows = self.users[0].total_shows()
        fs_total_shows = self.users[1].total_shows()
        self.assertEqual(jd_total_shows, 3)
        self.assertEqual(fs_total_shows, 2)

    def test_user_first_show(self):
        jd_first_show = self.users[0].first_show()
        self.assertEqual(jd_first_show, 'Grateful Dead - 05/08/1977 - Barton Hall, Ithaca, NY')
        fs_first_show = self.users[1].first_show()
        self.assertEqual(fs_first_show, 'Grateful Dead - 08/27/1972 - Springfield Creamery, Veneta, OR')
