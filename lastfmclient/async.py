from __future__ import unicode_literals
import json
import urllib

if hasattr(urllib, 'urlencode'):
    urlencode = urllib.urlencode
else:
    import urllib.parse
    urlencode = urllib.parse.urlencode

from tornado.gen import coroutine, Return
from tornado.httpclient import AsyncHTTPClient

from .client import LastfmClient, API_URL


class AsyncLastfmClient(LastfmClient):
    """
    Non-blocking Last.fm API client for Tornado.

    Uses ``tornado.httpclient.AsyncHTTPClient`` to perform HTTP requests.

    """
    def __init__(self, api_key=None, api_secret=None, session_key=None):
        super(AsyncLastfmClient, self).__init__(
            api_key, api_secret, session_key)
        if not AsyncHTTPClient:
            raise RuntimeError(
                'You need to install Tornado to be able use the async client.')
        self._async_client = AsyncHTTPClient()

    @coroutine
    def call(self, http_method, method, auth, params):

        url = API_URL

        params = self._get_params(method, params, auth)
        params = urlencode(params)
        if http_method == 'POST':
            body = params
        else:
            body = None
            url = url + '?' + params

        response = yield self._async_client.fetch(url,
                                                  method=http_method,
                                                  body=body)
        if response.error is not None:
            response.rethrow()
        body = response.body.decode('utf-8')
        data = self._process_response_data(json.loads(body))
        raise Return(data)
