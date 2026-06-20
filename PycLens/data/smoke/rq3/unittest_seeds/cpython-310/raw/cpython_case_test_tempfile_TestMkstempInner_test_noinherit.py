# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstempInner_test_noinherit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        v = 'v'
    else:
        v = 'q'
    file = self.do_create()
    self.assertEqual(os.get_inheritable(file.fd), False)
    fd = '%d' % file.fd
    try:
        me = __file__
    except NameError:
        me = sys.argv[0]
    tester = os.path.join(os.path.dirname(os.path.abspath(me)), 'tf_inherit_check.py')
    if sys.platform == 'win32':
        decorated = '"%s"' % sys.executable
        tester = '"%s"' % tester
    else:
        decorated = sys.executable
    retval = os.spawnl(os.P_WAIT, sys.executable, decorated, tester, v, fd)
    self.assertFalse(retval < 0, 'child process caught fatal signal %d' % -retval)
    self.assertFalse(retval > 0, 'child process reports failure %d' % retval)
