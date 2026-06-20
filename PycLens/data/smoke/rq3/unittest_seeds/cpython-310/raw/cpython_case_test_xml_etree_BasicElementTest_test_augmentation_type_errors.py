# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_augmentation_type_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.Element('joe')
    self.assertRaises(TypeError, e.append, 'b')
    self.assertRaises(TypeError, e.extend, [ET.Element('bar'), 'foo'])
    self.assertRaises(TypeError, e.insert, 0, 'foo')
    e[:] = [ET.Element('bar')]
    with self.assertRaises(TypeError):
        e[0] = 'foo'
    with self.assertRaises(TypeError):
        e[:] = [ET.Element('bar'), 'foo']
    if hasattr(e, '__setstate__'):
        state = {'tag': 'tag', '_children': [None], 'attrib': 'attr', 'tail': 'tail', 'text': 'text'}
        self.assertRaises(TypeError, e.__setstate__, state)
    if hasattr(e, '__deepcopy__'):

        class E(ET.Element):

            def __deepcopy__(self, memo):
                return None
        e[:] = [E('bar')]
        self.assertRaises(TypeError, copy.deepcopy, e)
