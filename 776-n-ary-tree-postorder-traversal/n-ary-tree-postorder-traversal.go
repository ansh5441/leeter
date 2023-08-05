/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Children []*Node
 * }
 */

func postorder(root *Node) []int {
  if root == nil {
		return []int{}
	}
	ret := []int{}
	for _, child := range root.Children {
		ret = append(ret, postorder(child)...)
	}
	ret = append(ret, root.Val)
	return ret   
}