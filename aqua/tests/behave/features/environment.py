import os
import shutil
import behave
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from aqualab.aqualab import AquaLab
from aqualab.aquavision import AquaVision
from aqualab.aquadrop import AquaDrop
from aqualab.aquabox import AquaBox
from aqualab.framework.selenium_wrappers import SeleniumWrappers
from playwright.sync_api import sync_playwright			# Support for Microsoft PlayWright Testing Framework

def before_all(context):  
    # Mandatory import for AquaLab hook
	context.aqualab = AquaLab(context)
	context.aqualab.before_all(context)

	# Optional Component - AquaVision 
	context.aquavision = AquaVision("./features/aquavision.config.json")

	# Optional Component - AquaDrop 
	context.aquadrop = AquaDrop("./features/aquadrop.config.json")

	# Optional Component - AquaBox M1
	context.aquabox = AquaBox('AQUABOX/A-1', True)      # TRUE = Dry run mode
 
	# ===========================================================================================
	# AquaLab supports two different web-testing frameworks:
	# - Selenium
	# - Microsoft PlayWright
	# By default, AquaLab uses Selenium, and the configuration below is for Selenium
	# For PlayWright, comment the selenium block below, and uncomment the PlayWright block below
	# ===========================================================================================

	# Selenium Driver Configuration	
	options = Options()
	options.add_argument('--allow-running-insecure-content')
	options.add_argument('--ignore-certificate-errors')
	options.add_argument("--disable-dev-shm-usage")
	options.add_argument("--window-size=1920x1080")
	options.add_argument("--no-sandbox")

	# Special configuration for running in background, on the AquaRunner environment
	if os.getenv("AQUA_RUNNER_ENVIRONMENT") == "True":
		# Add headless mode when running in AquaCore (Docker)
		options.add_argument("--headless")
		options.add_argument("--disable-gpu")
		
    # Define one ore more browsers (for integration testing, you may define as many browser instances as needed). Name/index is not relevant
    # It is important to have separate services for each driver for resource management and aqualab management, even if services are configured identically
	chrome_driver_path=shutil.which("chromedriver")
	
	service = Service(executable_path=chrome_driver_path)
	context.browser  = webdriver.Chrome(service=service, options=options)

	service2 = Service(executable_path=chrome_driver_path)
	context.browser2 = webdriver.Chrome(service=service2, options=options)
 
	# Register browser(s) with AquaLab to let it know about it in order to control lifecycle and take screenshots
	context.aqualab.register_browser(context.browser)
	context.aqualab.register_browser(context.browser2)

	context.browser.maximize_window()
	context.browser2.maximize_window()
	context.browser.set_page_load_timeout(40)
	context.browser2.set_page_load_timeout(40)
	context.browser.get("https://acrom.ro")
	context.browser2.get("https://google.com")

	# Initialize SeleniumWrappers with the browser instance (optional, for more advanced functionality)
	context.selenium = SeleniumWrappers(context)
	context.memory = dict()
 
 
	# # PlayWright Testing Framework (alternative to Selenium)
	# if os.getenv("AQUA_RUNNER_ENVIRONMENT") == "True":
	# 	playwright_browser_options = {
	# 		"headless": False if os.getenv("AQUA_RUNNER_ENVIRONMENT") != "True" else True,
	# 		"args": [
	# 			'--allow-running-insecure-content',
	# 			'--ignore-certificate-errors',
	# 			'--disable-dev-shm-usage',
	# 			'--window-size=1920,1080',
	# 			'--start-maximized',
	# 			'--no-sandbox',
	# 			'--disable-web-security',
	# 			'--disable-features=StrictOriginIsolation,NetworkService,NetworkServiceInProcess'
	# 		]
	# 	}
	# context.playwright = sync_playwright().start()
	# context.browser  = context.playwright.chromium.launch(**playwright_browser_options)
	# context.browser2 = context.playwright.chromium.launch(**playwright_browser_options)
	# context.browser  = context.browser.new_context(no_viewport=True)	 # Remove any viewport restrictions to enable full-screen
	# context.browser2 = context.browser.new_context(no_viewport=True)	 # Remove any viewport restrictions to enable full-screen
	# context.page  = context.browser.new_page()
	# context.page2 = context.browser.new_page()
	# context.page.goto("https://acrom.ro")
	# context.page2.goto("https://google.com")
	# context.aqualab.register_playwright_session(context.browser, context.page)
	# context.aqualab.register_playwright_session(context.browser2, context.page2)
 
def before_scenario(context, scenario):
    context.aqualab.before_scenario(context, scenario)
 
def before_step(context, step):
    context.aqualab.before_step(context, step)	
 
def after_step(context, step):
    context.aqualab.after_step(context, step)	
    
def after_scenario(context, scenario):
	context.aqualab.after_scenario(context, scenario)

def after_all(context):  
    context.aqualab.after_all(context)
    


    