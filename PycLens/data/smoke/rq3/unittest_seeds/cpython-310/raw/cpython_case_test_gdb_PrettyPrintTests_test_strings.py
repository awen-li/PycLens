# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gdb.py
# case: PrettyPrintTests_test_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (out, err) = run_gdb('--eval-command', 'python import locale; print(locale.getpreferredencoding())')
    encoding = out.rstrip()
    if err or not encoding:
        raise RuntimeError(f'unable to determine the preferred encoding of embedded Python in GDB: {err}')

    def check_repr(text):
        try:
            text.encode(encoding)
        except UnicodeEncodeError:
            self.assertGdbRepr(text, ascii(text))
        else:
            self.assertGdbRepr(text)
    self.assertGdbRepr('')
    self.assertGdbRepr('And now for something hopefully the same')
    self.assertGdbRepr('string with embedded NUL here \x00 and then some more text')
    check_repr('☠')
    check_repr('文字化け')
    check_repr(chr(119073))
