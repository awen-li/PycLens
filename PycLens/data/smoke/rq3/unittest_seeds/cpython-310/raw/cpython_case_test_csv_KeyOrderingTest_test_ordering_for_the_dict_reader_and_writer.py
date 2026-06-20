# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: KeyOrderingTest_test_ordering_for_the_dict_reader_and_writer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    resultset = set()
    for keys in permutations('abcde'):
        with TemporaryFile('w+', newline='', encoding='utf-8') as fileobject:
            dw = csv.DictWriter(fileobject, keys)
            dw.writeheader()
            fileobject.seek(0)
            dr = csv.DictReader(fileobject)
            kt = tuple(dr.fieldnames)
            self.assertEqual(keys, kt)
            resultset.add(kt)
    self.assertEqual(len(resultset), 120, 'Key ordering: some key permutations not collected (expected 120)')
