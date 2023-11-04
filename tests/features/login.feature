Feature: Login
    Test pertaining user Login

Scenario: User Login
    Given there is a login page

    When user input correct username
    And user input correct password
    And user click login button
    
    Then user can see home page
