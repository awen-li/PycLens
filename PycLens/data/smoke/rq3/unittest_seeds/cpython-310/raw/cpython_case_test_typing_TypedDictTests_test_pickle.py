# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global EmpD
    EmpD = TypedDict('EmpD', name=str, id=int)
    jane = EmpD({'name': 'jane', 'id': 37})
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        z = pickle.dumps(jane, proto)
        jane2 = pickle.loads(z)
        self.assertEqual(jane2, jane)
        self.assertEqual(jane2, {'name': 'jane', 'id': 37})
        ZZ = pickle.dumps(EmpD, proto)
        EmpDnew = pickle.loads(ZZ)
        self.assertEqual(EmpDnew({'name': 'jane', 'id': 37}), jane)
