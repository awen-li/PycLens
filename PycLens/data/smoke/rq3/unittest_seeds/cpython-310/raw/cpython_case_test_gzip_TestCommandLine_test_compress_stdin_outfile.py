# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_compress_stdin_outfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = (sys.executable, '-m', 'gzip')
    with Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
        (out, err) = proc.communicate(self.data)
    self.assertEqual(err, b'')
    self.assertEqual(out[:2], b'\x1f\x8b')
