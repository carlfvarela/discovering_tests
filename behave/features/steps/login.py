from behave import *


@given(u'the user has the correct credentials')
def step_impl(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')


@when(u'the user enters username')
def step_impl(context):
    context.browser.find_element_by_name('email').send_keys('test@drugdev.com')


@when(u'the user enters password')
def step_impl(context):
    context.browser.find_element_by_name('password').send_keys('supers3cret')


@when(u'clicks Login')
def step_impl(context):
    context.browser.find_element_by_xpath("//*[@id=\"login-form\"]/fieldset/div[4]/button").click()


@then(u'the user is presented with a welcome message')
def step_impl(context):
    context.browser.find_element_by_xpath("/html/body/article")


@given(u'the user has the incorrect credentials')
def step_impl(context):
    context.browser.get('https://sprinkle-burn.glitch.me/')
    context.browser.find_element_by_name('email').send_keys('tesst@drugdev.com')
    context.browser.find_element_by_name('password').send_keys('superss3cret')
    context.browser.find_element_by_xpath("//*[@id=\"login-form\"]/fieldset/div[4]/button").click()


@then(u'the user is presented with a error message')
def step_impl(context):
    context.browser.find_element_by_xpath("//*[@id=\"login-error-box\"]")
