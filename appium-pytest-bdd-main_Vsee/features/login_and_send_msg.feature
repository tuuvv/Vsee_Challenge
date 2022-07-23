Feature: Vsee application


  Scenario Outline: Login and send message
    Given User fill '<username>' to Email field
    When User fill '<password>' to Password field
    Then User hit Sign In button
    And User hit message button menu
    And User tap on Start new chat textview
    And User tap on Test Call option
    And User hit on DONE button
    And User type '<message>' to the input
    And User hit send button

    Examples:
      | username            | password | message |
      | tuuvv.uit@gmail.com | 123456   | hello   |
