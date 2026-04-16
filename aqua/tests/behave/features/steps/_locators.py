# locators.py

class Locators:
    # Dictionary to store locators for different fields
    locators = {
        "aquarequest2_test": "https://rtms.mcd.com/",
        "aquarequest2_prod": "http://aquarequest2.test.acrom.ro/",
        "testreq_local": "http://localhost:3030/",
        "rtms_eu": "https://rtms.mcd.com/",
        "rtms_us": "https://rtms-us.mcd.com/",
        "acrom_logo": "//img[@alt='Acrom logo']",
        "test_user": "qa",
        "test_pass": "Romania072",
        "wrong_pass": "Romania07211",
        "test_user_av": "alexandra.velican@acrom.ro",
        "login_page": "//h1[normalize-space()='Login']",
        "login_page_rtms": "//span[@class='login-title primary-text']",
        "sidebar_btn": "//button[@type='button' and contains(@class,'app-bar-nav-icon')]",
        "save_btn": "//span[normalize-space()='Save']",
        "sidebar": "//nav[@id='sidebar']",
        "sidebar_title": "//div[@id='logo']//div[contains(text(),'AQUA Labs')]",
        "side_menu_generic": "//div[contains(text(),'{}')]",
        "side_menu_labs": "//div[@class='v-list-item-title'][normalize-space()='Labs']",
        "page_header_generic": "//div[@id='page_header']//h1[normalize-space()='{}']",
        "add_hardware_header": "//h3[normalize-space()='Add hardware']",
        "hw_mode_input": "//input[@id='hw_model']",
        "hw_owner_input": "//input[@id='hw_owner']",
        "hw_label_input": "//input[@id='hw_label']",
        "hw_mac_input": "//input[@id='hw_mac']",
        "hw_enabled_input": "//input[@id='hw_enabled']",
        "hw_available_input": "//input[@id='hw_available']",
        "hw_serial_number_input": "//input[@id='hw_serial_number']",
        "hw_type_input": "//input[@id='hw_type']",
        "hw_specifications_input": "//input[@id='hw_specifications']",
        "hw_oob_type_input": "//input[@id='ansible_oob_type']",
        "hw_oob_ip_input": "//input[@id='ansible_oob_ip']",
        "hw_oob_user_input": "//input[@id='ansible_oob_user']",
        "hw_oob_pass_input": "//input[@id='ansible_oob_pass']",
        "hardware_table_objects": "//table[@id='hardware_table']//tbody/tr",
        "new_btn": "//span[normalize-space()='New']",
        "saved_progress_title": "//h2[@id='swal2-title']",
        "login_username": "//input[@id='login_username']",
        "login_password": "//input[@id='login_password']",
        "login_user": "//input[@id='username']",
        "login_pass": "//input[@id='password']",
        "login_btn": "//button[@type='submit']",
        "login_error": "//div[@class='error_message']",
        "dashboard_title": "//h1[normalize-space()='Dashboard']",
        "Model": "//input[@id='model']",
        "Name": "//input[@id='name']",
        "Email": "//input[@id='email']",
    }

    @staticmethod
    def get_locator(field_type):
        """
        Returns the locator for the given field type.

        Args:
            field_type (str): The type of the field to get the locator for.

        Returns:
            str: The XPath or CSS selector of the field.

        Raises:
            KeyError: If the field_type is not found in the locators.
        """
        try:
            return Locators.locators[field_type]
        except KeyError:
            raise KeyError(f"Locator for field type '{field_type}' not found.")
