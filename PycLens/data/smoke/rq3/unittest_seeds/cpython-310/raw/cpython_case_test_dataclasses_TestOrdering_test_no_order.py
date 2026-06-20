# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestOrdering_test_no_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(order=False)
    class C:
        x: int
    self.assertNotIn('__le__', C.__dict__)
    self.assertNotIn('__lt__', C.__dict__)
    self.assertNotIn('__ge__', C.__dict__)
    self.assertNotIn('__gt__', C.__dict__)

    @dataclass(order=False)
    class C:
        x: int

        def __lt__(self, other):
            return False
    self.assertNotIn('__le__', C.__dict__)
    self.assertNotIn('__ge__', C.__dict__)
    self.assertNotIn('__gt__', C.__dict__)
