"""
downloader.py
~~~~~~~~~~~~~
download all your acceptted submissions in leetcode.
"""
import requests
import re
import os
import json
from html import unescape

url_template = 'https://leetcode.com/api/submissions/?offset={offset}&limit=20&lastkey={last_key}'

base_url = 'https://leetcode.com'

"""
PLEASE MODIFY THE HEADERS BELOW! COPY THE HEADERS FROM YOUR BROWSER WHEN YOU VISIT  https://leetcode.com/submissions/#/1
LOGIN FIRST AND THEN USE CHROME'S DEV TOOLS TO GET THE HEADERS.
"""
headers = {
    'cookie': '__cfduid=ddasdfasdfasdfasdf22209685; _ga=GA1.2.1721029897.1522209687; _gid=GA1.2.2122659710.1522209687; csrftoken=5VGxia5Jpn8s2sPNasdfasdfasdfRMOThVHsDA41U176qb8ry2auaRDMDNKS; LEETCODE_SESSION=eyJasdfasdfasdfdXNlcl9zbHVnIjoia2luZ25hbWUiLCJfYXV0aF91c2VyX2lkIjoiODMxMTciLCJSRU1PVEVfQUasdfasdfasdfCI6IjIwMTgtMDMtMjgwiX2F1dGhfdXNlcl9iYWNrZW5kIjasdfasdfasdfaGVudGljYXRpb25CYWNrZW5kIiwiaWQiOjgzMTE3LCJhdmF0YXasdffgasdfasdfasdfy5ncmF2YXRhci5jb20asdfasdfasdfjQ0NWNkYTNmYTEwN2U0ZDI1Mjk0MzNhLnBuZz9zPTIwMCIsIl9zZXNzaW9uX2V4cGlyeSI6MCwiX2F1dGhfdXNlcl9oYXNoIjoiNzUwNTI4ZWM0Mjk2YTAyMWEzNDA0YTg5OGQwMmI0NGYwOWJlZDRmNCIsImVtYWlsIjoiZ3JlZW5asdfasfasdf; __atuvc=8%7C13; __atuvs=5abb3f2a9ffd0ce1003; _gat=1',
    'referer': 'https://leetcode.com/submissions/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}


def fetch_submission_list_json(offset, last_key):
    url = url_template.format(offset=offset, last_key=last_key)
    content = requests.get(url, headers=headers).json()
    return content


def generate_filepath(file_name):
    print(file_name)
    file_path = file_name + '.py'
    index = 1
    while True:
        if not os.path.exists(file_path):
            break
        file_path = '{}_{}.py'.format(file_name, index)
        index += 1
    return file_path


def write_code(file_path, url, problem_description, code):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write(url)
        f.write('\n\n')
        f.write(problem_description)
        f.write('"""')
        f.write('\n\n\n')
        f.write(code)


def extract_code_info(html):
    problem_description = re.search('name="description" content="(.*?)" />', html, re.S)
    if problem_description:
        problem_description = unescape(problem_description.group(1))
    code = re.search(r'submissionCode\:\ \'([^\']+)\'', html, re.S).group(1)
    code = json.loads('{"code": "%s"}' % code)
    format_code = code['code']
    file_name = re.search('/problems/(.*?)/', html).group(1)
    code_info = {'problem_description': problem_description,
                 'format_code': format_code,
                 'file_name': file_name}
    return code_info


def fetch_submission(row):
    url = base_url + row['url']
    html = requests.get(url, headers=headers).content.decode()
    code_info = extract_code_info(html)
    file_path = generate_filepath(code_info['file_name'])
    write_code(file_path,
               url,
               code_info['problem_description'],
               code_info['format_code'])


def get_submission_list():
    offset = 0
    last_key = ''
    while True:
        print(offset)
        submission_info = fetch_submission_list_json(offset, last_key)
        has_next = submission_info['has_next']
        if not has_next:
            break
        submission_list = submission_info['submissions_dump']
        for submission in submission_list:
            if submission['status_display'] == 'Accepted':
                fetch_submission(submission)
        last_key = submission_info['last_key']
        offset += 20


if __name__ == '__main__':
    get_submission_list()
