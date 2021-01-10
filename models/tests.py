from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         ListField,
                         FloatField,
                         EmbeddedDocumentListField,
                         IntField,
                         DateTimeField,
                         StringField,
                         EmailField,
                         BooleanField,
                         ListField,
                         ReferenceField)
import datetime
from mongoengine.errors import ValidationError

class Answer(EmbeddedDocument):
    author = StringField(required=True)
    comment = StringField()
    finished_at = DateTimeField(required=False, default=datetime.datetime.now(),editable=False)

class Option(EmbeddedDocument):
    char = StringField(required=True)
    text = StringField(required=True)
    isright = BooleanField(required=False , default=False)
    chosenby = EmbeddedDocumentListField(Answer)

class Question(EmbeddedDocument):
	options = EmbeddedDocumentListField(Option)
	duration = IntField(required=True , min_value=0 , max_value=123)



class Test(Document):
    author = StringField(required=True)
    questions = EmbeddedDocumentListField(Question,required=True)

	#start date and duration time
    start_date = DateTimeField(required=False, default=datetime.datetime.now(),editable=True)
    duration = IntField(required=True , min_value=0 , max_value=1223)
    created_date = DateTimeField(required=False,default=datetime.datetime.now() , editable=False)
    # complexity indicators
    complexity = IntField(required=False,default=5,editable=True)
    outof = IntField(required=False,default=3,editable=True)
	# out of smth
    assignedforcategory= IntField(required=False)
    assignedforperson = ListField(IntField(required=False))
    assignedgroup = StringField(required=False)
    assignedgrade = StringField(required=False)

    def clean(self):
        """
        Ensures that only published essays have a `pub_date` and
        automatically sets the pub_date if published and not set.
        """
        if self.complexity > self.outof:
            from flask import jsonify

            msg = 'complexity should not exceed the limit'
            
            raise ValidationError(msg)
