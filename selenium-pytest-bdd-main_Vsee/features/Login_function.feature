Feature: Home Page
  Tests for the 'https://gmail.com/' home page

  Scenario Outline: Login to gmail and send mail
    #a
    Given I have navigated to the gmail.com page
    When I type '<username>' to the input field
    Then I click on the next button
    And  I type '<password>' to the input field
    And I click on the password next button
    And the gmail.com page opens
#    #b
    And I click on Compose button
    And I entering the '<email>' to the mail recipients input
    And I entering the "this is test from demo project" to the Subject input
    And the body message text is
      """
      This is where you can log into the secure area. Enter tomsmith for the username and
      SuperSecretPassword! for the password. If the information is wrong you should see error
      messages.
      """
    #c
    And I click send button

    Examples:
      | username          | password | email                  |
      | nguyenhoaibao2023 | bean1991 | vuvandai2024@gmail.com |

