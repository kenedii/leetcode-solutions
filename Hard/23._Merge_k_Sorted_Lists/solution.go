// beats 71.25% runtime 
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 import (
    "slices"
)

func mergeKLists(lists []*ListNode) *ListNode {
    final := []int{}
    for i := range len(lists) {
        node := lists[i]
        cur := node
        for cur != nil {
            final = append(final, cur.Val)
            cur = cur.Next
        }

    }
    if len(final) == 0 {
        return nil
    }
    slices.Sort(final)
    cur := &ListNode{}
    root := cur
    for i := range len(final) {
        cur.Val = final[i]
        if i < len(final)-1 {
            cur.Next = &ListNode{}
            cur = cur.Next
        }
    }
    return root
}
