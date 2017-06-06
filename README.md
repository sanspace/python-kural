# Kural API Library

Kural is a wrapper to [getthirukkural API](http://getthirukural.appspot.com).

Get an API Key from [getthirukkural](http://getthirukural.appspot.com) and you
can start making API requests as below:

```python
import kural

api = kural.Kural(api_key='API_KEY') # initialize with your key

kural = api.get_kural(2) # fetches you second kural

kurals = api.get_kurals(1,5) # fetches kurals 1 to 5

kural = api.get_random() # fetches a random kural

```

It is licensed under [MIT](https://san.mit-license.org/).