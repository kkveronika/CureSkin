# Created by Veronika at 4/25/2023
Feature: Home Page
  Scenario: User open Terms of Service page
    Given Open main page
    When From page footer, click "Terms of Service"
    Then Verify Terms page opened
    # Enter steps here

#Feature: Home Page
  #Scenario: User enter invalid email
#  Given Open main page
#  When From page footer, in email field enter vvvkkk
#  When Click on search button
#  Then Verify error message displays
