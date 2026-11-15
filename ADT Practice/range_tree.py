class AssocNode:
    """Node for the associate balanced BST T_ass(z) (keyed by y-coordinate)."""
    def __init__(self, point):
        self.point = point  # Tuple (x, y)
        self.left = None
        self.right = None


class RangeNode:
    """Node for the primary balanced BST T (keyed by x-coordinate)."""
    def __init__(self, point):
        self.point = point  # Tuple (x, y)
        self.left = None
        self.right = None
        self.t_ass = None   # Root of associate tree T_ass(z) storing P(z)


class RangeTree2D:
    def __init__(self, points):
        """
        Initializes and builds the 2D Range Tree from a list of (x, y) tuples.
        Assumes points are in general position (distinct x and y coordinates).
        """
        if not points:
            self.root = None
            return

        # Pre-sort points once by x and once by y
        px = sorted(points, key=lambda p: p[0])
        py = sorted(points, key=lambda p: p[1])
        self.root = self._build_range_tree(px, py)

    # ---------------------------------------------------------
    # 1. Construction Methods
    # ---------------------------------------------------------
    def _build_balanced_y_bst(self, py):
        if not py: 
            return None
        median = len(py) // 2
        root = py[median]

        node = AssocNode(root)
        node.left = self._build_balanced_y_bst(py[:median])
        node.right = self._build_balanced_y_bst(py[median + 1:])

        return node

    def _build_range_tree(self, px, py):
        if not px: 
            return None
        median = len(px) // 2
        root = px[median]

        node = RangeNode(root)

        node.t_ass = self._build_balanced_y_bst(py)
        py_left = []
        py_right = []

        for x, y in py:
            if x < root[0]:
                py_left.append((x,y))
            elif x > root[0]:
                py_right.append((x,y))
        node.left = self._build_range_tree(px[:median], py_left)
        node.right = self._build_range_tree(px[median + 1:], py_right)

        return node

    # ---------------------------------------------------------
    # 2. 1D Range Search Helper (for Associate Trees)
    # ---------------------------------------------------------
    def _range_search_y(self, node, y1, y2, results):
        """
        TODO: Perform a 1D range search on an associate tree T_ass(z)
        for all points with y1 <= y <= y2, appending matches to `results`.
        """
        if node is None: return 
        if node.point[1] >= y1 and node.point[1] <= y2:
            results.append(node.point)
            self._range_search_y(node.left, y1, y2, results)
            self._range_search_y(node.right, y1, y2, results)
        elif node.point[1] > y2: # we are too big
            self._range_search_y(node.left, y1, y2, results)
        elif node.point[1] < y1: # we are too small 
            self._range_search_y(node.right, y1, y2, results)

    # ---------------------------------------------------------
    # 3. 2D Orthogonal Range Search
    # ---------------------------------------------------------
    def _point_in_range(self, point, x1, x2, y1, y2):
        """Helper to check if a single point lies inside Q = [x1, x2] x [y1, y2]."""
        px, py = point
        return x1 <= px <= x2 and y1 <= py <= y2
        
    def range_search(self, x1, x2, y1, y2): 
        """
        2D range search for Q = [x1, x2] x [y1, y2] using the two-path (P1, P2) method.
        """
        results = []
        if self.root is None:
            return results

        # 1. Walk down from root to find v_split:
        #    The first node where P1 (search for x1) and P2 (search for x2) diverge.
        v_split = self.root
        while v_split is not None:
            vx = v_split.point[0]
            if x2 < vx:
                v_split = v_split.left
            elif x1 > vx:
                v_split = v_split.right
            else:
                # x1 <= vx <= x2: paths P1 and P2 split here!
                break

        # If v_split is None, no points in the tree fall within [x1, x2]
        if v_split is None:
            return results

        # v_split is a boundary node: test if its point is in Q
        if self._point_in_range(v_split.point, x1, x2, y1, y2):
            results.append(v_split.point)

        # 2. Trace P1 down the left subtree of v_split (searching for left boundary x1)
        curr = v_split.left
        while curr is not None:
            # Test boundary node curr
            if self._point_in_range(curr.point, x1, x2, y1, y2):
                results.append(curr.point)

            if x1 <= curr.point[0]:
                # P1 goes left -> curr.right is trapped between P1 and P2!
                # Thus, curr.right is a topmost inside node.
                if curr.right is not None:
                    self._range_search_y(curr.right.t_ass, y1, y2, results)
                curr = curr.left
            else:
                # P1 goes right -> nothing trapped between P1 and P2 at this step
                curr = curr.right

        # 3. Trace P2 down the right subtree of v_split (searching for right boundary x2)
        curr = v_split.right
        while curr is not None:
            # Test boundary node curr
            if self._point_in_range(curr.point, x1, x2, y1, y2):
                results.append(curr.point)

            if x2 >= curr.point[0]:
                # P2 goes right -> curr.left is trapped between P1 and P2!
                # Thus, curr.left is a topmost inside node.
                if curr.left is not None:
                    self._range_search_y(curr.left.t_ass, y1, y2, results)
                curr = curr.right
            else:
                # P2 goes left -> nothing trapped between P1 and P2 at this step
                curr = curr.left

        return results


# =========================================================
# Quick Test Harness
# =========================================================
if __name__ == "__main__":
    # Sample points from Module 8 lecture slides
    sample_points = [
        (1, 5), (2, 7), (3, 1), (4, 4), (5, 13), (6, 15), (7, 11), (8, 10),
        (9, 6), (10, 12), (11, 8), (12, 14), (13, 2), (14, 9), (15, 16), (16, 3)
    ]

    rt = RangeTree2D(sample_points)
    # Query rectangle Q = [3, 15] x [8, 11]
    found = rt.range_search(3, 15, 8, 11)
    print("Points in range:", sorted(found))
    # Expected: [(7, 11), (8, 10), (11, 8), (14, 9)]