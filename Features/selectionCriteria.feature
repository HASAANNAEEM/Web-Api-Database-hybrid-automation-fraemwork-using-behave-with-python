@selection_criteria
Feature: Verification of the selection criteria
  Background:
    Then I connect to YW database
  @create_loader_policy_for_selection_criteria @smoke_test
  Scenario Outline: Create a loader policy for selection criteria verification
    Given I delete files from AWS S3 bucket
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Loader Policies" from menu
    And I verify the create policy button is displayed
    And I click on the create policy button
    And I enter policy name <policy>
    And I enter policy version <policy>
    And I enter policy description <policy>
    And I enter policy owner email <ownerEmail>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I check the "Read PTR" option in die
    And I check the "Read FTR" option in die
    And I check the "Read MPR" option in die
    And I check all summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

    Examples:
      |Credential | policy        | loaderBucketName | markFilePath     | policyName | expectedGoldenFilePath    |stage|ownerEmail|tagName|markedCollection|loaderFileCollectionName| expectedStatus|
      | Login   | LoaderPolicy   | yw-loader-2      | marked_selection_file_path | Loader     | Expected_Selection_Golden_file_Path |load |automation@yieldwerx.com|MIR,WIR,WRR|Marking_file|loader_file_location|FINISHED|



  @selection_criteria_for_single_table
  Scenario Outline: Verify the selection criteria with data base for single table
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I verify the <table_data> table data from data base
    Examples:
      |Credential  | table_data            | policyName | markFilePath     |
      | Login     | Facility              | Loader     | marked_selection_file_path |
      | Login     | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Device                | Loader     | marked_selection_file_path |
      | Login     | Test Program          | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision | Loader     | marked_selection_file_path |
      | Login     | Lot                   | Loader     | marked_selection_file_path |
      | Login     | Wafer                 | Loader     | marked_selection_file_path |
      | Login     | Test Parameter        | Loader     | marked_selection_file_path |

  @selection_criteria_verification_for_multiple_table
  Scenario Outline: Verify the selection criteria with data base for multiple table
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_name> from selection criteria
    Then I verify the <table_data> table data from data base
    Examples:
      |Credential  | table_data                           | table_name            | policyName | markFilePath     |
      | Login     | Facility,Work Center                 | Facility              | Loader     | marked_selection_file_path |
      | Login     | Facility,Device                      | Facility              | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program                | Facility              | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program Revision       | Facility              | Loader     | marked_selection_file_path |
      | Login     | Facility , Lot                       | Facility              | Loader     | marked_selection_file_path |
      | Login     | Facility , Wafer                     | Facility              | Loader     | marked_selection_file_path |
      | Login     | Facility , Test Parameter            | Facility              | Loader     | marked_selection_file_path |
      | Login     | Work Center,Device                   | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Work Center,Test Program             | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Work Center,Test Program Revision    | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Work Center , Lot                    | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Work Center , Wafer                  | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Work Center , Test Parameter         | Work Center           | Loader     | marked_selection_file_path |
      | Login     | Device,Test Program                  | Device                | Loader     | marked_selection_file_path |
      | Login     | Device,Test Program Revision         | Device                | Loader     | marked_selection_file_path |
      | Login     | Device , Lot                         | Device                | Loader     | marked_selection_file_path |
      | Login     | Device , Wafer                       | Device                | Loader     | marked_selection_file_path |
      | Login     | Device , Test Parameter              | Device                | Loader     | marked_selection_file_path |
      | Login     | Test Program,Test Program Revision   | Test Program          | Loader     | marked_selection_file_path |
      | Login     | Test Program , Lot                   | Test Program          | Loader     | marked_selection_file_path |
      | Login     | Test Program , Wafer                 | Test Program          | Loader     | marked_selection_file_path |
      | Login     | Test Program , Test Parameter        | Test Program          | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision, Lot           | Test Program Revision | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision, Wafer         | Test Program Revision | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision,Test Parameter | Test Program Revision | Loader     | marked_selection_file_path |
      | Login     | Lot , Wafer                          | Lot                   | Loader     | marked_selection_file_path |
      | Login     | Lot, Test Parameter                  | Lot                   | Loader     | marked_selection_file_path |
      | Login     | Wafer, Test Parameter                | Wafer                 | Loader     | marked_selection_file_path |
#
  @selection_criteria_verification_for_multiple's_table
  Scenario Outline: Verify the selection criteria with data base for multiple table
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_name> from selection criteria
    Then I verify the <table_data> table data from data base
    Examples:
      |Credential  | table_data                           | table_name                      | policyName | markFilePath     |
      | Login    | Facility,Work Center                 | Facility, Work Center           | Loader     | marked_selection_file_path |
      | Login     | Facility,Device                      | Facility, Device                        | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program                | Facility,Test Program               | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program Revision       | Facility,Test Program Revision              | Loader     | marked_selection_file_path |
      | Login     | Facility , Lot                       | Facility , Lot           | Loader     | marked_selection_file_path |
      | Login     | Facility , Wafer                     | Facility , Wafer               | Loader     | marked_selection_file_path |
      | Login     | Work Center,Device                   | Work Center,Device            | Loader     | marked_selection_file_path |
      | Login     | Work Center,Test Program             | Work Center,Test Program             | Loader     | marked_selection_file_path |
      | Login     | Work Center,Test Program Revision    | Work Center,Test Program Revision          | Loader     | marked_selection_file_path |
      | Login     | Work Center , Lot                    | Work Center , Lot           | Loader     | marked_selection_file_path |
      | Login     | Work Center , Wafer                  | Work Center , Wafer            | Loader     | marked_selection_file_path |
      | Login     | Device,Test Program                  | Device,Test Program                 | Loader     | marked_selection_file_path |
      | Login     | Device,Test Program Revision         | Device,Test Program Revision                | Loader     | marked_selection_file_path |
      | Login     | Device , Lot                         | Device , Lot                | Loader     | marked_selection_file_path |
      | Login     | Device , Wafer                       | Device , Wafer                | Loader     | marked_selection_file_path |
      | Login     | Test Program,Test Program Revision   | Test Program,Test Program Revision           | Loader     | marked_selection_file_path |
      | Login     | Test Program , Lot                   | Test Program , Lot           | Loader     | marked_selection_file_path |
      | Login     | Test Program , Wafer                 | Test Program , Wafer          | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision, Lot           | Test Program Revision, Lot | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision, Wafer         | Test Program Revision, Wafer | Loader     | marked_selection_file_path |
      | Login     | Lot , Wafer                          | Lot , Wafer                   | Loader     | marked_selection_file_path |
      | Login    | Facility,Work Center                 | Facility, Work Center           | Loader     | marked_selection_file_path |
      | Login     | Facility,Device                      | Facility, Device                        | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program                | Facility,Test Program               | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program Revision       | Facility,Test Program Revision              | Loader     | marked_selection_file_path |


  @selection_criteria_verification_for_multiple's_table
  Scenario Outline: Verify the selection criteria with data base for more that two tables
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_name> from selection criteria
    Then I verify the <table_data> table data from data base
    Examples:
      |Credential  | table_data                                             | table_name                      | policyName | markFilePath     |
      | Login    | Facility,Work Center , Device                           | Facility, Work Center , Device          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Program , Device                          | Facility, Test Program , Device          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Program Revision , Device                 | Facility, Test Program Revision , Device          | Loader     | marked_selection_file_path |
      | Login    | Facility,Lot , Device                                   | Facility, Lot , Device          | Loader     | marked_selection_file_path |
      | Login    | Facility,Wafer , Device                                 | Facility, Wafer , Device          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Program , Work Center                     | Facility, Test Program , Work Center          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Program Revision , Work Center            | Facility, Test Program Revision , Work Center          | Loader     | marked_selection_file_path |
      | Login    | Facility,Lot , Work Center                              | Facility, Lot , Work Center          | Loader     | marked_selection_file_path |
      | Login    | Facility, Wafer , Work Center                            | Facility, Wafer , Work Center          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Program Revision , Test Program           | Facility, Test Program Revision , Test Program          | Loader     | marked_selection_file_path |
      | Login    | Facility,Lot , Test Program                             | Facility, Lot , Test Program          | Loader     | marked_selection_file_path |
      | Login    | Facility,Wafer , Test Program                           | Facility, Wafer , Test Program          | Loader     | marked_selection_file_path |
      | Login    | Facility,Lot , Test Program Revision                    | Facility, Lot , Test Program Revision          | Loader     | marked_selection_file_path |
      | Login    | Facility,Wafer , Test Program Revision                  | Facility, Wafer , Test Program Revision          | Loader     | marked_selection_file_path |
      | Login    | Facility,Wafer , Lot                                    | Facility, Wafer ,Lot          | Loader     | marked_selection_file_path |
       | Login    | Facility,Work Center                 | Facility, Work Center           | Loader     | marked_selection_file_path |
      | Login     | Facility,Device                      | Facility, Device                        | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program                | Facility,Test Program               | Loader     | marked_selection_file_path |
      | Login     | Facility,Test Program Revision       | Facility,Test Program Revision              | Loader     | marked_selection_file_path |
      | Login     | Facility , Lot                       | Facility , Lot           | Loader     | marked_selection_file_path |
      | Login     | Facility , Wafer                     | Facility , Wafer               | Loader     | marked_selection_file_path |
      | Login     | Work Center,Device                   | Work Center,Device            | Loader     | marked_selection_file_path |
      | Login     | Work Center,Test Program             | Work Center,Test Program             | Loader     | marked_selection_file_path |
      | Login     | Work Center,Test Program Revision    | Work Center,Test Program Revision          | Loader     | marked_selection_file_path |
      | Login     | Work Center , Lot                    | Work Center , Lot           | Loader     | marked_selection_file_path |
      | Login     | Work Center , Wafer                  | Work Center , Wafer            | Loader     | marked_selection_file_path |
      | Login     | Device,Test Program                  | Device,Test Program                 | Loader     | marked_selection_file_path |
      | Login     | Device,Test Program Revision         | Device,Test Program Revision                | Loader     | marked_selection_file_path |
      | Login     | Device , Lot                         | Device , Lot                | Loader     | marked_selection_file_path |
      | Login     | Device , Wafer                       | Device , Wafer                | Loader     | marked_selection_file_path |


    @selection_criteria_verification_for_multiple's_table
  Scenario Outline: Select and Verify the selection criteria with data base for multiple table
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_name> from selection criteria
    Examples:
      |Credential  | table_data                           | table_name                      | policyName | markFilePath     |
      | Login    | Facility,Test Parameter , Device                        | Facility, Test Parameter , Device          | Loader     | marked_selection_file_path |
      | Login     | Work Center , Test Parameter         | Work Center , Test Parameter            | Loader     | marked_selection_file_path |
      | Login     | Facility , Test Parameter            | Facility , Test Parameter               | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Parameter , Lot                           | Facility, Test Parameter , Lot         | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Parameter , Wafer                         | Facility, Test Parameter , Wafer         | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Parameter , Test Program Revision         | Facility, Test Parameter , Test Program Revision          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Parameter , Test Program                  | Facility, Test Parameter , Test Program          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Parameter , Work Center                   | Facility, Test Parameter , Work Center          | Loader     | marked_selection_file_path |
      | Login    | Facility,Test Parameter , Device                        | Facility, Test Parameter , Device          | Loader     | marked_selection_file_path |
      | Login     | Lot, Test Parameter                  | Lot, Test Parameter                   | Loader     | marked_selection_file_path |
      | Login     | Wafer, Test Parameter                | Wafer, Test Parameter                 | Loader     | marked_selection_file_path |
      | Login     | Test Program Revision,Test Parameter | Test Program Revision,Test Parameter | Loader     | marked_selection_file_path |
      | Login     | Test Program , Test Parameter        | Test Program , Test Parameter          | Loader     | marked_selection_file_path |
      | Login     | Device , Test Parameter              | Device , Test Parameter                | Loader     | marked_selection_file_path |
      | Login     | Work Center , Test Parameter         | Work Center , Test Parameter            | Loader     | marked_selection_file_path |
      | Login     | Facility , Test Parameter            | Facility , Test Parameter               | Loader     | marked_selection_file_path |

  @work_center_selection_criteria @smoke_test
  Scenario Outline: Verify the work center and test program is exist in selection criteria with work center in the file
   Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
       |Credential | table_data                 | policyName | markFilePath     |
      | Login  | Work Center | Loader     | marked_selection_file_path |

  @device_selection_criteria @smoke_test
  Scenario Outline: Verify the device is exist in selection criteria with facility in the file
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
      |Credential | table_data | policyName | markFilePath     |
      | Login    | Device     | Loader     | marked_selection_file_path |

  @test_program_selection_criteria @smoke_test
  Scenario Outline: Verify the test program is exist in selection criteria with facility in the file
   Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
      |Credential | table_data   | policyName | markFilePath     |
      | Login  | Test Program | Loader     | marked_selection_file_path |

   @test_program_revision_selection_criteria
  Scenario Outline: Verify the test program is exist in selection criteria with facility in the file
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
      |Credential | table_data   | policyName | markFilePath     |
      | Login  | Test Program Revision   | Loader     | marked_selection_file_path |

  @lot_selection_criteria
  Scenario Outline: Verify the test program is exist in selection criteria with facility in the file
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
      |Credential | table_data   | policyName | markFilePath     |
      | Login  | Lot   | Loader     | marked_selection_file_path |

   @wafer_selection_criteria
  Scenario Outline: Verify the test program is exist in selection criteria with facility in the file
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
      |Credential | table_data   | policyName | markFilePath     |
      | Login  | Wafer   | Loader     | marked_selection_file_path |

  @test_parameter_selection_criteria
  Scenario Outline: Verify the test program is exist in selection criteria with facility in the file
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select selection criteria button
    Then I select the <table_data> from selection criteria
    Examples:
      |Credential | table_data   | policyName | markFilePath     |
      | Login  | Test Parameter    | Loader     | marked_selection_file_path |