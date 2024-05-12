from time import sleep

from behave import step
from bs4 import BeautifulSoup


@step('User clicks on Judge This')
def select_judge_button(context):
    sb = context.sb
    sb.find_element('//span[contains(text(), "JUDGE THIS")]').click()

@step('Assert user is shown verdict page')
def check_verdict_page(context):
    sb = context.sb
    sb.assert_text("Is Kevin guilty?", '//div[@data-role="page.intro__text"]')
    sb.assert_element('//span[contains(text(), "VOTE")]')

@step('Assert user {vote_condition} click on Vote')
def click_vote(context, vote_condition):
    sb = context.sb
    vote = sb.get_attribute('//i[contains(@class,"ti ti-link-external")]', 'class')
    vote_button = sb.find_element('//i[contains(@class,"ti ti-link-external")]')
    if vote_condition == "can't":
        sb.assert_true('ti-lock' in vote, msg="User cannot vote")
        vote_button.click()
        check_verdict_page(context)
    elif vote_condition == "can":
        sb.assert_true('ti-lock' not in vote, msg="User can vote")
        vote_button.click()

@step('User clicks on {verdict}')
def click_verdict(context, verdict):
    sb = context.sb
    sb.find_element(f'//strong[normalize-space()="{verdict}"]/ancestor::span').click()

@step('Assert Popup says User thinks Kevin is {verdict}')
def check_popup(context, verdict):
    sb = context.sb
    popup = "//div[@id='pa_5c9126fe47260_p1554e607d21-modal__header']"
    sb.assert_element(popup)
    context_verdict = 'innocent' if verdict == 'Not guilty' else 'guilty'
    text = BeautifulSoup(sb.get_attribute(popup, 'innerHTML'), features='lxml').getText()
    sb.assert_true(f"You think Kevin is {context_verdict}" in text)