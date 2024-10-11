from database import db
from database import models


def create_question(content: str, answer: str, right_response: str, wrong_response: str, group_id: int):
	session = db.SessionLocal()
	side_question = models.SideQuestion(
		content=content,
		answer=answer,
		right_response=right_response,
		wrong_response=wrong_response,
		group_id=group_id
	)
	session.add(side_question)
	session.commit()


def get_questions(group_id: int):
	session = db.SessionLocal()
	query = session.query(models.SideQuestion)
	return query.filter(models.SideQuestion.group_id == group_id).all()


def delete_question(question_id: int):
	session = db.SessionLocal()
	query = session.query(models.SideQuestion)
	query.filter(models.SideQuestion.id == question_id).delete()
	session.commit()


def edit_question(
		question_id: int,
		content: str = None,
		answer: str = None,
		right_response: str = None,
		wrong_response: str = None):
	content = models.SideQuestion.content if not content else content
	answer = models.SideQuestion.answer if not answer else answer
	right_response = models.SideQuestion.right_response if not right_response else right_response
	wrong_response = models.SideQuestion.wrong_response if not wrong_response else wrong_response

	session = db.SessionLocal()
	query = session.query(models.SideQuestion)
	query.filter(models.SideQuestion.id == question_id).update(
		{
			models.SideQuestion.content: content,
			models.SideQuestion.answer: answer,
			models.SideQuestion.right_response: right_response,
			models.SideQuestion.wrong_response: wrong_response
		}
	)
	session.commit()
