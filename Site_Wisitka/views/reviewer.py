from pyramid.view import view_config
from Site_Wisitka.registration.review_registrator import register_review, get_all_reviews
from ..registration.feedback_registrator import register_feedback


@view_config(route_name='home', renderer='../templates/index.jinja2')
def reviewer(request):
    feedback = None

    if request.params.__contains__('review'):
        register_review(request)
    elif request.params.__contains__('feedback'):
        feedback = register_feedback()

    reviews = get_all_reviews(request)
    return {'project': 'Site_Wisitka',
            'reviews': reviews,
            'feedback': feedback}
