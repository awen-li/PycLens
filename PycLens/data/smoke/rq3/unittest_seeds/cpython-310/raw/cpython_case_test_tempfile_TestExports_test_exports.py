# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestExports_test_exports

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dict = tempfile.__dict__
    expected = {'NamedTemporaryFile': 1, 'TemporaryFile': 1, 'mkstemp': 1, 'mkdtemp': 1, 'mktemp': 1, 'TMP_MAX': 1, 'gettempprefix': 1, 'gettempprefixb': 1, 'gettempdir': 1, 'gettempdirb': 1, 'tempdir': 1, 'template': 1, 'SpooledTemporaryFile': 1, 'TemporaryDirectory': 1}
    unexp = []
    for key in dict:
        if key[0] != '_' and key not in expected:
            unexp.append(key)
    self.assertTrue(len(unexp) == 0, 'unexpected keys: %s' % unexp)
