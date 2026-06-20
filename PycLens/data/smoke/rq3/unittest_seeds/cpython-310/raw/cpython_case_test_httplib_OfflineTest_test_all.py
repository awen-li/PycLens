# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: OfflineTest_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = {'responses'}
    denylist = {'HTTPMessage', 'parse_headers'}
    for name in dir(client):
        if name.startswith('_') or name in denylist:
            continue
        module_object = getattr(client, name)
        if getattr(module_object, '__module__', None) == 'http.client':
            expected.add(name)
    self.assertCountEqual(client.__all__, expected)
