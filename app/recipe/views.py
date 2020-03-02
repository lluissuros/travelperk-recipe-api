from rest_framework import viewsets

from core.models import Recipe

from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action

        if (action == 'list'):
            context['fields'] = ('name', 'description', 'ingredients',)
        return context
