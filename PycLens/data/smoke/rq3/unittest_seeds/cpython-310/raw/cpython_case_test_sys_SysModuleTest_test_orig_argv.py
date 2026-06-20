# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SysModuleTest_test_orig_argv

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            print(sys.argv)\n            print(sys.orig_argv)\n        ')
    args = [sys.executable, '-I', '-X', 'utf8', '-c', code, 'arg']
    proc = subprocess.run(args, check=True, capture_output=True, text=True)
    expected = [repr(['-c', 'arg']), repr(args)]
    self.assertEqual(proc.stdout.rstrip().splitlines(), expected, proc)
