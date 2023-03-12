@performance_verification
Feature: Performance log verification
  Background:
    Given I delete files from AWS S3 bucket
  @loader_performance_verification @loader @loader_1
  Scenario Outline: Create loader policy and verify the performance log
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <payload> for <policyName> with <newPolicyName> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
   Examples:
   |login |policyName|newPolicyName            |tagName     |markFilePath     |markedCollection |loaderBucketName |loaderFileCollectionName |expectedStatusCode |expectedStatus |payload |querySource       |targetFileTable               |expectedGoldenFilePath    |startingDateTable  |endDateTable     |expectedPerformanceLog |
   |Login |Loader    |ModifiedLoaderPolicyName |MIR,WIR,WRR |marked_file_path |Marking_file     |yw-loader-2      |loader_file_location     |200                |SUCCESS        |Payload |YieldWerxDataBase |workflow_target_file_location |Expected_Golden_file_Path |workflow_start_date |workflow_end_date |Expected_Execution_Time|

  @converter_performance_verification @converter
  Scenario Outline: Create converter policy and verify the performance log
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
    Examples:
      | policyName |newPolicyName               |login |expectedGoldenFile   |expectedStatusCode |inputGoldenFilePath    |expectedGoldenFilePath    |inputGoldenFileBucketName |expectedGoldenFileBucketName |payload |inputGoldenFileCollectionName |expectedGoldenFileCollectionName |targetFileTable        |startingDateTable  |endDateTable     |expectedStatus |querySource       |expectedPerformanceLog|
      | Converter  |ModifiedConverterPolicyName |Login |Expected_Golden_file |200                |Input_Golden_file_Path |Expected_Golden_file_Path |yw-rawfile-1              |yw-golden-1                  |Payload |source_file_location          |target_file_location             |workflow_target_file_location |workflow_start_date |workflow_end_date |SUCCESS        |YieldWerxDataBase |Expected_Execution_Time|
