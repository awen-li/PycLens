# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: MiscTestCase_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = []
    denylist = {'executable', 'nobody_uid', 'test'}
    for name in dir(server):
        if name.startswith('_') or name in denylist:
            continue
        module_object = getattr(server, name)
        if getattr(module_object, '__module__', None) == 'http.server':
            expected.append(name)
    self.assertCountEqual(server.__all__, expected)
