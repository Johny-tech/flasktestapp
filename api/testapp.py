# flask packages
from flask import Response, request, jsonify
from flask_restful import Resource
import json
# mongo-engine models
from models.tests import Answer , Test , Question , Option

# https://www.youtube.com/watch?v=188Fy-oCw4w

class QuestionApi(Resource):

	def post(self) -> Response:
		from mongoengine.errors import ValidationError
		data = request.get_json()

		test = Test.objects(id=data['id']).first()
		print(data['id'])
		print(test.author)
		for question in data['questions']:

				questionforSaving = Question()
				questionforSaving.author = question['author'] 
				questionforSaving.duration = int(question['duration'])
				test.questions.append(questionforSaving)
				if 'options' in question.keys():
					for option in question['options']:

						OptionForSaving = Option()
						OptionForSaving.char = option['char'] 
						OptionForSaving.text = option['text']

						if OptionForSaving.isright =="True" or OptionForSaving.isright =="False" or OptionForSaving.isright =="":
							OptionForSaving.isright = option['isrigth']
							
						questionforSaving.options.append(OptionForSaving)
					
		test.save()

		return jsonify({'result':'success'})

	def get(self):
		
		data = request.get_json()
		output = Test.objects(id=data['test_id'])
		print(data['test_id'])
		print(output)
		# filtering nested object is here 
		# https://stackoverflow.com/questions/11876518/how-to-perform-such-filter-queries-in-mongoengine-on-nested-dicts-or-arrays-cont




class TestApi(Resource):

	@staticmethod
	def validateTest(data):
				
		if data['questions']=="":
			msg =+{'questions Creating Error':'Questions must be given'}
		elif data['start_data']=="":
			msg =+{'questions Creating Error':'Questions must be given'}


	def get(self):
		output = Test.objects()
		return jsonify({'result':output})

	def post(self) -> Response:
		from mongoengine.errors import ValidationError
		data = request.get_json()


		try:
			test = Test()  

			#validation must be handled into anthother service
			if data.get('duration') in data:
				return jsonify({'result': 'Sorry but duration are required'})
			
			if data.get('author') in data:
				return jsonify({'result': 'Sorry but author  fields are required'})
			#___________________________________________________________________

			test.duration=data['duration']
			test.author=data['author']

			if "start_date" in data:
				test.start_date=data['start_date']

			if "complexity" in data:
				test.complexity=data['complexity']
		
			if "outof" in data:
				test.outof =data['outof']
		
			if "assignedforcategory" in data:
				test.assignedforcategory = data['assignedforcategory']
		
			if "assignedforperson" in data:
				test.assignedforperson=data['assignedforperson']
		
			if "assignedgroup" in data:
				test.assignedgroup = data['assignedgroup']
		
			if "assignedgrade" in data:
				test.assignedgrade = data['assignedgrade']
			
		
			for question in data['questions']:

				questionforSaving = Question()
				questionforSaving.author = question['author'] 
				questionforSaving.duration = int(question['duration'])
				test.questions.append(questionforSaving)
				if 'options' in question.keys():
					for option in question['options']:

						OptionForSaving = Option()
						OptionForSaving.char = option['char'] 
						OptionForSaving.text = option['text']

						if OptionForSaving.isright =="True" or OptionForSaving.isright =="False" or OptionForSaving.isright =="":
							OptionForSaving.isright = option['isrigth']
							
						questionforSaving.options.append(OptionForSaving)
					
			test.save()
		
			return jsonify({'result': 'created Successfuly'})

		except ValidationError as e:

			print(e.message)
			return jsonify({'result':'error has happened','detailed':e.message})


	def delete(self) -> Response:
		data = request.get_json()
		print(data)

		try:
	
			import bson
			
			output = Test.objects(id=data['id']).delete()
	
			return jsonify({'result': 'Object has been deleted','object':output})
	
		except ValidationError as e:
			
			return json.jsonify({'result': 'errror has happened' , 'detailed':e.message})
			




# new_user = User()
# user_settings = UserSettings()
# user_settings.default_cal = resp['calendar']
# new_user.settings = user_settings
# # more stuff
# new_user.save()