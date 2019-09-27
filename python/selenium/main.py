from aegisblade import aegisblade
from aegisblade import JobConfig, Capability

from selenium import webdriver

def selenium_firefox_job():
    """
    In this example we will deploy & run this function
    inside of AegisBlade.

    selenium_firefox_job demonstrates how to specify the 
    firefox browser requirement to AegisBlade and subsequently
    run a job able to use Selenium with Firefox.
    """
    driver = webdriver.Firefox()
    driver.get("https://www.python.org")
    print(driver.title)

    return driver.title

def selenium_chrome_job():
    """
    In this example we will deploy & run this function
    inside of AegisBlade.

    selenium_chrome_job demonstrates how to specify the 
    chrome browser requirement to AegisBlade and subsequently
    run a job able to use Selenium with Chrome.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    print(driver.title)

    return driver.title

def main():
    """
    The main() function will run on your local machine
    and start two jobs on AegisBlade with the above functions.
    """

    # Use Capability.chrome to specify that chrome should be installed.
    chrome_job_config = JobConfig() \
            .with_memory(1024) \
            .with_capability(Capability.chrome)

    # Use Capability.firefox to specify that firefox should be installed.
    firefox_job_config = JobConfig() \
            .with_memory(1024) \
            .with_capability(Capability.firefox)

    # Start the chrome & firefox jobs at the same time, in parallel.
    # AegisBlade will handle provisioning hosts, deploying your code, and running it.
    chrome_job = aegisblade.run(lambda: selenium_chrome_job(), chrome_job_config)
    firefox_job = aegisblade.run(lambda: selenium_firefox_job(), firefox_job_config)

    # Calling .get_return_value() will wait for the job to end, then get the 
    # value returned by the function run on AegisBlade.
    try:
        chrome_job_return_value = chrome_job.get_return_value()
        firefox_job_return_value = firefox_job.get_return_value()
    finally:
        print("Chrome Job Logs:")
        print(chrome_job.get_logs())
        print(" ---- ---- ----")

        print("")

        print("Firefox Job Logs:")
        print(firefox_job.get_logs())
        print(" ---- ---- ----")

    assert "Python" in chrome_job_return_value
    assert "Python" in firefox_job_return_value


# Using the __name__ == "__main__" idiom to only run main when this script
# is called directly is especially important when using AegisBlade.
#
# This script may be imported by the AegisBlade runtime, and without the 
# protective check of __name__, main() would be called inside the job 
# potentially causing an infinite loop of jobs starting more jobs 0_o
if __name__ == "__main__":
    main()
