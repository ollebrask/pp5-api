from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from tags.models import Tag


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    # https://www.django-rest-framework.org/api-guide/relations/
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(), slug_field='name', many=True
    )

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size is larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)
        instance.tags.clear()
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)
        return instance

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'tags', 'like_id',
            'likes_count', 'comments_count',
        ]