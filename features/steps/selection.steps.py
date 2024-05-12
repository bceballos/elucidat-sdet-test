from behave import step
from bs4 import BeautifulSoup
@step('The selection page is open')
def selection_page_is_visible(context):
    sb = context.sb
    sb.assert_element('//em[normalize-space()="Press on a case to get started."]')

@step('Assert that progress should be {progress}')
def check_progress(context, progress):
    sb = context.sb
    progress_xpath = '//p[contains(text(), "Your score so far:")]'
    sb.assert_element(progress_xpath)
    text = BeautifulSoup(sb.get_attribute(progress_xpath, 'innerHTML'), features='lxml').getText()
    sb.assert_true("Your score so far: 0%" in text)

@step('Click on the course {course_name}')
def select_course(context, course_name):
    sb = context.sb
    course_button = f'//span[contains(text(), "{course_name}")]'
    sb.find_element(course_button).click()

@step('Assert User has redirected to video page')
def video_page_is_visible(context):
    sb = context.sb
    sb.assert_element('//div[contains(@class, "video_player")]', )

@step('Assert that the Summary is {summary}')
def check_summary(context, summary):
    sb = context.sb
    sb.assert_text(summary, '//div[contains(@data-role, "page.intro__text")]/*[1]')

@step('Assert that the VideoId is {video_id}')
def check_video_id(context, video_id):
    sb = context.sb
    video_url = sb.get_attribute('//div[contains(@class, "video_player")]', 'data-media')
    sb.assert_true(video_id in video_url, msg=f"Correct Video has been loaded ({video_url})")
