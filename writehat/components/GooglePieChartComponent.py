from .base import *

class PieChartComponentForm(ComponentForm):

    field_order = [
                'name',
                'pageBreakBefore',
                'showTitle'
    ]


class Component(BaseComponent):

    default_name = 'Google PieChart Component'
    formClass = PieChartComponentForm

    # make sure to specify the HTML template
    htmlTemplate = 'componentTemplates/GooglePieChartComponent.html'

    # Font Awesome icon type + color (HTML/CSS)
    # This is just eye candy in the web app
    iconType = 'fas fa-stream'
    iconColor = 'var(--blue)'

    # the "preprocess" function is executed when the report is rendered
    # use this to perform any last-minute operations on its data
    def preprocess(self, context):

        # for example, to uppercase the entire "summary" field:
        #   context['summary'] = context['summary'].upper()
        return context
