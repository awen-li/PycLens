# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignaturePrivateHelpers_test_signature_strip_non_python_syntax

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._strip_non_python_syntax('($module, /, path, mode, *, dir_fd=None, ' + 'effective_ids=False,\n       follow_symlinks=True)', '(module, path, mode, *, dir_fd=None, ' + 'effective_ids=False, follow_symlinks=True)', 0, 0)
    self._strip_non_python_syntax('($module, word, salt, /)', '(module, word, salt)', 0, 2)
    self._strip_non_python_syntax('(x, y=None, z=None, /)', '(x, y=None, z=None)', None, 2)
    self._strip_non_python_syntax('(x, y=None, z=None)', '(x, y=None, z=None)', None, None)
    self._strip_non_python_syntax('(x,\n    y=None,\n      z = None  )', '(x, y=None, z=None)', None, None)
    self._strip_non_python_syntax('', '', None, None)
    self._strip_non_python_syntax(None, None, None, None)
