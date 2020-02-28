from django.test import TestCase

from core import models


class ModelTests(TestCase):

    def test_new_recipe_without_name_raises_error(self):
        """Test creating recipe with no name raises error"""
        with self.assertRaises(Exception):
            models.Recipe.objects.create(
                name=None,
                description=None
            )

    def test_new_recipe_with_name_works_fine(self):
        """Test creating recipe with name works"""
        recipe = models.Recipe.objects.create(
            name='yeah name',
            description=None
        )
        self.assertEquals(recipe.name, 'yeah name')

    def test_recipe_str(self):
        """Test the recipe string representation"""
        recipe = models.Recipe.objects.create(
            name='recipe 1 test name',
            description='test description'
        )
        self.assertEqual(str(recipe), recipe.name)
