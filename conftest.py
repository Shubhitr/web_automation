from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest
from selenium.webdriver.common.by import By
import os

from tests.test_flipkart import logger


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.set_window_size(1280, 1200)
    logger.info("Driver initialized")
    yield driver

    # driver.find_element()
    # ele = driver.find_element()._get

def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="Environment to run tests against"
    )
    parser.addoption(
        "--htmlpath", action="store", default="report.html", help="Path to save the HTML report"
    )

def pytest_configure(config):
    print(f"ENVVVVVVVVVV------{config.getoption('--env')}")

def pytest_sessionstart(session):
    logger.info("Starting the test session...")

def pytest_sessionfinish(session, exitstatus):
    html_path = session.config.getoption("--htmlpath")
    logger.info(f"HTML: {html_path}")
    session.config._html = None  # Ensure no conflict with previous reports
    terminal_reporter = session.config.pluginmanager.getplugin("terminalreporter")

    if terminal_reporter:
        terminal_reporter.write(f"\n[INFO] Generating HTML report at: {html_path}\n")
    session.config.hook.pytest_html_report_title(report="My Custom Report")
    session.config.hook.pytest_html_results_summary(report="Summary Section")
    # session.config.hook.pytest_html_path(htmlpath=html_path)







