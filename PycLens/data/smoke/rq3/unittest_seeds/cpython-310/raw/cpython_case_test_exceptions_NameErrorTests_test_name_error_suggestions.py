# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: NameErrorTests_test_name_error_suggestions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def Substitution():
        noise = more_noise = a = bc = None
        blech = None
        print(bluch)

    def Elimination():
        noise = more_noise = a = bc = None
        blch = None
        print(bluch)

    def Addition():
        noise = more_noise = a = bc = None
        bluchin = None
        print(bluch)

    def SubstitutionOverElimination():
        blach = None
        bluc = None
        print(bluch)

    def SubstitutionOverAddition():
        blach = None
        bluchi = None
        print(bluch)

    def EliminationOverAddition():
        blucha = None
        bluc = None
        print(bluch)
    for (func, suggestion) in [(Substitution, "'blech'?"), (Elimination, "'blch'?"), (Addition, "'bluchin'?"), (EliminationOverAddition, "'blucha'?"), (SubstitutionOverElimination, "'blach'?"), (SubstitutionOverAddition, "'blach'?")]:
        err = None
        try:
            func()
        except NameError as exc:
            with support.captured_stderr() as err:
                sys.__excepthook__(*sys.exc_info())
        self.assertIn(suggestion, err.getvalue())
