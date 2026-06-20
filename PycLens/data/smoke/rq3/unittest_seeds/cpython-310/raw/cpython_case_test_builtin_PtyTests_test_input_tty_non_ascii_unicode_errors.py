# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: PtyTests_test_input_tty_non_ascii_unicode_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.skip_if_readline()
    self.check_input_tty('prompté', b'quux\xe9', 'ascii')
