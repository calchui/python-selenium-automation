#  Created by edc_p at 8/7/2023
Feature: Tests for Main page UI
#
#  Scenario: Verify that footer has correct amount of links
#    Given Open Amazon Page
#    Then Verify footer has 36 links
#
#  Scenario: Verify that footer has correct amount of links
#    Given Open Amazon Page
#    Then Verify many links are shown in the footer
#
#
#  Scenario: User can see language options
#    Given Open Amazon page
#    When Hover over language options
#    Then Verify Spanish option present

#    #*****  HW 9 Problem 2 *****
  Scenario: Opens up Amazon Fashion
    Given Open Amazon Fashion Page
    When Hover over New Arrivals
    Then Verify sees the deals