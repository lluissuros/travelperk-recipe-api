from rest_framework import serializers

from core.models import Recipe


# class RecipeSerializer(serializers.ModelSerializer):
#     """Serializer for recipe object."""
#     # TODO later we need to serialize ingredients as well

#     class Meta:
#         model = Recipe
#         fields = ('id', 'name', 'description')
#         read_only_Fields = ('id',)


# class RecipeDetailSerializer(RecipeSerializer):
#     """Serializer for recipe detail"""
#     ingredients = IngredientSerializer(many=True, read_only=True)
#     tags = TagSerializer(many=True, read_only=True)


class DynamicFieldSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        context = kwargs.get('context', None)
        fields = None
        if context:
            fields = context.get('fields')

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class RecipeSerializer(DynamicFieldSerializer):
    """Serializer for recipe object."""
    # TODO later we need to serialize ingredients as well

    class Meta:
        model = Recipe
        fields = ('__all__')
        read_only_Fields = ('id',)
