# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for kwargs in [{'mode': 'w'}, {'mode': 'wb'}, {'mode': 'wb', 'buffering': 0}, {'mode': 'r'}, {'mode': 'rb'}, {'mode': 'rb', 'buffering': 0}, {'mode': 'w+'}, {'mode': 'w+b'}, {'mode': 'w+b', 'buffering': 0}]:
        if 'b' not in kwargs['mode']:
            kwargs['encoding'] = 'utf-8'
        for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.open(os_helper.TESTFN, **kwargs) as f:
                self.assertRaises(TypeError, pickle.dumps, f, protocol)
