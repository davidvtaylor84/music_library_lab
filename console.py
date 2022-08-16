import pdb
from models.album import Album
import repositories.album_repository as album_repository

album1 = Album("I love life", "Mac Miller")

album_repository.save(album1)