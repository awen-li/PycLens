# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = types.SimpleNamespace(breakfast='spam', lunch='spam')
    for protocol in range(pickle.HIGHEST_PROTOCOL + 1):
        pname = 'protocol {}'.format(protocol)
        try:
            ns_pickled = pickle.dumps(ns, protocol)
        except TypeError as e:
            raise TypeError(pname) from e
        ns_roundtrip = pickle.loads(ns_pickled)
        self.assertEqual(ns, ns_roundtrip, pname)
