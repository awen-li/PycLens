# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_marshal.py
# case: IntTestCase_test_int64

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxint64 = (1 << 63) - 1
    minint64 = -maxint64 - 1
    for base in (maxint64, minint64, -maxint64, -(minint64 >> 1)):
        while base:
            s = b'I' + int.to_bytes(base, 8, 'little', signed=True)
            got = marshal.loads(s)
            self.assertEqual(base, got)
            if base == -1:
                base = 0
            else:
                base >>= 1
    got = marshal.loads(b'I\xfe\xdc\xba\x98vT2\x10')
    self.assertEqual(got, 1167088121787636990)
    got = marshal.loads(b'I\x01#Eg\x89\xab\xcd\xef')
    self.assertEqual(got, -1167088121787636991)
    got = marshal.loads(b'I\x08\x19*;L]n\x7f')
    self.assertEqual(got, 9182379272246532360)
    got = marshal.loads(b'I\xf7\xe6\xd5\xc4\xb3\xa2\x91\x80')
    self.assertEqual(got, -9182379272246532361)
