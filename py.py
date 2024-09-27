from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import os

def youtube_search_and_play(query):
    # Path to the chromedriver executable
    chrome_driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update this path

    # Verify ChromeDriver path
    if not os.path.exists(chrome_driver_path):
        print(f"ChromeDriver not found at {chrome_driver_path}. Please check the path.")
        return

    # Set up the WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)

    try:
        # Open YouTube
        driver.get('https://www.youtube.com')

        # Find the search box and enter the query
        search_box = driver.find_element(By.NAME, 'search_query')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        time.sleep(5)  # Adjust the sleep time if necessary

        # Retrieve the first video result and click on it
        first_video = driver.find_element(By.XPATH, '//*[@id="video-title"]')
        first_video.click()

        # Wait for the video to play for a while (e.g., 30 seconds)
        time.sleep(30)  # Adjust the sleep time to your needs

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == '__main__':
    query = input("Enter search query: ")
    youtube_search_and_play(query)
