class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        st = []

        largestArea, area = 0, 0
        nse = pse = 0

        for i in range(N):
            while st and heights[st[-1]] >= heights[i]:
                ind = st.pop()

                pse = st[-1] if st else -1
                nse = i
                area = heights[ind] * (nse - pse - 1)
                largestArea = max(largestArea, area)
            st.append(i)

        while st:
            ind = st.pop()
            pse = st[-1] if st else -1
            nse = N
            area = heights[ind] * (nse - pse - 1)
            largestArea = max(largestArea, area)
        return largestArea