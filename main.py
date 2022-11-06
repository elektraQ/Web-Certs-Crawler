from libraries import *



if __name__ == '__main__':

    # Getting AllowList root CA certs
    allow_list_root_ca_url = yaml_parser('allow-list-root-ca-url-html').readYAML()

    print("Let's start crawling...")

    for i in range(len(allow_list_root_ca_url)):
        print("Crawling " + allow_list_root_ca_url[i][0] + " " + "website...")
        print(allow_list_root_ca_url[i][1])
        crawl_webspace(allow_list_root_ca_url[i][0], allow_list_root_ca_url[i][1], allow_list_root_ca_url[i][2]).crawl_website_bs4()

    print("Finished crawling")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
