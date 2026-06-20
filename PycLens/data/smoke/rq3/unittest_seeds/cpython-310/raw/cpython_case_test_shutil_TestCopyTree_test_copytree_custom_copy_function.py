# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_shutil.py
# case: TestCopyTree_test_copytree_custom_copy_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def custom_cpfun(a, b):
        flag.append(None)
        self.assertIsInstance(a, str)
        self.assertIsInstance(b, str)
        self.assertEqual(a, os.path.join(src, 'foo'))
        self.assertEqual(b, os.path.join(dst, 'foo'))
    flag = []
    src = self.mkdtemp()
    dst = tempfile.mktemp(dir=self.mkdtemp())
    with open(os.path.join(src, 'foo'), 'w', encoding='utf-8') as f:
        f.close()
    shutil.copytree(src, dst, copy_function=custom_cpfun)
    self.assertEqual(len(flag), 1)
