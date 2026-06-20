# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_check_encoding_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = self.io.__name__
    filename = __file__
    invalid = 'Boom, Shaka Laka, Boom!'
    code = textwrap.dedent(f'\n            import sys\n            from {mod} import open, TextIOWrapper\n\n            try:\n                open({filename!r}, encoding={invalid!r})\n            except LookupError:\n                pass\n            else:\n                sys.exit(21)\n\n            try:\n                open({filename!r}, errors={invalid!r})\n            except LookupError:\n                pass\n            else:\n                sys.exit(22)\n\n            fp = open({filename!r}, "rb")\n            with fp:\n                try:\n                    TextIOWrapper(fp, encoding={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(23)\n\n                try:\n                    TextIOWrapper(fp, errors={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(24)\n\n            sys.exit(10)\n        ')
    proc = assert_python_failure('-X', 'dev', '-c', code)
    self.assertEqual(proc.rc, 10, proc)
