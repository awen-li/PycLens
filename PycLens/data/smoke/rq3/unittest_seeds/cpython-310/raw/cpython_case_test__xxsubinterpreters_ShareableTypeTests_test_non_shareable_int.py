# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ShareableTypeTests_test_non_shareable_int

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ints = [sys.maxsize + 1, -sys.maxsize - 2, 2 ** 1000]
    for i in ints:
        with self.subTest(i):
            with self.assertRaises(OverflowError):
                interpreters.channel_send(self.cid, i)
