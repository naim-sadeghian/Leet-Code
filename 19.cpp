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
    /**
     Move right pointer n nodes so that when it reaches the end the left pointer
     will be n places beind it

     Time Complexity: O(n) 
     Space Complexity: O(1) done in place
     */
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* left = head;
        ListNode* right =  head;
        while(n--){
            right = right->next;
        }
        if(right == nullptr){//if you need to remove the first one
            return head->next;
        }
        while(right->next != nullptr){
            cout << right->val <<endl;
            left = left->next;
            right = right->next;
        }
        left->next = left->next->next;
        return head;
    }
};