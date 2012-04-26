###############################################################################
#  Copyright 2011,2012 GISA Elkartea.                                         #
#                                                                             #
#  This file is part of django-ws.                                            #
#                                                                             #
#  django-ws is free software: you can redistribute it and/or modify it       #
#  under the terms of the GNU Affero General Public License as published      #
#  by the Free Software Foundation, either version 3 of the License, or       #
#  (at your option) any later version.                                        #
#                                                                             #
#  django-ws is distributed in the hope that it will be useful, but WITHOUT   #
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or      #
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public       #
#  License for more details.                                                  #
#                                                                             #
#  You should have received a copy of the GNU Affero General Public License   #
#  along with django-ws. If not, see <http://www.gnu.org/licenses/>.          #
###############################################################################

from django import forms
from django.core import validators


class BPMTaskForm(forms.Form):
    def get_fields(self, params={}):
        fields = []
        for key, field in self.fields.items():
            if not key in params:
                fields.append(field.to_ext_dict(key))
        return fields


class Field(forms.Field):
    def to_ext_dict(self, fieldname):
        ext_dict = {
            'name': fieldname,
            'xtype': 'textfield',  # Default field type
        }
        ext_dict['fieldLabel'] = self.label or fieldname

        if self.initial:
            ext_dict['value'] = self.initial

        self.field_extras(ext_dict)
        return ext_dict

    def field_extras(self, ext_dict):
        raise NotImplementedError


class IntegerField(Field, forms.IntegerField):
    def field_extras(self, ext_dict):
        ext_dict['xtype'] = 'numberfield'
        for validator in self.validators:
            if type(validator) == validators.MaxValueValidator:
                ext_dict['max_value'] = validator.limit_value
            elif type(validator) == validators.MinValueValidator:
                ext_dict['min_value'] = validator.limit_value


class CharField(Field, forms.CharField):
    def field_extras(self, ext_dict):
        if type(self.widget) == forms.Textarea:
            ext_dict['xtype'] = 'textarea'
        for validator in self.validators:
            if type(validator) == validators.MinLengthValidator:
                ext_dict['minLength'] = validator.limit_value
            elif type(validator) == validators.MaxLengthValidator:
                ext_dict['maxLength'] = validator.limit_value


class BooleanField(Field, forms.BooleanField):
    def field_extras(self, ext_dict):
        ext_dict['xtype'] = 'checkbox'
        if self.initial:
            ext_dict['checked'] = self.initial


class ChoiceField(Field, forms.ChoiceField):
    def field_extras(self, ext_dict):
        fieldname = ext_dict['name']
        ext_dict['xtype'] = 'fieldcontainer'
        ext_dict['name'] = 'fieldcontainer-' + fieldname
        ext_dict['defaultType'] = 'radiofield'
        ext_dict['items'] = []
        for item in self.choices:
            ext_dict['items'].append({
                'boxLabel': item[1],
                'name': fieldname,
                'inputValue': item[0],
            })


class ModelChoiceField(forms.ModelChoiceField, ChoiceField):
    pass