from selenium.webdriver.common.by import By


class ReportsElements:
    soft_bin = (By.XPATH, "//div[@class='wafer-tooltip']/div[1]/text()")
    is_selected = (By.XPATH, "//div[@class='wafer-tooltip']/div[2]/text()")
    x_axis = (By.XPATH, "//div[@class='wafer-tooltip']/div[3]/text()")
    y_axis = (By.XPATH, "//div[@class='wafer-tooltip']/div[4]/text()")

    data_tab = (By.XPATH, "//a[@id='customized-report-tabs-tab-data' and text()='Data']")
    data_grid_view_element = (By.XPATH, "//tr[@class='dx-row dx-data-row dx-column-lines']//td")
    grid_column_chooser = (By.XPATH, "//button[text()='Grid Column Chooser']")

    stats_tab = (By.XPATH, "//a[@id='customized-report-tabs-tab-statistics' and text()='Statistics']")
    errors_tab = (By.XPATH, "//a[contains( text(),'Errors')]")
    download_plot_as_png = (By.XPATH, "//a[@data-title='Download plot as a png']")
    expend_all_legends = (By.XPATH, "//button[@class='mr10 btn btn-secondary']")
    remove_all_legends = (By.XPATH, "//button[@class='btn btn-danger']")
    legend_btn = (By.XPATH, "//*[text()='Legend']")
    min_legend = "//tbody[@role='presentation']//tr[@class='dx-row dx-data-row " \
                 "dx-column-lines']//td[@aria-colindex='5']"
    max_legend = "//tbody[@role='presentation']//tr[@class='dx-row dx-data-row" \
                 " dx-column-lines']//td[@aria-colindex='6']"
    die_count_legend = "//tbody[@role='presentation']//tr[@class='dx-row dx-data-row" \
                       " dx-column-lines']//td[@aria-colindex='7']"

    download_plot_as_png_btn = (By.XPATH, "//a[@class='modebar-btn' and "
                                          "@data-title='Download plot as a png']")
    zoom_btn = (By.XPATH, "//a[@data-title='Zoom']")
    pan_btn = (By.XPATH, "//a[@data-title='Pan']")
    box_select_btn = (By.XPATH, "//a[@data-title='Box Select']")
    lasso_select_btn = (By.XPATH, "//a[@data-title='Lasso Select']")
    zoom_in_btn = (By.XPATH, "//a[@data-title='Zoom in']")
    zoom_out_btn = (By.XPATH, "//a[@data-title='Zoom out']")
    autoscale_btn = (By.XPATH, "//a[@data-title='Autoscale']")
    reset_axes_out_btn = (By.XPATH, "//a[@data-title='Reset axes']")
    toggle_spike_lines_btn = (By.XPATH, "//a[@data-title='Toggle Spike Lines']")
    show_closest_data_on_hover_btn = (By.XPATH, "//a[@data-title='Show closest data on hover']")
    compare_data_on_hover_btn = (By.XPATH, "//a[@data-title='Compare data on hover']")

    show_hide_designer_btn = (By.XPATH, "//a[@data-title='Show/Hide Designer']")
    y_axis_break_btn = (By.XPATH, "//a[@data-title='YAxis Break']")
    x_axis_break_btn = (By.XPATH, "//a[@data-title='XAxis Break']")
    produced_with_plotly_btn = (By.XPATH, "//a[@data-title='Produced with Plotly']")

    graph_svg_element = "//*[local-name()='svg']//*[name()='g' and @class='point']"
    graph_g_ytick = "//*[name()='g' and @class='ytick']"
    graph_g_xtick = "//*[name()='g' and @class='xtick']"



    graph_bar_value = "//*[local-name()='svg']//*[name()='g' and @class='hovertext']//*[name()='text']"

    btn_element_grid_chooser = (By.XPATH, "(//div[@title='Grid Column Chooser']//button[text()='Grid Column Chooser'])[1]")
    generate_report_btn = (By.XPATH, "//button[text()='Generate']")
    canvas_exists = (By.XPATH, "//canvas")
    bar_histogram = (By.XPATH, "//*[local-name()='svg']//*[name()='g' and @class='point']")

    grid_window_chooser_chkbox_unchecked = (By.XPATH, "//*[@class='dx-treeview-node dx-treeview-item-with-checkbox' "
                                       "and @aria-selected='false']")
    grid_window_chooser_chkbox_checked = (By.XPATH, "//*[@class='dx-show-invalid-badge dx-checkbox "
                                                    "dx-checkbox-indeterminate dx-widget' and @aria-checked='mixed']")
    mode_bar_btn_element = (By.XPATH, "//a[@class='modebar-btn']")
    li_grid_column_chooser = (By.XPATH, "//li[@class='dx-treeview-node dx-treeview-item-with-checkbox"
                                        " dx-state-selected dx-treeview-node-is-leaf']")
    grid_window_form = (By.XPATH, "//ul[@class='dx-treeview-node-container dx-treeview-node-container-opened']")
    grid_column_chooser_tree_btn = (By.XPATH, "//div[@class='dx-treeview-toggle-item-visibility']")

    grid_window_facility_child_element = (By.XPATH, "//div[text()='FACILITY']//..//..//ul//li[@aria-selected='true']//div[contains(@class,'dx-item-content')]")
    grid_window_facility_sib = (By.XPATH, "//li[@class='dx-treeview-node dx-treeview-item-with-checkbox']"
                                          "//div[@class='dx-show-invalid-badge dx-"
                                          "checkbox dx-checkbox-indeterminate dx-widget'][@aria-checked='mixed']"
                                          "/following-sibling::div[contains(@class,'dx-item')]//div")