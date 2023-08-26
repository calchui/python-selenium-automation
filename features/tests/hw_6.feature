# Created by edc_p at 8/22/2023
Feature: Verify Open Amazon Sign-in page

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened