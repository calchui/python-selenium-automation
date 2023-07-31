# Created by edc_p at 7/29/2023
Feature: Tests for amazon search

#  Scenario: Verify that a user can search for a table
#    Given Open Amazon page
#    When Search for table
#    Then Verify search result is correct
#
#  Scenario: Verify that clicking Orders
#    Given Open Amazon page
#    When Click Orders
#    Then Verify sign in page opened
#
#  Scenario: Verify that Cart is Empty
#    Given Open Amazon page
#    When Click Cart Icon
#    Then Verify Amazon Cart is Empty


  Scenario: Verify and search for shelves and then add to cart
    Given Open Amazon page
    When Search for shelves
    Then Click on shelves
    Then Add to Cart
    Then Click on Cart
    Then Verify Shelves in Cart








