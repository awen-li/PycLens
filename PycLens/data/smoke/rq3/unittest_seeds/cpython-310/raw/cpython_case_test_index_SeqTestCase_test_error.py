# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: SeqTestCase_test_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 'dumb'
    self.n.ind = 'bad'
    indexobj = lambda x, obj: obj.seq[x]
    self.assertRaises(TypeError, indexobj, self.o, self)
    self.assertRaises(TypeError, indexobj, self.n, self)
    sliceobj = lambda x, obj: obj.seq[x:]
    self.assertRaises(TypeError, sliceobj, self.o, self)
    self.assertRaises(TypeError, sliceobj, self.n, self)
