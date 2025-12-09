#include<stdio.h>
struct node{
    int data;
    struct node* next;
};
void printhead(struct node* n){
    while(n->next!=NULL){
        printf("%d\t",n->data);
        n=n->next;

    }
}
int main(){
struct node *head;
struct node *second;
struct node * third;
head=(struct node*)malloc(sizeof(struct node));
second=(struct node*)malloc(sizeof(struct node));
third=(struct node*)malloc(sizeof(struct node));
head->data=10;
head->next=second;
second->data=20;
second->next=third;
third->data=20;
third->next=NULL;
printhead(head);
free(head);
free(second);
free(third);

return 0;

}