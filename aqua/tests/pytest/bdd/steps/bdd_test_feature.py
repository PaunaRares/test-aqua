from pytest_bdd import given, when, then, parsers, scenarios

scenarios("test.feature")

@given("Common precondition for all scenarios")
def common_precondition():
    assert True


@given("Precondition")
def precondition():
    assert True


@when("This action is performed")
def this_action_is_performed():
    assert True


@when("This action")
def this_action():
    assert True


@then("Expected outcome")
def expected_outcome():
    assert True
