# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: ExceptHookTest_test_excepthook_bytes_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', BytesWarning)
        try:
            raise SyntaxError('msg', (b'bytes_filename', 123, 0, 'text'))
        except SyntaxError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
    err = err.getvalue()
    self.assertIn('  File "b\'bytes_filename\'", line 123\n', err)
    self.assertIn('    text\n', err)
    self.assertTrue(err.endswith('SyntaxError: msg\n'))
