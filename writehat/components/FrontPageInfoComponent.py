from .base import *
from django import forms


class FrontPageInfoComponentForm(ComponentForm):

    field_order = [
        'unit',
        'document_type',
        'document_id',
        'distribution',
        'version',
        'date',
        'pageBreakBefore',
        'showTitle'
    ]

    # Customer Information
    unit          = forms.CharField(label='Unit',          required=False)
    document_type = forms.CharField(label='Document Type', required=False)
    document_id   = forms.CharField(label='Document ID',   required=False)
    distribution  = forms.CharField(label='Distribution',  required=False)
    version       = forms.CharField(label='Version',       required=False)
    date          = forms.CharField(label='Date',          required=False)

class Component(BaseComponent):

    default_name = 'Front Page Informations'
    htmlTemplate = 'componentTemplates/FrontPageInfoComponent.html'
    fieldList = {
        'unit'         : StringField(templatable=False),
        'document_type': StringField(templatable=False),
        'document_id'  : StringField(templatable=False),
        'distribution' : StringField(templatable=False),
        'version'      : StringField(templatable=False),
        'date'         : StringField(templatable=False),
    }
    formClass = FrontPageInfoComponentForm
    iconType = 'fas fa-id-card-alt'
    iconColor = 'var(--cyan)'
