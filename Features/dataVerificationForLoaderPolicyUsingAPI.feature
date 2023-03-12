@data_verify @loader
Feature: Data verification from database
  Background:
    Given I delete files from AWS S3 bucket

  @test_parameter_verify @smoke_test
  Scenario Outline: Create loader policy and verified the test parameter from database
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
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |
###
  @bin_summary_verify
  Scenario Outline: Create loader policy and verified the bin summary from database
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I get the <getTagData> data from <markFilePath> for <policyName>
    Then I verify the bin summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog   | getTagData |checkbox|
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time  | SBR, HBR   |readHbr, readSbr|
##
  @test_summary_verify
  Scenario Outline: Create loader policy and verified the test summary from database
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
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I get the <getTagData> data from <markFilePath> for <policyName>
#    Then I verify the test summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  | getTagData |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time | TSR        |
#
  @dynamic_table_verify
  Scenario Outline: Create loader policy and verified the dynamic table from database
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
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
#    Then I verify the dynamic table from test parameter Yield-werx database table
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |
#
  @loader_data_verify_for_generated_hbr_sbr @loader_1
  Scenario Outline: Create loader policy and verified the data from database with generated hbr and sbr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I generate the <generatedBin> bin data from <markFilePath> file for <policyName>
    Then I verify the <checkbox> bin summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox                | generatedBin | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | generateHbr,generateSbr | hard, soft   | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |

  @loader_data_verify_for_generated_hbr @loader_1
  Scenario Outline: Create loader policy and verified the data from database with generated hbr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I generate the <generatedBin> bin data from <markFilePath> file for <policyName>
    Then I verify the <checkbox> bin summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox    | generatedBin | querySource  | targetFileTable           | expectedGoldenFilePath | startingDateTable | endDateTable            | expectedPerformanceLog |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | generateHbr | hard         | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date    | workflow_end_date | Expected_Execution_Time |
#
  @loader_data_verify_for_generated_sbr @loader_1
  Scenario Outline: Create loader policy and verified the data from database with generated sbr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I generate the <generatedBin> bin data from <markFilePath> file for <policyName>
    Then I verify the <checkbox> bin summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox    | generatedBin | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | generateSbr | soft         | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |

  @loader_data_verify_for_read_hbr_sbr @loader_1
  Scenario Outline: Create loader policy and verified the data from database with read hbr and sbr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then  I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I get the <getTagData> data from <markFilePath> for <policyName>
    Then I verify the <checkbox> bin summary table data from yield-werx database

    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox         | getTagData | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | readHbr, readSbr | HBR , SBR  | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |

  @loader_data_verify_for_read_hbr
  Scenario Outline: Create loader policy and verified the data from database with read hbr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I get the <getTagData> data from <markFilePath> for <policyName>
    Then I verify the <checkbox> bin summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox | getTagData | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | readHbr  | HBR        | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |
  @loader_data_verify_for_read_sbr
  Scenario Outline: Create loader policy and verified the data from database with read sbr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I get the <getTagData> data from <markFilePath> for <policyName>
    Then I verify the <checkbox> bin summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox | getTagData | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | readSbr  | SBR        | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |
#
  @loader_data_verify_for_read_tsr
  Scenario Outline: Create loader policy and verified the data from database with read tsr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the ptr data from <markFilePath> for <policyName>
    Then I get the <getTagData> data from <markFilePath> for <policyName>
    Then I verify the test summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | selectionCriteria  | checkbox | getTagData | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | Selection_Criteria | readTsr  | TSR        | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |
#
  @loader_data_verify_for_generate_tsr @loader_1
  Scenario Outline: Create loader policy and verified the data from database with generate tsr
    Given I mark the <expectedGoldenFilePath> for <tagName> tag in <policyName> for verification the change and store into <markFilePath>
    Then I save the marked data into <markedCollection>
    Given I upload the <policyName> files from <markFilePath> into <loaderBucketName> AWS S3 bucket
    Then I delete the data from <loaderFileCollectionName> collection
    Then I write the data into <loaderFileCollectionName> collection
    When I login to application using <login> api with <payload>
    Then I verify the response status code <expectedStatusCode> for <login>
    Then I update the <policyName> <payload> with <newPolicyName>, <checkbox> and <loaderBucketName> bucket
    Then I create policy for <policyName> stage and add <payload>
    Then I verify the response status code <expectedStatusCode> for <policyName>
    Then I connect to YW database
    Then I verify policy data is created in yield-werx-db
    Then I verify the <expectedStatus> status of policy in database from <loaderFileCollectionName>
    Then I get the data <targetFileTable> , <startingDateTable> and <endDateTable> from <loaderFileCollectionName> with <querySource> for <policyName> policy validation of Calculated Performance log with <expectedPerformanceLog>
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I verify the <markFilePath> file of <policyName> from test parameter Yield-werx database table
    Then I generate the test data from <markFilePath> file for <policyName>
    Then I verify the test summary table data from yield-werx database
    Examples:
      | login | policyName | newPolicyName            | tagName     | markFilePath     | markedCollection | loaderBucketName | loaderFileCollectionName | expectedStatusCode | expectedStatus | payload | expectedGoldenFilePath    | checkbox    | querySource       | targetFileTable               | expectedGoldenFilePath    | startingDateTable   | endDateTable      | expectedPerformanceLog  |
      | Login | Loader     | ModifiedLoaderPolicyName | MIR,WIR,WRR | marked_file_path | Marking_file     | yw-loader-2      | loader_file_location     | 200                | SUCCESS        | Payload | Expected_Golden_file_Path | generateTsr | YieldWerxDataBase | workflow_target_file_location | Expected_Golden_file_Path | workflow_start_date | workflow_end_date | Expected_Execution_Time |
