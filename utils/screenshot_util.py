import os
import time

def take_screenshot(driver, name_prefix="screenshot"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    folder_path = "screenshots"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{name_prefix}_{timestamp}.png")
    driver.save_screenshot(file_path)
    print(f"[INFO] Screenshot saved to {file_path}")