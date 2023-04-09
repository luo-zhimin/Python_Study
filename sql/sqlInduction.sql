-- 操作数据库的SQL语言，也基于功能，可以划分为4类
-- 数据定义：DDL（Data Definition Language）
-- 库的创建删除、表的创建删除等
-- 数据操纵：DML（Data Manipulation Language）
-- 新增数据、删除数据、修改数据等
-- 数据控制：DCL（Data Control Language）
-- 新增用户、删除用户、密码修改、权限管理等
-- 数据查询：DQL（Data Query Language）
-- 基于需求查询和计算数据

# 注释
# 单行
# # and --
# 多行
/* 我是多行注释 */

# DDL
# 查看数据库
show databases;
# 使用数据库
use student;
# 查看当前使用的数据库
SELECT database();
# 创建数据库
create database test charset utf8;
# 删除数据库
drop database test;
# all tables
show tables;
# drop table
drop table sys_leave;
drop table if exists sys_leave;
# create table
create table test
(
    id          bigint,
    name        varchar(50),
    money       float,
    create_time timestamp
);



