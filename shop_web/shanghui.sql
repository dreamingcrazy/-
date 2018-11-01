create database tor_db charset=utf8;

use tor_db;


CREATE TABLE user_info(
    user_id int not null PRIMARY KEY auto_increment comment '用户ID',
    user_name VARCHAR(10) not null comment '用户名',
    password VARCHAR(16) not null comment '密码',
    phone VARCHAR(11) UNIQUE not NULL comment '手机号码',
    e_mail VARCHAR(50) not NULL comment '邮箱',
    create_time datetime not null DEFAULT CURRENT_TIMESTAMP comment '创建时间',
    update_time datetime not null DEFAULT CURRENT_TIMESTAMP comment '更新时间时间',
    role INT not null DEFAULT '0' comment '这是权限问题，0普通用户 1 商家 2 超级管理员',
    is_delete int not null DEFAULT '0' comment '是否删除0-未删1-删除',
    is_active  int not null DEFAULT '0' comment '是否激活0-未激活1-激活'
);


CREATE TABLE user_address_info(
  id int not null PRIMARY KEY auto_increment comment '地址ID',
  user_id int not null  comment '用户ID',
  add_detail  VARCHAR(50) not NULL comment '详细地址',
  receive_phone VARCHAR(11) UNIQUE not NULL comment '收货号码',
  is_delete int not null DEFAULT '0' comment '是否删除0-未删1-删除',
  is_default int not null DEFAULT '0' comment '是否默认0-未默认1-默认',
  CONSTRAINT FOREIGN KEY (user_id) REFERENCES user_info (user_id)
);