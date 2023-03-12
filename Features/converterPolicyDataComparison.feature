@comparison @converter_comparison @converter
Feature: Compare the newly generated files with golden file
  Background:
    Given I delete files from AWS S3 bucket
  @converter_comparison @smoke_test
  Scenario Outline: Create converter policy and Compare the newly generated files with golden file
    Given I upload the <policyName> files from <inputGoldenFilePath> into <inputGoldenFileBucketName> AWS S3 bucket
    Then I connect to test database
    Then I delete the data from <inputGoldenFileCollectionName> collection
    Then I write the data into <inputGoldenFileCollectionName> collection
    Given I upload the <expectedGoldenFile> files from <expectedGoldenFilePath> into <expectedGoldenFileBucketName> AWS S3 bucket
    Then I delete the data from <expectedGoldenFileCollectionName> collection
    Then I write the data into <expectedGoldenFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <payload> for <policyName> with <newPolicyName> and <inputGoldenFileBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <inputGoldenFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <inputGoldenFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I delete the data from <downloadFileCollection> collection
    Then I store the values into source file location <downloadFileCollection>
    Then I get the Source file list from test database <downloadFileCollection> then download converted file from Aws s3
    Then I compare both <goldenFilePath> files and <downloadedFilePath> file for <policyName> from <inputGoldenFileCollectionName> and store value into <identicalFilePath> and <differentLinesFilePath> local directory path
    Examples:
      | policyName |newPolicyName               |login |expectedGoldenFile   |expectedStatusCode |inputGoldenFilePath    |expectedGoldenFilePath    |inputGoldenFileBucketName |expectedGoldenFileBucketName |payload |inputGoldenFileCollectionName |expectedGoldenFileCollectionName |targetFileTable               |startingDateTable   |endDateTable     |expectedStatus  |querySource       |downloadFileCollection |downloadedFilePath   |goldenFilePath   |identicalFilePath   |differentLinesFilePath    |expectedPerformanceLog|
      | Converter  |ModifiedConverterPolicyName |Login |Expected_Golden_file |200                |Input_Golden_file_Path |Expected_Golden_file_Path |yw-rawfile-1              |yw-golden-1                  |Payload |source_file_location          |target_file_location             |workflow_target_file_location |workflow_start_date |workflow_end_date |SUCCESS        |YieldWerxDataBase |workflow_db_convert   |downloaded_file_path |golden_file_path |identical_file_path |different_lines_file_path |Expected_Execution_Time|
