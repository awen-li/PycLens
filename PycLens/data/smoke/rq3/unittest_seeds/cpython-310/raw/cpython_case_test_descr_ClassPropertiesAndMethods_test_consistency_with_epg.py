# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_consistency_with_epg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Pane(object):
        pass

    class ScrollingMixin(object):
        pass

    class EditingMixin(object):
        pass

    class ScrollablePane(Pane, ScrollingMixin):
        pass

    class EditablePane(Pane, EditingMixin):
        pass

    class EditableScrollablePane(ScrollablePane, EditablePane):
        pass
    self.assertEqual(EditableScrollablePane.__mro__, (EditableScrollablePane, ScrollablePane, EditablePane, Pane, ScrollingMixin, EditingMixin, object))
