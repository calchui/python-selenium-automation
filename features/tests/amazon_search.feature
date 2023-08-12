# Created by edc_p at 7/29/2023
Feature: Tests for amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is "table"

#    Scenario: Verify that a user can search for a cup
#    Given O pen Amazon page
#    When Search for cup
#    Then Verify search result is "cup"
#
#    Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for dress
#    Then Verify search result is "dress"

    Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_result>
    Examples:
    |search_word        |search_result      |
    |cup                |"cup"              |
    |dress              |"dress"            |
    |tea                |"tea"              |
    |coffee             |"coffee"           |
    |forks              |"forks"            |
    |spoon              |"spoon"            |



#     #*****  Problem 2 *****
#  Scenario: Verify that clicking Orders
#    Given Open Amazon page
#    When Click Orders
#    Then Verify sign in page opened
#
#     #*****  Problem 3 *****
#  Scenario: Verify that Cart is Empty
#    Given Open Amazon page
#    When Click Cart Icon
#    Then Verify Amazon Cart is Empty
#
#    #*****  Problem 4 *****
#  Scenario: Verify and search for shelves and then add to cart
#    Given Open Amazon page
#    When Search for shelves
#    Then Click on shelves
#    Then Add to Cart
#    Then Click No Thanks
#    Then Click on Cart
#    Then Verify Shelves in Cart








