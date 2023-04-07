/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/4/7 21:59:00                            */
/*==============================================================*/


drop table if exists ϰ��;

drop table if exists �ѵ�¼�û�;

drop table if exists �ο�;

drop table if exists ����Ա;

drop table if exists ��Ƶ�γ�;

drop table if exists ��֤֤��;

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
/* Table: �ο�                                                    */
/*==============================================================*/
create table �ο�
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
/* Table: ��Ƶ�γ�                                                  */
/*==============================================================*/
create table ��Ƶ�γ�
(
   �γ�id                 int not null,
   ����Աid                int,
   �û�id                 int,
   �ѵ�¼_�û�id             int,
   �γ���                  char(20) not null,
   ������                  int not null,
   �����Ա                 char(20),
   �������                 datetime,
   ��˽��                 char(10) not null,
   primary key (�γ�id)
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
      references �ο� (�û�id) on delete restrict on update restrict;

alter table ϰ�� add constraint FK_�û�����ϰ�� foreign key (�ѵ�¼_�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ϰ�� add constraint FK_�γ�ϰ�� foreign key (�γ�id)
      references ��Ƶ�γ� (�γ�id) on delete restrict on update restrict;

alter table �ѵ�¼�û� add constraint FK_��¼ foreign key (�û�id)
      references �ο� (�û�id) on delete restrict on update restrict;

alter table ��Ƶ�γ� add constraint FK_�û�������Ƶ foreign key (�ѵ�¼_�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ��Ƶ�γ� add constraint "FK_����Ա����/�����Ƶ" foreign key (����Աid)
      references ����Ա (����Աid) on delete restrict on update restrict;

alter table ��Ƶ�γ� add constraint FK_�ۿ���Ƶ�γ� foreign key (�û�id)
      references �ο� (�û�id) on delete restrict on update restrict;

alter table ��֤֤�� add constraint FK_���֤�� foreign key (�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

alter table ��֤֤�� add constraint FK_�γ�֤�� foreign key (�γ�id)
      references ��Ƶ�γ� (�γ�id) on delete restrict on update restrict;

alter table ���� add constraint FK_���� foreign key (���⼯id)
      references ���⼯ (���⼯id) on delete restrict on update restrict;

alter table ���� add constraint FK_�̳� foreign key (ϰ����)
      references ϰ�� (ϰ����) on delete restrict on update restrict;

alter table ���⼯ add constraint "FK_����/����" foreign key (�û�id)
      references �ѵ�¼�û� (�û�id) on delete restrict on update restrict;

