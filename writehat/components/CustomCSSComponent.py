from .base import *

class CustomCSSComponentForm(ComponentForm):

    css_code = forms.CharField(label='CSS Code', required=False, widget=forms.Textarea, max_length=50000)

    field_order = [
                'name',
                'css_code',
                'pageBreakBefore',
                'showTitle'
    ]


class Component(BaseComponent):

    default_name = 'Custom CSS Component'
    formClass = CustomCSSComponentForm

    # make sure to specify the HTML template
    htmlTemplate = 'componentTemplates/CustomCSSComponent.html'

    fieldList = {
        'css_code': StringField(templatable=True, markdown=True),
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
