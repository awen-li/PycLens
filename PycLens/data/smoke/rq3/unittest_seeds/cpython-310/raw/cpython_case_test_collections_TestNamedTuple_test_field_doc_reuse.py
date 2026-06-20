# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_field_doc_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = namedtuple('P', ['m', 'n'])
    Q = namedtuple('Q', ['o', 'p'])
    self.assertIs(P.m.__doc__, Q.o.__doc__)
    self.assertIs(P.n.__doc__, Q.p.__doc__)
