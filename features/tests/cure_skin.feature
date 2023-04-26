# Created by Veronika at 4/25/2023
Feature: Terms of Service
  Scenario: User open Terms of Service page
  Given Open main page
  When From page footer, click "Terms of Service"
  Then Verify Terms page opened
    # Enter steps here