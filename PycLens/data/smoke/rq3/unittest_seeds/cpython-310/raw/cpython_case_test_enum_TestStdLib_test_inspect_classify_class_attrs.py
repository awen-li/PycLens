# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestStdLib_test_inspect_classify_class_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from inspect import Attribute
    values = [Attribute(name='__class__', kind='data', defining_class=object, object=EnumMeta), Attribute(name='__doc__', kind='data', defining_class=self.Color, object='An enumeration.'), Attribute(name='__members__', kind='property', defining_class=EnumMeta, object=EnumMeta.__members__), Attribute(name='__module__', kind='data', defining_class=self.Color, object=__name__), Attribute(name='blue', kind='data', defining_class=self.Color, object=self.Color.blue), Attribute(name='green', kind='data', defining_class=self.Color, object=self.Color.green), Attribute(name='red', kind='data', defining_class=self.Color, object=self.Color.red), Attribute(name='name', kind='data', defining_class=Enum, object=Enum.__dict__['name']), Attribute(name='value', kind='data', defining_class=Enum, object=Enum.__dict__['value'])]
    values.sort(key=lambda item: item.name)
    result = list(inspect.classify_class_attrs(self.Color))
    result.sort(key=lambda item: item.name)
    failed = False
    for (v, r) in zip(values, result):
        if r != v:
            print('\n%s\n%s\n%s\n%s\n' % ('=' * 75, r, v, '=' * 75), sep='')
            failed = True
    if failed:
        self.fail('result does not equal expected, see print above')
