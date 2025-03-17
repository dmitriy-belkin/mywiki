# This extension adds a custom admonition for examples in text

from docutils import nodes
from docutils.parsers.rst import Directive, directives

class ExampleAdmonition(Directive):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        'title': directives.unchanged,
    }
    has_content = True

    def run(self):
        admonition_node = nodes.admonition()

        title_text = self.options.get('title')
        if not title_text and self.arguments:
            title_text = self.arguments[0]
        if not title_text:
            title_text = "Пример"

        title_node = nodes.title(title_text, title_text)
        admonition_node += title_node

        self.state.nested_parse(self.content, self.content_offset, admonition_node)
        return [admonition_node]