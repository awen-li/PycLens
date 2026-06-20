# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: PicklingTests_test_issue24097

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class S(str):
        pass

    class A:
        __slotnames__ = [S('spam')]

        def __getattr__(self, attr):
            if attr == 'spam':
                A.__slotnames__[:] = [S('spam')]
                return 42
            else:
                raise AttributeError
    import copyreg
    expected = (copyreg.__newobj__, (A,), (None, {'spam': 42}), None, None)
    self.assertEqual(A().__reduce_ex__(2), expected)
