/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/4/7 22:52:22                            */
/*==============================================================*/


drop table if exists 习题;

drop table if exists 封禁;

drop table if exists 已登录用户;

drop table if exists 用户;

drop table if exists 管理员;

drop table if exists 视频;

drop table if exists 认证证书;

drop table if exists 课程;

drop table if exists 错题;

drop table if exists 错题集;

/*==============================================================*/
/* Table: 习题                                                    */
/*==============================================================*/
create table 习题
(
   习题编号                 int not null,
   用户id                 int,
   课程id                 int,
   已登录_用户id             int,
   题干                   char(256) not null,
   题目类型                 char(20),
   答案                   char(1024),
   primary key (习题编号)
);

/*==============================================================*/
/* Table: 封禁                                                    */
/*==============================================================*/
create table 封禁
(
   管理员id                int not null,
   用户id                 int not null,
   primary key (管理员id, 用户id)
);

/*==============================================================*/
/* Table: 已登录用户                                                 */
/*==============================================================*/
create table 已登录用户
(
   用户id                 int not null,
   用户名                  char(20) not null,
   用户密码                 char(30) not null,
   金牌讲师认证               bool not null,
   封禁情况                 bool not null,
   封禁截止日期               datetime,
   primary key (用户id)
);

/*==============================================================*/
/* Table: 用户                                                    */
/*==============================================================*/
create table 用户
(
   用户id                 int not null,
   primary key (用户id)
);

/*==============================================================*/
/* Table: 管理员                                                   */
/*==============================================================*/
create table 管理员
(
   管理员id                int not null,
   管理员名                 char(20) not null,
   管理员密码                char(20) not null,
   primary key (管理员id)
);

/*==============================================================*/
/* Table: 视频                                                    */
/*==============================================================*/
create table 视频
(
   视频id                 int not null,
   管理员id                int,
   课程id                 int,
   用户id                 int,
   已登录_用户id             int,
   视频名                  char(20) not null,
   播放量                  int not null,
   审核人员                 char(20),
   审核日期                 datetime,
   审核结果                 char(10) not null,
   primary key (视频id)
);

/*==============================================================*/
/* Table: 认证证书                                                  */
/*==============================================================*/
create table 认证证书
(
   证书编号                 int not null,
   课程id                 int,
   用户id                 int,
   完成日期                 date not null,
   primary key (证书编号)
);

/*==============================================================*/
/* Table: 课程                                                    */
/*==============================================================*/
create table 课程
(
   课程id                 int not null,
   课程名                  char(20) not null,
   观看人数                 int not null,
   primary key (课程id)
);

/*==============================================================*/
/* Table: 错题                                                    */
/*==============================================================*/
create table 错题
(
   习题编号                 int not null,
   错题集id                int,
   用户id                 int,
   课程id                 int,
   题干                   char(256) not null,
   题目类型                 char(20),
   答案                   char(1024),
   错误答案                 char(1024),
   掌握情况                 bool not null,
   primary key (习题编号)
);

/*==============================================================*/
/* Table: 错题集                                                   */
/*==============================================================*/
create table 错题集
(
   错题集id                int not null,
   用户id                 int,
   错题集名                 char(20) not null,
   题目数量                 int not null,
   primary key (错题集id)
);

alter table 习题 add constraint FK_做题 foreign key (用户id)
      references 用户 (用户id) on delete restrict on update restrict;

alter table 习题 add constraint FK_用户发布习题 foreign key (已登录_用户id)
      references 已登录用户 (用户id) on delete restrict on update restrict;

alter table 习题 add constraint FK_课程习题 foreign key (课程id)
      references 课程 (课程id) on delete restrict on update restrict;

alter table 封禁 add constraint FK_管理员 foreign key (用户id)
      references 已登录用户 (用户id) on delete restrict on update restrict;

alter table 封禁 add constraint FK_被封禁用户 foreign key (管理员id)
      references 管理员 (管理员id) on delete restrict on update restrict;

alter table 已登录用户 add constraint FK_登录 foreign key (用户id)
      references 用户 (用户id) on delete restrict on update restrict;

alter table 视频 add constraint FK_用户发布视频 foreign key (已登录_用户id)
      references 已登录用户 (用户id) on delete restrict on update restrict;

alter table 视频 add constraint "FK_管理员发布/审核视频" foreign key (管理员id)
      references 管理员 (管理员id) on delete restrict on update restrict;

alter table 视频 add constraint FK_观看视频课程 foreign key (用户id)
      references 用户 (用户id) on delete restrict on update restrict;

alter table 视频 add constraint FK_课程视频 foreign key (课程id)
      references 课程 (课程id) on delete restrict on update restrict;

alter table 认证证书 add constraint FK_获得证书 foreign key (用户id)
      references 已登录用户 (用户id) on delete restrict on update restrict;

alter table 认证证书 add constraint FK_课程证书 foreign key (课程id)
      references 课程 (课程id) on delete restrict on update restrict;

alter table 错题 add constraint FK_包含 foreign key (错题集id)
      references 错题集 (错题集id) on delete restrict on update restrict;

alter table 错题 add constraint FK_继承 foreign key (习题编号)
      references 习题 (习题编号) on delete restrict on update restrict;

alter table 错题集 add constraint "FK_制作/管理" foreign key (用户id)
      references 已登录用户 (用户id) on delete restrict on update restrict;

