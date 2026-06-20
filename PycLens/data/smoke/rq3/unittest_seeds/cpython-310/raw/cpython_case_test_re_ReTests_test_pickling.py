# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    oldpat = re.compile('a(?:b|(c|e){1,2}?|d)+?(.)', re.UNICODE)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        pickled = pickle.dumps(oldpat, proto)
        newpat = pickle.loads(pickled)
        self.assertEqual(newpat, oldpat)
    from re import _compile
