from unittest import result
from db.run_sql import run_sql
from models.album import Album

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        album = Album(result["album_name"], result["artist"], result["id"])
        return album

def save(album):
    sql = "INSERT INTO albums(album_name, artist) VALUES (%s, %s) RETURNING *"
    values = [album.album_name, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(row["album_name"], row["artist"], row["id"])
        albums.append(album)
    return albums



