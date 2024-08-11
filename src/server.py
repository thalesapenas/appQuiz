from fastapi import FastAPI, Depends, status, APIRouter
from src.schemas import schema
from typing import List
from src.infra.sqlalchemy.repositories import repository 
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db,create_database
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(middleware=middleware)
create_database()

# Roteadores para cada seção da API
alternatives_router = APIRouter(prefix="/alternatives", tags=["Alternatives"])
questions_router = APIRouter(prefix="/questions", tags=["Questions"])
quizzes_router = APIRouter(prefix="/quizzes", tags=["Quizzes"])
users_router = APIRouter(prefix="/users", tags=["Users"])
options_router = APIRouter(prefix="/options", tags=["Options"])

#ALTERNATIVES
@alternatives_router.post("", status_code=status.HTTP_201_CREATED)
def create_alternative(alternative: schema.Alternative, db: Session = Depends(get_db)):
    created_alternative = repository.Alternative(db).create(alternative)
    return created_alternative

@alternatives_router.get("", status_code=status.HTTP_200_OK)
def get_alternative(alternative_id: int, db: Session = Depends(get_db)):
    alternative_finded = repository.Alternative(db).get(alternative_id)
    return alternative_finded

@alternatives_router.get("/{alternative_id}")
def get_all_alternatives( db: Session = Depends(get_db)):
    alternatives_finded = repository.Alternative(db).get_all()
    return alternatives_finded

@alternatives_router.put("/{alternative_id}")
def update_alternative(alternative: schema.AlternativeForUpdate,alternative_id: int, db: Session = Depends(get_db)):
    updated_alternative = repository.Alternative(db).update(alternative_id,alternative)
    return updated_alternative

@alternatives_router.put("/isCorrect/{alternative_id}")
def update_alternative_isCorrect(alternative_id: int, db: Session = Depends(get_db)):
    updated_alternative = repository.Alternative(db).toggle_is_correct(alternative_id)
    return updated_alternative

@alternatives_router.delete("/{alternative_id}")
def delete_alternative(alternative_id: int, db: Session = Depends(get_db)):
    deleted_alternative = repository.Alternative(db).remove(alternative_id)
    return deleted_alternative


#Question
@questions_router.post("", status_code=status.HTTP_201_CREATED)
def create_question(question: schema.Question, db: Session = Depends(get_db)):
    created_question = repository.Question(db).create(question)
    return created_question

@questions_router.get("")
def get_all_questions(db: Session = Depends(get_db)):
    questions_finded = repository.Question(db).get_all()
    return questions_finded

@questions_router.get("/{question_id}")
def get_question(question_id: int, db: Session = Depends(get_db)):
    questions_finded = repository.Question(db).get_all()
    return questions_finded

@questions_router.put("/{question_id}")
def get_question(question: schema.QuestionForUpdate, question_id: int, db: Session = Depends(get_db)):
    questions_finded = repository.Question(db).get_all()
    return questions_finded

@questions_router.delete("/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    deleted_question = repository.Question(db).remove(question_id)
    return deleted_question


#Quiz
@quizzes_router.post("", status_code=status.HTTP_201_CREATED)
def create_quiz(quiz: schema.Quiz, db: Session = Depends(get_db)):
    created_quiz = repository.Quiz(db).create(quiz)
    return created_quiz

@quizzes_router.get("")
def get_all_quizzes(db: Session = Depends(get_db)):
    quizzes_finded = repository.Quiz(db).get_all()
    return quizzes_finded

@quizzes_router.get("/{quiz_id}")
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    quiz_finded = repository.Quiz(db).get(quiz_id)
    return quiz_finded

@quizzes_router.put("/{quiz_id}")
def update_quiz(quiz: schema.QuizForUpdate, quiz_id: int, db: Session = Depends(get_db)):
    updated_quiz = repository.Quiz(db).update(quiz_id,quiz)
    return updated_quiz

@quizzes_router.put("/isDone/{quiz_id}")
def update_quiz_isDone(quiz_id: int, db: Session = Depends(get_db)):
    updated_quiz = repository.Quiz(db).toggle_is_done(quiz_id)
    return updated_quiz

@quizzes_router.delete("/{quiz_id}")
def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    deleted_quiz = repository.Quiz(db).remove(quiz_id)
    return deleted_quiz


#User
@users_router.post("", status_code=status.HTTP_201_CREATED)
def create_User(user: schema.User, db: Session = Depends(get_db)):
    created_user = repository.User(db).create(user)
    return created_user

@users_router.get("")
def get_all_users(db: Session = Depends(get_db)):
    users_finded = repository.User(db).get_all()
    return users_finded

@users_router.get("/{user_id}") 
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_finded = repository.User(db).get(user_id)
    return user_finded

@users_router.put("/{user_id}")
def update_user(user: schema.UserForUpdate, user_id: int, db: Session = Depends(get_db)):
    updated_user = repository.User(db).update(user_id,user)
    return updated_user

@users_router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = repository.User(db).remove(user_id)
    return deleted_user


#options
@options_router.post("/add/alternative_to_question", status_code=status.HTTP_201_CREATED)
def add_alternative_to_question(alternative:schema.Alternative, question:schema.Question, db: Session = Depends(get_db)):
    result = repository.Option(db).add_alternative_to_question(alternative, question)
    return result




app.include_router(alternatives_router)
app.include_router(questions_router)
app.include_router(quizzes_router)
app.include_router(users_router)
app.include_router(options_router)