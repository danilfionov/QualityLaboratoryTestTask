class Locators:
    class Button:
        buttons = ["//input[@class='button' and @value=\'{}\']",
                   "//div[@style='display: block;']/div/button[.=\'{}\']",
                   "//button[contains(text(),\'{}\') and not(ancestor::*[contains(@style,'display: none')])]",
                   #"//button[contains(text(),\'{}\')]",
                   "//input[@type='submit' and @value=\'{}\']"]

        button_delete_client = "//a[@class='js-change-client change-client']"
        button_save = "//input[@type='submit' and @value='Сохранить']"
        button_close = "//div[@class='gootax-modal-wrapper active']/child::*/child::i[@class='button close-modal']"
        button_edit = "//span[@class='edit_client_data']"
        button_plus = "//a[@class='add-point js-add-order-point']"
        button_send = "//a[@class='send-to-order-chat']/i"
        button_orders_history = ("//a[normalize-space(@class) = 'order-point-history js-address-history active' and "
                                 "not(ancestor::"
                                 "div[contains(@style,'display:none')]) and not(ancestor::div[contains(@style,"
                                 "'display: none')])]")

        button_action_with_address = "//i[@class='toggle-actions ui-sortable-handle']"
        button_delete = "//a[@class='delete-point']"

    class Button_Type_Link:
        button_type_link = ["//a[@href and contains(text(),\'{}\') and (ancestor::*[@class='opened'])]",
                            "//a[text()=\'{}\' and not(@rel) and not(contains(@style, 'display: none')) and not("
                            "ancestor::*[contains(@style,'display: none')])]",
                            "//a[text()=\'{}\' and not(@class='a_select sel_active') and not(contains(@style, "
                            "'display: none')) and not(ancestor::*[contains(@style,'display: none')])]",
                            "//a[contains(text(),\'{}\') and not(contains(@style, 'display: none')) and not("
                            "ancestor::*[contains(@style, 'display: none')])]",
                            "//a/child::*[contains(text(),\'{}\') and not(contains(@style, 'display: none'))]"]

    class Link:
        link = ["//a[normalize-space(.) = \'{}\' and (@href or @rel) and not(ancestor::*[contains(@style, 'display: "
                "none')])]",
                "//a[text()=\'{}\' and @href]",
                "//a/child::*[contains(text(),\'{}\')]",
                "//a[text()=\'{}\']",
                "//a[normalize-space(text()) = \'{}\' and not(ancestor::*[@style='display: none']) and @href]",
                "//a[normalize-space(text()) = \'{}\']"]

    class Fields:
        fields = ["//strong[contains(text(), \'{}\')]/child::span[contains(@class,'response-code')]",
                  "//div[@placeholder=\'{}\']",
                  "//div[text()=\'{}\']/following-sibling::textarea",
                  "//textarea[@placeholder=\'{}\'  and not(ancestor::div[contains(@style, 'display:none')]) "
                  "and not(ancestor::div[contains(@style,'display: none')])]",
                  "//*[text()=\'{}\']/parent::*/descendant::input[not(ancestor::div[contains(@style,"
                  "'display:none')]) and not(ancestor::div[contains(@style,'display: none')])]",
                  "//input[@placeholder=\'{}\'  and not(ancestor::div[contains(@style, 'display:none')]) "
                  "and not(ancestor::div[contains(@style,'display: none')])]",
                  "//*[text()=\'{}\']/parent::*/descendant::input[not(ancestor::div[contains(@style,"
                  "'display:none')]) and not(ancestor::div[contains(@style,'display: none')])]",
                  "//input[@value=\'{}\' and not(@type='hidden')]",
                  "//label[text()=\'{}\']/parent::*/parent::*/descendant::input[not(@type='hidden') and not"
                  "(ancestor::div[contains(@style,'display:none')]) and not(ancestor::div[contains(@style,'display: none')])]",
                  "//label[text()=\'{}\']/parent::*/parent::*/descendant::textarea[not(@type='hidden') and not(ancestor::div[contains(@style,'display:none')]) and not(ancestor::div[contains(@style,'display: none')])]",
                  "//b[.=\'{}\']/following-sibling::b/span",
                  "//p[@id=\'{}\']"
                  "//span[.=\'{}\']/following-sibling::span/span",
                  "//b[.=\'{}\']/following-sibling::p",
                  "//b[.=\'{}\']/parent::*/following-sibling::*/input",
                  "//label[.=\'{}\']/parent::*/following-sibling::input[1]"]
        product_field = "//input[@name='autocomplete-items']"
        fields_point = ["//label[.=\'{}\']/following-sibling::input[(not(@data-type) or @data-type != 'hidden') "
                        "and @type='text' and not(ancestor::div[@style='display: none'])]"]

    class Heading:
        heading = ["//h1[contains(text(),\'{}\')]",
                   "//h2[contains(text(),\'{}\')]",
                   "//h3[contains(text(),\'{}\')]"]

    class Text:
        text = ["//span[text()=\'{}\']",
                "//p[normalize-space(.)=\'{}\' and not(@hidden)]",
                "//label[contains(text(),\'{}\')]",
                "//td[@data-year='2000']/a[.=\'{}\']",
                "//table[@class='ui-datepicker-calendar']/descendant::a[@class='ui-state-default' and .=\'{}\']",
                "//*[text()=\'{}\' and not(contains(@style, 'display: none')) and not(contains(@style, "
                "'visibility:hidden')) and not(ancestor-or-self::*[contains(@style,'display: none') or contains("
                "@style,'visibility: hidden')]) and"
                "(not(@aria-hidden) or @aria-hidden='false') and (self::a or self::button or self::input or "
                "self::select or self::textarea or self::label)]",
                "//*[text()=\'{}\' and not(preceding-sibling::*[@style='display: none;']) and "
                "not(ancestor::*[contains(@style, 'display: none')])]",
                "//span[normalize-space(.)=\'{}\']",
                "//*[normalize-space(.)=\'{}\' and not(ancestor::*[contains(@style,'display: none')])]"]
        text_contains = ["//*[contains(text(),\'{}\')]"]
        errors = ["//*[contains(@class,'error') and normalize-space(.)=\'{}\']",
                  "//*[@id='order-error' and contains(text(),\'{}\')]",
                  "//div[contains(@class,'empty') and contains(text(),\'{}\')]",
                  "//div[contains(@class,'error')]//child::*[contains(text(),\'{}\')]"]

    class Drop_Down_List:
        list = ["//*[contains(text(),\'{}\')]/ancestor::*[1]/descendant::div[@class='d_select ' and not(ancestor::*["
                "@style='display: none'])]/a",
                "//a[@class='a_select' and normalize-space(.)=\'{}\' and not(ancestor::*[contains(@style,'display: "
                "none')])]",
                "//a[contains(@class,'s_datepicker') and normalize-space(.)=\'{}\' and not(ancestor::*[contains("
                "@style,'display: none')])]",
                "//*[@class='select_checkbox']/a[normalize-space(.)=\'{}\']",
                "//a[normalize-space(.) = \'{}\' and @class='a_select' and ancestor::div[@class='d_select ']]",
                "//label[normalize-space(.)=\'{}\']/ancestor::section[1]/descendant::a[contains(@class,'show-picker')]",
                "//div[(text()=\'{}\')]/following-sibling::*/descendant::*/select/parent::*[@class='js-select']",
                "//*[contains(text(),\'{}\')]/ancestor::*[1]/descendant::select/parent::*",
                "//div[@class='js-select']/a[normalize-space(.)=\'{}\' and not(ancestor::*[contains(@style,'display: "
                "none')])]"]
        list_by_number = ["//*[normalize-space(.) = \'{}\']/following-sibling::*/descendant::*["
                          "@class='a_select' and not(ancestor::*[contains(@style, 'display: none')])]"]
        list_without_name = ("//select/following-sibling::div[not(ancestor::*[contains(@style,'display: none')])]"
                             "/a[not(ancestor::*[@style='display: none'])]|//div[@class='d_select tariff-groups']/a["
                             "not(ancestor::*[@style='display: none'])]")

    class Check_Box:
        check_box = ["//label/input/ancestor::label[contains(normalize-space(),\'{}\')]",
                     "//div[text()=\'{}\']/input",
                     "//input[@type='checkbox' and parent::*[normalize-space(.) = \'{}\']]"]
        radio = ["//div[text()=\'{}\']/input"]

    class Table:
        table = "//table[not(@class='ui-datepicker-calendar')]"
        column_name = ("//table[@class='js-orders order_table sortable']/tbody/tr[{}]/td[count(//table["
                       "@class='js-orders order_table sortable']/tbody/tr/th[contains(text(),\'{}\') or "
                       "child::a[contains(text(),\'{}\')]]/preceding-sibling::th) + 1]")
        column_number = "/tbody/tr[\'{}\']/td[count(//table/tbody/tr/th[\'{}\']/preceding-sibling::th)+1]"

    class Elements:
        delete_item = "//a[@class='delete-shop-button' and not(ancestor::*[contains(@style,'display: none')])]"
        executor = "//input[@placeholder='Поиск']/following-sibling::a[@class='order-free-drivers active js-order-free-drivers']"

    class Mouse:
        toggle_action = "//(@class='toggle-actions ui-sortable-handle')"

    class Map:
        map = "//div[@id='order-map' or @id='map']"
        map_point = "//*[contains(@class,'map_icon_point')]"
        edit_order = "//i[contains(@class,'toggle-actions ui-sortable-handle')]"

    class Modal_Window:
        window = ("//ul[@class='ui-menu ui-widget ui-widget-content ui-autocomplete ui-front' and not(contains(@style,"
                  "'display: none'))]")
        modal_window = "//div[@class='gootax-modal']"

