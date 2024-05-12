# Elucidat SDET Test

---
## 1) How to run the test suite / generate reports
First please open a terminal instance in the elucidat_test folder and install the requirements by entering:
```commandline
pip install -r requirements.txt
```
The project uses Allure in order to generate nice looking HTML reports as SeleniumBase reports typically don't work properly, please make sure Allure is installed: https://allurereport.org/docs/install/

Once all the requirements have been installed in the same terminal instance enter the following:
```commandline
behave -f allure_behave.formatter:AllureFormatter -o allure/results ./features
allure generate allure/results/ -o allure/reports — clean
allure open allure/reports
```
SeleniumBase will install chromedriver when running so the first run will take longer than expected
___

## 2) Features tested 

#### Selection Screen: 
- One of the features tested was the main selection screen as both learning paths result in the same video and thus are not independent courses.
- Additionally, the progress is not accurately tracked between the two courses as the course progress is mirrored between the first and second course.
#### Learning Path: 
- When selecting a learning path, it doesn't matter if the User selects "Making a case against Kevin" or "Who is to Blame" as they will always be directed to "Making a case against Kevin"
- When the user is selecting a verdict for the case if they select Guilty the popup will always show Not Guilty as the verdict
- When the user is selecting a verdict for the case if they select Not Guilty the popup will always show Guilty 

#### API Testing: 
- Was going to mock an API request to force the progress to 100% and see the response, ran out of time
___

## 3) Improvements 

Overall the suite is a very rough implementation using SeleniumBase and it would benefit from using just Selenium and PyTest which would allow for more control surrounding the configuration and calls to the Selenium APIs such as Before and Afters.

These are some of the improvements I would make to the suite given more time:
* Cleanup: The cleanup of the chromedriver post test run is unreliable and thus might leave some processes running in the background so a better cleanup needs to be implemented
* API Test: Ran out of time making the API feature, would finish mocking a POST request to force the course completion and check that the UI reflects that 
* Issues with the tests: Some of the tests I lacked information to properly finish such as the selection_page.feature the outline needs a summary for course 2 and the video ID was taken by scouring through the vimeo account they come from
* Project structure: There's inefficiency in the way which the project is structured as a lot of the stuff could be abstracted into helper files and then included as needed such as clicking on certain buttons or checking for values, but this would be tied into the larger rework of not using SeleniumBase and gaining more library control. As this was time limited SeleniumBase provided a good foundation. POMs (Page Object Models) would be a bit unnecessary as there's not really enough functionality on the pages to justify individual models per page. A good way to fix this would be to co-operate with developers and get more thorough tagging on certain controls to allow for easier x-path routes or css selectors
* Visual Regression: SeleniumBase has a visual regression library and do something like general area pixel matching since a lot of the App is UI based make sure that there are no visual regressions