/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* ans = head;
        ListNode* prev = NULL;
        while(head != NULL){
            if(head->val == val){
                if(prev != NULL){
                    prev->next = head->next;
                }
                else{
                    ans = head->next;
                }
            }
            else{
                prev = head;
            }
           
            head = head->next;
        }
        return ans;
    }
};