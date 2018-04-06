import wikipediaapi as wiki
wiki_wiki = wiki.Wikipedia('zh',extract_format=wiki.ExtractFormat.WIKI)
page_py = wiki_wiki.page('香港學生自殺事件列表')

page_py.exists()
page_py.title
page_py.summary
page_py.text
page_py.sections

def print_sections(sections, level=0):
        for s in sections:
                print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text))
                print_sections(s.sections, level + 1)


print_sections(page_py.sections)
