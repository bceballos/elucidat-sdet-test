Feature: Selecting cases - Learning Path

  Background:
    Given Navigate to the selection page

  Scenario: Score so far on startup is 0
    Given The selection page is open
    Then Assert that progress should be "0"

  Scenario Outline: Navigate to the selected course
    Given Click on the Course <course_name>
    Then Assert User has redirected to video page
    Then Assert that the VideoId is <video_id>
    Then Assert that the Summary is <summary>

    Examples:
      | course_name                 | summary                                                  | video_id  |
      | Making a case against Kevin | A murder has been committed in an alleyway outside a pub | 176711900 |
      | Who is to blame             | Summary would be different here                          | 176711880 |
