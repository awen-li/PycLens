# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_eq_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (eq, order, result) in [(False, False, 'neither'), (False, True, 'exception'), (True, False, 'eq_only'), (True, True, 'both')]:
        with self.subTest(eq=eq, order=order):
            if result == 'exception':
                with self.assertRaisesRegex(ValueError, 'eq must be true if order is true'):

                    @dataclass(eq=eq, order=order)
                    class C:
                        pass
            else:

                @dataclass(eq=eq, order=order)
                class C:
                    pass
                if result == 'neither':
                    self.assertNotIn('__eq__', C.__dict__)
                    self.assertNotIn('__lt__', C.__dict__)
                    self.assertNotIn('__le__', C.__dict__)
                    self.assertNotIn('__gt__', C.__dict__)
                    self.assertNotIn('__ge__', C.__dict__)
                elif result == 'both':
                    self.assertIn('__eq__', C.__dict__)
                    self.assertIn('__lt__', C.__dict__)
                    self.assertIn('__le__', C.__dict__)
                    self.assertIn('__gt__', C.__dict__)
                    self.assertIn('__ge__', C.__dict__)
                elif result == 'eq_only':
                    self.assertIn('__eq__', C.__dict__)
                    self.assertNotIn('__lt__', C.__dict__)
                    self.assertNotIn('__le__', C.__dict__)
                    self.assertNotIn('__gt__', C.__dict__)
                    self.assertNotIn('__ge__', C.__dict__)
                else:
                    assert False, f'unknown result {result!r}'
