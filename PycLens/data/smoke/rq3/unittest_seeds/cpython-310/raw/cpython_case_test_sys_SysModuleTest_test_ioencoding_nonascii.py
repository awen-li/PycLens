# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_ioencoding_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = dict(os.environ)
    env['PYTHONIOENCODING'] = ''
    p = subprocess.Popen([sys.executable, '-c', 'print(%a)' % os_helper.FS_NONASCII], stdout=subprocess.PIPE, env=env)
    out = p.communicate()[0].strip()
    self.assertEqual(out, os.fsencode(os_helper.FS_NONASCII))
