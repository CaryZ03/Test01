/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/4/7 22:52:22                            */
/*==============================================================*/


drop table if exists ϰ��;

drop table if exists ���;

drop table if exists �ѵ�¼�û�;

drop table if exists �û�;

drop table if exists ����Ա;

drop table if exists ��Ƶ;

drop table if exists ��֤֤��;

drop table if exists �γ�;

drop table if exists ����;

drop table if exists ���⼯;

/*==============================================================*/
/* Table: ϰ��                                                    */
/*==============================================================*/
create table ϰ��
(
   ϰ����                 int not null,
   �û�id                 int,
   �γ�id                 int,
   �ѵ�¼_�û�id             int,
   ���                   char(256) not null,
   ��Ŀ����                 char(20),
   ��                   char(1024),
   primary key (ϰ����)
);

/*==============================================================*/
/* Table: ���                                                    */
/*==============================================================*/
create table ���
(
   ����Աid                int not null,
   �û�id                 int not null,
   primary key (����Աid, �û�id)
);

/*==============================================================*/
/* Table: �ѵ�¼�û�                                                 */
/*==============================================================*/
create table �ѵ�¼�û�
(
   �û�id                 int not null,
   �û���                  char(20) not null,
   �û�����                 char(30) not null,
   ���ƽ�ʦ��֤               bool not null,
   ������                 bool not null,
   �����ֹ����               datetime,
   primary key (�û�id)
);

/*==============================================================*/
/* Table: �û�                                                    */
/*==============================================================*/
create table �û�
(
   �û�id                 int not null,
   primary key (�û�id)
);

/*==============================================================*/
/* Table: ����Ա                                                   */
/*==============================================================*/
create table ����Ա
(
   ����Աid                int not null,
   ����Ա��                 char(20) not null,
   ����Ա����                char(20) not null,
   primary key (����Աid)
);

/*==============================================================*/
/* Table: ��Ƶ                                                    */
/*==============================================================*/
create table ��Ƶ
(
   ��Ƶid                 int not null,
   ����Աid                int,
   �γ�id                 int,
   �û�id                 int,
   �ѵ�¼_�û�id             int,
   ��Ƶ��                  char(20) not null,
   ������                  int not null,
   �����Ա                 char(20),
   �������                 datetime,
   ��˽��                 char(10) not null,
   primary key (��Ƶid)
);

/*==============================================================*/
/* Table: ��֤֤��                                                  */
/*==============================================================*/
create table ��֤֤��
(
   ֤����                 int not null,
   �γ�id                 int,
   �û�id                 int,
   �������                 date not null,
   primary key (֤����)
);

/*==============================================================*/
/* Table: �γ�                                                    */
/*==============================================================*/
create table �γ�
(
   �γ�id                 int not null,
   �γ���                  char(20) not null,
   �ۿ�����                 int not null,
   primary key (�γ�id)
);

/*==============================================================*/
/* Table: ����                                                    */
/*==============================================================*/
create table ����
(
   ϰ����                 int not null,
   ���⼯id                int,
   �û�id                 int,
   �γ�id                 int,
   ���                   char(256) not null,
   ��Ŀ����                 char(20),
   ��                   char(1024),
   �����                 char(1024),
   �������                 bool not null,
   primary key (ϰ����)
);

/*==============================================================*/
/* Table: ���⼯                                                   */
/*==============================================================*/
create table ���⼯
(
   ���⼯id                int not null,
   �û�id                 int,
   ���⼯��                 char(20) not null,
   ��Ŀ����                 int not null,
   primary key (���⼯id)
);

alter table ϰ�� add constraint FK_���� foreign key (�û�id)
      references �û� (�û�id) on delete restrict on update restrict;

alter table ϰ�� add constraint FK_�û�����ϰ�� foreign key (�ѵ�¼_�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ϰ�� add constraint FK_�γ�ϰ�� foreign key (�γ�id)
      references �γ� (�γ�id) on delete restrict on update restrict;

alter table ��� add constraint FK_����Ա foreign key (�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ��� add constraint FK_������û� foreign key (����Աid)
      references ����Ա (����Աid) on delete restrict on update restrict;

alter table �ѵ�¼�û� add constraint FK_��¼ foreign key (�û�id)
      references �û� (�û�id) on delete restrict on update restrict;

alter table ��Ƶ add constraint FK_�û�������Ƶ foreign key (�ѵ�¼_�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ��Ƶ add constraint "FK_����Ա����/�����Ƶ" foreign key (����Աid)
      references ����Ա (����Աid) on delete restrict on update restrict;

alter table ��Ƶ add constraint FK_�ۿ���Ƶ�γ� foreign key (�û�id)
      references �û� (�û�id) on delete restrict on update restrict;

alter table ��Ƶ add constraint FK_�γ���Ƶ foreign key (�γ�id)
      references �γ� (�γ�id) on delete restrict on update restrict;

alter table ��֤֤�� add constraint FK_���֤�� foreign key (�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ��֤֤�� add constraint FK_�γ�֤�� foreign key (�γ�id)
      references �γ� (�γ�id) on delete restrict on update restrict;

alter table ���� add constraint FK_���� foreign key (���⼯id)
      references ���⼯ (���⼯id) on delete restrict on update restrict;

alter table ���� add constraint FK_�̳� foreign key (ϰ����)
      references ϰ�� (ϰ����) on delete restrict on update restrict;

alter table ���⼯ add constraint "FK_����/����" foreign key (�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

