# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_regexps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def by(s):
        return bytearray(map(ord, s))
    b = by('Hello, world')
    self.assertEqual(re.findall(b'\\w+', b), [by('Hello'), by('world')])
