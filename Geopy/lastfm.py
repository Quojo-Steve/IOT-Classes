import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "59356699753ca02196f4c5f41bb506b7"
API_SECRET = "71a76e1c5a5c17bb1292ad60ac88d929"

# In order to perform a write operation, you need to authenticate yourself
username = "Ashafa-Ahmed"
password_hash = pylast.md5("SuzzyA-2")

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)

# Get artist information
artist_name = "Adele"
artist = network.get_artist(artist_name)

# Display artist details
print("Artist Information:")
print("Name:", artist.get_name())
print("Listeners:", artist.get_listener_count())
print("Play Count:", artist.get_playcount())
# print("Tags:", ", ".join(tag_item.get_name() for tag_item in artist.get_top_tags()))
print("Biography:", artist.get_bio_summary())

# Get top tracks by the artist
top_tracks = artist.get_top_tracks(limit=5)
print("\nTop Tracks:")
for i, track in enumerate(top_tracks):
    print(f"{i+1}. {track.item.get_name()} - {track.weight}")

# Get similar artists
similar_artists = artist.get_similar()
print("\nSimilar Artists:")
for i, similar_artist in enumerate(similar_artists):
    print(f"{i+1}. {similar_artist.item.get_name()}")

