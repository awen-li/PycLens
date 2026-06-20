# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: ExceptionPicklingTestCase_test_parsingerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    e1 = configparser.ParsingError('source')
    e1.append(1, 'line1')
    e1.append(2, 'line2')
    e1.append(3, 'line3')
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        pickled = pickle.dumps(e1, proto)
        e2 = pickle.loads(pickled)
        self.assertEqual(e1.message, e2.message)
        self.assertEqual(e1.args, e2.args)
        self.assertEqual(e1.source, e2.source)
        self.assertEqual(e1.errors, e2.errors)
        self.assertEqual(repr(e1), repr(e2))
    e1 = configparser.ParsingError(filename='filename')
    e1.append(1, 'line1')
    e1.append(2, 'line2')
    e1.append(3, 'line3')
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        pickled = pickle.dumps(e1, proto)
        e2 = pickle.loads(pickled)
        self.assertEqual(e1.message, e2.message)
        self.assertEqual(e1.args, e2.args)
        self.assertEqual(e1.source, e2.source)
        self.assertEqual(e1.errors, e2.errors)
        self.assertEqual(repr(e1), repr(e2))
