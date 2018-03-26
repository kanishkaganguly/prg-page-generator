#!/usr/bin/env python3

import xml.etree.ElementTree as ET

from jinja2 import Environment, FileSystemLoader, select_autoescape

templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)
autoescape = select_autoescape(['html', 'xml'])
TEMPLATE_FILE = "project_template.html"
template = templateEnv.get_template(TEMPLATE_FILE)

tree = ET.parse("./gapflyt/settings.xml")
root = tree.getroot()
project_settings = list(root.iter())

author_list = []
root_folder, save_as, js_folder, css_folder, img_folder, misc_folder = [""] * 6
page_title, project_heading, lab_name, lab_url, univ_name = [""] * 5
abstract, project_description, project_poster, paper_pdf_url, bibtex = [""] * 5
yt_link, overview_pdf, overview_img = [""] * 3

for each_setting in project_settings:
    if each_setting.tag == 'root_folder':
        root_folder = each_setting.text
    if each_setting.tag == 'save_as':
        save_as = each_setting.text
    if each_setting.tag == 'js_folder':
        js_folder = each_setting.text
    if each_setting.tag == 'css_folder':
        css_folder = each_setting.text
    if each_setting.tag == 'img_folder':
        img_folder = each_setting.text
    if each_setting.tag == 'misc_folder':
        misc_folder = each_setting.text
    if each_setting.tag == 'page_title':
        page_title = each_setting.text
    if each_setting.tag == 'project_heading':
        project_heading = each_setting.text
    if each_setting.tag == 'lab_name':
        lab_name = each_setting.text
    if each_setting.tag == 'lab_url':
        lab_url = each_setting.text
    if each_setting.tag == 'univ_name':
        univ_name = each_setting.text
    if each_setting.tag == 'yt_link':
        yt_link = each_setting.text
    if each_setting.tag == 'overview_pdf':
        overview_pdf = each_setting.text
    if each_setting.tag == 'overview_img':
        overview_img = each_setting.text
    if each_setting.tag == 'abstract':
        abstract = each_setting.text
    if each_setting.tag == 'project_description':
        project_description = each_setting.text
    if each_setting.tag == 'project_poster':
        project_poster = each_setting.text
    if each_setting.tag == 'paper_pdf_url':
        paper_pdf_url = each_setting.text
    if each_setting.tag == 'bibtex':
        bibtex = each_setting.text

for author in root.iter('author'):
    author_dict = {}
    author_dict['name'] = author.find('author_name').text
    author_dict['url'] = author.find('author_url').text
    if author:
        author_list.append(author_dict)
outputText = template.render(
    js_analytics=js_folder + "/analytics.js",
    jsapi=js_folder + "/jsapi",
    gtagjs=js_folder + "/js",
    overview_pdf=misc_folder + "/" + overview_pdf,
    overview_img=img_folder + "/" + overview_img,
    project_poster=img_folder + "/" + project_poster,
    bibtex=misc_folder + "/" + bibtex,
    page_title=page_title,
    project_heading=project_heading,
    author_list=author_list,
    lab_url=lab_url,
    lab_name=lab_name,
    univ_name=univ_name,
    yt_link=yt_link,
    abstract=abstract,
    project_description=project_description,
    paper_pdf_url=paper_pdf_url
)

save_to = root_folder + "/" + save_as

with open(save_to, "w") as fh:
    fh.write(outputText)
