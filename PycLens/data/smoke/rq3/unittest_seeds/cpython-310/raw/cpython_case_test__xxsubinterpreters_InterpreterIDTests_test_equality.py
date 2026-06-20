# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: InterpreterIDTests_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id1 = interpreters.create()
    id2 = interpreters.InterpreterID(int(id1))
    id3 = interpreters.create()
    self.assertTrue(id1 == id1)
    self.assertTrue(id1 == id2)
    self.assertTrue(id1 == int(id1))
    self.assertTrue(int(id1) == id1)
    self.assertTrue(id1 == float(int(id1)))
    self.assertTrue(float(int(id1)) == id1)
    self.assertFalse(id1 == float(int(id1)) + 0.1)
    self.assertFalse(id1 == str(int(id1)))
    self.assertFalse(id1 == 2 ** 1000)
    self.assertFalse(id1 == float('inf'))
    self.assertFalse(id1 == 'spam')
    self.assertFalse(id1 == id3)
    self.assertFalse(id1 != id1)
    self.assertFalse(id1 != id2)
    self.assertTrue(id1 != id3)
