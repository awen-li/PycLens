# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_literal_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for n in (0, 1, 6, 256, 400):
        items = [(''.join(random.sample(string.ascii_letters, 8)), i) for i in range(n)]
        random.shuffle(items)
        formatted_items = ('{!r}: {:d}'.format(k, v) for (k, v) in items)
        dictliteral = '{' + ', '.join(formatted_items) + '}'
        self.assertEqual(eval(dictliteral), dict(items))
