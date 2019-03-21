from django_elasticsearch_dsl import DocType, Index, fields
from products.models import Product, ProductCategory


product = Index('products')

product.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@product.doc_type
class ProductDocument(DocType):
    category = fields.NestedField(properties={
        'name': fields.TextField(),
    })
    discount = fields.FloatField(attr='discount')

    class Meta:
        model = Product

        fields = [
            'name',
            'regular_price',
            'final_price',
            'is_available',
            'description',
            'timestamp',
        ]

    related_models = [ProductCategory]

    def get_queryset(self):
        return super(ProductDocument, self).get_queryset().select_related(
            'category'
        )
