from .base import *

class PieChartComponentForm(ComponentForm):

    critical = forms.CharField(label='Critical', required=True)
    high     = forms.CharField(label='High',     required=True)
    medium   = forms.CharField(label='Medium',   required=True)
    low      = forms.CharField(label='Low',      required=True)

    field_order = [
                'name',
                'critical',
                'high',
                'medium',
                'low',
                'pageBreakBefore',
                'showTitle'
    ]


class Component(BaseComponent):

    default_name = 'PieChart Component'
    formClass = PieChartComponentForm

    # the "templatable" attribute decides whether or not that field
    # gets saved if the report is ever converted into a template
    fieldList = {
        'critical': StringField(markdown=False, templatable=False),
        'high'    : StringField(markdown=False, templatable=False),
        'medium'  : StringField(markdown=False, templatable=False),
        'low'     : StringField(markdown=False, templatable=False),
    }

    # make sure to specify the HTML template
    htmlTemplate = 'componentTemplates/PieChartComponent.html'

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
