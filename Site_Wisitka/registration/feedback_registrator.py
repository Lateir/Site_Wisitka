import transaction
from Site_Wisitka.models.feedbackDb import FeedbackDb


def register_feedback(request):
    feedback_db = FeedbackDb(
        username=request.params['username'],
        phone=request.params['phone']
    )
    request.dbsession.add(feedback_db)
    transaction.commit()

    query = request.dbsession.query(FeedbackDb)
    return query.order_by(FeedbackDb.id.desc()).first()
