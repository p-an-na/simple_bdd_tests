Feature: Cart
    User add an item to cart and remove it.
Scenario: Add to cart and remove
    Given there is a home page

    When user add to cart first item
    And user go to cart
    
    Then user check item in cart and remove it