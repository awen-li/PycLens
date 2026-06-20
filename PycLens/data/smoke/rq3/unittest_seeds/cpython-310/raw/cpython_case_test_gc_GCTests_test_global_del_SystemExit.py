# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_global_del_SystemExit

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = "if 1:\n            class ClassWithDel:\n                def __del__(self):\n                    print('__del__ called')\n            a = ClassWithDel()\n            a.link = a\n            raise SystemExit(0)"
    self.addCleanup(unlink, TESTFN)
    with open(TESTFN, 'w', encoding='utf-8') as script:
        script.write(code)
    (rc, out, err) = assert_python_ok(TESTFN)
    self.assertEqual(out.strip(), b'__del__ called')
