# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xxtestfuzz.py
# case: TestFuzzer_test_sample_input_smoke_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _xxtestfuzz.run(b'')
    _xxtestfuzz.run(b'\x00')
    _xxtestfuzz.run(b'{')
    _xxtestfuzz.run(b' ')
    _xxtestfuzz.run(b'x')
    _xxtestfuzz.run(b'1')
    _xxtestfuzz.run(b'AAAAAAA')
    _xxtestfuzz.run(b'AAAAAA\x00')
