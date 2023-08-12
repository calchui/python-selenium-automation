# Created by edc_p at 8/7/2023
Feature: Check if there are 5 links

  Scenario: Verify Best Seller
    Given Open Amazon Page
    Then  Click on Best Seller
    Then Verify Best Sellers link
    Then Verify New Releases
    Then Movers & Shakers
    Then Most Wished For
    Then Gift Ideas

  Scenario:
    Given Open Customer Service
    Then Verify Welcome to Amazon Customer Service
    Then Verify 11 boxes of links
    Then Verify Search our help library
    Then Verify Search Bar
#    Then Verify All help topics
    Then Verify All Drop Down Topics