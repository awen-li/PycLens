# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: BaseTestCase_test_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.o.ind = 'dumb'
    self.n.ind = 'bad'
    self.assertRaises(TypeError, operator.index, self.o)
    self.assertRaises(TypeError, operator.index, self.n)
    self.assertRaises(TypeError, slice(self.o).indices, 0)
    self.assertRaises(TypeError, slice(self.n).indices, 0)
