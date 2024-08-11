from pydantic import BaseModel
from typing import List, Optional


class Alternative(BaseModel):
    id: Optional[int] = None
    statement: str
    isCorrect: bool = False
    question_id: Optional[int] = None

class AlternativeForUpdate(BaseModel):
    statement: Optional[str] = None
    question_id: Optional[int] = None
    
class Question(BaseModel):
    id: Optional[int] = None
    statement: str
    quiz_id: Optional[int] = None
    alternatives: Optional[List[Alternative]] = []

class QuestionForUpdate(BaseModel): 
    statement: Optional[str] = None
    quiz_id: Optional[int] = None
    
class QuestionSimple(BaseModel):
    id: Optional[int] = None
    statement: str
    quiz_id: Optional[int] = None
    

class Quiz(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    category: str
    isDone: bool = False
    user_id: Optional[int] = None
    questions: Optional[List[QuestionSimple]] = []

class QuizForUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    user_id: Optional[int] = None
    
class QuizSimple(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    category: str
    isDone: bool = False
    user_id: Optional[int] = None
    
    
    
class User(BaseModel):
    id: Optional[int] = None
    email: str
    password: str
    quizzes: Optional[List[QuizSimple]] = []
    
class UserForUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    

   