from behave import step

TIMEOUT = 5000

@step('Navigate to the selection page')
def setup(context):
    sb = context.sb
    sb.open('https://learning.elucidat.com/course/5c9126fd760e5-611a53751213a')
    sb.clear_local_storage()
    sb.find_element('//strong[normalize-space()="FINDING THE TRUTH"]', timeout=TIMEOUT)
    sb.find_element('//a[@id="pa_5c9126fe3b767_p15577f075e9-textButton"]').click()
    sb.assert_element('//em[normalize-space()="Press on a case to get started."]', timeout=TIMEOUT)