@UI_converter_policy @converter
Feature: Create converter policy from UI
  @converterFE @smoke_test
  Scenario Outline: Create a converter policy
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
##    # And I click on View button
    Then I select source format as <converter>
    And I select source as "Cloud Storage"
    And I enter source container <policy>
    And I select schedule mode as "Poller"
    And I select the starting time
    And I enter policy polling time <policy>
    And I click on Save button
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
      And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
  Examples:
    | Credential | policy          |expectedStatus| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
    | Login      | ConverterPolicy |FINISHED| IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
###
#  @converterFE @smoke_test
#  Scenario Outline: Create a converter policy and verify the convert policy stage and and download the file from target file location
#   Given I delete files from AWS S3 bucket
#    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
#    Then I connect to test database
#    Then I delete the data from <inputGoldenFileCollectionName> collection
#    Then I write the data into <inputGoldenFileCollectionName> collection
#    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
#    Then I delete the data from <expectedGoldenFileCollectionName> collection
#    Then I write the data into <expectedGoldenFileCollectionName> collection
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
#    And I select "Converter" stage
##    # And I click on View button
#    Then I select source format as <converter>
#    And I select source as "Cloud Storage"
#    And I enter source container <policy>
#    And I select schedule mode as "Poller"
#    And I select the starting time
#    And I enter policy polling time <policy>
#    And I click on Save button
  #    Then I verify policy data is created in yield-werx-db
#    And I click on "Control Tower" from menu
#      And I verify the <expectedStatus> status from step intake queue
#    And I verify the <stage> is successfully executed
#    And I download the converted files form s3
#  Examples:
#    | Credential | policy          |expectedStatus| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
#    | Login      | ConverterPolicy |FINISHED| IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
##
#  @converterFE
#  Scenario Outline: Create a converter policy, verify the convert policy stage and download file
#    Given I delete files from AWS S3 bucket
#    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
#    Then I connect to test database
#    Then I delete the data from <inputGoldenFileCollectionName> collection
#    Then I write the data into <inputGoldenFileCollectionName> collection
#    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
#    Then I delete the data from <expectedGoldenFileCollectionName> collection
#    Then I write the data into <expectedGoldenFileCollectionName> collection
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
#    And I select "Converter" stage
##    # And I click on View button
#
#    Then I select source format as <converter>
#    And I select source as "Cloud Storage"
#    And I enter source container <policy>
#    And I select schedule mode as "Poller"
#
#    And I select the starting time
#    And I enter policy polling time <policy>
#    And I click on Save button
  #    Then I verify policy data is created in yield-werx-db
#    And I click on "Control Tower" from menu
#      And I verify the <expectedStatus> status from step intake queue
#    And I verify the <stage> is successfully executed
#    And I download the converted files form s3
#  Examples:
#   | Credential | policy          |expectedStatus| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
#    | Login      | ConverterPolicy |FINISHED| IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
##
#  @converterFE
#  Scenario Outline: Create a converter policy, verify the convert policy stage and download file
#    Given I delete files from AWS S3 bucket
#    Given I upload the <satge> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
#    Then I connect to test database
#    Then I delete the data from <inputGoldenFileCollectionName> collection
#    Then I write the data into <inputGoldenFileCollectionName> collection
#    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
#    Then I delete the data from <expectedGoldenFileCollectionName> collection
#    Then I write the data into <expectedGoldenFileCollectionName> collection
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
#    And I select "Converter" stage
##    # And I click on View button
#    Then I select source format as <converter>
#  Examples:
#   | Credential | policy          | converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
#    | Login      | ConverterPolicy | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
##
#  @converterFE @ftp
#  Scenario Outline: Create a converter policy, verify the convert policy stage and download file
#    Given I delete files from AWS S3 bucket
#    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
#    Then I connect to test database
#    Then I delete the data from <inputGoldenFileCollectionName> collection
#    Then I write the data into <inputGoldenFileCollectionName> collection
#    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
#    Then I delete the data from <expectedGoldenFileCollectionName> collection
#    Then I write the data into <expectedGoldenFileCollectionName> collection
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
#    And I select "Converter" stage
##    # And I click on View button
#    Then I select source format as <converter>
#    And I select source as "ftp"
#
#  Examples:
# | Credential | policy          | converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
#    | Login      | ConverterPolicy | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
##
#
#  @converterFE @ftp
#  Scenario Outline: Create a converter policy, verify the convert policy stage and download file
#    Given I delete files from AWS S3 bucket
#    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
#    Then I connect to test database
#    Then I delete the data from <inputGoldenFileCollectionName> collection
#    Then I write the data into <inputGoldenFileCollectionName> collection
#    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
#    Then I delete the data from <expectedGoldenFileCollectionName> collection
#    Then I write the data into <expectedGoldenFileCollectionName> collection
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
#    And I select "Converter" stage
##    # And I click on View button
#    Then I select source format as <converter>
#    And I select source as "ftp"
#    And I enter source <ftp_text> <policy>
#    And I enter source ftp username <policy>
#    And I enter source ftp password <policy>
#    And I enter source Folder to transfer files from <policy>
#    And I select schedule mode as "Poller"
#    And I select the starting time
#    And I enter policy polling time <policy>
#    And I click on Save button
  #    Then I verify policy data is created in yield-werx-db
#    And I click on "Control Tower" from menu
#      And I verify the <expectedStatus> status from step intake queue
#    And I verify the <stage> is successfully executed
##    And I download the converted files form s3
#  Examples:
#  | Credential | policy          |expectedStatus|ftp_text| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
#    | Login      | ConverterPolicy|FINISHED |ftp address | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
##
#
#  @converterFE @ftp_verification
#  Scenario Outline: Create a converter policy, verify the convert policy stage and download file
#    Given I delete files from AWS S3 bucket
#    Given I upload the <stage> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
#    Then I connect to test database
#    Then I delete the data from <inputGoldenFileCollectionName> collection
#    Then I write the data into <inputGoldenFileCollectionName> collection
#    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
#    Then I delete the data from <expectedGoldenFileCollectionName> collection
#    Then I write the data into <expectedGoldenFileCollectionName> collection
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
#    And I select "Converter" stage
##    # And I click on View button
#    Then I select source format as <converter>
#    And I select source as "ftp"
#    And I enter source <ftp_text> <policy>
#    And I enter source ftp username <policy>
#    And I enter source ftp password <policy>
#    And I enter source Folder to transfer files from <policy>
#    And I select schedule mode as "Poller"
#    And I select the starting time
#    And I enter policy polling time <policy>
#    And I click on Save button
  #    Then I verify policy data is created in yield-werx-db
#    And I click on "Control Tower" from menu
#      And I verify the <expectedStatus> status from step intake queue
#    And I verify the <stage> is successfully executed
#    And I download the converted files form s3
#  Examples:
#  | Credential    | policy         | expectedStatus| ftp_text| converter   | ownerEmail               |stage|expectedGoldenFile|expectedGoldenFilePath|inputGoldenFilePath|inputGoldenFileBucketName|expectedGoldenFileBucketName|inputGoldenFileCollectionName|expectedGoldenFileCollectionName|
#    | Login      | ConverterPolicy |FINISHED|ftp address | IMS       | automation@yieldwerx.com |Converter  |Expected_Golden_file|Expected_Golden_file_Path|Input_Golden_file_Path|yw-rawfile-1      |yw-golden-1                 |source_file_location         |target_file_location            |
