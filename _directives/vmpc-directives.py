from docutils import nodes
from docutils.parsers.rst.directives.images import Image 

class VmpcLcdScreenshotDirective(Image):
    def run(self):
        node = super().run()[0]
        node['classes'] = ['vmpc-lcd-screenshot', 'align-center']
        return [node]

def setup(app):
    app.add_directive('vmpc-lcd-screenshot', VmpcLcdScreenshotDirective)

