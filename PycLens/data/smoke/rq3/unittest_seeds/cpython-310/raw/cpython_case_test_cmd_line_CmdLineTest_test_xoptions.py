# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_xoptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def get_xoptions(*args):
        args = (sys.executable, '-E') + args
        args += ('-c', 'import sys; print(sys._xoptions)')
        out = subprocess.check_output(args)
        opts = eval(out.splitlines()[0])
        return opts
    opts = get_xoptions()
    self.assertEqual(opts, {})
    opts = get_xoptions('-Xa', '-Xb=c,d=e')
    self.assertEqual(opts, {'a': True, 'b': 'c,d=e'})
