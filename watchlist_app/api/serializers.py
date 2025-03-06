from rest_framework import serializers
from ..models import Movie


# -----------------------------ModelSerializer--------------------------------
class MovieSerializer(serializers.ModelSerializer):
    # serializer method field
    len_title= serializers.SerializerMethodField()
    class Meta:
        model = Movie
        # fields = '__all__'
        # fields = ['id', 'title', 'description', 'active', 'genre', 'year', 'created_at', 'updated_at']
        exclude = ['created_at', 'updated_at', ]

    # custom serializer field
    def get_len_title(self, object):
        title = object.title
        return len(title)

    # field level validation
    def validate_title(self, value):
        if len(value) <= 1:
            raise serializers.ValidationError('Title is too short!')
        return value
    
    # object level validation
    def validate(self, data):
        if (data['title']).lower() == data['description'].lower():
            raise serializers.ValidationError('Title and Description should be different!')
        return data



# # validator function
# def year_validator(value):
#     if value < 1940:
#         raise serializers.ValidationError('Year should be greater than 1940!')

# -----------------------------------Serializer--------------------------------
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     active = serializers.BooleanField(required=False)
#     genre = serializers.CharField(max_length=100, required=False)
#     year = serializers.IntegerField(required=False, validators=[year_validator, ])
#     created_at = serializers.DateTimeField(required=False)
#     updated_at = serializers.DateTimeField(required=False)


#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.genre = validated_data.get('genre', instance.genre)
#         instance.year = validated_data.get('year', instance.year)
#         instance.save()
#         return instance
    
#     # field level validation
#     def validate_title(self, value):
#         if len(value) <= 1:
#             raise serializers.ValidationError('Title is too short!')
#         return value
    
#     # object level validation
#     def validate(self, data):
#         if (data['title']).lower() == data['description'].lower():
#             raise serializers.ValidationError('Title and Description should be different!')
#         return data
