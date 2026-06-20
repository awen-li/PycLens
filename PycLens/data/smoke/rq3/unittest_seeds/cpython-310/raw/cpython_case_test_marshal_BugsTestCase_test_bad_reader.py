# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: BugsTestCase_test_bad_reader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadReader(io.BytesIO):

        def readinto(self, buf):
            n = super().readinto(buf)
            if n is not None and n > 4:
                n += 10 ** 6
            return n
    for value in (1.0, 1j, b'0123456789', '0123456789'):
        self.assertRaises(ValueError, marshal.load, BadReader(marshal.dumps(value)))
