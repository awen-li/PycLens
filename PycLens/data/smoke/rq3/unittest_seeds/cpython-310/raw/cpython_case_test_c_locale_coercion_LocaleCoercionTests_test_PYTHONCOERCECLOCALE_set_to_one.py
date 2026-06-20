# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_c_locale_coercion.py
# case: LocaleCoercionTests_test_PYTHONCOERCECLOCALE_set_to_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_loc = locale.setlocale(locale.LC_CTYPE, None)
    self.addCleanup(locale.setlocale, locale.LC_CTYPE, old_loc)
    try:
        loc = locale.setlocale(locale.LC_CTYPE, '')
    except locale.Error as e:
        self.skipTest(str(e))
    if loc == 'C':
        self.skipTest('test requires LC_CTYPE locale different than C')
    if loc in TARGET_LOCALES:
        self.skipTest('coerced LC_CTYPE locale: %s' % loc)
    code = 'import locale; print(locale.setlocale(locale.LC_CTYPE, None))'
    env = dict(os.environ, PYTHONCOERCECLOCALE='1')
    cmd = subprocess.run([sys.executable, '-c', code], stdout=subprocess.PIPE, env=env, text=True)
    self.assertEqual(cmd.stdout.rstrip(), loc)
