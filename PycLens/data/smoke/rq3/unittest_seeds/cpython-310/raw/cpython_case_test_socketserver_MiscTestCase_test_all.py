# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: MiscTestCase_test_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = []
    for name in dir(socketserver):
        if not name.startswith('_'):
            mod_object = getattr(socketserver, name)
            if getattr(mod_object, '__module__', None) == 'socketserver':
                expected.append(name)
    self.assertCountEqual(socketserver.__all__, expected)
