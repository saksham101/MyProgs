#include<stdio.h>
#include<stdlib.h>
struct node{
struct node *next;
struct node *prev;
int data;
struct node *new_node;
};
int loc,len=0 ,i;
struct node *temp,*head=NULL , *p;
void delete_specific();
void insert_specific();
void disp_front();
void disp_back();
void main()
{
int ch;
do
{
printf("# DOUBLY LINKED LIST #\n<1> Insertion\n<2> Deletion\n<3> Display Front\n<4> Display Backward\n <5> Exit :( \n Enter your choice \n");
scanf("%d",&ch);
switch(ch) {
case 1 :
insert_specific();
break;
case 2 :
delete_specific();
break;
case 3 :
disp_front();
break;
case 4 :
disp_back();
break;
case 5 :
break;
default :
printf("Wrong Choice");
}}while(ch!=5);
}
void insert_specific()
{
p=head;
temp=head;
printf("Enter the data");
scanf("%d",&data);
printf("Enter the location");
scanf("%d",&loc);
new_node=(struct node*)malloc(sizeof(struct node));
new_node->data = data;
new_node->next=NULL;
new_node->prev=NULL;
p=p->next;
if(head==NULL && loc!=1)
{
	printf("Empty List");
	return;
}
if(loc>len+1)
{
	printf("Exceeding the limit");
	return;
}
if(loc==1 && head==NULL)
{
	new_node->next=temp;
	temp->prev=new_node;
	head=new_node;
	len+=1;
}
for(i=0;i<loc;i++)
{
	temp=temp->next;
	p=p->next;
}
new_node->prev=temp;
new_node->next=p;
temp->next=new_node;
p->prev=new_node;
return;
}
void delete_specific()
{
printf("Enter the location");
scanf("%d",&loc);
if(head==NULL)
{
	printf("Underflow");
	return;
}
if(loc==1 && temp->next=NULL)
{
	free(temp);
	head=NULL;
}
for(i=0;i<loc;i++)
{
	temp=temp->next;
}
}
void disp_front()
{
if(head==NULL)
{
	printf("Underflow");
	return;
}
else
{
	while(temp!=NULL)
	{
		printf("%d",temp->data);
		temp=temp->next;
	}
}
}
void disp_back()
{
if(head==NULL)
{
	printf("Underflow");
	return;
}
while(temp!=NULL)
{
	temp=temp->next;
}
while(temp!=NULL)
{
	printf("%d",(temp->data));
	temp=temp->prev;
}
}
