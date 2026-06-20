# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_input

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.write_testfile()
    fp = open(TESTFN, encoding='utf-8')
    savestdin = sys.stdin
    savestdout = sys.stdout
    try:
        sys.stdin = fp
        sys.stdout = BitBucket()
        self.assertEqual(input(), '1+1')
        self.assertEqual(input(), 'The quick brown fox jumps over the lazy dog.')
        self.assertEqual(input('testing\n'), 'Dear John')
        sys.stdout = savestdout
        sys.stdin.close()
        self.assertRaises(ValueError, input)
        sys.stdout = BitBucket()
        sys.stdin = io.StringIO('NULL\x00')
        self.assertRaises(TypeError, input, 42, 42)
        sys.stdin = io.StringIO("    'whitespace'")
        self.assertEqual(input(), "    'whitespace'")
        sys.stdin = io.StringIO()
        self.assertRaises(EOFError, input)
        del sys.stdout
        self.assertRaises(RuntimeError, input, 'prompt')
        del sys.stdin
        self.assertRaises(RuntimeError, input, 'prompt')
    finally:
        sys.stdin = savestdin
        sys.stdout = savestdout
        fp.close()
