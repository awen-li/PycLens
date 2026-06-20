# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_comm_kludge_compname_even

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'FORM' + struct.pack('>L', 4) + b'AIFC'
    b += b'COMM' + struct.pack('>LhlhhLL', 18, 1, 0, 8, 16384 | 12, 11025 << 18, 0)
    b += b'NONE' + struct.pack('B', 4) + b'even' + b'\x00'
    b += b'SSND' + struct.pack('>L', 8) + b'\x00' * 8
    with self.assertWarns(UserWarning) as cm:
        f = aifc.open(io.BytesIO(b))
    self.assertEqual(str(cm.warning), 'Warning: bad COMM chunk size')
    self.assertEqual(f.getcompname(), b'even')
