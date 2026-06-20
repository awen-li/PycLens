# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_check_encoding_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    invalid = 'Boom, Shaka Laka, Boom!'
    encodings = ('ascii', 'utf8', 'latin1')
    code = textwrap.dedent(f"\n            import sys\n            type2test = {self.type2test.__name__}\n            encodings = {encodings!r}\n\n            for data in ('', 'short string'):\n                try:\n                    type2test(data, encoding={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(21)\n\n                for encoding in encodings:\n                    try:\n                        type2test(data, encoding=encoding, errors={invalid!r})\n                    except LookupError:\n                        pass\n                    else:\n                        sys.exit(22)\n\n            for data in (b'', b'short string'):\n                data = type2test(data)\n                print(repr(data))\n                try:\n                    data.decode(encoding={invalid!r})\n                except LookupError:\n                    sys.exit(10)\n                else:\n                    sys.exit(23)\n\n                try:\n                    data.decode(errors={invalid!r})\n                except LookupError:\n                    pass\n                else:\n                    sys.exit(24)\n\n                for encoding in encodings:\n                    try:\n                        data.decode(encoding=encoding, errors={invalid!r})\n                    except LookupError:\n                        pass\n                    else:\n                        sys.exit(25)\n\n            sys.exit(10)\n        ")
    proc = assert_python_failure('-X', 'dev', '-c', code)
    self.assertEqual(proc.rc, 10, proc)
