# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestNamedTemporaryFile_test_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = [b'spam\n', b'eggs\n', b'beans\n']

    def make_file():
        f = tempfile.NamedTemporaryFile(mode='w+b')
        f.write(b''.join(lines))
        f.seek(0)
        return f
    for (i, l) in enumerate(make_file()):
        self.assertEqual(l, lines[i])
    self.assertEqual(i, len(lines) - 1)
