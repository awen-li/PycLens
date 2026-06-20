# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_hardlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for dedup in (True, False):
        with tempfile.TemporaryDirectory() as path:
            with self.subTest(dedup=dedup):
                script = script_helper.make_script(path, 'script', 'a = 0')
                pycs = get_pycs(script)
                args = ['-q', '-o 0', '-o 1', '-o 2']
                if dedup:
                    args.append('--hardlink-dupes')
                self.assertRunOK(path, *args)
                self.assertEqual(is_hardlink(pycs[0], pycs[1]), dedup)
                self.assertEqual(is_hardlink(pycs[1], pycs[2]), dedup)
                self.assertEqual(is_hardlink(pycs[0], pycs[2]), dedup)
