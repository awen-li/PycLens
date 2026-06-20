# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_expanduser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tester('ntpath.expanduser("test")', 'test')
    with os_helper.EnvironmentVarGuard() as env:
        env.clear()
        tester('ntpath.expanduser("~test")', '~test')
        env['HOMEDRIVE'] = 'C:\\'
        env['HOMEPATH'] = 'Users\\eric'
        env['USERNAME'] = 'eric'
        tester('ntpath.expanduser("~test")', 'C:\\Users\\test')
        tester('ntpath.expanduser("~")', 'C:\\Users\\eric')
        del env['HOMEDRIVE']
        tester('ntpath.expanduser("~test")', 'Users\\test')
        tester('ntpath.expanduser("~")', 'Users\\eric')
        env.clear()
        env['USERPROFILE'] = 'C:\\Users\\eric'
        env['USERNAME'] = 'eric'
        tester('ntpath.expanduser("~test")', 'C:\\Users\\test')
        tester('ntpath.expanduser("~")', 'C:\\Users\\eric')
        tester('ntpath.expanduser("~test\\foo\\bar")', 'C:\\Users\\test\\foo\\bar')
        tester('ntpath.expanduser("~test/foo/bar")', 'C:\\Users\\test/foo/bar')
        tester('ntpath.expanduser("~\\foo\\bar")', 'C:\\Users\\eric\\foo\\bar')
        tester('ntpath.expanduser("~/foo/bar")', 'C:\\Users\\eric/foo/bar')
        env.clear()
        env['HOME'] = 'F:\\'
        env['USERPROFILE'] = 'C:\\Users\\eric'
        env['USERNAME'] = 'eric'
        tester('ntpath.expanduser("~test")', 'C:\\Users\\test')
        tester('ntpath.expanduser("~")', 'C:\\Users\\eric')
        env.clear()
        env['USERPROFILE'] = 'C:\\Users\\eric'
        env['USERNAME'] = 'idle'
        tester('ntpath.expanduser("~test")', '~test')
        tester('ntpath.expanduser("~")', 'C:\\Users\\eric')
