#@Reports
#Feature: Verification of the GL-reports
#
#  @wafer_map
#  Scenario Outline: Verify GL-report
#    Given I am on login screen
#    When I enter the valid <Credential> credential
#    And I hit login button
#    And I verify dashboard is displayed
#    Then I click on "Power View" from menu
#    Then I check the selection criteria for <table_name>
#    Then Generate the Bin Wafer Map Report
#    Then Verify bin wafer map report
#    Then verifying the canvas exists
#
#  Examples:
#    |Credential | policy       | stage  | table_name                      | lotName  | waferId | testParameter    |
#    | admin    | LoaderPolicy | load  | ywAdmin!1  | Demo Facility,Demo LOT,W008,tot | Demo Lot | W008    | Iq tot <> IQ_TOT |
