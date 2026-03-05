# Bugs Fixed

## Bug 1: Search Only Worked by Artist
**Issue**: Users could only search playlists by artist name, not by song title or other fields.

**Location**: `app.py:279-280`

**Fix**: Modified `render_playlist()` to search both by artist and title, then combine the results.

```python
query = st.text_input(f"Search {label} playlist", key=f"search_{label}")
by_artist = search_songs(songs, query, field="artist")
by_title = search_songs(songs, query, field="title")
```

## Bug 2: Search Logic Was Backwards
**Issue**: In `playlist_logic.py:171`, the search condition was `if value in q:` instead of `if q in value:`.

**Impact**: This checked if the field value was contained within the query, when it should check if the query is contained within the field value.

**Fix**: Changed the condition to properly match queries within song fields.

```python
# Before
if value in q:

# After
if q in value:
```

## Bug 3: TypeError with set() on Dictionaries
**Issue**: After combining artist and title search results, the code tried to use `set()` to remove duplicates: `list(set(by_artist + by_title))`.

**Error**: `TypeError: unhashable type: 'dict'` - dictionaries cannot be added to a set.

**Location**: `app.py:282`

**Fix**: Use song identity tuples (title, artist) to track duplicates instead:

```python
seen = set()
filtered = []
for song in by_artist + by_title:
    song_id = (song.get("title"), song.get("artist"))
    if song_id not in seen:
        seen.add(song_id)
        filtered.append(song)
```

## Result
Users can now search playlists by both song title and artist, with proper deduplication when results overlap.
