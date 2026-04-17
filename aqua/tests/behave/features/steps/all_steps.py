# -*- coding: utf-8 -*-
import re
import time
import requests
from lib2to3.fixes.fix_input import context
from struct import pack_into

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from _locators import Locators


# ========================================================================================== Gherkin Functions ==========================================================================================
# Write all the tests gherkin function definitions here 

# Delays execution for the specified number of seconds
@given(u'Sleep "{time_seconds}" seconds')
@when(u'Sleep "{time_seconds}" seconds')
@then(u'Sleep "{time_seconds}" seconds')
def step_impl(context, time_seconds): #@DuplicatedSignature
    # Pass test
    time.sleep(int(time_seconds))
    assert True


# Test step designed to pass
@given(u'Sample step pass')
@when(u'Sample step pass')
@then(u'Sample step pass')
def step_impl(context): #@DuplicatedSignature
    # Pass test
	assert True


# Test step designed to fail
@given(u'Sample step fail')
@when(u'Sample step fail')
@then(u'Sample step fail')
def step_impl(context): #@DuplicatedSignature
    # Pass test
	assert False


@given(u'New Acrom session')
@when(u'New Acrom session')
def step_impl(context): #@DuplicatedSignature
	try:
		context.browser.get("https://acrom.ro")
	except Exception as e:
		print("\t\t[DEBUG] Exception: " + str(e))
		assert False


@given(u'Page "{text}" is diplayed')
@when(u'Page "{text}" is diplayed')
@then(u'Page "{text}" is diplayed')
def step_impl(context, text): #@DuplicatedSignature
    try:
        context.browser.find_element(By.XPATH, '//div//h1[contains(text(), "' + text + '")]')
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False


@given(u'Page contains menu "{menu}"')
@when(u'Page contains menu "{menu}"')
@then(u'Page contains menu "{menu}"')
def step_impl(context, menu): #@DuplicatedSignature
    try:
        context.browser.find_element(By.XPATH, '//li[contains(@class, "submenu")]//a[contains(text(), "' + menu + '")]')
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False


@given(u'Page select menu "{menu}"')
@when(u'Page select menu "{menu}"')
@then(u'Page select menu "{menu}"')
def step_impl(context, menu): #@DuplicatedSignature
    try:
        select = context.browser.find_element(By.XPATH, '//li[contains(@class, "submenu")]//a[contains(text(), "' + menu + '")]')
        select.click()
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False


@given(u'Page contains text "{text}"')
@when(u'Page contains text "{text}"')
@then(u'Page contains text "{text}"')
def step_impl(context, text): #@DuplicatedSignature
    try:
        context.browser.find_element(By.XPATH, '//h1[contains(text(), "' + text + '")]')
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False