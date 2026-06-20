# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_written

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def read_written(self, what):
        f = io.BytesIO()
        getattr(aifc, '_write_' + what)(f, x)
        f.seek(0)
        return getattr(aifc, '_read_' + what)(f)
    for x in (-1, 0, 0.1, 1):
        self.assertEqual(read_written(x, 'float'), x)
    for x in (float('NaN'), float('Inf')):
        self.assertEqual(read_written(x, 'float'), aifc._HUGE_VAL)
    for x in (b'', b'foo', b'a' * 255):
        self.assertEqual(read_written(x, 'string'), x)
    for x in (-2147483647, -1, 0, 1, 2147483647):
        self.assertEqual(read_written(x, 'long'), x)
    for x in (0, 1, 4294967295):
        self.assertEqual(read_written(x, 'ulong'), x)
    for x in (-32767, -1, 0, 1, 32767):
        self.assertEqual(read_written(x, 'short'), x)
    for x in (0, 1, 65535):
        self.assertEqual(read_written(x, 'ushort'), x)
