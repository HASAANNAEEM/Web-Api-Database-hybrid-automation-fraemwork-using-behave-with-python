#@post_processing
#Feature: Data verification from database
#  Background:
#    Given I delete files from AWS S3 bucket
#@post_processing
#  Scenario Outline: Create loader policy and verified the data from database
#    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
#    Then I save the marked data into <markedCollection>
#    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
#    Then I delete the data from <loaderFileCollectionName> collection
#    Then I write the data into <loaderFileCollectionName> collection
#    When I login to application using <login> api with <payload>
#    Then I verify the response status code <expectedStatusCode> for <login>
#    Then I update the <payload> for <policyName> with <newPolicyName> and <loaderBucketName> bucket
#    Then I create policy for <policyName> stage and add <payload>
#    Then I verify the response status code <expectedStatusCode> for <policyName>
#    Then I connect to YW database
#    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
#    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
#    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
#    Then I verify the dynamic table from test parameter Yield-werx database table
#    Then I get the <getTagData> data from <markFilePath> for <policyName>
#    Then I verify the test summary table data from yield-werx database
#    Then I verify the bin summary table data from yield-werx database
#    Then I update the <payload> for <postProcessing>
#    Then I calling the <postProcessing> api with <payload> and getting the execution time
#    Then I close to YW database
#     Examples:
#     | login | policyName |newPolicyName            |tagName     |markFilePath     |markedCollection | loaderBucketName |loaderFileCollectionName |expectedStatusCode |expectedStatus |payload |querySource       |targetFileTable               |expectedGoldenFilePath     |startingDateTable   |endDateTable      |expectedPerformanceLog  |postProcessing |getTagData   |
#     | Login | Loader     |ModifiedLoaderPolicyName |MIR,WIR,WRR |marked_file_path |Marking_file     |yw-loader-2       |loader_file_location     |200                |SUCCESS        |Payload |YieldWerxDataBase |workflow_target_file_location |Expected_Golden_file_Path  |workflow_start_date |workflow_end_date |Expected_Execution_Time |Post_Processing|SBR, HBR, TSR|