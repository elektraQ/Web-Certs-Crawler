from libraries import *

class crawl_webspace:
    def __init__(self, vendor, url, file_type):
        self.url = url
        self.file_type = file_type
        self.vendor = vendor

    def crawl_website_bs4(self):

        # If there is no such folder, the script will create one automatically
        folder_location = 'Certificates/' + self.vendor + "_" + self.file_type
        if not os.path.exists(folder_location): os.mkdir(folder_location)

        # HTML GET response
        response = requests.get(self.url)
        soup_obj = BeautifulSoup(response.text, "html.parser")

        return soup_obj, folder_location

    def crawl_website_selenium(self):

        # If there is no such folder, the script will create one automatically
        folder_location = 'Certificates/' + self.vendor + "_" + self.file_type
        if not os.path.exists(folder_location): os.mkdir(folder_location)

        # Set Chrome Extensions
        # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver = webdriver.PhantomJS("/usr/bina/phantomjs")
        # Get URL object including js,css & html
        driver.get(self.url)

        #driver.find_element_by_css_selector("a[onclick*=DownloadData]").click();

        # Extract a required portion from the Selenium object
        #selenium_obj = driver.find_element_by_tag_name('body')
        #selenium_obj = driver.page_source

        print(driver.page_source)
        driver.close()
        #return selenium_obj, folder_location

    def download_all_extensions_bs4(self):

        soup_obj, folder_location = self.crawl_website_bs4()

        for link in soup_obj.select("a[href$=" + "'." + str(self.file_type) + "'" + "]"):
            # Name the pdf files using the last portion of each link which are unique in this case
            filename = os.path.join(folder_location, link['href'].split('/')[-1])
            with open(filename, 'wb') as f:
                f.write(requests.get(urljoin(self.url, link['href'])).content)

        return


    def download_all_extensions_selenium(self):

        selenium_obj, folder_location = self.crawl_website_selenium()

        print(selenium_obj)

        # for link in selenium_obj.select("a[href$=" + "'." + str(self.file_type) + "'" + "]"):
        #     # Name the pdf files using the last portion of each link which are unique in this case
        #     filename = os.path.join(folder_location, link['href'].split('/')[-1])
        #     with open(filename, 'wb') as f:
        #         f.write(requests.get(urljoin(self.url, link['href'])).content)

        return