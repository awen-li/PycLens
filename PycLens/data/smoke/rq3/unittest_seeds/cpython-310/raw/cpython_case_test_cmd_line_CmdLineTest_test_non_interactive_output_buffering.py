# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cmd_line.py
# case: CmdLineTest_test_non_interactive_output_buffering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import sys\n            out = sys.stdout\n            print(out.isatty(), out.write_through, out.line_buffering)\n            err = sys.stderr\n            print(err.isatty(), err.write_through, err.line_buffering)\n        ')
    args = [sys.executable, '-c', code]
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    self.assertEqual(proc.stdout, 'False False False\nFalse False True\n')
