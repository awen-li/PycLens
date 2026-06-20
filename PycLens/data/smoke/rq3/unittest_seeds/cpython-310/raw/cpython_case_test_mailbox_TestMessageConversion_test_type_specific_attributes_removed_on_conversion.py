# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailbox.py
# case: TestMessageConversion_test_type_specific_attributes_removed_on_conversion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    reference = {class_: class_(_sample_message).__dict__ for class_ in self.all_mailbox_types}
    for class1 in self.all_mailbox_types:
        for class2 in self.all_mailbox_types:
            if class1 is class2:
                continue
            source = class1(_sample_message)
            target = class2(source)
            type_specific = [a for a in reference[class1] if a not in reference[class2]]
            for attr in type_specific:
                self.assertNotIn(attr, target.__dict__, 'while converting {} to {}'.format(class1, class2))
