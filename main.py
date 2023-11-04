# --------- imports ---------
from Session import Session
from UserPrompt import UserPrompt
from constants import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pdfkit

if __name__ == "__main__":

    # Session List
    sessions: [Session]
    json_file = {}
    html_template: str = """
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                </head>
                <body>
            """

    # Display all the programs that offers ETS & Ask the user to pick a program
    print("Welcome to the typical path generator for ETS students please pick your desired program !")

    # Ask for debut year and witch program he studies
    options = UserPrompt.pick_a_program()

    # Ask other questions
    options = ask_right_questions(options=options)

    program = options.get("program")
    link_ets = f"https://www.etsmtl.ca/etudes/premier-cycle/Baccalaureat-genie-{program}#Cheminement-type"

    # set the right parser
    parser = get_parser_of(options=options)

    # set the browser
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # Opens the page
    driver.get(link_ets)
    driver.implicitly_wait(10)

    # clicks on the right button
    section = driver.find_element(By.XPATH, f"//*[contains(text(),' {parser.get_courses_div_content()} ')]")
    ActionChains(driver) \
        .click(section) \
        .perform()
    driver.implicitly_wait(10)

    # Gets the source code
    html = driver.page_source
    driver.implicitly_wait(10)

    # initialize a parser with BS4
    soup = BeautifulSoup(html, 'html.parser')

    content_table = soup.find_all("div", class_=Parser.COURSE_PER_SESSION_DIV)[0]

    sessions = parser.parse_all_courses(html=content_table, options=options)

    for s in sessions:
        for c in s.get_courses():
            link = c.get_link()
            if link:
                driver.get(link)
                driver.implicitly_wait(20)
                html = driver.page_source
                driver.implicitly_wait(20)
                soup = BeautifulSoup(html, "html.parser")
                html = soup.find_all("div", "fiche__descr")[0]
                c.set_description(parser.parse_course_details(html=html))
        # Generating the json file
        json_file[s.get_title()] = s.get_dict()
        html_template += s.get_html()
    html_template += """
            </body>
        </html>
        """
    driver.implicitly_wait(10)
    driver.quit()

    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

    opt = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        '--user-style-sheet': "style.css"
    }
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    pdfkit.from_file('output.html', output_path="output.pdf", configuration=config, options=opt)
