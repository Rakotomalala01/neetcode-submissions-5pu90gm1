import heapq


class Solution:
    def minInterval(
        self,
        intervals: list[list[int]],
        queries: list[int]
    ) -> list[int]:

        # Sort intervals by their left endpoint.
        # This lets us add intervals in order as queries increase.
        intervals.sort()

        # Sort queries, but keep their original index.
        # Example:
        # queries = [6, 2]
        # sorted_queries = [(2, 1), (6, 0)]
        sorted_queries = sorted(
            (query, index)
            for index, query in enumerate(queries)
        )

        result = [-1] * len(queries)

        # Heap stores:
        # (interval length, interval right endpoint)
        #
        # The shortest interval stays at heap[0].
        heap = []

        # Points to the next interval that has not yet been examined.
        i = 0

        # Process every query from smallest to largest.
        for query, original_index in sorted_queries:

            # Add every interval that has started:
            # left <= query
            while i < len(intervals) and intervals[i][0] <= query:
                left, right = intervals[i]

                # Optional optimization:
                # If this interval already ended before the current query,
                # do not add it.
                if right >= query:
                    length = right - left + 1
                    heapq.heappush(heap, (length, right))

                # Never reset i.
                # Each interval is examined only once.
                i += 1

            # Some intervals may have been valid for earlier queries,
            # but are now expired.
            #
            # Remove them while they are at the top of the heap.
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # After removing expired intervals, heap[0] is:
            # - the shortest interval
            # - that contains the current query
            if heap:
                result[original_index] = heap[0][0]

        return result