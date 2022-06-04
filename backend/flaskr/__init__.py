import os
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app, resources={r"/api/*": {"origins": "*"}})

   
    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
 # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add( "Access-Control-Allow-Headers", "Content-Type,Authorization,true")
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response
    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """

    @app.route("/categories")
    def retrieve_categories():

        # Query to fetch categories ordering by id
        categories = Category.query.order_by(Category.id).all()

        # Format tha data so it can be sent using jsonify
        all_categories = [category.format() for category in categories]


        return jsonify(
            {
                "success": True,
                "categories": all_categories,
                "total_categories": len(Category.query.all())
            }
        )

    @app.route("/questions")
    def retrieve_questions():

        # Query to fetch all questions ordering by id
        selection = Question.query.order_by(Question.id).all()

        # Query to fetch categories ordering by id
        categories = Category.query.order_by(Category.id).all()

        # Pass request and questions data as arguements for pagination and formating
        current_questions = paginate_questions(request, selection)

        # If there are no questions fetch, abort the operation
        if len(current_questions) == 0:
            abort(404)

        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
                "categories":  [category.format() for category in categories],
                "currentCategory": 'History'
            }
        )

    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):

        try:
            # Get the question to delete by the question unique id
            question = Question.query.filter(Question.id == question_id).one_or_none()

            # If no question is found abort the operation
            if question is None:
                abort(404)

            question.delete()

            selection = Question.query.order_by(Question.id).all()
            categories = Category.query.order_by(Category.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify(
               {
                "success": True,
                "questions": current_questions,
                "deleted": question_id,
                "total_questions": len(Question.query.all()),
                "categories":  [category.format() for category in categories],
                "currentCategory": 'History'
            }
            )

        except:
            abort(422)


    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route("/questions", methods=["POST"])
    def create_question():
        
        # Get data from the received request
        body = request.get_json()

        # Get each data from the body object
        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_difficulty = body.get("difficulty", None)
        new_category = body.get("category", None)

        try:
            # Create a new question data to be inserted to the DB
            question = Question(
                question = new_question, 
                answer = new_answer, 
                difficulty = new_difficulty,
                category = new_category
                )
            question.insert()

            selection = Question.query.order_by(Question.id).all()
            categories = Category.query.order_by(Category.id).all()

            # Pass request and questions data as arguements for pagination and formating
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                "success": True,
                "questions": current_questions,
                "created": True,
                "total_questions": len(Question.query.all()),
                "categories":  [category.format() for category in categories],
                "currentCategory": 'History'
            }
            )

        except Exception as e:
            print(e)
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route("/questions/search", methods=["POST"])
    def search_questions():
        body = request.get_json()

        # Get the text to search for from the body object
        searchTerm = body.get("searchTerm", None)

        try:

            # uSing the SQL LIKE keyword, fetch all questions that has that search term
            selection = Question.query.filter(Question.question.ilike(f'%{searchTerm}%')).all()
        
            # Pass request and questions data as arguements for pagination and formating
            current_questions = paginate_questions(request, selection)

            return jsonify(
                {
                "success": True,
                "questions": current_questions,
                "total_questions": len(current_questions),
                "currentCategory": 'History'
            }
            )

        except Exception as e:
            print(e)
            abort(422)
    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route("/categories/<string:category_id>/questions")
    def retrieve_questions_category(category_id):

        # Get the category data by the category id
        category = Category.query.filter_by(id = category_id).one_or_none()

        # If no category is found abort the operation
        if category is None:
            abort(422)

        # Fetch all questions by the category id, ordering all records by question id
        selection = Question.query.filter(Question.category == category_id).order_by(Question.id).all()

        # Pass request and questions data as arguements for pagination and formating
        current_questions = paginate_questions(request, selection)


        return jsonify(
            {
                "success": True,
                "questions": current_questions,
                "total_questions": len(Question.query.all()),
                "currentCategory": category.type
            }
        )

    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route("/quizzes", methods=["POST"])
    def get_question():
        body = request.get_json()

        # Get received data from the body object
        previous_questions = body.get("previous_questions", None)
        quiz_category = body.get("quiz_category", None)

        if "previous_questions" in body:
            pass
        else:
            abort(400)

        if "quiz_category" in body:
            pass
        else:
            abort(400)

        # Check if the all text was clicked to fetch all questions
        if quiz_category['type'] == 'click':
            questions = Question.query.order_by('id').all()
            category = Category.query.filter_by(id = '1').first()
        else:
            # Fetch all questions by the category id
            questions = Question.query.filter(Question.category == quiz_category['type']).all()
            category = Category.query.filter_by(id = quiz_category['type']).first()

        # if the list is empty abort the operation
        if questions == []:
            abort(404)

        try:

            filter_questions = []

            # If the previous_question list is empty, no need to filter the questions from the previous questions
            if len(previous_questions) == 0:
                filter_questions = questions

            # If the prevoius_question list is not empty loop through the questions data to remove each of them
            for p in previous_questions:
                filter_questions = filter(lambda a: a.id != p, questions)
                questions = list(filter_questions)
                

            # # Format tha rest of the question data so it can be sent using jsonify
            selection = [question.format() for question in questions]

            # If the question data is not empty, randomly select one question from the list
            if len(selection) != 0: 
                random_selection = random.randrange(len(selection))
                selection = selection[random_selection]
            else:
                selection = []

            return jsonify(
                {
                "success": True,
                "question": selection,
                "currentCategory": category.type
            }
            )

        except Exception as e:
            print(e)
            abort(422)
    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )


    @app.errorhandler(500)
    def server_error(error):
        return (
            jsonify({"success": False, "error": 500, "message": "Internal server error"}),
            500,
        )

        
    return app

