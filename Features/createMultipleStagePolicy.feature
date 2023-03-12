@UI_converter_to_loader_policy @converter-2-loader
Feature: Create converter to loader policy from UI
  @converter-2-loader-FE @converter-2-loader-read-hbr
  Scenario Outline: Create a converter to loader policy with read hbr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          | expectedStatus|converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
    | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read HBR|

  @converter-2-loader-FE @converter-2-loader-read-sbr
  Scenario Outline: Create a converter to loader policy with read sbr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          | expectedStatus|converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read SBR |

  @converter-2-loader-read-tsr
  Scenario Outline: Create a converter to loader policy with read tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read TSR |

  @converter-2-loader-read-hbr-sbr
  Scenario Outline: Create a converter to loader policy with read hbr and read sbr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read HBR, Read SBR |


  @converter-2-loader-read-hbr-tsr
  Scenario Outline: Create a converter to loader policy with read hbr and read tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read HBR, Read TSR |


  @converter-2-loader-read-sbr-tsr
  Scenario Outline: Create a converter to loader policy with read sbr and read tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read SBR, Read TSR |


  @converter-2-loader-read-hbr-sbr-tsr
  Scenario Outline: Create a converter to loader policy with read hbr , read sbr and read tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Read SBR, Read HBR, Read TSR |

  @converter-2-loader-FE @converter-2-loader-generate-hbr
  Scenario Outline: Create a converter to loader policy with generate hbr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
    | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate HBR|

  @converter-2-loader-FE @converter-2-loader-generate-sbr
  Scenario Outline: Create a converter to loader policy with generate sbr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate SBR |

  @converter-2-loader-generate-tsr
  Scenario Outline: Create a converter to loader policy with generate tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate TSR |

  @converter-2-loader-generate-hbr-sbr
  Scenario Outline: Create a converter to loader policy with generate hbr and generate sbr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus |converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate HBR, Generate SBR |


  @converter-2-loader-generate-hbr-tsr
  Scenario Outline: Create a converter to loader policy with generate hbr and generate tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
       And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy|FINISHED | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate HBR, Generate TSR |


  @converter-2-loader-generate-sbr-tsr
  Scenario Outline: Create a converter to loader policy with generate sbr and generate tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
    And I check the "Read FTR" option in die
    And I check the checkbox for <check_box_text> for summary records
    And I select schedule mode as "Poller"
    And I select schedule mode as
    And I enter policy polling time <policy>
    And I click on Save button
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
     | Login      | ConverterToLoaderPolicy| FINISHED| IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate SBR, Generate TSR |


  @converter-2-loader-generate-hbr-sbr-tsr
  Scenario Outline: Create a converter to loader policy with generate hbr , generate sbr and generate tsr
    Given I delete files from AWS S3 bucket
    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
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
    And I select "Converter" stage
    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I click on Add stage button
    And I select "Load" stage
    # And I click on View button
    And I select source as "Policy Step"
    And I select policy step "Previous Step Output"
#    And I check the "Read FTR" option in die
#    And I check the checkbox for <check_box_text> for summary records
#    And I select schedule mode as "Poller"
#    And I select schedule mode as
#    And I enter policy polling time <policy>
#    And I click on Save button
#    And I verify the Saved alert message
  #    Then I verify policy data is created in yield-werx-db
#    And I click on "Control Tower" from menu
#    And I verify the <expectedStatus> status from step intake queue
#    And I verify the <stage> is successfully executed
#  Examples:
#     | Credential | policy                   |expectedStatus| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|check_box_text|
#     | Login      | ConverterToLoaderPolicy |FINISHED| IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |Generate SBR, Generate HBR, Generate TSR |
