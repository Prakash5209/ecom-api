from rest_framework import mixins, generics 
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from store.models import CategoryModel,ProductModel,ProductImageModel,ProductColorModel,ProductSizeModel
from store.serializers import CategoryModelSerializer,ProductModelSerializer,ProductImageModelSerializer,ProductModelListSerializer,ProductColorModelSerializer,ProductSizeModelSerializer,ProductModelDetailSerializer


# test 
from django.contrib.auth import get_user_model

class CategoryListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class CategoryRetrieveUpdateDestory(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

#class CategoryProductListView(mixins.ListModelMixin,generics.GenericAPIView):
#    serializer_class = ProductModelSerializer
#    permission_classes = (AllowAny,)
#
#    def get_queryset(self,*args,**kwargs):
#        modl = ProductModel.objects.filter(category__name = kwargs.get('name'))
#        return modl
#
#    def get(self,request,*args,**kwargs):
#        self.queryset = self.get_queryset(*args,**kwargs)
#        return self.list(request,*args,**kwargs)



class ProductListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (AllowAny,)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(user = self.request.user)


class ProductRetrieveUpdateDestory(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    lookup_field = 'slug'

    #def get_queryset(self):
    #    modl = ProductModel.objects.filter(slug = self.kwargs.get('slug'))

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class ProductColorListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProductColorRUD(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = ProductColorModel.objects.all()
    serializer_class = ProductColorModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class ProductSizeListCreateView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = ProductSizeModel.objects.all()
    serializer_class = ProductSizeModelSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProductSizeRUD(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = ProductSizeModel.objects.all()
    serializer_class = ProductSizeModelSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



class ProductImageCRUDView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            models = ProductImageModel.objects.filter(id=kwargs.get('pk'))
            serializer = ProductImageModelSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductImageModel.DoesNotExist:
            return Response(
                {"error": "Product colors not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, *args, **kwargs):
        serializer = ProductImageModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        try:
            model = get_object_or_404(ProductImageModel, id=kwargs.get('pk'))
            print(model)
            serializer = ProductImageModelSerializer(model, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProductImageModel.DoesNotExist:
            return Response(
                {"error": "Product color not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            model = get_object_or_404(ProductImageModel, id=kwargs.get('pk'))
            model.delete()  # Call delete() as a method, not property
            return Response(
                {"message": "Product color deleted successfully"},
                status=status.HTTP_204_NO_CONTENT
            )
        except ProductImageModel.DoesNotExist:
            return Response(
                {"error": "Product color not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )




# extra views for info 


# category product list with slug field
class CategoryProductListView(APIView):
    def get(self,request,*args,**kwargs):
        modl = ProductModel.objects.filter(category__name = kwargs.get('name'))
        seri = ProductModelListSerializer(modl,many=True)
        print('mero')
        User = get_user_model()
        for i in User._meta.get_fields():
            print(i)
        return Response(seri.data,status = status.HTTP_200_OK)



# product detail view with all the info image, color and size..
class ProductDetailView(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelDetailSerializer
    lookup_field = 'slug'
    def get(self,request,*args,**kwargs):
        response = self.retrieve(request,*args,**kwargs)
        return self.retrieve(request,*args,**kwargs)

