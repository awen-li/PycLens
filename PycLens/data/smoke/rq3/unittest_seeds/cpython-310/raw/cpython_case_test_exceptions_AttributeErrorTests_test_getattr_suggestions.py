# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: AttributeErrorTests_test_getattr_suggestions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Substitution:
        noise = more_noise = a = bc = None
        blech = None

    class Elimination:
        noise = more_noise = a = bc = None
        blch = None

    class Addition:
        noise = more_noise = a = bc = None
        bluchin = None

    class SubstitutionOverElimination:
        blach = None
        bluc = None

    class SubstitutionOverAddition:
        blach = None
        bluchi = None

    class EliminationOverAddition:
        blucha = None
        bluc = None
    for (cls, suggestion) in [(Substitution, "'blech'?"), (Elimination, "'blch'?"), (Addition, "'bluchin'?"), (EliminationOverAddition, "'bluc'?"), (SubstitutionOverElimination, "'blach'?"), (SubstitutionOverAddition, "'blach'?")]:
        try:
            cls().bluch
        except AttributeError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
        self.assertIn(suggestion, err.getvalue())
