# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_cmd_line

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    arg = 'hé€'.encode('utf-8')
    arg_utf8 = arg.decode('utf-8')
    arg_ascii = arg.decode('ascii', 'surrogateescape')
    code = 'import locale, sys; print("%s:%s" % (locale.getpreferredencoding(), ascii(sys.argv[1:])))'

    def check(utf8_opt, expected, **kw):
        out = self.get_output('-X', utf8_opt, '-c', code, arg, **kw)
        args = out.partition(':')[2].rstrip()
        self.assertEqual(args, ascii(expected), out)
    check('utf8', [arg_utf8])
    for loc in POSIX_LOCALES:
        with self.subTest(LC_ALL=loc):
            check('utf8', [arg_utf8], LC_ALL=loc)
    if sys.platform == 'darwin' or support.is_android or VXWORKS:
        c_arg = arg_utf8
    elif sys.platform.startswith('aix'):
        c_arg = arg.decode('iso-8859-1')
    else:
        c_arg = arg_ascii
    for loc in POSIX_LOCALES:
        with self.subTest(LC_ALL=loc):
            check('utf8=0', [c_arg], LC_ALL=loc)
