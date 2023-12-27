from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


@api_view(['POST'])
def growth_prediction(request):
    if request.method == 'POST':
        user_question = request.data.get('question', '')

        if not user_question:
            return JsonResponse({'msg':'Please provide the question.'})

        response = "The projected growth rate is 5%"

        with open('user_q.log', 'a') as log_file:
            log_file.write(f"User Question: {user_question}\n")

        return Response({'prediction': response})
