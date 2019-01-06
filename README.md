# OWBC
Simple web client for Cowlwoc OW stats

* compute_table.py: reads JSON data from friends and a batch of random players (for average stats) to compute a JSON table directly usable by the web client.
* fetch.py: fetches some random player tags.
* near.py: fetches stats from players with rank close to friends using a public API.
* query_friends.py: queries friends stats using a public API.
* repeat.bash: regularly updates friends stats and computes the JSON table
