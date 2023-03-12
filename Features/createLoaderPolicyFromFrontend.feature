@UI_policy @loader @create_converter_policy_from_ui
Feature: Create loader policy from UI
  Background:
    Then I connect to YW database

  @ui_create_policy @smoke_test @loader_1
  Scenario Outline: Create a loader policy and verify the load saved alert message
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
#    # And I click on View button
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
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |
###
  @ui_create_policy @loader_1
  Scenario Outline: Create a loader policy and verify the load update alert message
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
#    # And I click on View button
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
    And I click on Save button
    And I verify the Updated! alert message
      And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
     |Credential | policy      | expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |


  @ui_create_policy @loader_1
  Scenario Outline: Create a loader policy and verify the load policy stage from data intake
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
#    # And I click on View button
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
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
    |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |

#
  @ui_create_policy @loader_1
  Scenario Outline: Create a loader policy and verify the load policy status from yw-db
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
#    # And I click on View button
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
    Then I connect to YW database
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatusForDB> status of policy in database from <loaderFileCollectionName>

  Examples:
     |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|expectedStatusForDB|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |SUCCESS       |


   @ui_create_policy
  Scenario Outline: Create a loader policy with read ptr and verify the load policy stage
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
    And I check all summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
    |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |


  @ui_create_policy
  Scenario Outline: Create a loader policy with read ftr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check all summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
    |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |


  @ui_create_policy_and_verify_policy
  Scenario Outline: Create a loader policy with read mrp and verify the load policy stage
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
    And I check the "Read MPR" option in die
    And I check all summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
    |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |

   @ui_create_policy @read_hbr
  Scenario Outline: Create a loader policy with read hbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR|

  @ui_create_policy @read_sbr
  Scenario Outline: Create a loader policy with read sbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR |


  @ui_create_policy @read_tsr
  Scenario Outline: Create a loader policy with read tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read TSR |


   @ui_create_policy @read_hbr_sbr
  Scenario Outline: Create a loader policy with read hbr read sbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read HBR |


   @ui_create_policy @read_sbr_tsr
  Scenario Outline: Create a loader policy with read sbr and read tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read TSR|

   @ui_create_policy @read_hbr_tsr
  Scenario Outline: Create a loader policy with read hbr and read tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR, Read TSR|


   @ui_create_policy @generate_hbr
  Scenario Outline: Create a loader policy with generate hbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate HBR |

  @ui_create_policy @generate_sbr
  Scenario Outline: Create a loader policy with generate sbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR |


  @ui_create_policy @generate_tsr
  Scenario Outline: Create a loader policy with generate tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate TSR |


   @ui_create_policy @generate_hbr_sbr
  Scenario Outline: Create a loader policy with generate hbr and tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR, Generate HBR|


   @ui_create_policy @generate_sbr_tsr
  Scenario Outline: Create a loader policy with generate sbr and tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR, Generate TSR |

  @ui_create_policy @read_hbr
  Scenario Outline: Create a loader policy with read ptr and read hbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR |

  @ui_create_policy @read_sbr
  Scenario Outline: Create a loader policy with read ptr and read sbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR |


  @ui_create_policy @read_tsr
  Scenario Outline: Create a loader policy with read ptr and read tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read TSR |


   @ui_create_policy @read_hbr_sbr
  Scenario Outline: Create a loader policy with read ptr, read hbr and read sbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read HBR |

   @ui_create_policy @read_sbr_tsr
  Scenario Outline: Create a loader policy with read ptr, read sbr and read tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read TSR |


   @ui_create_policy @read_hbr_tsr
  Scenario Outline: Create a loader policy with read ptr, read hbr and read tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR, Read TSR |

  @ui_create_policy @generate_hbr
  Scenario Outline: Create a loader policy with read ptr, generate hbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate HBR |

  @ui_create_policy @generate_sbr
  Scenario Outline: Create a loader policy with read ptr , generate sbr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR |


  @ui_create_policy @generate_tsr
  Scenario Outline: Create a loader policy with read ptr , generate tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate TSR |


   @ui_create_policy @generate_hbr_sbr
  Scenario Outline: Create a loader policy with read ptr, generate hbr and tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR, Generate HBR|


   @ui_create_policy @generate_sbr_tsr
  Scenario Outline: Create a loader policy with read ptr,  generate sbr and tsr and verify the load policy stage
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
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR, Generate TSR |




    @ui_create_policy @read_hbr
  Scenario Outline: Create a loader policy with read ftr and read hbr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR |

  @ui_create_policy @read_sbr
  Scenario Outline: Create a loader policy with read ftr and read sbr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR |

  @ui_create_policy @read_tsr
  Scenario Outline: Create a loader policy with read ftr and read tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read TSR |


   @ui_create_policy @read_hbr_sbr
  Scenario Outline: Create a loader policy with read ftr and read tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read HBR |

   @ui_create_policy @read_sbr_tsr
  Scenario Outline: Create a loader policy with read ftr, read sbr and read tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read TSR |


   @ui_create_policy @read_hbr_tsr
  Scenario Outline: Create a loader policy with read ftr, read hbr and read tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR, Read TSR |



  @ui_create_policy @generate_hbr
  Scenario Outline: Create a loader policy with read ftr, generate hbr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate HBR |

  @ui_create_policy @generate_sbr
  Scenario Outline: Create a loader policy with read ftr , generate sbr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR |


  @ui_create_policy @generate_tsr
  Scenario Outline: Create a loader policy with read ftr , generate tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate TSR |


   @ui_create_policy @generate_hbr_sbr
  Scenario Outline: Create a loader policy with read ftr, generate hbr and tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR, Generate HBR|


   @ui_create_policy @generate_sbr_tsr
  Scenario Outline: Create a loader policy with read ftr,  generate sbr and tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Generate SBR, Generate TSR |





      @ui_create_policy @read_hbr
  Scenario Outline: Create a loader policy with read mpr and read hbr and verify the load policy stage
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
    And I check the "Read MPR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR |

  @ui_create_policy @read_sbr
  Scenario Outline: Create a loader policy with read mpr and read sbr and verify the load policy stage
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
    And I check the "Read MPR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy      | expectedStatus |policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR |

  @ui_create_policy @read_tsr
  Scenario Outline: Create a loader policy with read mpr and read tsr and verify the load policy stage
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
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read TSR |


   @ui_create_policy @read_hbr_sbr
  Scenario Outline: Create a loader policy with read mpr and read tsr and verify the load policy stage
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
    And I check the "Read MPR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy |FINISHED|Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read HBR |

   @ui_create_policy @read_sbr_tsr
  Scenario Outline: Create a loader policy with read mpr, read sbr and read tsr and verify the load policy stage
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
    And I check the "Read MPR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read SBR, Read TSR |


   @ui_create_policy @read_hbr_tsr
  Scenario Outline: Create a loader policy with read mpr, read hbr and read tsr and verify the load policy stage
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
    And I check the "Read MPR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed

  Examples:
   |Credential | policy       |expectedStatus|policyName| tagName| expectedGoldenFilePath         |markFilePath       |ownerEmail              |markedCollection|loaderFileCollectionName|stage|loaderBucketName|check_box_text|
    | Login     | LoaderPolicy|FINISHED |Loader    |MIR,WIR,WRR  | Expected_Golden_file_Path |marked_file_path  |automation@yieldwerx.com |Marking_file|loader_file_location|load         |yw-loader-2     |Read HBR, Read TSR |
