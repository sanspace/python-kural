import requests
import os
import json

class KuralError(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(KuralError):
    """Invalid input passed
    
    Pay attention to the function specs and pass correct args
    """
    def __init__(self, expression, message):
        self.message = message
        self.expression = expression

class ServerError(KuralError):
    """API returned error or did not respond
    """
    def __init__(self, resp):
        self.http_code = resp.status_code
        self.message = resp.text

class Kural:
    """An Interface to talk to Kural API
    
    Need to have a Kural API key from http://getthirukural.appspot.com
    """
    api_key = ""
    api_url = "https://getthirukkural.appspot.com/api/2.0/kural/"
    
    def __init__(self, api_key):
        """Initialize Kural Object with API Key"""
        self.api_key = api_key
    
    def _send_req(self, srch):
        """Sends API request and gets response
        
        srch is a valid search as per Kural API criteria.
        """
        url = self.api_url + srch
        parms = {'appid':self.api_key, 'format':'json'}
        
        resp = requests.get(url, params=parms)
        
        if resp.status_code == 200:
            return json.loads(resp.text)["KuralSet"]["Kural"]
        else:
            raise ServerError(resp)
    
    def get_kurals(self, start, end):
        """Get Kurals belong to a range
        
        Range should be a start, end where
        1 <= start <= 1330
        start <= end <= 1330
        end <= start + 20 (API allows end 20 Kurals per request)
        """
        if 1 > start or start > 1330:
            raise InputError(start, "Invalid start of range. Allowed: 1 - 1330.")
        if 1 > end or end > 1330:
            raise InputError(end, "Invalid end of range. Allowed: 1 - 1330.")
        if end > start + 20:
            raise InputError(end, "Invalid Range. Max allowed is 20 Kurals")
            
        return self._send_req(str(start) + "-" + str(end))

    def get_kural(self, kural):
        """Get specific kural
        
        1 <= kural_id <= 1330
        Kurals range from 1 to 1330. So, make sure your input is within range.
        """
        if 1 > kural or kural > 1330:
            raise InputError(kural, "Invalid Kural. Allowed range: 1 - 1330.")
        return self._send_req(kural)[0]

    def get_random(self):
        """Get a random Kural
        
        Accepts no args. Returns a random Kural.
        """
        return self._send_req("rnd")[0]


if __name__ == "__main__":
    """Example to show usage and test functions
    
    """
    kural = Kural(api_key=os.environ['KURAL_API_KEY'])
    k = kural.get_kurals(1, 5)
    print "Kurals 1 to 5"
    print k
    
    k = kural.get_kural(2)
    print "Kural 2"
    print k
    
    k = kural.get_random()
    print "Random Kural"
    print k