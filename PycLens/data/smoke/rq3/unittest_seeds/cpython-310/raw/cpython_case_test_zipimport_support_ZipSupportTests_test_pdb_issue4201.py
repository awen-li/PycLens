# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipimport_support.py
# case: ZipSupportTests_test_pdb_issue4201

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_src = textwrap.dedent('                    def f():\n                        pass\n\n                    import pdb\n                    pdb.Pdb(nosigint=True).runcall(f)\n                    ')
    with os_helper.temp_dir() as d:
        script_name = make_script(d, 'script', test_src)
        p = spawn_python(script_name)
        p.stdin.write(b'l\n')
        data = kill_python(p)
        self.assertIn(os.path.normcase(script_name.encode('utf-8')), data)
        (zip_name, run_name) = make_zip_script(d, 'test_zip', script_name, '__main__.py')
        p = spawn_python(zip_name)
        p.stdin.write(b'l\n')
        data = kill_python(p)
        self.assertIn(os.path.normcase(run_name.encode('utf-8')), data)
