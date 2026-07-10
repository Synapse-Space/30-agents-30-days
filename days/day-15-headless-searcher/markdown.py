class MarkdownBuilder:

    def build(
        self,
        page_data,
    ):

        markdown = f"""# {page_data['title']}

Source

{page_data['url']}

---

{page_data['body']}
"""

        return markdown