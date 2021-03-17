from .base import *

class PieChartComponentForm(ComponentForm):

    height           = forms.CharField(label='Height', required=True)
    width            = forms.CharField(label='Width', required=True)
    legend_position  = forms.CharField(label='Legend position', required=True)

    field_order = [
                'name',
                'width',
                'height',
                'legend_position',
                'pageBreakBefore',
                'showTitle'
    ]


class Component(BaseComponent):

    default_name = 'Google PieChart Component'
    formClass = PieChartComponentForm

    # make sure to specify the HTML template
    htmlTemplate = 'componentTemplates/GooglePieChartComponent.html'

    fieldList = {
        'width'          : StringField(templatable=False, default="500"),
        'height'         : StringField(templatable=False, default="500"),
        'legend_position': StringField(templatable=False, default="right")
    }

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
