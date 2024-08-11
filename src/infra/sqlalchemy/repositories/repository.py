from sqlalchemy.orm import Session
from src.schemas import schema
from src.infra.sqlalchemy.models import models


class Alternative():
    
    def __init__(self,db: Session):
        self.db = db
    
    def create(self, alternative: schema.Alternative):
        try:
            db_alternative = models.Alternative(id = alternative.id,
                                                statement= alternative.statement, 
                                                isCorrect=alternative.isCorrect,
                                                question_id=alternative.question_id)
            self.db.add(db_alternative)
            self.db.commit()
            self.db.refresh(db_alternative)
            return db_alternative
        except Exception as e:
            return e
    
    def get_all(self):
        try:
            alternatives = self.db.query(models.Alternative).all()
            return alternatives
        except Exception as e:
            return e
    
    def get(self, alternative_id: int):
        try:
            alternative = self.db.query(models.Alternative).filter(models.Alternative.id == alternative_id).first()
            return alternative
        except Exception as e:
            return e
    
    def remove(self, alternative_id: int):
        try:
            alternative = self.db.query(models.Alternative).filter(models.Alternative.id == alternative_id).first()
            self.db.delete(alternative)
            self.db.commit()
            return alternative
        except Exception as e:
            return e
        
    def update(self,alternative_id: int, alternative_update: schema.AlternativeForUpdate):
        try:
            alternative= self.db.query(models.Alternative).filter(models.Alternative.id == alternative_id).first()
            if alternative_update.statement != None:
                alternative.statement = alternative_update.statement
            if alternative_update.question_id != None:
                alternative.question_id = alternative_update.question_id
                
            self.db.commit()
            self.db.refresh(alternative)
            return alternative
        except Exception as e:
            return e
        
    def toggle_is_correct(self,alternative_id: int):
        try:
            alternative= self.db.query(models.Alternative).filter(models.Alternative.id == alternative_id).first()
            
            if alternative.isCorrect == True:
                alternative.isCorrect = False
            else:
                alternative.isCorrect = True
                others_alternatives = self.db.query(models.Alternative).filter(models.Alternative.question_id == alternative.question_id).all()
                for x in others_alternatives:
                    if x.id != alternative_id:
                        x.isCorrect = False

            self.db.commit()
            self.db.refresh(alternative)
            return alternative
        except Exception as e:
            return e
    
    
class Question():
    
    def __init__(self,db: Session):
        self.db = db
    
    def create(self, question: schema.Question):
        try:
            db_question = models.Question(  id = question.id,
                                            statement= question.statement,
                                            quiz_id= question.quiz_id)
                                            
            self.db.add(db_question)
            self.db.commit()
            self.db.refresh(db_question)
            return db_question
        except Exception as e:
            return e
    
    def get_all(self):
        questions = self.db.query(models.Alternative).all()
        return questions
    
    def get(self, question_id: int):
        try:
            question = self.db.query(models.Question).filter(models.Question.id == question_id).first()
            return question
        except Exception as e:
            return e
    
    def remove(self, quesiton_id: int):
        try:
            question = self.db.query(models.Question).filter(models.Question.id == quesiton_id).first()
            self.db.delete(question)
            self.db.commit()
            return question
        
        except Exception as e:
            return e
        
    def update(self,question_id: int, question_update: schema.QuestionForUpdate):
        try:
            question= self.db.query(models.Question).filter(models.Question.id == question_id).first()
            if question_update.statement != None:
                question.statement = question_update.statement
            if question_update.quiz_id != None:
                question.quiz_id = question_update.quiz_id
                
            self.db.commit()
            self.db.refresh(question)
            return question
        
        except Exception as e:
            return e
        
    
class Quiz():
    
    def __init__(self,db: Session):
        self.db = db
    
    def create(self, quiz: schema.Quiz):
        try:
            db_quiz = models.Quiz( id = quiz.id,
                                    title= quiz.title,
                                    description= quiz.description,
                                    category= quiz.category,
                                    isDone= quiz.isDone,
                                    user_id= quiz.user_id)
            
                                            
            self.db.add(db_quiz)
            self.db.commit()
            self.db.refresh(db_quiz)
            return db_quiz
        except Exception as e:
            return e
        
    def get_all(self):
        quizzes = self.db.query(models.Quiz).all()
        return quizzes
    
    def get(self, quiz_id: int):
        try:
            quiz = self.db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
            return quiz
        except Exception as e:
            return e
    
    def remove(self, quiz_id: int):
        try:
            quiz = self.db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
            self.db.delete(quiz)
            self.db.commit()
            return quiz
        
        except Exception as e:
            return e
        
    def update(self,quiz_id: int, quiz_update: schema.QuizForUpdate):
        try:
            quiz= self.db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
            if quiz_update.title != None:
                quiz.title = quiz_update.title
            if quiz_update.description != None:
                quiz.description = quiz_update.description
            if quiz_update.category != None:
                quiz.category = quiz_update.category
            if quiz_update.user_id != None:
                quiz.user_id = quiz_update.user_id
            
                
            self.db.commit()
            self.db.refresh(quiz)
            return quiz
        
        except Exception as e:
            return e
    
    def toggle_is_done(self,quiz_id: int):
        try:
            quiz= self.db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
            
            if quiz.isDone == True:
                quiz.isDone = False
            else:
                quiz.isDone = True

            self.db.commit()
            self.db.refresh(quiz)
            return quiz
        except Exception as e:
            return e
        

class User():
    
    def __init__(self,db: Session):
        self.db = db
    
    def create(self, user: schema.User):
        if self.db.query(models.User).filter(models.User.email == user.email).first():
            return "User already exists"        
        try:
            db_user = models.User(  id = user.id,
                                    email= user.email,
                                    password= user.password)
        
                                            
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        except Exception as e:
            return e
    
    def get_all(self):
        users = self.db.query(models.User).all()
        return users
    
    def get(self, user_id: int):
        try:
            user = self.db.query(models.User).filter(models.User.id == user_id).first()
            return user
        except Exception as e:
            return e
    
    def remove(self, user_id: int):
        try:
            user = self.db.query(models.User).filter(models.User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return user
        
        except Exception as e:
            return e
        
    def update(self,user_id: int, user_update: schema.UserForUpdate):
        try:
            user= self.db.query(models.User).filter(models.User.id == user_id).first()
            if user_update.email != None:
                user.email = user_update.email
                
            if user_update.password != None:
                user.password = user_update.password

            self.db.commit()
            self.db.refresh(user)
            return user
        
        except Exception as e:
            return e
        
        
class Options():
    
    def __init__(self,db: Session):
        self.db = db
    
    def add_alternative_to_question(self, alternative:schema.Alternative, question: schema.Question):
        try:
            db_question = models.Question(id = question.id,
                                          statement= question.statement,
                                          quiz_id= question.quiz_id)
            db_alternative = models.Alternative(id = alternative.id,
                                                statement= alternative.statement, 
                                                isCorrect=alternative.isCorrect,
                                                question_id=alternative.question_id)
            self.db.add(db_question)
            self.db.add(db_alternative)
            self.db.commit()
            self.db.refresh(db_question)
            self.db.refresh(db_alternative)
            return "created"
        except Exception as e:
            return e