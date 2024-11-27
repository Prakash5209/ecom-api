from django.urls import path

from store.views import CategoryListCreateView,CategoryRetrieveUpdateDestory,CategoryProductListView,ProductListCreateView,ProductRetrieveUpdateDestory,ProductImageCRUDView,ProductColorListCreateView,ProductColorRUD,ProductSizeListCreateView,ProductSizeRUD,ProductDetailView

app_name = "store"
urlpatterns = [
    path('api/categories/',CategoryListCreateView.as_view(),name="categorylistcreateview"),
    path('api/categories/<int:pk>/',CategoryRetrieveUpdateDestory.as_view(),name="categoryretrieveupdatedestory"),

    # category product list with slug 
    path('category-product/<str:name>/',CategoryProductListView.as_view(),name="categoryproductlistview"),

    path('create-product/',ProductListCreateView.as_view(),name="productlistcreateview"),
    path('rud-product/<str:slug>/',ProductRetrieveUpdateDestory.as_view(),name="productretrieveupdatedestory"),

    path('color/',ProductColorListCreateView.as_view(),name="productcolorlistcreateview"),
    path('colorrud/<int:pk>/',ProductColorRUD.as_view(),name="ProductColorRUD"),

    path('size/',ProductSizeListCreateView.as_view(),name="productsizelistcreateview"),
    path('sizerud/<int:pk>/',ProductSizeRUD.as_view(),name="productsizerud"),


    path('image/<int:pk>/',ProductImageCRUDView.as_view(),name="productimageRview"),
    path('create-image/',ProductImageCRUDView.as_view(),name="productimageCview"),
    path('update-image/<int:pk>/',ProductImageCRUDView.as_view(),name="productimageUview"),
    path('delete-image/<int:pk>/',ProductImageCRUDView.as_view(),name="productimageDview"),

    #product detail view
    path('product-detail/<str:slug>/',ProductDetailView.as_view(),name="productdetailview"),

]
