from .models import *
from django.db.models import Q


def counter_new_qna(request):
	q = Q()
	q &= Q(answered_at=None)
	result = QnA.objects.filter(q).count()
	return {'counter_new_qna':  result}