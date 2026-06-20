# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_selectors.py
# case: EpollSelectorTestCase_test_register_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = self.SELECTOR()
    with tempfile.NamedTemporaryFile() as f:
        with self.assertRaises(IOError):
            s.register(f, selectors.EVENT_READ)
        with self.assertRaises(KeyError):
            s.get_key(f)
