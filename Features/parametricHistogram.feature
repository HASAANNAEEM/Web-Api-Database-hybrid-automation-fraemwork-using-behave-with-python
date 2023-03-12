@parametric_histogram_report @report
Feature: Verification of Parametric Histogram
  Background:
    Then I connect to YW database
   @create_loader_policy_for_selection_criteria @smoke_test
  Scenario Outline: Create a loader policy for parametric histogram report
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
    And I verify the Saved alert message
      Then I verify policy data is created in yield-werx-db
    And I click on "Control Tower" from menu
    And I verify the <expectedStatus> status from step intake queue
    And I verify the <stage> is successfully executed
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>

    Examples:
      |Credential| policy        |expectedStatus| loaderBucketName | markFilePath                | tagName |policyName | expectedGoldenFilePath                  |stage|ownerEmail                |markedCollection|loaderFileCollectionName|
      |Login     | LoaderPolicy  |FINISHED     | yw-loader-2      | marked_parametric_file_path | MIR,WIR,WRR  |Loader     | Expected_Parametric_Golden_file_Path |load |automation@yieldwerx.com|Marking_file|loader_file_location|

  @parametric_histogram
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu

    Examples:
      |Credential |
      | Login   |
#  @parametric_histogram
#  Scenario Outline: Verify Parametric Histogram Report
#    Given I am on login screen
#    When I enter the valid <Credential> credential
#    And I hit login button
#    And I verify dashboard is displayed
#    Then I click on "Histogram" from menu
#    Then I select selection criteria button
#
#    Examples:
#      |Credential |
#      | Login   |
#  @parametric_histogram
#  Scenario Outline: Verify Parametric Histogram Report
#    Given I am on login screen
#    When I enter the valid <Credential> credential
#    And I hit login button
#    And I verify dashboard is displayed
#    Then I click on "Histogram" from menu
#    Then I select selection criteria button
#    Then I verify the selection criteria window in displayed
#
#    Examples:
#      |Credential |
#      | Login    |
  @parametric_histogram @smoke_test
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the data from Yield-werx database table for <policyName> from <markFilePath>
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Examples:
      |Credential  | table_data                              | table_name                             | policyName | markFilePath     |
      | Login      | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Examples:

      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login       | Facility,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
  @parametric_histogram
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Examples:
     |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login       | Facility,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
#  @parametric_histogram @graph_verification
#  Scenario Outline: Verify Parametric Histogram Report
#    Given I am on login screen
#    When I enter the valid <Credential> credential
#    And I hit login button
#    And I verify dashboard is displayed
#    Then I click on "Histogram" from menu
#    Then I select selection criteria button
#    Then I verify the selection criteria window in displayed
#    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
#    Then I select the <table_name> from selection criteria
#    Then I click on Select and Close button
#    Then I generate the report
#    Then I click on data tab
#    Then I click on the grid column chooser
#    Then I get selected tables from grid chooser
#    Then I Verify the tables data against Grid view
#    Then I click on the tree button to expend <table_name> tree
#    Then I get the checked <column_name> from selected <table_name>
#    Then I click on the tree button to contract <table_name> tree
#    Then I connect to YW database
#    Then I verify parametric histogram report
#    Then I verify the graph elements x axis
#    Then I verify the graph elements y axis
#    Examples:
#      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
#      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
  @parametric_histogram @errors_tab
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on errors tab
    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
  @parametric_histogram @data_tab
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on data tab
    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
  @parametric_histogram @parametric_histogram_legends @legends
  Scenario Outline: Parametric Histogram - Legends
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on the legends button
    Then I connect to test database
    Then Save in <expected_result_col> across <expected_result_key> test database
    Then I get the <expected_result_col> across <expected_result_key> from test automation database
#    Then I get the <expected_result_col> expected output data from test automation database
    Then I verify the Min, Max , Die Count
#    Then Get the Expected result
#
    Examples:
     |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col|expected_result_key|
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |expected_legend_histo|min_max_diecount|

  @parametric_histogram @grid_column_chooser
  Scenario Outline: Verify Parametric Histogram - grid column chooser
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on data tab
    Then I click on the grid column chooser
    Then I get selected tables from grid chooser
    Then I Verify the tables data against Grid view
    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
  @parametric_histogram @grid_col_chooser
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on data tab
    Then I click on the grid column chooser

    Examples:
      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @grid_col_chooser
  Scenario Outline: Verify Parametric Histogram Report
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on data tab
    Then I click on the grid column chooser
    Then I get selected tables from grid chooser

    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |
  @parametric_histogram @histogram_data_tab
  Scenario Outline: Verify parametric histogram data tab
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on data tab
    Then I get the data from Data Grid View
    Then I connect to test database
    Then Save in <expected_result_col> across <expected_result_key> test database
    Then I get the <expected_result_col> across <expected_result_key> from test automation database
    Then I verify the data grid views data against database data
    Examples:
     |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

#  @parametric_histogram @stats_tab
#  Scenario Outline: Verify Parametric Histogram Report stats tab
#    Given I am on login screen
#    When I enter the valid <Credential> credential
#    And I hit login button
#    And I verify dashboard is displayed
#    Then I click on "Histogram" from menu
#    Then I select selection criteria button
#    Then I verify the selection criteria window in displayed
#    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
#    Then I select the <table_name> from selection criteria
#    Then I click on Select and Close button
#    Then I generate the report
#    Then I click on stats tab
#    Then I connect to test database
#    Then I get the data from statistics grid
#    Then Save in <expected_result_col> across <expected_result_key> test database
#    Then I get the <expected_result_col> across <expected_result_key> from test automation database
#    Then I verify the stats tab
#
#    Examples:
#      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
#      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

  @parametric_histogram @errors_tab
  Scenario Outline: Verify Parametric Histogram Report error tabs
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on errors tab
    Then I connect to YW database
    Then I get the data from Errors Grid View
    Then Save in <expected_result_col> across <expected_result_key> test database
    Then I get the <expected_result_col> across <expected_result_key> from test automation database
    Then I verify the errors tab

    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Download plot as a png" from graph

    Examples:
      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Zoom" from graph

    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Pan" from graph

    Examples:
       |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Box Select" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Lasso Select" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Zoom in" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Zoom out" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Autoscale" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Reset axes" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Toggle Spike Lines" from graph

    Examples:
      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Show closest data on hover" from graph

    Examples:
      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Compare data on hover" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Show/Hide Designer" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "YAxis Break" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "XAxis Break" from graph

    Examples:
        |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |

  @parametric_histogram @histogram_graph_btn
  Scenario Outline: Verify Parametric Histogram - Graph buttons
    Given I am on login screen
    When I enter the valid <Credential> credential
    And I hit login button
    And I verify dashboard is displayed
    Then I click on "Histogram" from menu
    Then I select selection criteria button
    Then I verify the selection criteria window in displayed
    Then I get the <table_data> names of column against <policyName> policy from <markFilePath> from data base
    Then I select the <table_name> from selection criteria
    Then I click on Select and Close button
    Then I generate the report
    Then I click on "Produced with Plotly" from graph

    Examples:
      |Credential  | table_data                             | table_name                             | policyName | markFilePath     |expected_result_col   | expected_result_key |
      | Login     | Facility ,Wafer, Lot, Test Parameter   | Facility,Wafer, Lot, One Test Parameter    | Loader     | marked_parametric_file_path  | expected_legend_histo | data_tab_grid       |



###      stats vs Database
###     Then I verify the statistics grid against database data

###    error vs Database
###    Then I get the data from database across <facility_name>
#
