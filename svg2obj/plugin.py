# plugin.py
import re
from mkdocs.plugins import BasePlugin

class SvgToObjPlugin(BasePlugin):

    def on_page_markdown(self, markdown, **kwargs):
      
        pattern = re.compile(r"!\[(.*?)\]\((.*?)\.svg\)", flags=re.IGNORECASE)
        
        markdown = re.sub(pattern,
            r'<object type="image/svg+xml" data="../\2.svg" height="auto" width="100%">\n' + \
            r'<img src="../\2.svg" alt="\1" />' + \
            r'</object>\n' + \
            r'<p><center>\1</center></p>',                 
            markdown)     

        return markdown
