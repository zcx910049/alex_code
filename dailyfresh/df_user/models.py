from django.db import models
from db.base_model import BaseModel
from utils.get_hash import get_hash
from db.base_manager import BaseManager # 导入抽象模型管理器类


# Create your models here.
class PassportManager(BaseManager):
    """账户模型管理器类"""
    def add_one_passport(self,username,password,email):
        """添加一个用户注册信息"""
        obj = self.create_one_object(username=username,password=password,email=email)
        # 返回obj
        return obj

    # def get_one_object(self,**filter)
    def get_one_passport(self,username,password=None):
        """根据用户名查询账户信息"""
        if password is None:
            # 根据用户名查找账户信息
            obj = self.get_one_object(username=username)
        else:
            # 根据用户名查找账户信息
            obj = self.get_one_passport(username=username,password=get_hash(password))
        return obj


class Passport(BaseModel):
    """账户信息模型类"""
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=40,verbose_name='密码')
    email = models.CharField(max_length=254,verbose_name='邮箱')

    objects = PassportManager()  # 自定义模型管理器类对象

    class Meta:
        db_table = 's_user_account'


class AddressManager(BaseManager):
    """地址模型管理器类"""
    def get_one_address(self,passport_id):
        """查询账户的默认收货地址"""
        addr = self.get_one_object(passport_id=passport_id,is_default=True)
        return addr

    def add_one_address(self,passport_id,recipient_name,recipient_addr,recipient_phone,zip_code):
        """添加一个收货地址"""
        addr = self.get_one_address(passport_id=passport_id)
        is_default = False
        if addr is None:
            # 1.没有默认收货地址
            is_default = True
        # 2.已存在默认收货地
        addr = self.create_one_object(passport_id=passport_id,recipient_name=recipient_name,recipient_addr=recipient_addr,recipient_phone=recipient_phone,zip_code=zip_code,is_default=is_default)
        # 返回addr
        return addr


class Address(BaseModel):
    """地址模型类"""
    passport = models.ForeignKey('Passport',verbose_name='所属账户')
    recipient_name = models.CharField(max_length=24,verbose_name='收件人')
    recipient_addr = models.CharField(max_length=256,verbose_name='收件地址')
    recipient_phone = models.CharField(max_length=11,verbose_name='联系电话')
    zip_code = models.CharField(max_length=6,verbose_name='邮政编码')
    is_default = models.BooleanField(default=False,verbose_name='是否默认')

    objects = AddressManager()

    class Meta:
        db_table = 's_user_address'