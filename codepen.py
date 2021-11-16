def get_codepen_data(driver, URL):
    codepen_data = {}
    
    driver.get(URL)

    # author name and title
    title = driver.find_element_by_id("item-title").text
    author_div = driver.find_element_by_css_selector("[data-test='AnItemBy']")
    author_name = author_div.find_element_by_css_selector("a").text

    codepen_data["title"] = title
    codepen_data["author-name"] = author_name

    # made with 
    html_script = driver.find_element_by_class_name("html-editor-resizer")
    html_preprocessor = html_script.find_element_by_class_name("box-title-preprocessor-name").text
    html_script = f"HTML{html_preprocessor if html_preprocessor else ''}"

    css_script = driver.find_element_by_class_name("css-editor-resizer")
    css_preprocessor = css_script.find_element_by_class_name("box-title-preprocessor-name").text
    css_script = f"CSS{css_preprocessor if css_preprocessor else ''}"

    js_script = driver.find_element_by_class_name("js-editor-resizer")
    js_preprocessor = js_script.find_element_by_class_name("box-title-preprocessor-name").text
    js_script = f"JS{js_preprocessor if js_preprocessor else ''}"

    codepen_data["made-with"] = f"{html_script}, {css_script}, {js_script}"

    # created date
    comments_button = driver.find_element_by_css_selector("[data-id='editor-comments-button']")
    comments_button.click()
    created_date = driver.find_element_by_xpath("//*[contains(text(), 'Created on')]/following-sibling::dd").text

    codepen_data["created-date"] = created_date

    # driver.close()

    return codepen_data