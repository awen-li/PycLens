# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestBytes_test_byte_filenames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fna = b'\xb3odz.txt'
    fnb = b'\xc5\x82odz.txt'
    a = [b'\xa3odz is a city in Poland.']
    b = [b'\xc5\x81odz is a city in Poland.']
    check = self.check
    unified = difflib.unified_diff
    context = difflib.context_diff
    check(difflib.diff_bytes(unified, a, b, fna, fnb))
    check(difflib.diff_bytes(context, a, b, fna, fnb))

    def assertDiff(expect, actual):
        actual = list(actual)
        self.assertEqual(len(expect), len(actual))
        for (e, a) in zip(expect, actual):
            self.assertEqual(e, a)
    expect = [b'--- \xb3odz.txt', b'+++ \xc5\x82odz.txt', b'@@ -1 +1 @@', b'-\xa3odz is a city in Poland.', b'+\xc5\x81odz is a city in Poland.']
    actual = difflib.diff_bytes(unified, a, b, fna, fnb, lineterm=b'')
    assertDiff(expect, actual)
    datea = b'2005-03-18'
    dateb = b'2005-03-19'
    check(difflib.diff_bytes(unified, a, b, fna, fnb, datea, dateb))
    check(difflib.diff_bytes(context, a, b, fna, fnb, datea, dateb))
    expect = [b'--- \xb3odz.txt\t2005-03-18', b'+++ \xc5\x82odz.txt\t2005-03-19', b'@@ -1 +1 @@', b'-\xa3odz is a city in Poland.', b'+\xc5\x81odz is a city in Poland.']
    actual = difflib.diff_bytes(unified, a, b, fna, fnb, datea, dateb, lineterm=b'')
    assertDiff(expect, actual)
