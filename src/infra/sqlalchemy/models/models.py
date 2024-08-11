from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

#there we have a hierarchy of relationships between the tables, so i have decided 
#to create then based on order of its level of hierarchy

class Alternative(Base):
    __tablename__= 'Alternatives'
    id = Column(Integer, primary_key=True, index=True)
    statement = Column(String)
    isCorrect = Column(Boolean)
    question_id = Column(Integer, ForeignKey('Questions.id'),name='question_id' )
    
    questionFK = relationship("Question", back_populates="alternativesFK")
    
class Question(Base):
    __tablename__= 'Questions'
     
    id = Column(Integer, primary_key=True, index=True)
    statement = Column(String)
    quiz_id = Column(Integer, ForeignKey('Quizzes.id'),name='quiz_id' )
    
    alternativesFK = relationship("Alternative", back_populates="questionFK")    
    quizFK = relationship("Quiz", back_populates="questionsFK")
    
class Quiz(Base):
    __tablename__= 'Quizzes'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    isDone = Column(Boolean)
    user_id = Column(Integer, ForeignKey('Users.id'),name='user_id')
    
    questionsFK = relationship("Question", back_populates="quizFK")
    userFK = relationship("User", back_populates="quizzesFK")
    
class User(Base):
    __tablename__= 'Users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String) 
    quizzesFK = relationship("Quiz", back_populates="userFK")