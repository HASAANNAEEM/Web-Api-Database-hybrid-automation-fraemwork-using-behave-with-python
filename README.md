**HYBRID-AUTOMATION-FRAMEWORK with ALLURE Reporting**
We setup the environment and run the automation scripts individually for Websites so that
 we can test our basic scripts in that and get ourselves going for automation.


Now having this  project ,we just need to install the requirments.txt and run the basic automation scripts in BDD framework.

 In addition to the web, we have added the Database (MariaDB) and API's Automation support.
**TO RUN THE PROJECT:**

1.install python 64 bit version

2.Install the following libraries:

    allure_python_commons==2.9.43
    jsonpath==0.82
    requests==2.26.0
    selenium==3.141.0
    behave==1.2.6
    pymongo==3.12.0
    pywinauto==0.6.8
    Appium_Python_Client==1.3.0
    PyYAML==5.4.1

 Or you can simply pip install -r requirements.txt


3.Install Allure
    i.Download the latest file from https://github.com/allure-framework/allure2/releases
    ii.Extract the file contents to you local drive e.g. c:\allure
    iii.Add the bin directory of allure to PATH  variable. e.g. C:\allure\allure-2.6.0\bin
    iv. Open a new Terminal and type allure --version => Should give the correct version number

    [For Reference - Detailed/Alternate Install instructions are in the link
     - https://github.com/allure-framework/allure2#download]

4.Test Execution:
    i.To Execute All features
        behave -f allure_behave.formatter:AllureFormatter -c -o allure-report ./Features
    ii.To execute particular feature file
        behave -f allure_behave.formatter:AllureFormatter -c -o allure-report ./Features/TestCase.feature
    iii.To execute using tags
        a.Using one tag -
                behave -f allure_behave.formatter:AllureFormatter -c -o allure-report --tags=@taggOfScenerio1
        b.Using multiple tags -
            behave -f allure_behave.formatter:AllureFormatter -c -o allure-report --tags=@taggOfScenerio1,@taggOfScenerio2
        c.Skip a Scenario or a feature:
            add the tag @skip to the scenario or at the top of the feature
        d.Using the test Suite:
            behave -f allure_behave.formatter:AllureFormatter -c -o allure-report ./Features/TestSuitDIr/
    iv.To re run failed Test cases
            behave -f allure_behave.formatter:AllureFormatter -c -o allure-report @rerun_failing.features

5.To generate report:
  allure serve allure-report

6. To add All dependent Libraries:
    pip install -r requirements.txt

