from Helpers.generics import GenericMethods
helpers = GenericMethods()


def verify_values(context, actual_value, expected_value):
    helpers.verify_values(context, actual_value, expected_value)


def verify_policy_values(context, locator, expected_value):
    actual_value = helpers.get_element_text(context, locator)
    verify_values(context, actual_value, expected_value)

