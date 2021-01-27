import transaction

from Site_Wisitka.models.reviewDb import ReviewDb
from datetime import datetime


def register_review(request):
    review_db = ReviewDb(
        username=request.params['username'],
        comment=request.params['comment'],
        date=datetime.now(tz=None)
    )
    request.dbsession.add(review_db)
    transaction.commit()

    query = request.dbsession.query(ReviewDb)
    return query.order_by(ReviewDb.id.desc()).first()


def get_all_reviews(request):
    query = request.dbsession.query(ReviewDb)
    rows = len(query.all())
    if rows == 0:
        return None
    return query.order_by(ReviewDb.id)
