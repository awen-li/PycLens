# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_gc_ordinary_module_at_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with temp_dir() as script_dir:
        module = "if 1:\n                class C:\n                    def __del__(self):\n                        print('__del__ called')\n                l = [C()]\n                l.append(l)\n                "
        code = 'if 1:\n                import sys\n                sys.path.insert(0, %r)\n                import gctest\n                ' % (script_dir,)
        make_script(script_dir, 'gctest', module)
        (rc, out, err) = assert_python_ok('-c', code)
        self.assertEqual(out.strip(), b'__del__ called')
