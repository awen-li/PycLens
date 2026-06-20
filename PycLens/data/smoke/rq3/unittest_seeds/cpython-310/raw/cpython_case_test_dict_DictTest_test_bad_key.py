# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_bad_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CustomException(Exception):
        pass

    class BadDictKey:

        def __hash__(self):
            return hash(self.__class__)

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                raise CustomException
            return other
    d = {}
    x1 = BadDictKey()
    x2 = BadDictKey()
    d[x1] = 1
    for stmt in ['d[x2] = 2', 'z = d[x2]', 'x2 in d', 'd.get(x2)', 'd.setdefault(x2, 42)', 'd.pop(x2)', 'd.update({x2: 2})']:
        with self.assertRaises(CustomException):
            exec(stmt, locals())
