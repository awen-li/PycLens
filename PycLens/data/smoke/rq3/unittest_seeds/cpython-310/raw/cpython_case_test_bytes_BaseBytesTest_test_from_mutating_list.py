# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_from_mutating_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __index__(self):
            a.clear()
            return 42
    a = [X(), X()]
    self.assertEqual(bytes(a), b'*')

    class Y:

        def __index__(self):
            if len(a) < 1000:
                a.append(self)
            return 42
    a = [Y()]
    self.assertEqual(bytes(a), b'*' * 1000)
