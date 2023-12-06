import re

from . import models
from bs4 import BeautifulSoup
from django.db.models import F
from django.contrib import auth
from django.db import transaction
from django.db.models import Count
from rest_framework import serializers
from django.db.models.functions import TruncMonth
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


# LoginView

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.UserInfo
        fields = ['username', 'password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        user_obj = self._get_user_obj(attrs)
        token = self._get_token(user_obj)
        self.context['user_obj'] = user_obj
        self.context['token'] = token
        return attrs

    def _get_user_obj(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user_obj = auth.authenticate(username=username, password=password)
        if user_obj:
            return user_obj
        raise ValidationError('用户名或密码错误!')

    def _get_token(self, user_obj):
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        return token


# RegisterView

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(min_length=3, max_length=8, allow_blank=True, write_only=True, error_messages={'min_length': '确认密码最少3位!', 'max_length': '确认密码最大8位!'})
    email = serializers.EmailField(allow_blank=True, error_messages={'invalid': '邮箱格式不正确!'})

    class Meta:
        model = models.UserInfo
        fields = ['username', 'password', 'confirm_password', 'email', 'avatar']
        extra_kwargs = {
            'username':{
                'min_length':3, 'max_length':8, 'allow_blank':True,
                'error_messages':{
                    'min_length': '用户名最少3位!',
                    'max_length': '用户名最大8位!'
                }
            },
            'password':{
                'min_length':3, 'max_length':8, 'allow_blank':True,
                'error_messages':{
                    'min_length': '密码最少3位!',
                    'max_length': '密码最大8位!'
                }
            }
        }

    def validate_username(self, attr):
        if not attr:
            raise ValidationError('用户名不能为空!')
        return attr

    def validate_password(self, attr):
        if not attr:
            raise ValidationError('密码不能为空!')
        if not re.match('^[0-9]+$', attr):
            raise ValidationError('密码不能为非数字!')
        return attr

    def validate_confirm_password(self, attr):
        if not attr:
            raise ValidationError('确认密码不能为空!')
        return attr

    def validate_email(self, attr):
        if not attr:
            raise ValidationError('邮箱不能为空!')
        return attr

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password == confirm_password:
            attrs.pop('confirm_password')
            return attrs
        raise ValidationError({'confirm_password': '两次输入的密码不一致!'})

    def create(self, validated_data):
        categories = ['手机', '平板', '笔记本电脑']
        tags = ['华为', '苹果', '三星', 'OPPO', '真我', 'IQOO', '戴尔', '￥0-3000', '￥3000-6000', '￥6000-10000', '￥10000-15000', '￥15000+']
        site_name = validated_data.get('username')
        site_title = validated_data.get('username') + '的网店'
        mall = models.Mall.objects.create(site_name=site_name, site_title=site_title)
        for name in categories:
            models.Category.objects.create(name=name, mall_id=mall.pk)
        for name in tags:
            models.Tag.objects.create(name=name, mall_id=mall.pk)
        validated_data['mall_id'] = mall.pk
        user_obj = models.UserInfo.objects.create_user(**validated_data)
        return user_obj


# HomeCreatedView   SearchView

class HomeCreatedSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')
    site_title = serializers.CharField(source='mall.site_title')
    avatar = serializers.FileField(source='mall.userinfo.avatar')

    class Meta:
        model = models.Goods
        fields = ['id', 'shop_name', 'desc', 'shop_picture', 'create_time', 'up_num', 'comment_num', 'site_name', 'site_title', 'avatar']


# CreatedView

class CreatedTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = ['id', 'name']


class CreatedSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')
    tags = CreatedTagSerializer(many=True)

    class Meta:
        model = models.Goods
        fields = ['id', 'shop_name', 'shop_price', 'shop_picture', 'up_num', 'down_num', 'site_name', 'tags']


# ExhibitView

class ExhibitSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.UserInfo
        fields = ['username', 'password']
        extra_kwargs = {
            'password':{'allow_blank':True, 'write_only':True}
        }

    def validate_password(self, attr):
        if not attr:
            raise ValidationError('账号密码不能为空!')
        if not re.match('^[0-9]+$', attr):
            raise ValidationError('密码不能为非数字!')
        return attr

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user_obj = auth.authenticate(username=username, password=password)
        if user_obj:
            return attrs
        raise ValidationError('账号密码错误!')


# SiteCreatedView

class LeftCategorySerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')
    count_num = serializers.SerializerMethodField()

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'site_name', 'count_num']

    def get_count_num(self, instance):
        return instance.goods_set.count()


class LeftTagSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')
    count_num = serializers.SerializerMethodField()

    class Meta:
        model = models.Tag
        fields = ['id', 'name', 'site_name', 'count_num']

    def get_count_num(self, instance):
        return instance.goods_set.count()


class LeftMenuSerializer(serializers.ModelSerializer):
    category_list = LeftCategorySerializer(many=True, source='category_set')
    tag_list = LeftTagSerializer(many=True, source='tag_set')
    date_list = serializers.SerializerMethodField()

    class Meta:
        model = models.Mall
        fields = ['site_title', 'category_list', 'tag_list', 'date_list']

    def get_date_list(self, instance):
        return models.Goods.objects.filter(mall=instance).annotate(month=TruncMonth('create_time')).values('month').annotate(count_num=Count('pk')).values_list('month', 'count_num')


class SiteCreatedSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')
    left_menu = LeftMenuSerializer(source='mall')

    class Meta:
        model = models.Goods
        fields = ['id', 'shop_name', 'desc', 'shop_picture', 'create_time', 'up_num', 'comment_num', 'site_name', 'left_menu']


# GoodsDetailCreatedView

class GoodsDetailCommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    parent = serializers.SerializerMethodField()

    class Meta:
        model = models.Comment
        fields = ['id', 'content', 'content_time', 'username', 'parent']

    def get_parent(self, instance):
        if instance.parent:
            return instance.parent.user.username
        return None


class GoodsDetailCreatedSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')
    comment = GoodsDetailCommentSerializer(many=True, source='comment_set')
    left_menu = LeftMenuSerializer(source='mall')

    class Meta:
        model = models.Goods
        fields = ['id', 'shop_name', 'shop_price', 'content', 'shop_picture', 'up_num', 'down_num', 'site_name', 'comment', 'left_menu']


# SetPasswordView

class SetPasswordSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    old_password = serializers.CharField(allow_blank=True, write_only=True)
    new_password = serializers.CharField(min_length=3, max_length=8, allow_blank=True, write_only=True, error_messages={'min_length': '新密码最少3位!', 'max_length': '新密码最大8位!'})
    confirm_password = serializers.CharField(min_length=3, max_length=8, allow_blank=True, write_only=True, error_messages={'min_length': '确认密码最少3位!', 'max_length': '确认密码最大8位!'})

    class Meta:
        model = models.UserInfo
        fields = ['username', 'old_password', 'new_password', 'confirm_password']

    def validate_old_password(self, attr):
        if not attr:
            raise ValidationError('原密码不能为空!')
        return attr

    def validate_new_password(self, attr):
        if not attr:
            raise ValidationError('新密码不能为空!')
        if not re.match('^[0-9]+$', attr):
            raise ValidationError('新密码不能为非数字!')
        return attr

    def validate_confirm_password(self, attr):
        if not attr:
            raise ValidationError('确认密码不能为空!')
        return attr

    def validate(self, attrs):
        username = attrs.get('username')
        old_password = attrs.get('old_password')
        user_obj = auth.authenticate(username=username, password=old_password)
        if user_obj:
            new_password = attrs.get('new_password')
            confirm_password = attrs.get('confirm_password')
            if new_password == confirm_password:
                if not new_password == old_password:
                    return attrs
                raise ValidationError('新密码不能与原密码重复')
            raise ValidationError('两次密码不一致')
        raise ValidationError('原密码错误')

    def update(self, instance, validated_data):
        new_password = validated_data.get('new_password')
        instance.set_password(new_password)
        instance.save()
        return instance


# SetAvatarView

class SetAvatarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInfo
        fields = ['avatar']

    def update(self, instance, validated_data):
        file_obj = validated_data.get('avatar')
        if file_obj:
            instance.avatar = file_obj
        else:
            instance.avatar = 'avatar/w.jpg'
        instance.save()
        return instance


# BackendCreatedView

class BackendShopCarSerializer(serializers.ModelSerializer):
    goods_id = serializers.CharField(source='goods.id')
    shop_name = serializers.CharField(source='goods.shop_name')
    shop_price = serializers.CharField(source='goods.shop_price')
    site_name = serializers.CharField(source='goods.mall.site_name')

    class Meta:
        model = models.ShopCar
        fields = ['id', 'shop_time', 'goods_id', 'shop_name', 'shop_price', 'site_name']


class BackendFlowSerializer(serializers.ModelSerializer):
    goods_id = serializers.CharField(source='goods.id')
    shop_name = serializers.CharField(source='goods.shop_name')
    shop_price = serializers.CharField(source='goods.shop_price')
    site_name = serializers.CharField(source='goods.mall.site_name')

    class Meta:
        model = models.Flow
        fields = ['balance_flow', 'buy_num', 'sell_num', 'pay_time', 'goods_id', 'shop_name', 'shop_price', 'site_name']


class BackendGoodsSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='mall.site_name')

    class Meta:
        model = models.Goods
        fields = ['id', 'shop_name', 'shop_price', 'up_num', 'comment_num', 'site_name']


class BackendCreatedSerializer(serializers.ModelSerializer):
    car_list = BackendShopCarSerializer(many=True, source='userinfo.shopcar_set')
    flow_list = BackendFlowSerializer(many=True, source='userinfo.flow_set')
    goods_list = BackendGoodsSerializer(many=True, source='goods_set')

    class Meta:
        model = models.Mall
        fields = ['car_list', 'flow_list', 'goods_list']


# ShopCarView

class ShopCarSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_null=True)
    goods_id = serializers.CharField()

    class Meta:
        model = models.ShopCar
        fields = ['username', 'goods_id']

    def validate_username(self, attr):
        if not attr:
            raise ValidationError('<a href="/login" style="text-decoration:none">请先登录</a>')
        return attr

    def validate(self, attrs):
        username = attrs.get('username')
        goods_id = attrs.get('goods_id')
        user = models.UserInfo.objects.filter(username=username).first()
        goods_obj = models.Goods.objects.filter(pk=goods_id).first()
        if not goods_obj.mall == user.mall:
            is_click = models.ShopCar.objects.filter(user=user, goods=goods_obj)
            if not is_click:
                attrs['user'] = user
                attrs['goods_obj'] = goods_obj
                return attrs
            raise ValidationError('不能重复点击')
        raise ValidationError('自己不能点击')

    def create(self, validated_data):
        user = validated_data.get('user')
        goods_obj = validated_data.get('goods_obj')
        user_obj = models.ShopCar.objects.create(user=user, goods=goods_obj)
        return user_obj


# UpOrDownView

class UpOrDownSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_null=True)
    is_up = serializers.BooleanField()

    class Meta:
        model = models.Goods
        fields = ['username', 'is_up']

    def validate_username(self, attr):
        if not attr:
            raise ValidationError('<a href="/login" style="text-decoration:none">请先登录</a>')
        return attr

    def validate(self, attrs):
        username = attrs.get('username')
        user = models.UserInfo.objects.filter(username=username).first()
        if not self.instance.mall == user.mall:
            is_click = models.UpAndDown.objects.filter(user=user, goods=self.instance)
            if not is_click:
                attrs['user'] = user
                return attrs
            raise ValidationError('不能重复点击')
        raise ValidationError('自己不能点击')

    def update(self, instance, validated_data):
        user = validated_data.get('user')
        is_up = validated_data.get('is_up')
        if is_up:
            instance.up_num += 1
            self.context['msg'] = '点赞成功'
        else:
            instance.down_num += 1
            self.context['msg'] = '点踩成功'
        models.UpAndDown.objects.create(user=user, goods=instance, is_up=is_up)
        instance.save()
        return instance


# CommentView

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(allow_null=True)
    goods_id = serializers.CharField()
    parent_id = serializers.CharField(allow_blank=True)

    class Meta:
        model = models.Comment
        fields = ['username', 'goods_id', 'content', 'parent_id']

    def validate(self, attrs):
        username = attrs.get('username')
        if username:
            user = models.UserInfo.objects.filter(username=username).first()
            attrs.pop('username')
            attrs['user'] = user
            return attrs
        raise ValidationError({'comment_error': '<a href="/login" style="text-decoration:none">请先登录</a>'})

    def create(self, validated_data):
        goods_id = validated_data.get('goods_id')
        with transaction.atomic():
            models.Goods.objects.filter(pk=goods_id).update(comment_num=F('comment_num') + 1)
            user_obj = models.Comment.objects.create(**validated_data)
        content_time = user_obj.content_time
        self.context['msg'] = content_time.strftime('%Y-%m-%d %H:%M:%S')
        return user_obj


# PayView

class PaySerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    goods_id = serializers.CharField()

    class Meta:
        model = models.Flow
        fields = ['username', 'goods_id']

    def validate(self, attrs):
        username = attrs.get('username')
        goods_id = attrs.get('goods_id')
        buy_user = models.UserInfo.objects.filter(username=username).first()
        goods_obj = models.Goods.objects.filter(pk=goods_id).first()
        if buy_user.balance >= goods_obj.shop_price:
            attrs['goods_obj'] = goods_obj
            return attrs
        raise ValidationError('您的余额不足')

    def create(self, validated_data):
        username = validated_data.get('username')
        goods_id = validated_data.get('goods_id')
        goods_obj = validated_data.get('goods_obj')
        models.UserInfo.objects.filter(username=username).update(balance=F('balance') - goods_obj.shop_price)
        models.UserInfo.objects.filter(mall=goods_obj.mall_id).update(balance=F('balance') + goods_obj.shop_price)
        buy_user = models.UserInfo.objects.filter(username=username).first()
        sell_user = models.UserInfo.objects.filter(mall=goods_obj.mall_id).first()
        models.Flow.objects.create(user=buy_user, goods_id=goods_id, buy_num=1, balance_flow=buy_user.balance)
        models.Flow.objects.create(user=sell_user, goods_id=goods_id, sell_num=1, balance_flow=sell_user.balance)
        models.ShopCar.objects.filter(user=buy_user, goods_id=goods_id).delete()
        return sell_user


# CancelView

class CancelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ShopCar
        fields = '__all__'


# VipView

class VipSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInfo
        fields = ['username']

    def validate(self, attrs):
        if not self.instance.is_staff:
            return attrs
        raise ValidationError('不能重复购买')

    def update(self, instance, validated_data):
        instance.is_staff = True
        instance.save()
        return instance


# AddGoodsCreatedView

class AddGoodsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ['id', 'name']


class AddGoodsTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = ['id', 'name']


class AddGoodsCreatedSerializer(serializers.ModelSerializer):
    category_list = AddGoodsCategorySerializer(many=True, source='category_set')
    tag_list = AddGoodsTagSerializer(many=True, source='tag_set')

    class Meta:
        model = models.Mall
        fields = ['category_list', 'tag_list']


# AddGoodsView

class AddGoodsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    tag = serializers.ListField(write_only=True)

    class Meta:
        model = models.Goods
        fields = ['username', 'shop_name', 'shop_price', 'content', 'shop_picture', 'category', 'tag']

    def validate_content(self, attr):
        soup = BeautifulSoup(attr, 'html.parser')
        tags = soup.find_all()
        for tag in tags:
            if tag.name == 'script':
                tag.decompose()
        return attr

    def validate(self, attrs):
        username = attrs.get('username')
        content = attrs.get('content')
        user = models.UserInfo.objects.filter(username=username).first()
        soup = BeautifulSoup(content, 'html.parser')
        desc = soup.text[0:130]
        attrs.pop('username')
        attrs['content'] = str(soup)
        attrs['desc'] = desc
        attrs['mall'] = user.mall
        return attrs

    def create(self, validated_data):
        tag_id_list = validated_data.get('tag')
        validated_data.pop('tag')
        goods_obj = models.Goods.objects.create(**validated_data)
        goods_obj_list = []
        for tag_id in tag_id_list:
            tag_goods_obj = models.Goods2Tag(goods=goods_obj, tag_id=tag_id)
            goods_obj_list.append(tag_goods_obj)
        models.Goods2Tag.objects.bulk_create(goods_obj_list)
        return goods_obj