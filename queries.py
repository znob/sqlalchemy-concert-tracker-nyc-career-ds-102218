from user import User
from band import Band
from sqlalchemy import func


def count_user_ids(session):
    count_userids = session.query(func.count(User.id)).one()
    return count_userids

def return_band_name_and_total_shows_histogram(session):
    bands = session.query(Band).all()
    band_histo = {}
    for band in bands:
        band_histo[band.name] = len(band.shows)
    return band_histo
