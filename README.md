
## Trivia App

The Trivia App is a python full stack app display questions and allows users to perform the following;

1. Display questions - both questions and thier category. Questions show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Completing this trivia app has given me an indepth experiance and the ability to structure plan, implement, and test an API - skills essential for enabling my future applications to communicate with others.


## About the Stack

The full stack application is designed with some key functional areas:

### Backend

From the backend folder run `pip install requirements.txt`. All required packages are included in the requirements file. 

To run the application run the following commands: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the [Flask documentation](http://flask.pocoo.org/docs/1.0/tutorial/factory/).

The application is run on `http://127.0.0.1:5000/` by default and is a proxy in the frontend configuration. 

#### Frontend

From the frontend folder, run the following commands to start the client: 
```
npm install // only once to install dependencies
npm start 
```

By default, the frontend will run on localhost:3000. 

### Tests
In order to run tests navigate to the backend folder and run the following commands: 

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command. 

All tests are kept in that file and should be maintained as updates are made to app functionality. 

## API Reference

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return three error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 200: Successful
- 405: Method Not Allowed



### Endpoints 
#### GET /questions
- General:
    - Returns a list of questions and categories, success value, and total number of questions
    - Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1. 
- Sample: `curl http://127.0.0.1:5000/questions`

``` 
{
    "categories": 
    [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "currentCategory": "History",
    "questions": 
    [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "John",
            "category": "1",
            "difficulty": 1,
            "id": 3,
            "question": "What is my name?"
        },
        {
            "answer": "Tom Cruise",
            "category": "5",
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": "5",
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "kolo",
            "category": "3",
            "difficulty": 1,
            "id": 7,
            "question": "What is my surname?"
        },
        {
            "answer": "Muhammad Ali",
            "category": "4",
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": "6",
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "6",
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
    ],
        "success": true,
        "total_questions": 21
    }
```

#### POST /questions
- General:
    - Creates a new question using the submitted question, difficulty and selected category. Returns the id of the created question, success value, current category, total questions, categories and questions list based on current page number to update the frontend. 
- `curl http://127.0.0.1:5000/questions?page=3 -X POST -H "Content-Type: application/json" -d '{'question': 'What is my surname?', 'answer': 'kolo', 'category': '3', 'difficulty': 1}'`
```
{
      "categories": 
    [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "currentCategory": "History",
    "questions": 
    [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "John",
            "category": "1",
            "difficulty": 1,
            "id": 3,
            "question": "What is my name?"
        },
        {
            "answer": "Tom Cruise",
            "category": "5",
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": "5",
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "kolo",
            "category": "3",
            "difficulty": 1,
            "id": 7,
            "question": "What is my surname?"
        },
        {
            "answer": "Muhammad Ali",
            "category": "4",
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": "6",
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "6",
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
  ],
  "created": 24,
  "success": true,
  "total_questions": 17
}
```
#### DELETE /questions/{question_id}
- General:
    - Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total questions, current category and questions list based on current page number to update the frontend. 
- `curl -X DELETE http://127.0.0.1:5000/questions/16?page=2`
```
{
    "categories": 
    [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "currentCategory": "History",
    "questions": 
    [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
            "answer": "John",
            "category": "1",
            "difficulty": 1,
            "id": 3,
            "question": "What is my name?"
        },
        {
            "answer": "Tom Cruise",
            "category": "5",
            "difficulty": 4,
            "id": 4,
            "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
            "answer": "Maya Angelou",
            "category": "4",
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": "5",
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
            "answer": "kolo",
            "category": "3",
            "difficulty": 1,
            "id": 7,
            "question": "What is my surname?"
        },
        {
            "answer": "Muhammad Ali",
            "category": "4",
            "difficulty": 1,
            "id": 9,
            "question": "What boxer's original name is Cassius Clay?"
        },
        {
            "answer": "Brazil",
            "category": "6",
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": "6",
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
            "answer": "George Washington Carver",
            "category": "4",
            "difficulty": 2,
            "id": 12,
            "question": "Who invented Peanut Butter?"
        }
    ],
    "deleted": 16,
    "success": true,
    "total_questions": 15
}
```


#### POST /questions/search
- General:
    - A post request that Search by any phrase to get questions based on a search term, it return any questions for whom the search term is a substring of the question. Returns success value, total questions, current category and questions list to update the frontend
- `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{'searchTerm': 'Tom Hanks'}'`

```
{
    "currentCategory": 'Science',
    "questions": 
    [
        {
            "answer": "Apollo 13",
            "category": "5",
            "difficulty": 4,
            "id": 2,
            "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        
    ],
        "success": true,
        "total_questions": 1
    }
```



#### GET /categories/3/questions
- General:
    - A get request that get questions based on a specified category, it return any questions for whom the category id is of the question. Returns success value, total questions, current category and questions list to update the frontend
- `curl http://127.0.0.1:5000/categories/3/questions`

```
{
    "currentCategory": "History",
    "questions": 
    [
        {
            "answer": "kolo",
            "category": "3",
            "difficulty": 1,
            "id": 7,
            "question": "What is my surname?"
        },
        {
            "answer": "Lake Victoria",
            "category": "3",
            "difficulty": 2,
            "id": 13,
            "question": "What is the largest lake in Africa?"
        },
        {
            "answer": "The Palace of Versailles",
            "category": "3",
            "difficulty": 3,
            "id": 14,
            "question": "In which royal palace would you find the Hall of Mirrors?"
        },
        {
            "answer": "Agra",
            "category": "3",
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        }
    ],
    "success": true,
    "total_questions": 4
}
```



#### GET /categories
- General:
    - Returns a list of categories, success value, and total number of categories. Returns success value, total categories, and categories list to update the frontend
- Sample: `curl http://127.0.0.1:5000/categories`

```
{
    "categories": 
    [
        {
            "id": 1,
            "type": "Science"
        },
        {
            "id": 2,
            "type": "Art"
        },
        {
            "id": 3,
            "type": "Geography"
        },
        {
            "id": 4,
            "type": "History"
        },
        {
            "id": 5,
            "type": "Entertainment"
        },
        {
            "id": 6,
            "type": "Sports"
        }
    ],
    "success": true,
    "total_categories": 6
}

```



#### POST /quizzes
- General:
    - A post request that to get questions to play the quiz. This endpoint should takes a category id and previous question parameters in a list and return a random questions within the given category, if provided, and that is not one of the previous questions. Returns a success value, current category and a single question
- `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{'previous_questions': [1, 2], 'quiz_category': {'type': '3'}}'`

```
{
    "currentCategory": 'History',
    "questions": 
    [
        {
            "answer": "kolo",
            "category": "3",
            "difficulty": 1,
            "id": 7,
            "question": "What is my surname?"
        },
        
    ],
    "success": true
}

```
## Deployment N/A

## Authors
Yours truly, John Kolo 

## Acknowledgements 
Stackoverflow! 