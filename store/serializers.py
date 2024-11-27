from rest_framework.serializers import ModelSerializer

from store.models import CategoryModel,ProductModel,ProductImageModel,ProductColorModel,ProductSizeModel

class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ('user','slug',)

class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = '__all__'

class ProductColorModelSerializer(ModelSerializer):
    class Meta:
        model = ProductColorModel
        fields = '__all__'

class ProductSizeModelSerializer(ModelSerializer):
    class Meta:
        model = ProductSizeModel
        fields = '__all__'


# extra serializer

class ProductModelListSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ('user',)

class ProductModelDetailSerializer(ModelSerializer):
    category = CategoryModelSerializer()
    productmodel_image = ProductImageModelSerializer(many=True)
    product_color = ProductColorModelSerializer(many=True)
    product_size = ProductSizeModelSerializer(many=True)
    class Meta:
        model = ProductModel
        fields = '__all__'

