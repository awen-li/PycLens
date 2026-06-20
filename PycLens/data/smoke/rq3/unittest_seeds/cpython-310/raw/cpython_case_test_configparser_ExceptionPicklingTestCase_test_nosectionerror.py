# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ExceptionPicklingTestCase_test_nosectionerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    e1 = configparser.NoSectionError('section')
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        pickled = pickle.dumps(e1, proto)
        e2 = pickle.loads(pickled)
        self.assertEqual(e1.message, e2.message)
        self.assertEqual(e1.args, e2.args)
        self.assertEqual(e1.section, e2.section)
        self.assertEqual(repr(e1), repr(e2))
