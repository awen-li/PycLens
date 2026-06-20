# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_check_encoding_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encodings = ('ascii', 'utf8', 'latin1')
    invalid = 'Boom, Shaka Laka, Boom!'
    code = textwrap.dedent(f"\n            import sys\n            encodings = {encodings!r}\n\n            for data in (b'', b'short string'):\n                try:\n                    str(data, encoding={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(21)\n\n                try:\n                    str(data, errors={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(22)\n\n                for encoding in encodings:\n                    try:\n                        str(data, encoding, errors={invalid!r})\n                    except LookupError:\n                        pass\n                    else:\n                        sys.exit(22)\n\n            for data in ('', 'short string'):\n                try:\n                    data.encode(encoding={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(23)\n\n                try:\n                    data.encode(errors={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(24)\n\n                for encoding in encodings:\n                    try:\n                        data.encode(encoding, errors={invalid!r})\n                    except LookupError:\n                        pass\n                    else:\n                        sys.exit(24)\n\n            sys.exit(10)\n        ")
    proc = assert_python_failure('-X', 'dev', '-c', code)
    self.assertEqual(proc.rc, 10, proc)
