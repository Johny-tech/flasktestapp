#packages for need
from flask_restful import Api

# project resources
from api.testapp import QuestionApi , TestApi


def create_routes(api: Api):
    """Adds resources to the api.
    :param api: Flask-RESTful Api Object
    :Example:
        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")
    """
    # api.add_resource(HelloWorld, '/')
    api.add_resource(QuestionApi, '/question/')

    api.add_resource(TestApi,'/test/')
    # Test crud functionality
    # api.add_resource(TestCreateApi, '/testCreate')
    # api.add_resource(TestDeleteApi, '/testDelete/')
    # api.add_resource(TestUpdateApi, '/TestUpdate/<test_id>')
    # api.add_resource(TestListApi, '/testlist')
    #pagination of tests
    # api.add_resource(TestPaginationApi, '/Test/prvpage/<prvpage_id>/nxtpage/<nxt_page>')
    #question CRUD functionality
    # api.add_resource(QuestionAddApi, '/Test/<test_id>/QuestionAdd/')
    # api.add_resource(QuestionDeleteApi, '/Test/<test_id>/QuestionDelete/')
    # api.add_resource(QuestionUpdateApi, '/Test/<test_id>/QuestionUpdate/<question_id>')
    # api.add_resource(QuestionUpdateApi, '/Test/<test_id>/QuestionUpdate/<question_id>')
    # Option Crud functionality 
    # api.add_resource(P=)


