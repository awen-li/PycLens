# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: StringModuleTest_test_formatter_field_name_split

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def split(name):
        items = list(_string.formatter_field_name_split(name))
        items[1] = list(items[1])
        return items
    self.assertEqual(split('obj'), ['obj', []])
    self.assertEqual(split('obj.arg'), ['obj', [(True, 'arg')]])
    self.assertEqual(split('obj[key]'), ['obj', [(False, 'key')]])
    self.assertEqual(split('obj.arg[key1][key2]'), ['obj', [(True, 'arg'), (False, 'key1'), (False, 'key2')]])
    self.assertRaises(TypeError, _string.formatter_field_name_split, 1)
