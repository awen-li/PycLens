# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestFlag_test_cascading_failure

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Bizarre(Flag):
        c = 3
        d = 4
        f = 6
    name = 'TestFlag.test_cascading_failure.<locals>.Bizarre'
    self.assertRaisesRegex(ValueError, '5 is not a valid ' + name, Bizarre, 5)
    self.assertRaisesRegex(ValueError, '5 is not a valid ' + name, Bizarre, 5)
    self.assertRaisesRegex(ValueError, '2 is not a valid ' + name, Bizarre, 2)
    self.assertRaisesRegex(ValueError, '2 is not a valid ' + name, Bizarre, 2)
    self.assertRaisesRegex(ValueError, '1 is not a valid ' + name, Bizarre, 1)
    self.assertRaisesRegex(ValueError, '1 is not a valid ' + name, Bizarre, 1)
