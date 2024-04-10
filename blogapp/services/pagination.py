# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response

# class CustomPagination(PageNumberPagination):
#     # page_size_query_param = 'page_size'  # Specify the query parameter for page size
#     # max_page_size = 1000  # Optionally specify the maximum page size
#     # page_query_param = 'page'  # Specify the query parameter for page number

#     def get_paginated_response(self, data):
#         page_size_query_param = self.request.page_size
#         page_query_param = self.request.page
#         max_page_size = 1000
#         return Response({
#             'count': self.page.paginator.count,  # Fix this line
#             'next': self.get_next_link(),
#             'previous': self.get_previous_link(),
#             'results': data
#         })
