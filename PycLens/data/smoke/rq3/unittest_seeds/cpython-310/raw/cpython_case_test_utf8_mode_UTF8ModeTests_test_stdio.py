# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8_mode.py
# case: UTF8ModeTests_test_stdio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            print(f"stdin: {sys.stdin.encoding}/{sys.stdin.errors}")\n            print(f"stdout: {sys.stdout.encoding}/{sys.stdout.errors}")\n            print(f"stderr: {sys.stderr.encoding}/{sys.stderr.errors}")\n        ')
    out = self.get_output('-X', 'utf8', '-c', code, PYTHONIOENCODING='')
    self.assertEqual(out.splitlines(), ['stdin: utf-8/surrogateescape', 'stdout: utf-8/surrogateescape', 'stderr: utf-8/backslashreplace'])
    out = self.get_output('-X', 'utf8', '-c', code, PYTHONIOENCODING='latin1')
    self.assertEqual(out.splitlines(), ['stdin: iso8859-1/strict', 'stdout: iso8859-1/strict', 'stderr: iso8859-1/backslashreplace'])
    out = self.get_output('-X', 'utf8', '-c', code, PYTHONIOENCODING=':namereplace')
    self.assertEqual(out.splitlines(), ['stdin: utf-8/namereplace', 'stdout: utf-8/namereplace', 'stderr: utf-8/backslashreplace'])
