from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Recipe

from recipe.serializers import RecipeSerializer


RECIPES_URL = reverse('recipe:recipe-list')


def detail_url(recipe_id):
    return reverse('recipe:recipe-detail', args=[recipe_id])


def sample_recipe(**params):
    """Create and return a sample recipe"""
    defaults = {
        'name': 'Sample recipe',
        'description': 'some default description',
    }
    defaults.update(params)

    return Recipe.objects.create(**defaults)


class PublicRecipesApiWithoutIngredientsTests(TestCase):
    """Test the publicly available recipes API"""

    def setUp(self):
        self.client = APIClient()

    def test_GET_recipes_list_single_recipe(self):
        """Test retriving a list of recipes"""
        sample_recipe()
        res = self.client.get(RECIPES_URL)

        recipes_from_db = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes_from_db, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        for recipe, serialized in zip(res.data, serializer.data):
            for key in recipe.keys():
                self.assertEqual(recipe[key], serialized[key])

    def test_GET_recipes_list_have_no_id(self):
        """Test retriving a list of recipes"""
        sample_recipe()
        sample_recipe()
        res = self.client.get(RECIPES_URL)

        recipes_from_db = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes_from_db, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        for recipe, serialized in zip(res.data, serializer.data):
            self.assertIn('name', recipe)
            self.assertIn('name', serialized)
            self.assertNotIn('id', recipe)
            self.assertIn('id', serialized)

    def test_GET_recipe_detail(self):
        """Test viewing a recipe detail"""
        recipe = sample_recipe()

        url = detail_url(recipe.id)
        print(url)
        res = self.client.get(url)

        serializer = RecipeSerializer(recipe)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_POST_basic_recipe(self):
        """Test creating recipe"""
        payload = {
            'name': 'Test recipe',
            'description': 'a description',
        }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe_from_db = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe_from_db, key))


class PublicRecipesApiWithIngredientsTests(TestCase):
    """TODO"""
