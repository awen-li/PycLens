# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_site.py
# case: StartupImportTests_test_startup_imports

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    popen = subprocess.Popen([sys.executable, '-I', '-c', 'import sys; print(repr(sys.path))'], stdout=subprocess.PIPE, encoding='utf-8')
    stdout = popen.communicate()[0]
    self.assertEqual(popen.returncode, 0, repr(stdout))
    isolated_paths = eval(stdout)
    for path in isolated_paths:
        pth_files = glob.glob(os.path.join(glob.escape(path), '*.pth'))
        if pth_files:
            self.skipTest(f'found {len(pth_files)} .pth files in: {path}')
    popen = subprocess.Popen([sys.executable, '-I', '-v', '-c', 'import sys; print(set(sys.modules))'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    (stdout, stderr) = popen.communicate()
    self.assertEqual(popen.returncode, 0, (stdout, stderr))
    modules = eval(stdout)
    self.assertIn('site', modules)
    re_mods = {'re', '_sre', 'sre_compile', 'sre_constants', 'sre_parse'}
    self.assertFalse(modules.intersection(re_mods), stderr)
    self.assertNotIn('locale', modules, stderr)
    self.assertNotIn('copyreg', modules, stderr)
    collection_mods = {'_collections', 'collections', 'functools', 'heapq', 'itertools', 'keyword', 'operator', 'reprlib', 'types', 'weakref'}.difference(sys.builtin_module_names)
    self.assertFalse(modules.intersection(collection_mods), stderr)
