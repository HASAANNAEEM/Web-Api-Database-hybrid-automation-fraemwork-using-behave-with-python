#@parametric_trend_report @report
#Feature: Verification of Parametric Histogram
#  Background:
#    Then I connect to YW database
#   @create_loader_policy_for_selection_criteria
#  Scenario Outline: Create a loader policy for parametric
#    Given I delete files from AWS S3 bucket
#    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
#    Then I save the marked data into <markedCollection>
#    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
#    Then I delete the data from <loaderFileCollectionName> collection
#    Then I write the data into <loaderFileCollectionName> collection
#    Given I am on login screen
#    When I enter the valid <Credential> credential
#    And I hit login button
#    And I verify dashboard is displayed
#    Then I click on "Loader Policies" from menu
#    And I verify the create policy button is displayed
#    And I click on the create policy button
#    And I enter policy name <policy>
#    And I enter policy version <policy>
#    And I enter policy description <policy>
#    And I enter policy owner email <ownerEmail>
#    And I click on Add stage button
#    And I select "Load" stage
#    # And I click on View button
#    And I select source as "Cloud Storage"
#    And I enter source container <policy>
#    And I check the "Read PTR" option in die
#    And I check the "Read FTR" option in die
#    And I check the "Read MPR" option in die
#    And I check all summary records
#    And I select schedule mode as "Poller"
#    And I select schedule mode as
#    And I enter policy polling time <policy>
#    And I click on Save button
#     And I verify the Saved alert message
  #    Then I verify policy data is created in yield-werx-db
#    And I click on "Control Tower" from menu
#       And I verify the <expectedStatus> status from step intake queue
#    And I verify the <stage> is successfully executed
#     Then Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
#
#    Examples:
#      |Credential| policy        |expectedStatus| loaderBucketName | markFilePath       | tagName |policyName | expectedGoldenFilePath    |stage|ownerEmail|markedCollection|loaderFileCollectionName|
#      |Login     | LoaderPolicy  |FINISHED| yw-loader-2      | marked_file_path | MIR,WIR,WRR  |Loader     | Expected_Golden_file_Path |load |automation@yieldwerx.com|Marking_file|loader_file_location|
##
##  @parametric_trend
##  Scenario Outline: Verify Parametric Histogram Report
##    Given I am on login screen
##    When I enter the valid <Credential> credential
##    And I hit login button
##    And I verify dashboard is displayed
##    Then I click on "Trend" from menu
##    Then I select selection criteria button
##    Then I verify the selection criteria window in displayed
##    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
##    Then I select the <table_name> from selection criteria
##    Then I click on Select and Close button
##    Then I generate the report
##    Then I connect to YW database
##    Then I click on data tab
##    Then I connect to YW database
##    Then I get the data from database across <facility_name>
##    Then I get the data from Data Grid View
##    Then I verify the data grid views data against database data
##    Then I click on stats tab
##    Then I connect to YW database
##    Then I get the data from database across <facility_name>
##    Then I get the data from statistics grid
##    Then I verify the statistics grid against database data
##    Then I verify the stats tab
##    Then I click on errors tab
##    Then I verify the errors tab
##
##  Examples:
##    |Credential |table_data| table_name                           | stage  | table_name   | lotName  | waferId | testParameter    | facility_name |
##    | Login    |Facility ,Wafer, Lot, Test Parameter| Facility,Wafer, Lot, One Test Parameter  | load  | ywAdmin!1  | NGP754,02,wp | Demo Lot | W008    | Iq tot <> IQ_TOT | Demo Facility |
