Feature: Learning Path - Make a case against Kevin

  Background:
    Given Navigate to the selection page
    Then Click on the Course Making a case against Kevin
    Then Assert user has redirected to video page

  Scenario: User has not voted
    Given User clicks on Judge This
    Then Assert User is shown verdict page
    Then Assert User can't click on Vote

  Scenario Outline:
    Given User clicks on Judge This
    Then Assert User is shown verdict page
    When User clicks on <verdict>
    Then Assert user can click on Vote
    Then Assert Popup says User thinks Kevin is <verdict>

  Examples:
    | verdict     |
    | Guilty      |
    | Not guilty  |