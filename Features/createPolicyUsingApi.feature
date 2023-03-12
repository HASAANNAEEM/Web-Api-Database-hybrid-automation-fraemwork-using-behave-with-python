@create_policy
Feature: Create policy
  Background:
    Given I delete files from AWS S3 bucket

  @loader_policy @loader @loader_1
  Scenario Outline: Create loader policy
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
   Examples:
   | login | policyName|newPolicyName            |tagName     |markFilePath     |markedCollection | loaderBucketName|loaderFileCollectionName|expectedStatusCode  |payload  |expectedGoldenFilePath     |
   | Login | Loader    |ModifiedLoaderPolicyName |MIR,WIR,WRR |marked_file_path |Marking_file     |yw-loader-2      |loader_file_location    |200                 |Payload  |Expected_Golden_file_Path  |

  @converter_policy @converter
  Scenario Outline: Create converter policy
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
      Examples:
      | policyName |newPolicyName               |login |expectedGoldenFile   |expectedStatusCode |inputGoldenFilePath    |expectedGoldenFilePath    |inputGoldenFileBucketName |expectedGoldenFileBucketName |payload |inputGoldenFileCollectionName |expectedGoldenFileCollectionName |
      | Converter  |ModifiedConverterPolicyName |Login |Expected_Golden_file |200                |Input_Golden_file_Path |Expected_Golden_file_Path |yw-rawfile-1              |yw-golden-1                  |Payload |source_file_location          |target_file_location             |
