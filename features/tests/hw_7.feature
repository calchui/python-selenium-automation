# Created by edc_p at 8/29/2023
Feature: Verify Empty Cart

  Scenario: Verify Text in Cart
      Given Open Amazon page
      When Click Cart Icon
      Then Verify Amazon Cart is Empty Text



  Scenario: Verify and search for shelves and then add to cart
    Given Open Amazon page
    When Click on Search Bar
#    Then Click Search
    Then Click on shelves
    Then Add to Cart
    Then Click No Thanks
    Then Click on Cart
    Then Verify Shelves in Cart