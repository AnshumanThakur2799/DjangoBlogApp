from django.http import JsonResponse, HttpResponseNotFound,HttpResponseServerError,Http404
from django.core.paginator import Paginator
from rest_framework import generics,status
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.core.exceptions import ObjectDoesNotExist,PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny

class ListView(APIView):
    queryset = Post.objects.all().order_by('published_date')
    serializer_class = PostSerializer
    def get(self,request , *args , **kwargs):
        try:
            queryset = self.queryset
            page_number = self.request.GET.get('page', 1)
            page_size = self.request.GET.get('page_size', 10)
            paginator = Paginator(queryset, page_size)
            page = paginator.get_page(page_number)
            serializer = self.serializer_class(page.object_list, many=True)
            data = {
                'results': serializer.data,
                'total_pages': paginator.num_pages,
                'current_page': page_number,
            }
            return JsonResponse(data)
        except Exception as e:
            return HttpResponseServerError(str(e))
    
class CreatePostView(APIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    Permisssion_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                print(f"aaaaaaaaaaaaaaaaaa{type(self.request.user)}")
                serializer.save(author=self.request.user)
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except Exception as e:
            return HttpResponseServerError(str(e))

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        post_id = self.kwargs.get('pk')
        try:
            post = Post.objects.get(pk=post_id) 
            return post
        except Post.DoesNotExist:
            raise Http404("Post not found")
        
    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request, *args, **kwargs):
        try: 
            post = self.get_object()
            serializer = self.serializer_class(post) 
            serializer.data["comments"] = post.comments.all()
            print(f"bbbbbb{serializer.data}")
            return JsonResponse(serializer.data)
        except Exception as e:
            return HttpResponseServerError(str(e))
        
    def put(self, request, *args, **kwargs):
        try:
            post = self.get_object()
            if request.user != post.author:
                raise PermissionDenied("You are not authorized to update this post.")
            
            serializer = self.get_serializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        
        except Exception as e:
            return HttpResponseServerError(str(e))

    def delete(self, request, *args, **kwargs):
        try:
            post = self.get_object()
            if request.user!= post.author:
                raise PermissionDenied("You are not authorized to delete this post.")
            post.delete()
            return JsonResponse({"message": "Post deleted successfully"}, status=204)
        except Exception as e:
            return HttpResponseServerError(str(e))

class PostComment(APIView):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(author = self.request.user)
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return HttpResponseServerError(str(e))

class EditComment(APIView):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        try:
            comment = Comment.objects.get(pk = comment_id)
            return comment
        except Exception as e:
            raise HttpResponseNotFound("Post not found" , status = status.HTTP_404_NOT_FOUND)
        
    def put(self, request, *args, **kwargs):
        try:
            comment = self.get_object()
            if request.user != comment.author:
                raise PermissionDenied("You are not authorized to update this comment.")
            
            serializer = self.serializer_class(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            else:
                return JsonResponse(serializer.errors, status=400)
        except Exception as e:
            return HttpResponseServerError(str(e))
    
    def delete(self, request, *args, **kwargs):
        try:
            comment = self.get_object()
            if request.user != comment.author:
                raise PermissionDenied("You are not authorized to delete this comment.")

            comment.delete()
            return JsonResponse({"message": "Comment deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return HttpResponseServerError(str(e))
