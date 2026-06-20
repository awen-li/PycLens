# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocServerTest_test_server

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def my_url_handler(url, content_type):
        text = 'the URL sent was: (%s, %s)' % (url, content_type)
        return text
    serverthread = pydoc._start_server(my_url_handler, hostname='0.0.0.0', port=0)
    self.assertIn('0.0.0.0', serverthread.docserver.address)
    starttime = time.monotonic()
    timeout = test.support.SHORT_TIMEOUT
    while serverthread.serving:
        time.sleep(0.01)
        if serverthread.serving and time.monotonic() - starttime > timeout:
            serverthread.stop()
            break
    self.assertEqual(serverthread.error, None)
