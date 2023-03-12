from selenium.webdriver.common.by import By


class CreatePolicyElements:
    SelectSelectionCriteria = (By.XPATH, "//button[contains(text(),'Selection Criteria')]")
    SelectAndCloseBtn = (By.XPATH, "//button[text()='Select and Close']")
    SearchFacilityNameInputField = (By.XPATH, "//*[text()='Facility']//..//..//..//..//input[contains(@class,'texteditor')]")
    SearchLotNameInputField = (By.XPATH, "(//*[text()='Lot']//..//..//..//..//input[contains(@class,'texteditor')])[1]")
    checkbox_input_field = "//*[contains(text(),'%s')]//..//..//..//..//..//*[contains(text(),'%s')]//..//..//span[@class='dx-checkbox-icon']"
    wafer_checkbox_input_field = "//*[contains(text(),'%s')]//..//..//..//..//..//*[text()='%s']//..//..//span[@class='dx-checkbox-icon']"
    SearchWaferNameInputField = (By.XPATH, "(//*[text()='Wafer']//..//..//..//..//input[contains(@class,'texteditor')])[1]")
    SearchTestParameterNameInputField = (By.XPATH, "(//*[text()='Test Parameter']//..//..//..//..//input[contains(@class,'texteditor')])[1]")
    SearchWorkCenterInputField = (
    By.XPATH, "//*[text()='Work Center']//..//..//..//..//input[contains(@class,'texteditor')]")
    SearchDeviceInputField = (
    By.XPATH, "//*[text()='Device']//..//..//..//..//input[contains(@class,'texteditor')]")
    SearchTestProgramInputField = (
        By.XPATH, "//*[text()='Test Program']//..//..//..//..//input[contains(@class,'texteditor')]")
    SearchTestProgramRevisionInputField = (
        By.XPATH, "//*[text()='Test Program Revision']//..//..//..//..//input[contains(@class,'texteditor')]")

    FacilityTable = (By.XPATH, "//*[text()='Facility']//..//..//..//..//table[contains(@class,'dx-select')]//tbody")
    FacilityScroll = (By.XPATH, "//*[text()='Facility']//..//..//..//..//table[contains(@class,'dx-select-checkboxes-hidden')]//tr[last()-2]")
    LotTable = (By.XPATH, "//*[text()='Lot']//..//..//..//..//table[contains(@class,'dx-select')")
    WaferTable = (By.XPATH, "//*[text()='Wafer']//..//..//..//..//table[contains(@class,'dx-select')]")
    TestParameterTable = (By.XPATH, "//*[text()='Test Parameter']//..//..//..//..//table[contains(@class,'dx-select')]")
    create_policy = '//button[text()="Create Policy"]'
    policy_name = '//input[@name="name"]'
    policy_version = '//input[@name="version"]'
    policy_desc = '//textarea[@name="purpose"]'
    policy_owner_email_input_field = "//input[@name = 'owner']"
    add_stage = '//div[@class=" dropdown-full dropdown"]//button[text()="Add Stage"]'
    policy_polling = '//span[contains(text(),"Polling Interval")]/parent::span/parent::div/div/div/input'
    view = '//button[contains(text(),"View")]'
    source_format = '//button[text()="ATDF"]'
    source_of_file = '//button[contains(text(),"Policy Step")]'
    policy_step_drop_down = (By.XPATH, "(//span[text()='Source'])[last()]//..//button")
    container = '//span[text()="Source Container"]/parent::div//div//input'
    ftp_address = '//span[text()="Ftp Address"]/parent::div//div//input'
    ftp_username = '//span[text()="Ftp Username"]/parent::div//div//input'
    ftp_password = '//span[text()="Ftp Password"]/parent::div//div//input'
    folder_to_transfer_files_from = '//span[text()="Folder to transfer files from"]/parent::div//div//input'
    type = '//span[text()="Type"]/parent::span/parent::div/div/div/div/button'
    start_time = '(//span[text()="Starts At"]/parent::span/parent::div/div/div//input)[2]'
    save_btn = '//*[text()="Save"]'
    success_alert_message = (By.XPATH, '//div[contains(@class,"toast--success")]//div[@role="alert"]')
    filter = '(//td[@aria-colindex="6" and @aria-label="Filter cell"]/div//div[2]//div//div//input)[last()]'
    step_intake_queue = (By.XPATH, "//a[contains(text(),'Step Intake')]")
    step_intake_queue_policy_name_input_field = (
    By.XPATH, "//div[contains(text(),'Policy Name')]//..//..//following-sibling::tr//td[3]//input")
    step_intake_queue_status = (
    By.XPATH, "(//table[contains(@class,'select-checkboxes')])[last()]//td[contains(@aria-colindex,'4')]//span")
    sort_start_time = '//div[text()="Start Time"]'
    success_msg = '//tr[@aria-rowindex="1"]//td//span[text()="SUCCESS"]'
    target_file = '(//tr[@aria-rowindex="1"]//td[@aria-colindex="4" and contains(text(),"s3://yw-temp-convert-files")])'
    source_file_location = '(//tr[@aria-rowindex="1"]//td[@aria-colindex="3"])'
    die_records = '//label[contains(text(),"Read PIR/PRR")]//input'
    read_die = '//h6[text()="Die Records"]/parent::div/div[2]/div'
    summary_records = '//h6[text()="Summary Records"]/parent::div/label/div/input'


    # LotCheckBox = (By.XPATH, "//td[text()='69807 LOT ID Test']//..//span[@class='dx-checkbox-icon']")

    # Edit policy name from Loader Policy Engine
    loader_policy_engine_input_field = (By.XPATH, "(//*[text()='Loader Policy Engine']//..//..//..//..//input[contains(@class,'texteditor')])[1]")
    select_policy = (By.XPATH, "//*[contains(text(),'%s')]")



