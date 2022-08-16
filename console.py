import pdb
from models.album import Album
import repositories.album_repository as album_repository

album1 = Album("I love life", "Mac Miller")
album2 = Album("White Light/White Heat", "Velvet Underground")
album3 = Album("Every Hero Needs a Villain", "Czarface")

album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)

result = album_repository.select(54)
print(result.__dict__)

# for mac in result:
#     print(mac.__dict__)

# album_repository.delete_all()

results = album_repository.select_all()

# for album in results:
#     print(album.__dict__)

