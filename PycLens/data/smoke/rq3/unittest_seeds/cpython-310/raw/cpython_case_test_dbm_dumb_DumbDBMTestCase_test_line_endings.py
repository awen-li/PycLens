# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dbm_dumb.py
# case: DumbDBMTestCase_test_line_endings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with contextlib.closing(dumbdbm.open(_fname)) as f:
        f[b'1'] = b'hello'
        f[b'2'] = b'hello2'
    with io.open(_fname + '.dir', 'rb') as file:
        data = file.read()
    if os.linesep == '\n':
        data = data.replace(b'\n', b'\r\n')
    else:
        data = data.replace(b'\r\n', b'\n')
    with io.open(_fname + '.dir', 'wb') as file:
        file.write(data)
    f = dumbdbm.open(_fname)
    self.assertEqual(f[b'1'], b'hello')
    self.assertEqual(f[b'2'], b'hello2')
