This is a Treap!
A treap is a binary combo tree-heap, in which each node contains data in the form (x, y). Nodes are organized as a tree wrt/x and a heap wrt/y. In this particular example, every new node is randomly assigned a y, which ensures that 	on average, the treap will be balanced if it has a lot of nodes.
Operations: insert, search, delete
Insert is different from a normal tree, because it occasionally requires an element to be spliced above the root of a tree, and from a normal heap, because it is not enough to place a new node at the end and trickle up.
Search would be the same as a tree.
Delete ?

Source: https://cp-algorithms.com/data_structures/treap.html