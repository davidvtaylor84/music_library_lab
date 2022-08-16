from unittest import result
from db.run_sql import run_sql
from models.album import Album

def save(album):
    sql = "INSERT INTO albums(album_name, artist) VALUES (%s, %s) RETURNING *"
    values = [album.album_name, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album